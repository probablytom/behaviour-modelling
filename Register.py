
class Registrar:
    def __init__(self):
        self.activities = {}

    def register(self, natural_language_function_string, function):
        self.activities[natural_language_function_string] = function

    def commit(self):
        with open("activity_record.cbr", 'a')as activity_record:
            for key, value in self.activities.items():
                activity_record.write(key + " " + value.__name__ + '\n')

    def load(self, filename = "activity_record.cbr", model_name = "Model"):
        imported_model = __import__(model_name)
        with open(filename, 'r') as activity_record:
            for line in activity_record.readlines():
                line_contents = line.rstrip("\n").split(" ")
                function_name = line_contents[-1]
                semantic_function_description = " ".join(line_contents[0:-1])
                # self.activities should have the first string on the line pointing to the function whose name is the second string on the line in the model provided.
                self.activities[semantic_function_description] = getattr(imported_model, function_name)


    def run_input(self, input_line):
        self.activities[input_line]()