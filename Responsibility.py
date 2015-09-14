class Responsibility:

    def __init__(self, responsibility = ""):
        self.responsibility_unparsed = responsibility
        self.responsibility = self.parse(responsibility)

    @staticmethod
    def parse(responsibility):
        return responsibility
