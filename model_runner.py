from Register import Registrar
import sys

registrar = Registrar()
registrar.load("activity_record.cbr", "software_engineering_workflow")

def console():

    # Print some introductory exposition
    for string, function in registrar.activities.items():
        print 'Type "' + string + '" to run a function in the model called:  ' + function.__name__

    uin = raw_input("    :: ")
    while (uin != "end"):
        try:
            if uin in registrar.activities.keys():
                registrar.run_input(uin)
            elif int(uin) - 1 in range(0, len(registrar.activities.keys())):
                registrar.run_input(registrar.activities.keys()[int(uin) -1])
            else:
                print "Sorry, we don't have any function corresponding to that input"
        except:
            print "We hit some error -- maybe your input was wrong! Try again or type 'end' to quit."

        # Get more input
        uin = raw_input("    :: ").lower()

    print "Quitting!"
    quit()


def parse_input(input_line):
    try:
        if input_line in registrar.activities.keys():
            registrar.run_input(input_line)
        elif int(input_line) - 1 in range(0, len(registrar.activities.keys())):
            registrar.run_input(registrar.activities.keys()[int(input_line) -1])
        else:
            print "Sorry, we don't have any function corresponding to that input"
    except:
        print "We hit some error -- maybe your input was wrong! Try again or type 'end' to quit."

if len(sys.argv) > 1:
    for filename in sys.argv[1:]:
        with open(filename, 'r') as journal_entry:
            for line in journal_entry.readlines():
                parse_input(line.rstrip("\n"))
else:
    console()