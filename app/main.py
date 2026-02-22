import sys

def echo(args=""):
    print(f"{args}")
    
def Practice(args=""):
    print("This a pa practice command")

#Dictionary of functions
COMMAND = {
    "ECHO" : echo,
    "PRACTICE" : Practice 
}


def main():
     while True:
        user_input = input("$ ").strip()

        #exits the loop
        if user_input.lower() == "exit":
            break

        #Commands and functions
        parts = user_input.split(" ", 1)
        command_name = parts[0].upper()

        #This gets the command and everything else after it, if needed
        args = parts[1] if len(parts) > 1 else ""
        
        command_func = COMMAND.get(command_name)
        if command_func:
            command_func(args)
        else:
            print(f"{user_input} not found")
            


if __name__ == "__main__":
    main()
