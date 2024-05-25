# tests/test_utils.py
from refactortool import utils

def test_run_tests():
    result = utils.run_tests()
    assert 'passed' in result