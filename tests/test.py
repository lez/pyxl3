from pyxl.codec.register import pyxl_decode
from pyxl.codec.tokenizer import PyxlParseError
from pyxl.codec.parser import ParseError
#import pyxl.codec.register

import os
import subprocess

passing_cases_path = os.path.dirname(os.path.abspath(__file__))
error_cases_path = os.path.join(passing_cases_path, 'error_cases')

def _expect_failure(file_name):
    path = os.path.join(error_cases_path, file_name)
    try:
        with open(path) as f:
            print(pyxl_decode(f.read()))
        assert False, "successfully decoded file %r" % file_name
    except (PyxlParseError, ParseError) as e:
        print('.', end='')

def test_error_cases():
    cases = os.listdir(error_cases_path)
    for file_name in cases:
        if file_name.endswith(".py"):
            _expect_failure(file_name)

def test_passing_cases():
    cases = os.listdir(passing_cases_path)
    for file_name in cases:
        if file_name in ('test_basic.py', 'test_rss.py'):
            subprocess.Popen(['python', file_name]).wait()
        elif file_name.startswith('test_'):
            module = __import__(file_name[:-3])
            if not module.test(): print('.', end='')
            else: print('F (%s)' % file_name, end='')

if __name__ == '__main__':
    test_error_cases()
    print()
    test_passing_cases()
    print()
