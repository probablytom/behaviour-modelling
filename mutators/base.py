import sys, re, ast, random
from codegen import to_source


INDENT_PAT = re.compile('^([ \t]*)[^ \t]', re.MULTILINE)

class MutantTransformer(ast.NodeTransformer):

    def __init__(self, source_lines, mutation='comment_line', strip_decorators = True):
        self.source_lines = source_lines
        self.strip_decorators = strip_decorators
        self.mutation = mutation

    def comment_line(self, line_node, lineno = None, indent = None):
        if lineno == None: lineno = line_node.lineno
        line = self.source_lines[lineno-1]
        if indent is None:
            indent = self.indentation(line)
        self.source_lines[lineno-1] = (indent + '#Mutant#  ' + line[len(indent):]).rstrip() + '\n'
        return indent

    # Returns line number comented or -1 if commenting failed
    def attempt_comment_from(self, lineno, indent = None):
        can_comment = False
        will_comment = True
        lineno -= 1
        
        while not can_comment:
            lineno += 1
            can_comment, will_comment = self.commentable_line(self.source_lines[lineno])
            if not will_comment:
                
                return -1  # Couldn't comment
        line = self.source_lines[lineno-1]
        if indent is None:
            indent = self.indentation(line)
        self.source_lines[lineno-1] = (indent + '#Mutant#  ' + line[len(indent):]).rstrip() + '\n'
        return 0

    def attempt_comment_node(self, node):
        linecount = 0
        for line in node.body:
            if not ('body' in dir(line)):
                line_source = self.source_lines[line.lineno-1]
                indent = self.indentation(line_source)
                self.source_lines[line.lineno-1] = (indent + '#Mutant#  ' + line_source[len(indent):]).rstrip() + '\n'
                return linecount
            linecount += 1
        return -1

    def indentation(self, line):
        m = INDENT_PAT.search(line)
        if m:
            return m.group(1)
        return ''

    # Currently doesn't deal with nested functions correctly, see 'def'
    def commentable_line(self, line):
        can_comment = True
        will_comment = True
        if "def" in line:
            can_comment = False
        if "for" in line:
            can_comment = False
            will_comment = False
        if "if" in line:
            can_comment = False
            will_comment = False
        if "while" in line:
            can_comment = False
            will_comment = False
        if "else" in line:
            can_comment = False
            will_comment = False
        if "class" in line:
            can_comment = False
            will_comment = False
        return can_comment, will_comment

    def prepare_mutest_import_node(self):
        return ast.ImportFrom(module = 'mutester.public', names = [ ast.alias(name = 'mutest_statement_reached', asname = None) ], level = 0)

    def prepare_mutest_reached_node(self):
        return ast.Call(func = ast.Name(id = 'mutest_statement_reached'), args = [ ], keywords = [ ], starargs = None, kwargs = None)

    def print_source_lines(self):
        for lineno, line in enumerate(self.source_lines):
            sys.stdout.write('%03d: %s' % ( lineno+1, line ))

    #NOTE: This will work differently depending on whether the decorator takes arguments. 
    def visit_FunctionDef(self, node):
        mutatables = []
        if self.strip_decorators == True:
            node.decorator_list = []
        linesToCheck = [node.body]
# This commented out because I suspect this actually doesn't make us any more secure.
#         for lineSet in linesToCheck:
#             for item in lineSet:
#                 if not hasattr(item, 'body'):
#                     mutatables.append(item)
#                 else:
#                     pass#lineSet.append(item.body)
        if self.mutation == 'comment_line':
            if len(mutatables) > 0: node.body.remove(random.choice(mutatables))
        elif self.mutation == 'truncate_function':
            truncation_point = random.randint(0,len(mutatables))
            node.body = node.body[0:truncation_point]
        return self.generic_visit(node)

if __name__ == "__main__":
    with open("test_code_to_mutate.py") as env:
        uin = env.read()
        visitor = MutantTransformer(uin.split('\n'))
        t = ast.parse(uin)
        t =visitor.visit(t)
        print to_source(t)
        print
        print
        exec( to_source(t) )#exec('\n'.join(visitor.source_lines))
