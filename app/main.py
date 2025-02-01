import sys,string

builtins = set(['echo','exit','type'])

def command_not_found(command: string):
    print(command + ":","not found") 


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        command_parts = command.split()
        if len(command_parts) > 1:
            if command_parts[0] == 'exit' and command_parts[1] == '0':
                sys.exit(0)
            if command_parts[0] == 'echo':
                print(" ".join(command_parts[1:]))
            if command_parts[0] == 'type':
                global builtins
                if command_parts[1] in builtins:
                    print(command_parts[1],'is a shell builtin')
                else:
                    command_not_found(command_parts[1])
        else:
            command_not_found(command)


if __name__ == "__main__":
    main()
