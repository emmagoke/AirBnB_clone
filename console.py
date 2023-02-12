#!/usr/bin/python3
"""
"""
import sys
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = '(hbnb)'

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file)
        """
        if line == "BaseModel":
            obj = eval("models.base_model" + '.' +"{}()".format(line))
            print(obj.id)

    def do_EOF(self, arg):
        """
        """
        return True

    def emptyline(self):
        """This method handle situation where empty Lines is
        typed into the console."""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
