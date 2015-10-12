import sys


class Logger:
    def __init__(self, filepath="event.log", logging=True, printing=False):
        self.filepath = filepath
        self.logging = logging
        self.printing = printing

    # Logs a line if self.logging and prints it if self.printing
    def log_line(self, string_to_log=""):
        if self.logging:
            # Note that `with` will close the file afterward
            with open(self.filepath, 'a') as logfile:
                logfile.write(string_to_log + '\n')
        if self.printing:
            print(string_to_log)


    # logs characters if self.logging and prints them without a newline if self.printing
    def log(self, string_to_log):
        if self.logging:
            # Note that `with` will close the file afterward
            with open(self.filepath, 'a') as logfile:
                logfile.write(string_to_log)
        if self.printing:
            sys.stdout.write(string_to_log)  # Write on the line without creating a newline


    # Allows for changing the log file used
    def change_log(self, new_filepath = "event.log", copy_old_logs = True):
        if copy_old_logs:
            # Note that `with` will close the file afterward
            with open(new_filepath, 'w') as newlog:
                with open(self.filepath, 'r') as oldlog:
                    newlog.write( oldlog.readall() )

        self.filepath = new_filepath

    # Toggles whether the logger will print to the console
    def to_print(self, to_print):
        self.printing = to_print

    # Toggles whether the logger will write to the log
    def to_write_to_log(self, to_write_to_log):
        self.logging = to_write_to_log