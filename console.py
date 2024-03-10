#!/usr/bin/python3
"""module that contains cmd program"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class_list = {'BaseModel', 'FileStorage'}


class HBNBCommand(cmd.Cmd):
    """simple console app for managing my airbnb application"""

    prompt = '(hbnb) '

    def emptyline(self):
        """empty line should not execute anything"""
        pass

    def do_EOF(self, line):
        """handle end of file character"""
        print()
        return True

    def do_quit(self, s):
        """Quit command to exit the program"""
        return True

    def do_create(self, args):
        """cmd so function to create BaseModel instance"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        else:
            if not args[0] in class_list:
                print(args[0], "** class doesn't exist **")
                print("class list: ", class_list)
            else:
                print(eval(args[0])().id)
                storage.save()

    def do_show(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("**class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
