#!/usr/bin/python3
"""module that contains cmd program"""

import cmd


class HBNBCommand(cmd.Cmd):
    """simple console app for managing my airbnb application"""

    prompt = '(hbnb) '

    def emptyline(self):
        """empty line should not execute anything"""
        pass

    def do_EOF(self, line):
        """handle end of file character"""
        return True

    def do_quit(self, s):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop('')
