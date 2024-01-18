import sys

version = "0.1.0"
mode = "normal"

user = input("User: ")
balance_path = f"/Users/{user}/Downloads/transaction-manager/balance.txt"

try:
    current_balance = float(open(balance_path, "r").read())
except:
    print(f"v{version}: Please make sure you are running the command from the correct directory")
    exit()

if len(sys.argv)>1:
    mode = "express"

def print_help():
    print("COMMANDS")
    print("-------------")
    print("get -> get current balance")
    print("set -> set new balance")
    print("add -> add funds")
    print("remove -> remove funds")
    print("exit -> exit Transaction Manager")
    print("-------------")

def print_balance():
    print(f'Your  balance is ${current_balance}')

def add_amount(amount):
    with open(balance_path,"w") as file_write:
        file_write.write(str(current_balance+amount))
        print(f'added {str(amount)} to balance')
        file_write.close()

def remove_amount(amount):
    file_write = open(balance_path,"w")
    file_write.write(str(current_balance-amount))
    print(f'removed {str(amount)} to balance')
    file_write.close()

if mode == "normal":

    print(f'Transaction Manager v{version}')
    print("enter 'help' for a list of commands")
    print("-----------------------------------")

    with open(balance_path, "r") as file_read:
        current_balance = file_read.read()
        current_balance = float(current_balance)
        file_read.close()
    print_balance()

    while(True):
        command = input()

        with open(balance_path, "r") as file_read:
            current_balance = file_read.read()
            current_balance = float(current_balance)
            file_read.close()

        if command=="help":
            print_help()
        elif command == "get":
            with open(balance_path, "r") as file_read:
                current_balance = file_read.read()
                current_balance = float(current_balance)
                file_read.close()
            print_balance()
        elif command == "set":
            amount = float(input("New balance: "))
            with open(balance_path, "w") as file_write:
                file_write.write(str(amount))
                file_write.close()
            print(f"Balance set to {amount}")
        elif command == "add":
            amount = float(input("Amount to add: "))
            add_amount(amount)
            with open(balance_path, "r") as file_read:
                current_balance = file_read.read()
                current_balance = float(current_balance)
                file_read.close()
            print_balance()
        elif command=="remove":
            amount = float(input("Amount to remove: "))
            remove_amount(amount)
            with open(balance_path, "r") as file_read:
                current_balance = file_read.read()
                current_balance = float(current_balance)
                file_read.close()
            print_balance()
        elif command=="exit":
            exit()
        else:
            print("Unknown command. Enter 'help' for a list of commands")

elif mode == "express":
    arg_count = len(sys.argv)
    if arg_count>2:
        print(str(sys.argv[2]))

    with open(balance_path, "r") as file_read:
        current_balance = file_read.read()
        current_balance = float(current_balance)
        file_read.close()

    if sys.argv[1]=="help":
        print_help()
    elif sys.argv[1] == "get":
        with open(balance_path, "r") as file_read:
            current_balance = file_read.read()
            current_balance = float(current_balance)
            file_read.close()
        print_balance()
    elif sys.argv[1] == "set":
        if arg_count>2:
            amount = float(sys.argv[2])
            with open(balance_path, "w") as file_write:
                file_write.write(str(amount))
                file_write.close()
            print(f"Balance set to {amount}")
        else:
            print("No amount set")
    elif sys.argv[1] == "add":
        if arg_count>2:
            amount = float(sys.argv[2])
            add_amount(amount)
            with open(balance_path, "r") as file_read:
                current_balance = file_read.read()
                current_balance = float(current_balance)
                file_read.close()
            print_balance()
        else:
            print("No add amount specified")
    elif sys.argv[1] =="remove":
        if arg_count>2:
            amount = float(sys.argv[2])
            remove_amount(amount)
            with open(balance_path, "r") as file_read:
                current_balance = file_read.read()
                current_balance = float(current_balance)
                file_read.close()
            print_balance()
        else:
            print("No remove amount specified")
    else:
        print("Unknown command. Enter 'help' for a list of commands")

    exit()
