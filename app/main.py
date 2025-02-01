import sys


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

        print(command + ":","command not found") 


if __name__ == "__main__":
    main()
