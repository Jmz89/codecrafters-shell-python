import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
     sys.stdout.write("$ ")
     user = input()
     while(user != '1'):
        print(f"{user}: command not found")
        sys.stdout.write("$ ")
        user = input()
pass


if __name__ == "__main__":
    main()
