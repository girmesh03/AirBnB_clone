#!/usr/bin/python3

import cmd
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models import storage
import sys
from re import search

"""This module contains the entry point of the command interpreter.
The command interpreter is a tool that allows us to manage the objects
of our project:
    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc
    - Do operations on objects (count, compute stats, etc)
    - Update attributes of an object
    - Destroy an object
"""


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HolbertonBnB project.
    """
    prompt = "(hbnb) "
    __classes = ['BaseModel', 'User', 'State',
                 'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """
        Exit command to quit the program.
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_EOF(self, arg):
        """
        Called when the end-of-file character is read in the prompt.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of a class and saves it to a JSON file.
        """
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return

        class_name = arg_list[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            obj = getattr(sys.modules[__name__], class_name)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return

        class_name = arg_list[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        if len(arg_list) == 2:
            key = "{}.{}".format(class_name, instance_id)
            objs = storage.all()

            if key not in objs:
                print("** no instance found **")
                return
            else:
                obj = objs[key]
                print(obj)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id and
        saves the changes to a JSON file.
        """

        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return

        class_name = arg_list[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        if len(arg_list) == 2:
            instance_id = arg_list[1]
            key = "{}.{}".format(class_name, instance_id)
            objs = storage.all()

            if key not in objs:
                print("** no instance found **")
                return
            else:
                del objs[key]
                storage.save()

    def do_all(self, arg):
        """This method prints all string representation of all instances
        based or not on the class name."""

        arg_list = shlex.split(arg)
        objs = storage.all()
        obj_list = []

        # If no argument is provided, print all instances
        if len(arg_list) == 0:
            for obj in objs.values():
                obj_list.append(str(obj))
            print(obj_list)

        # If a class name is provided, print all instances of that class
        else:
            class_name = arg_list[0]

            # Check if class exists
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return

            # Iterate through all instances and
            # append string representation to list
            for obj in objs.values():
                if obj.__class__.__name__ == class_name:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, args):
        """This method updates an instance based on the class name
        and id by adding or updating attribute."""

        if not args:
            print("** class name missing **")
            return
        arg = shlex.split(args)
        # storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(arg) == 2):
            print("** attribute name missing **")
            return
        if (len(arg) == 3):
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if arg[2] in obj_dict.keys():
            d_type = type(obj_dict[arg[2]])
            print(d_type)
            obj_dict[arg[2]] = type(obj_dict[arg[2]])(arg[3])
        else:
            obj_dict[arg[2]] = arg[3]
        storage.save()

    def do_update2(self, args):
        """This function updates an instance based on the class name
        and id by adding or updating attribute"""

        if not args:
            print("** class name missing **")
            return
        my_dict = "{" + args.split("{")[1]
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dict == "{"):
            print("** attribute name missing **")
            return
        my_dict = my_dict.replace("\'", "\"")
        my_dict = json.loads(my_dict)
        obj_inst = obj[obj_key]
        for k in my_dict:
            if hasattr(obj_inst, k):
                d_type = type(getattr(obj_inst, k))
                setattr(obj_inst, k, my_dict[k])
            else:
                setattr(obj_inst, k, my_dict[k])
        storage.save()

    def do_count(self, args):

        obj = storage.all()
        cnt = 0
        for key in obj:
            if (args in key):
                cnt += 1
        print(cnt)

    def default(self, args):
        """Default method for cmd module.
        This method is called on an input line when the command prefix is
        not recognized.  If this method is not overridden, it repeats the
        line."""

        cmd_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        arg = args.strip()
        val = arg.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = val[0]
        command = val[1].split("(")[0]
        line = ""
        if (command == "update" and val[1].split("(")[1][-2] == "}"):
            inputs = val[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = val[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in cmd_dict.keys()):
            cmd_dict[command](line.strip())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
