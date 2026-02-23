import sys
import shutil
import subprocess

#Repeats what user said on a new line
def echo(args=""):
    print(f"{args}")
    
#Pracitce
def practice(args=""):
    print("This a practice command")

#Checks to see if a command is a shell built in
def type(args=""):
    command_func = COMMAND.get(args.upper())
    if command_func:
        print(f"{args} is a shell builtin ")
    elif path := shutil.which(args):
        print(f"{args} is {path} ")
    else:
        print(f"{args}: not found")

#Exits the loop
def exit(args=""):
    sys.exit(0)



#Dictionary of functions
COMMAND = {
    "ECHO" : echo,
    "PRACTICE" : practice, 
    "TYPE" : type,
    "EXIT" : exit
}


def main():
     while True:
        user_input = input("$ ").strip()

        #Commands and functions
        parts = user_input.split(" ", 1)
        command_name = parts[0].upper()
        file_name = user_input.split(" ", 1)

        #This gets the command and everything else after it, if needed
        args = parts[1] if len(parts) > 1 else ""
        
        command_func = COMMAND.get(command_name)
        if command_func:
            command_func(args)
        elif path := shutil.which(file_name):
            arguments = [word for word in user_input.split(" ") if word != ""]
            file = ",".join(arguments)
            subprocess.run(file)
        else:
            print(f"{user_input}: command not found")
            


if __name__ == "__main__":
    main()
