version = "0.0.1"
balance_path = "./balance.txt"

try:
    current_balance = float(open(balance_path, "r").read())
except:
    print(f"v.{version}: Please make sure you are running the command from the correct directory")
    exit()

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

print(f'Transaction Manager v.{version}')
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
        print("COMMANDS")
        print("-------------")
        print("get -> get current balance")
        print("add -> add funds")
        print("remove -> remove funds")
        print("exit -> exit Transaction Manager")
        print("-------------")
    elif command == "get":
        with open(balance_path, "r") as file_read:
            current_balance = file_read.read()
            current_balance = float(current_balance)
            file_read.close()
        print_balance()
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
