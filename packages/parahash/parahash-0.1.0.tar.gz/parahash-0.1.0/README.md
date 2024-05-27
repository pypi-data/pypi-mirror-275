# Collection of some hash functions implemented with `torch`/`numpy`/`tensorflow`

WORK IN PROGRESS!

## Installation

```bash
pip install parahash
```

or clone this repo and run

```bash
pip install -U poetry
poetry install -E all

# To install to your current environment, do
# pip install .
```

Some dependencies are optional when installing because they are not required or you may need a custom-built version of `torch`/`tensorflow`/`numpy`. Make sure to install them if you need them.

## MD5

```python
import parahash
from bitarray import bitarray

device = "cpu"
# device = "cuda"

data = [b'hello', "world", bitarray('1101010101010101010101010101010101010101010101010101010101010101')]

for out in parahash.md5.md5(data, device=device):
    print(parahash.md5.hexdigest(out))
```

Current implementation with enough batch size can get 20 million hashes per second on a single RTX3090 GPU, 16 million hashes per second on a single RTX4070TiS GPU and 750K hashes per second on a single 7950x CPU.
