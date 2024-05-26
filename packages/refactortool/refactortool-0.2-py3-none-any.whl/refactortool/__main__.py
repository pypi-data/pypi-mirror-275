# __main__.py
import sys
from refactortool import analyzer, refactor, utils

def main():
    if len(sys.argv) < 2:
        print("Usage: refactortool <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print(f"Checking code style for {file_path}...")
    print(analyzer.check_code_style(file_path))
    
    print("Fixing code style...")
    analyzer.auto_fix_code_style(file_path)
    
    print(f"Finding redundant code in {file_path}...")
    redundant_lines = refactor.find_redundant_code(file_path)
    print(f"Redundant lines: {redundant_lines}")
    
    print("Suggesting performance improvements...")
    performance_suggestions = analyzer.suggest_performance_improvements(file_path)
    print(f"Performance suggestions: {performance_suggestions}")
    
    print("Running tests...")
    test_results = utils.run_tests()
    print(test_results)

if __name__ == '__main__':
    main()
