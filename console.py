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
        """cmd so to function to create BaseModel instance"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        else:
            if not args[0] in class_list:
                print("** class doesn't exist **")
            else:
                print(eval(args[0])().id)
                storage.save()

    def do_show(self, args):
        """usage: <show> <classname> <instanceid>"""
        args = shlex.split(args)
        objects = storage.all()
        if len(args) == 0:
            print("**class name missing **")
        else:
            if not args[0] in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in objects:
                print("** no instance found **")
            else:
                print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """usage: <destroy> <classname> <instanceid>"""
        args = shlex.split(args)
        objects = storage.all()
        if len(args) == 0:
            print("**class name missing **")
        else:
            if not args[0] in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in objects:
                print("** no instance found **")
            else:
                del objects["{}.{}".format(args[0], args[1])]
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
