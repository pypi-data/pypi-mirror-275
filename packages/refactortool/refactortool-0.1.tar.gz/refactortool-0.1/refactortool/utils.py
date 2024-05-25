# refactortool/utils.py
import subprocess

def run_tests(test_path='tests'):
    result = subprocess.run(['pytest', test_path], capture_output=True, text=True)
    return result.stdout
