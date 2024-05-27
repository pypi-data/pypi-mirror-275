import torch
from bitarray import bitarray
from typing import Sequence, cast
from itertools import batched


def F(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
    return (x & y) | (~x & z)


def G(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
    return (x & z) | (y & ~z)


def H(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
    return x ^ y ^ z


def I(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
    return y ^ (x | ~z)


def hexdigest(x: torch.Tensor) -> str:
    return ' '.join(f"{(x.item() & 0xFFFFFFFF).to_bytes(4, "little").hex():08}" for x in x)


def preprocess(msg: torch.Tensor, bitlength: torch.Tensor):
    device = msg.device
    dtype = msg.dtype
    batches = msg.shape[0]
    blocks = (bitlength + 512 + 64) // 512
    maxblocks = blocks.max()
    preprocessed: torch.Tensor = torch.zeros(
        (batches, maxblocks*16), dtype=dtype, device=device)
    preprocessed[:, :msg.shape[1]] = msg
    # bytes are grouped into words, to pad one bit, we must find which word and bit to pad
    if (bitlength[0] == bitlength).all():
        bitlength = bitlength[0]
        one_bit_word_index = bitlength >> 5  # // 32
        one_bit_mask = 0x80000000 >> (bitlength - (one_bit_word_index << 5))
        # convert bit mask to little endian
        one_bit_mask = ((one_bit_mask & 0xFFFF) << 16) | (one_bit_mask >> 16)
        one_bit_mask = ((one_bit_mask & 0x00FF00FF) << 8) | (
            (one_bit_mask & 0xFF00FF00) >> 8)
        preprocessed[:, one_bit_word_index] |= one_bit_mask
    else:
        one_bit_word_index = bitlength >> 5  # // 32
        one_bit_mask = 0x80000000 >> (bitlength - (one_bit_word_index << 5))
        # convert bit mask to little endian
        one_bit_mask = ((one_bit_mask & 0xFFFF) << 16) | (one_bit_mask >> 16)
        one_bit_mask = ((one_bit_mask & 0x00FF00FF) << 8) | (
            (one_bit_mask & 0xFF00FF00) >> 8)
        for i, (index, mask) in enumerate(zip(one_bit_word_index, one_bit_mask)):
            preprocessed[i, index] |= mask

    # append the length of the message in bits
    if (blocks == maxblocks).all():
        preprocessed[:, -2] = bitlength & 0xFFFFFFFF
        preprocessed[:, -1] = (bitlength >> 32) & 0xFFFFFFFF
    else:
        for i, (block, length) in enumerate(zip(blocks, bitlength)):
            preprocessed[i, (block-1)*16 + 14] = length & 0xFFFFFFFF
            preprocessed[i, (block-1)*16 + 15] = (length >> 32) & 0xFFFFFFFF

    return preprocessed.reshape(batches, maxblocks, 16), blocks


def md5_preprocessed(msg: torch.Tensor, blocks: torch.Tensor | None = None) -> torch.Tensor:
    """
    # Batched MD5 hash function core
    - msg: torch.Tensor of shape (batches, blocks, 16) with dtype treated as torch.uint32
    """

    def F(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
        return (x & y) | (~x & z)

    def G(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
        return (x & z) | (y & ~z)

    def H(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
        return x ^ y ^ z

    def I(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
        return y ^ (x | ~z)

    device = msg.device
    dtype = msg.dtype
    batches, maxblocks, _ = msg.shape

    K: torch.Tensor = (torch.arange(1, 65, dtype=torch.double, device=device).sin().abs()
                       * 2**32).type(dtype).reshape(4, 16)
    INIT_VECT = torch.tensor(
        [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476],
        dtype=dtype, device=device)
    SHIFTS = torch.tensor(
        [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21],
        dtype=dtype, device=device).reshape(4, 4).repeat(1, 4)
    ORDERS = torch.tensor([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12],
        [5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2],
        [0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9],
    ], dtype=dtype, device=device)

    init = INIT_VECT.reshape(1, -1).repeat(batches, 1)
    if blocks is not None and (blocks == maxblocks).all():
        blocks = None

    for block in range(maxblocks):
        md5: torch.Tensor = init.clone()
        mask: slice | torch.Tensor
        if blocks is None:
            mask = slice(batches+1)
        else:
            mask = blocks > block

        for s, func in zip(range(4), [F, G, H, I]):
            for i in range(16):
                md5[mask, 0] += func(md5[mask, 1], md5[mask, 2], md5[mask, 3]
                                     ) + msg[mask, block, ORDERS[s][i]] + K[s][i]
                md5[mask, 0] &= 0xFFFFFFFF
                md5[mask, 0] = (md5[mask, 0] << SHIFTS[s][i]) | (
                    md5[mask, 0] >> (32 - SHIFTS[s][i]))
                md5[mask, 0] += md5[mask, 1]
                md5[mask, 0] &= 0xFFFFFFFF
                md5 = md5.roll(1, 1)
        md5[mask] = (md5[mask] + init[mask]) & 0xFFFFFFFF
        init = md5.clone()

    return md5


def md5(msgs: Sequence[str | bytes | bitarray], *, device="cpu") -> torch.Tensor:
    batches = len(msgs)

    msgs = list(msgs)
    lengths = torch.zeros(batches, dtype=torch.int64, device=device)

    for i, msg in enumerate(msgs):
        if isinstance(msg, str):
            msg = msg.encode("utf-8")
        if isinstance(msg, bitarray):
            lengths[i] = len(msg)
            msg = msg.tobytes()
        else:
            lengths[i] = len(msg) * 8
        msgs[i] = msg
    msgs = cast(list[bytes], msgs)

    t = torch.zeros(batches, (lengths.max() + 32) // 32,
                    dtype=torch.int64, device=device)

    for batch, msg in enumerate(msgs):
        for i, quad in enumerate(batched(msg, 4)):
            for j, b in enumerate(quad):
                t[batch, i] |= b << (j * 8)

    t, blocks = preprocess(t, lengths)
    return md5_preprocessed(t, blocks)
