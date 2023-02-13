#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command intepreter which inherits from base class cmd"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """CRTL+D command to exit the program"""
        return True

    def emptyline(self):
        """Called when empty line + ENTER key,
        returns newline and does not execute any commands"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
