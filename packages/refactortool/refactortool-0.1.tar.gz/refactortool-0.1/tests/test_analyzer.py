# tests/test_analyzer.py
from refactortool import analyzer

def test_check_code_style():
    result = analyzer.check_code_style('example.py')
    assert 'Your code has been rated' in result

def test_auto_fix_code_style():
    original_code = 'x=  1+2'
    fixed_code = analyzer.auto_fix_code(original_code)
    assert fixed_code == 'x = 1 + 2\n'
