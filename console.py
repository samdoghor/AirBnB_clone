#!/usr/bin/python3
"""
Defines HBNBCommand class
This module contains the entry point of the command interpreter
"""

from ast import literal_eval
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """
        Called when an empty line is entered
          - Do nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        Usage: create <class>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        new_obj = storage.CLASSES[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
         Prints the string representation of an instance
         based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all(storage.CLASSES[class_name]):
            print(storage.all(storage.CLASSES[class_name])[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all(storage.CLASSES[class_name]):
            del storage.all(storage.CLASSES[class_name])[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name."""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if class_name not in storage.CLASSES:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in storage.all(
                storage.CLASSES[class_name]).values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change
        into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all(storage.CLASSES[class_name]):
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all(storage.CLASSES[class_name])[key]
        setattr(obj, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
