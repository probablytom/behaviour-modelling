class Behaviour:

    def __init__(self, behaviour = ""):
        self.behaviour_unparsed = behaviour
        self.behaviour = self.parse(behaviour)

    @staticmethod
    def parse(behaviour):
        return behaviour
