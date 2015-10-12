class Logger:
    def __init__(self, filepath="event.log", logging=True, printing=False):
        self.filepath = filepath
        self.logging = logging
        self.printing = printing

    def log_line(self, string_to_log=""):
        if self.logging:
            with open(self.filepath) as logfile:
                logfile.write(string_to_log)
        if self.printing:
            print(string_to_log)

    def change_log(self, new_filepath = "event.log", copy_old_logs = True):
        if copy_old_logs:
            with open(new_filepath) as newlog:
                with open(self.filepath) as oldlog:
                    newlog.write( oldlog.readall() )

        self.filepath = new_filepath