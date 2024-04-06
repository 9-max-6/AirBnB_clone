#!/usr/bin/python3
"""
Module - the console
"""
import cmd


class HBNBComand(cmd.Cmd):
    """
    the class that implements the command intepreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """A function to handle quit command"""
        return True

    def help_quit(self):
        """Function to give help doc for quit command"""
        print("Quit command to exit the program")
        print("")
        print("")

    def emptyline(self) -> bool:
        """A function to override the empty line function of Cmd class"""
        return

    def do_EOF(self):
        """A function to handle the EOF input from the user."""
        return True


if __name__ == '__main__':
    HBNBComand().cmdloop()
