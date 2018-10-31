import time
from functools import _make_key
from cachetools.keys import typedkey

if __name__ == '__main__':
    print(_make_key((), {}, False))
    print(typedkey((), {}))