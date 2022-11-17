# from expando import *
# import expando 
from .expando import Expando as Expando

# def reload(m = expando):
# m = expando
# importlib.reload(m)
# print(" ::: Reloaded", m, "::: at ", time.time())
# reload = lambda m: reload(m)

# reload()
# xo = Expando()
# xo = expando.Expando()

# from helper import *



xo = Expando()



# xo.reload(Expando)

# xo = Expando(xo)

#!/usr/bin/env python3

# Exported function
def as_int(a):
    return int(a)

# Test function for module


def _test():
    assert as_int('1') == 1


if __name__ == '__main__':
    _test()
