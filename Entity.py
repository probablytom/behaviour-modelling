from Attribute import Attribute
from Behaviour import Behaviour
from Responsibility import Responsibility
from Constraint import Constraint

class Entity:
    def __init__(self, name):
        self.name = name
        self.behaviours = []
        self.responsibilities = []
        self.attributes = []  # Any attributes of the entity's affect on the environment/how it defines its environment. Say the entity is a building; attributes might be seating arrangements.
        self.constraints = []


    def add_attribute(self, attribute_to_add):
        self.attributes.append( Attribute(attribute_to_add) )

    
    def add_behaviour(self, behaviour_to_add):
        self.behaviours.append( Behaviour(behaviour_to_add) )

    
    def add_responsibility(self, responsibility_to_add):
        self.responsibilities.append( Responsibility(responsibility_to_add) )

    
    def add_constraint(self, constraint_to_add):
        self.constraints.append( Constraint(constraint_to_add) )
    
    
    def list_attributes():
        print self.name + " has attributes: "
        for attribute in self.attributes: print attribute.semantic_text
    
    
    def list_behaviours():
        print self.name + " has behaviours: "
        for behaviour in self.behaviours: print behaviour.behaviour_unparsed
    
    def list_responsibilities():
        print self.name + " has responsibilities: "
        for responsibility in self.responsibilities: print responsibility.responsibility_unparsed

    def list_fulfilled_responsibilities(self):
        fulfilled_responsibilities = []
        for resp_index in range(0, len(self.responsibilities)):
            for beh_index in range(0, len(self.behaviours)):
                responsibility = self.responsibilities[resp_index]
                behaviour = self.behaviours[beh_index]
                if responsibility.responsibility_unparsed == behaviour.behaviour_unparsed  and  not(responsibility in fulfilled_responsibilities):
                    fulfilled_responsibilities.append(responsibility)
        # Print responsiblities that are fulfilled.
        if fulfilled_responsibilities == []:
            print "No fulfilled responsibilities for entity " + self.name + " found."
        else:
            print "Fulfilled responsibilities for entity " + self.name + ":"
            for responsibility in fulfilled_responsibilities: print responsibility.responsibility_unparsed

    def get_fulfilled_responsibilities(self):
        fulfilled_responsibilities = []
        for resp_index in range(0, len(self.responsibilities)):
            for beh_index in range(0, len(self.behaviours)):
                responsibility = self.responsibilities[resp_index]
                behaviour = self.behaviours[beh_index]
                if responsibility.responsibility_unparsed == behaviour.behaviour_unparsed  and  not(responsibility in fulfilled_responsibilities):
                    fulfilled_responsibilities.append(responsibility)
        # Return the responsibilities that have corresponding behaviours that make them fulfilled.
        return fulfilled_responsibilities
