# refactortool/refactor.py
import ast

class RedundantCodeDetector(ast.NodeVisitor):
    def __init__(self):
        self.redundant_code_lines = []

    def visit_If(self, node):
        # 例として、if False: や if True: を冗長コードとして検出
        if isinstance(node.test, ast.NameConstant) and node.test.value in [True, False]:
            self.redundant_code_lines.append(node.lineno)
        self.generic_visit(node)

def find_redundant_code(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    detector = RedundantCodeDetector()
    detector.visit(tree)
    return detector.redundant_code_lines