class Constraint:

    def __init__(self, constraint = ""):
        self.constraint_unparsed = constraint
        self.constraint = self.parse(constraint)

    @staticmethod
    def parse(constraint):
        return constraint
