#!/usr/bin/python3
"""module that contains cmd program"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage

class_list = {'BaseModel', 'FileStorage', 'User', 'Amenity',
              'Review', 'Place', 'City', 'State'}


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
        """cmd so to function to create instance of model classes"""
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

    def do_all(self, args):
        """usage: <all> <class name>  or
                  <all>
        """
        args = shlex.split(args)
        if len(args) > 0 and args[0] not in class_list:
            print("** class doesn't exist **")
        else:
            objects = []
            for obj in storage.all().values():
                objects.append(obj.__str__())
            print(objects)

    def do_update(self, args):
        """usage
            update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(args)
        objects = storage.all()
        forbidden_attrs = {'id', 'created_at', 'updated_at', '__class__'}
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] not in class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
        elif len(args) == 2 and "{}.{}".format(args[0], args[1]) in objects:
            print("** attribute name missing **")
        elif len(args) == 3 and "{}.{}".format(args[0], args[1]) in objects:
            print("** value missing **")
        elif len(args) > 3 and "{}.{}".format(args[0], args[1]) in objects:
            for obj in storage.all().values():
                if obj.id == args[1] and args[2] not in forbidden_attrs:
                    setattr(obj, args[2], args[3])
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
