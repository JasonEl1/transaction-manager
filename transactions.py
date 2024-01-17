current_balance = float(open("balance.txt", "r").read())

def print_balance():
    print(f'Your current balance is ${current_balance}')

def add_amount(amount):
    with open("balance.txt","w") as file_write:
        file_write.write(str(current_balance+amount))
        print(f'added {str(amount)} to balance')
        file_write.close()

def remove_amount(amount):
    file_write = open("balance.txt","w")
    file_write.write(str(current_balance-amount))
    print(f'removed {str(amount)} to balance')
    file_write.close()

version = "0.0.1"

print(f'Transaction Manager v.{version}')
print("enter 'help' for a list of commands")
print("-----------------------------------")

with open("balance.txt", "r") as file_read:
    current_balance = file_read.read()
    current_balance = float(current_balance)
    file_read.close()
print_balance()

while(True):
    command = input()

    with open("balance.txt", "r") as file_read:
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
        with open("balance.txt", "r") as file_read:
            current_balance = file_read.read()
            current_balance = float(current_balance)
            file_read.close()
        print_balance()
    elif command == "add":
        amount = float(input("Amount to add: "))
        add_amount(amount)
        with open("balance.txt", "r") as file_read:
            current_balance = file_read.read()
            current_balance = float(current_balance)
            file_read.close()
        print_balance()
    elif command=="remove":
        amount = float(input("Amount to remove: "))
        remove_amount(amount)
        with open("balance.txt", "r") as file_read:
            current_balance = file_read.read()
            current_balance = float(current_balance)
            file_read.close()
        print_balance()
    elif command=="exit":
        exit()
    else:
        print("Unknown command. Enter 'help' for a list of commands")
