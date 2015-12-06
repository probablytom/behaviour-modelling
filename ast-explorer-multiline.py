import ast 


class V(ast.NodeVisitor):
    def generic_visit(self, node):
        print dir(node)
        print type(node).__name__
        if "col_offset" in dir(node): print node.col_offset
        if type(node).__name__ == "Module":
            print dir(ast.NodeTransformer)
        print
        raw_input()
        ast.NodeVisitor.generic_visit(self, node)


visitor = V()
with open("environment.py") as env:
    uin = env.read()
    t = ast.parse(uin)
    visitor.visit(t)
