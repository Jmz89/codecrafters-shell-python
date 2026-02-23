import sys
import shutil
import subprocess
import os
import shlex

#Repeats what user said on a new line
def echo(args=""):
    if args.startswith("'") and args.endswith("'"):
        args = shlex.split(args)
        args = " ".join(args)
        print(f"{args}")
    else:
        args = shlex.split(args)
        args = " ".join(args)
        print(f"{" ".join(args.split())}")

def echo_test(args=""):
     args = shlex.split(args)
     print(" ".join(args))
     
    
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

def pwd(args=""):
    path = os.getcwd()
    print(path)

def cd(args=""):
    directory_path = args
    if args == "~" :
        Home = os.getenv('HOME') or os.getenv('USERPROFILE')
        os.chdir(Home)
        
    elif os.path.isdir(args):
        os.chdir(args)
    else:
        print(f"cd: {args}: No such file or directory")
    




#Dictionary of functions
COMMAND = {
    "ECHO" : echo,
    "PRACTICE" : practice, 
    "TYPE" : type,
    "EXIT" : exit,
    "PWD" : pwd,
    "CD" : cd,
    "TECHO" : echo_test
}


def main():
     while True:
        user_input = input("$ ").strip()

        #Commands and functions
        parts = user_input.split(" ", 1)
        command_name = parts[0].upper()

        #This gets only the file name
        file_name = parts[0]

        #This gets the command and everything else after it, if needed
        args = parts[1] if len(parts) > 1 else ""
        
        command_func = COMMAND.get(command_name)
        if command_func:
            command_func(args)
        elif path := shutil.which(file_name):
            subprocess.run(user_input.split())
        else:
            print(f"{user_input}: command not found")
            


if __name__ == "__main__":
    main()
