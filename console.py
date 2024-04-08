#!/usr/bin/python3
"""
Module - the console
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBComand(cmd.Cmd):
    """
    the class that implements the command intepreter
    """
    prompt = '(hbnb) '
    instances = ['BaseModel']
    storage_dict = storage.all()

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

    def do_create(self, line):
        """a function to create a new class of type <line>"""
        if not line:
            print("** class name missing **")
        elif line == 'BaseModel':
            new_base = BaseModel()
            if (isinstance(new_base, BaseModel)):
                print("{}".format(new_base.id))
                new_base.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        a function to Prints the string representation of an
        instance based on the class name and id
        """
        instance_id = None
        if line == "":
            print("** class name missing **")
            return
        new_line = shlex.split(line)
        if len(new_line) == 1:
            print("** instance id missing **")
        instance_name = new_line[0]
        if len(new_line) > 1:
            instance_id = new_line[1]
        if instance_name not in self.instances:
            print("** class doesn't exist **")
        elif instance_id is None:
            print("** instance id missing **")
        else:
            class_id = instance_name + "." + instance_id
            new_dict = self.check_instance(class_id, self.storage_dict)
            if new_dict:
                print(new_dict.to_dict())
            else:
                print("** no instance found **")

    @staticmethod
    def check_instance(class_name, class_dict):
        """
        A static method to check if a dictionary has a key with a
        particular name
        """
        dict_key = class_dict.get(class_name, 0)
        if dict_key == 0:
            return None
        else:
            return dict_key

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if line == "":
            print("** class name missing **")
        else:
            new_args = shlex.split(line)
            if new_args[0] not in self.instances:
                print("** class doesn't exist **")
            else:
                if len(new_args) == 1:
                    print("** instance id missing **")
                else:
                    dict_key = ".".join(new_args)
                    if self.check_instance(dict_key, self.storage_dict):
                        storage.delete(dict_key)
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name"""
        exists = False
        if line == "":
            new_dict = storage.all()
            for key, value in new_dict.items():
                print(value.to_dict())
        else:
            for item in self.instances:
                if item.startswith(line):
                    exists = True
            if not exists:
                    print("** class doesn't exist **")
            else:
                for key, value in new_dict.items():
                    if key.startswith(line):
                        print(value.to_dict())

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute (save the change
        into the JSON file)"""
        if line == "":
            print("** class name is missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.instances:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_id = args[0] + "." + args[1]
            obj_dict = self.check_instance(class_id, self.storage_dict)
            if not obj_dict:
                print("** no instance found **")
                return
            else:
                try:
                    if obj_dict.to_dict().get(args[2], 0) == 0:
                        print("** attribute name missing **")
                    else:
                        obj_dict.to_dict()[args[2]] = args[3]
                        storage.save()
                except Exception:
                    pass


if __name__ == '__main__':
    HBNBComand().cmdloop()
