#/usr/bin/env python3
"""
Main loop for Airbnb clone console
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class for Interperator
    """

    def do_quit(self, arg):
        """
        Quits the command Loop.
        """
        exit()

    def do_EOF(self, arg):
        """
        End-of-file
        """
        return True

    def help_quit(self):
        """
        Help for quit
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help for EOF
        """
        print("End of File")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
