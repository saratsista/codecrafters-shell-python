import sys,string
import os,subprocess
import random

from typing import Optional

shell_builtins = set(['echo','exit','type'])
builtins = {}

def command_not_found(command: string):
    print(command + ":","not found") 

def is_executable(file_path: string):
    return os.path.isfile(file_path) and os.access(file_path, os.X_OK)

def locate_executable(command) -> Optional[string]:
    path_dirs = set(os.environ.get("PATH","").split(":"))
    try:
        for dir in path_dirs:
            file_path = os.path.join(dir,command)
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                return file_path
    except FileNotFoundError:
        pass

def handle_type(args):
    global shell_builtins
    if args[0] in shell_builtins:
        print(args[0],'is a shell builtin')
    elif exec := locate_executable(args[0]):
        print(f"{args[0]} is {exec}")
    else:
        command_not_found(args[0])

def handle_executable(command, args):
    subprocess.run([command, *args])


    

def main():
    global shell_builtins

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command, *args = input().split(" ")
        if command == 'exit' and args[0] == '0':
            sys.exit(0)
        elif command == 'echo':
            print(" ".join(args))
        elif command == 'type':
            handle_type(args)
        # If command is part of the builtins, run it.
        elif executable := locate_executable(command):
            handle_executable(command, args)
        else:
            command_not_found(command)


if __name__ == "__main__":
    main()
