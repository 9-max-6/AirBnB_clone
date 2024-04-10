#!/usr/bin/python3
"""
Module - the console
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from  models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBComand(cmd.Cmd):
    """
    the class that implements the command intepreter
    """
    prompt = '(hbnb) '
    instances = ['BaseModel', 'User', 'State', 'City', 'Review',
                 'Place', 'Amenity']
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
        if line in self.instances:
            print(line)
            new_base = eval(f'{line}()')
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
                print(new_dict)
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
        new_dict = storage.all()
        if line == "":
            for key, value in new_dict.items():
                print(value)
        else:
            for item in self.instances:
                if item.startswith(line):
                    exists = True
            if not exists:
                print("** class doesn't exist **")
            else:
                for key, value in new_dict.items():
                    if key.startswith(line):
                        print(value)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute (save the change
        into the JSON file)"""
        if line == "":
            print("** class name missing **")
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
                new_dict = obj_dict.to_dict()
                new_dict[args[2]] = args[3]
                class_name = args[0]
                new = eval(f'{class_name}(**new_dict)')
                new.save()

    def default(self, line):
        """A function to handle all other commands"""
        if '.' in line:
            new_line = line.split('.')
            class_name = new_line[0]
            command = new_line[1]
            new_dict = storage.all()
            if command == 'all()':
                for key, value in new_dict.items():
                    if key.startswith(class_name):
                        print(value)
            elif command == 'count()':
                count = 0
                for key, value in new_dict.items():
                    if key.startswith(class_name):
                        count += 1
                print(count)
            elif command.startswith('show'):
                id = command[6:-2]
                present = False
                for key, value in new_dict.items():
                    key_class = key.split('.')[0]
                    key_id = key.split('.')[1]
                    print(key_id)
                    if key_id == id and key_class == class_name:
                        print(value)
                        present = True
                if not present:
                    print("** no instance found **")
            elif command.startswith('destroy'):
                id = command[9:-2]
                keys_to_delete = None
                for key, value in new_dict.items():
                    if key.endswith(id):
                        keys_to_delete = key
                        break
                if keys_to_delete:
                    storage.delete(keys_to_delete)
                else:
                    print("** no instance found **")
            elif command.startswith('update'):
                line = command[7:-1]
                new_line = line.split(',')
                a = b = c =""
                try:
                    a = new_line[0].strip()
                    b = new_line[1].strip()
                    c = new_line [2].strip()
                except IndexError:
                    pass
                final_line = (f'{class_name} {a} {b} {c}')
                self.do_update(final_line)



if __name__ == '__main__':
    HBNBComand().cmdloop()
