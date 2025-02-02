import sys,string
import os,subprocess
import random

from typing import Optional

def command_not_found(command: string):
    print(command + ":","not found") 

def handle_type(args):
    global shell_builtins
    if args[0] in shell_builtins:
        print(args[0],'is a shell builtin')
    elif exec := locate_executable(args[0]):
        print(f"{args[0]} is {exec}")
    else:
        command_not_found(args[0])

def handle_exit(args):
    if args[0] == '0':
        sys.exit(0)
    else:
        command_not_found('exit')

def handle_echo(args):
    print(" ".join(args))

def locate_executable(command) -> Optional[string]:
    path_dirs = set(os.environ.get("PATH","").split(":"))
    try:
        for dir in path_dirs:
            file_path = os.path.join(dir,command)
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                return file_path
    except FileNotFoundError:
        pass

def handle_executable(command, args):
    subprocess.run([command, *args])

def handle_pwd(args):
    print(os.getcwd())

def handle_cd(args):
    try:
        os.chdir(args[0])
    except OSError:
        print(f"cd: {args[0]}: No such file or directory")


shell_builtins = {
    "echo": handle_echo,
    "exit": handle_exit,
    "type": handle_type,
    "pwd": handle_pwd,
    "cd": handle_cd
}   

def main():
    global shell_builtins

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command, *args = input().split()
        if command in shell_builtins:
            shell_builtins[command](args)
        # If command is part of the builtins, run it.
        elif executable := locate_executable(command):
            handle_executable(command, args)
        else:
            command_not_found(command)


if __name__ == "__main__":
    main()
