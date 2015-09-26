from Entity import Entity

entities = []
definitions = None

def get_entity(entity_name):
    for index in range(0, len(entities)):
        if entity_name == entities[index].name: return index
    # Entity didn't exist, so we have to create one and return the index to that.
    new_entity = Entity(entity_name)
    entities.append( new_entity )
    return len(entities) - 1

def parse_line(line):
    
    # Is this an environmental attribute?
    if "@environment" in line[0]:
        environment = line[0][ len("@Environment(") :-1]
        entity_index = get_entity(environment)
        env_attribute = line[2][ len("@property(") : -1 ]
        entities[entity_index].add_attribute( env_attribute )

    # Is this an organisational constraint?
    elif "@organisation" in line[0]:
        organisation = line[0][ len("@Organisation(") : -1]
        entity_index = get_entity(organisation)
        org_constraint = line[2][ len("@property(") : -1 ]
        entities[entity_index].add_attribute( org_constraint )

    # Are we dealing with a behaviour or responsibility?
    elif "@entity" in line[0]:
        entity = line[0][ len("@Entity(") :-1 ]
        entity_index = get_entity(entity)
        
        # Here we check whether we're adding a behaviour or a responsibility.
        if "@behaviour" in line[2]:
            behaviour = line[2][len("@behaviour(") :-1 ]
            entities[entity_index].add_behaviour(behaviour)
        elif "@responsibility" in line[2]:
            responsibility = line[2][len("@responsibility(") :-1 ]
            entities[entity_index].add_responsibility(responsibility)
        else:
            print ' '.join(line)
            print "The above line could not be parsed; syntax error on attr. token."
        
    elif line[0] == "list":
        if line[1] == "entities":
            for entity in entities: print entity.name
        elif line[1] == "fulfilled" and line[2] == "responsibilities":
            # Line[3] should be 'of'
            entity_name = line[4][len("@entity("):-1]
            entity_index = get_entity(entity_name)
            entities[entity_index].list_fulfilled_responsibilities()
    
    # Default case
    else:
        print ' '.join(line)
        print "^"
        print "The above line could not be parsed; syntax error."


with open("definitions.cons") as definitions:
    line = definitions.readline().split(" ")
    while(line[0] != "end" and len(line) != 1):
        parse_line(line)
        line = definitions.readline().split(" ")

# Fully parsed the definitions file!
print "Definitions parsed. Jumping into a CLI for interacting with the model.\n"


# Here we jump into a CLI to interact with the model.
while True:
    line = raw_input("   :: ").split(" ")
    if line[0] == "end":
        print "Quitting!"
        quit()
    else:
        parse_line(line)
