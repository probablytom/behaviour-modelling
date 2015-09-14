class Attribute:
    
    def __init__(self, attribute = ""):
        self.semantic_text = attribute
        self.parsed_attribute = self.parse(attribute)
    
    
    @staticmethod
    def parse(attribute):
        return attribute
