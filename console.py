#!/usr/bin/env python3
"""
Main loop for Airbnb clone console
"""

import cmd
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for Interperator
    """

    prompt = '(hbnb) '

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

    def precmd(self, arg):
        """
        method to be executed before command line execution
        """
        parsed_args = arg.split('.')

        if parsed_args[0] in self.__hbnb_class_map:

            further_parsed_args = parsed_args[1].split("(")
            further_parsed_args2 = further_parsed_args[1].split(')')
            ids = further_parsed_args2[0].strip('"\'')

            if further_parsed_args[0] in ['all', 'count']:
                arg = ''.join(further_parsed_args[0],
                              ' ',
                              parsed_args[0])

            elif further_parsed_args[1] in ['show', 'destroy']:
                arg = ''.join(further_parsed_args[0],
                              ' ',
                              parsed_args[0],
                              ' ',
                              ids)
        return arg

    def do_quit(self, arg):
        """
        Quits the command Loop.
        """
        exit()

    def help_quit(self):
        """
        Help for quit
        """
        print('Quit command to exit the program')

    def do_EOF(self, arg):
        """
        End-of-file
        """
        return True

    def help_EOF(self):
        """
        Help for EOF
        """
        print('End of File')

    def emptyline(self):
        """
        do nothing
        """
        pass

    def help_emptyline(self):
        """
        help for empty line
        """
        print('Do Nothing (emptyline)')

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
            arg = self.__hbnb_class_map[arg]()
            arg.save()
            print(arg.id)

    def help_create(self):
        """
        Help for create
        """
        print('Creates an instance of a Base Model, saves it to  a JSON file')

    def do_show(self, arg):
        """
        Shows the string version of the objects
        """

        if not arg:
            print('** class name missing **')
        else:
            parsed_args = arg.split()

        if parsed_args[0] not in self.__hbnb_class_map:
            print('** class doesn\'t exist **')
        elif len(parsed_args) == 1:
            print('** instance id missing **')
        else:
            joined_obj_symbol = ''.join([parsed_args[0], '.', parsed_args[1]])
            try:
                print(storage.all()[joined_obj_symbol])
            except KeyError:
                print('** no instance found **')

    def help_show(self):
        """
        Help for show command
        """
        print('Prints the string representation of an instance.')

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """

        if not arg:
            print('** class name missing **')
        else:
            parsed_args = arg.split()

        if parsed_args[0] not in self.__hbnb_class_map:
            print('** class doesn\'t exist **')
        elif len(parsed_args) == 1:
            print('** instance id missing **')
        else:
            joined_obj_symbol = ''.join([parsed_args[0], '.', parsed_args[1]])
            try:
                del (storage.all()[joined_obj_symbol])
                storage.save()
            except KeyError:
                print('** no instance found **')

    def help_destroy(self):
        """
        Help for destroy command
        """
        print('Deletes an instance based on the class name and id')

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        if not arg:
            print('** class name missing **')
        else:
            parsed_args = arg.split()

        if parsed_args[0] not in self.__hbnb_class_map:
            print('** class doesn\'t exist **')
        elif len(parsed_args) == 2:
            obj_lst = []
            for i in storage.all().values():
                if len(parsed_args) > 0:
                    if parsed_args[0] == i.__class__.__name__:
                        obj_lst.append(i.__str__())
                elif len(parsed_args) == 0:
                    obj_lst.append(i.__str__())
            print(objl)

    def help_all(self):
        """
        Help for all command
        """
        print('Prints all string representation of all instances')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
