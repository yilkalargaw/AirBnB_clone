#!/usr/bin/env python3
"""
Main loop for Airbnb clone console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class for Interperator
    """

    prompt = "hbnb-> "

    __hbnb_class_map = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review,
    }
    __hbnb_methods = ['create', 'show', 'destroy', 'all', 'update', 'count']

    error_occured = False

    def do_quit(self, arg):
        """
        Quits the command Loop.
        """
        exit()

    def help_quit(self):
        """
        Help for quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        End-of-file
        """
        return True

    def help_EOF(self):
        """
        Help for EOF
        """
        print("End of File")

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
           - If the class name is missing, prints ** class name missing **
           - If the class name doesn’t exist, prints ** class doesn't exist **
        """

        if not arg:
            print('** class name missing **')
        elif arg not in self.__hbnb_class_map:
            print('** class doesn\'t exist **')
        else:
            arg = self.__hbnb_class_map(arg)
            arg.save()
            print(arg.id)

    def help_create(self):
        """Help for create"""
        print('Creates an instance of a Base Model, saves it to  a JSON file')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
