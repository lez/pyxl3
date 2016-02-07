#!/usr/bin/env python

import sys
from pyxl.codec.tokenizer import pyxl_tokenize, pyxl_untokenize

with open(sys.argv[1], 'r') as f:
    print(pyxl_untokenize(pyxl_tokenize(f.readline)), end='')
