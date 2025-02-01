import sys,string
import os

shell_builtins = set(['echo','exit','type'])
builtins = {}

def command_not_found(command: string):
    print(command + ":","not found") 

def is_executable(file_path: string):
    return os.path.isfile(file_path) and os.access(file_path, os.X_OK)

def load_execs_in_path_env():
    global builtins
    path_dirs = set(os.getenv("PATH").split(":"))
    try:
        for dir in path_dirs:
            builtins.update({entry.name : entry.path for entry in os.scandir(dir) if is_executable(entry.path)})
            #print(builtins)
    except FileNotFoundError:
        pass
    

def main():
    # Uncomment this block to pass the first stage
    global builtins, shell_builtins
    while True:
        sys.stdout.write("$ ")
        # load all the executable files in path env.
        load_execs_in_path_env()
        # Wait for user input
        command = input()
        command_parts = command.split()
        if len(command_parts) > 1:
            if command_parts[0] == 'exit' and command_parts[1] == '0':
                sys.exit(0)
            if command_parts[0] == 'echo':
                print(" ".join(command_parts[1:]))
            if command_parts[0] == 'type':
                if command_parts[1] in shell_builtins:
                    print(command_parts[1],'is a shell builtin')
                elif command_parts[1] in builtins:
                    print(command_parts[1], 'is', builtins[command_parts[1]])
                else:
                    command_not_found(command_parts[1])
        else:
            command_not_found(command)


if __name__ == "__main__":
    main()
