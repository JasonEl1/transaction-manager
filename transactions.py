from sre_constants import AT_BEGINNING_STRING
import subprocess
import sys
from datetime import datetime
from os import system
import subprocess

version = "0.2.0"
mode = "normal"

user = subprocess.getstatusoutput('id -un')
user = user[1]
balance_path = f"/Users/{user}/Downloads/transaction-manager/balance.txt"
log_path = f"/Users/{user}/Downloads/transaction-manager/transaction-log.txt"

try:
    current_balance = float(open(balance_path, "r").read())
except:
    print("Invalid username")
    exit()

def clean_log():
    with open(log_path, "r") as f:
        lines = f.readlines()
    with open(log_path, "w") as f:
        for line in lines:
            if line.strip("\n") != "":
                f.write(line)
clean_log()

if len(sys.argv)>1:
    mode = "express"

def get_datetime():
    now = datetime.now()
    now = now.strftime("%d-%m-%y %H:%M:%S")
    return now

def print_help():
    print("COMMANDS")
    print("-------------")
    print("get -> get current balance")
    print("set -> set new balance")
    print("add -> add funds")
    print("remove -> remove funds")
    print("log -> get most recent transaction log entries")
    print("exit -> exit Transaction Manager")
    print("-------------")

def print_balance():
    print(f'Your  balance is ${current_balance}')

def add_amount(amount):
    with open(balance_path,"w") as file_write:
        file_write.write(str(current_balance+amount))
        print(f'added {str(amount)} to balance')
        file_write.close()
    with open(log_path,"a") as file_write:
        file_write.write(f"\n{get_datetime()} Added S{amount} to balance.")
        file_write.close()

def remove_amount(amount):
    file_write = open(balance_path,"w")
    file_write.write(str(current_balance-amount))
    print(f'removed {str(amount)} to balance')
    file_write.close()

    with open(log_path,"a") as file_write:
        file_write.write(f"\n{get_datetime()} Removed S{amount} from balance.")
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
            with open(log_path,"a") as file_write:
                file_write.write(f"\n{get_datetime()} Balance set to S{amount}.")
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
        elif command=="log":
            amount = input("Entries to display: ")
            clean_log()
            with open(log_path,"r") as file_read:
                lines = file_read.readlines()
                for x in range(int(amount)):
                    try:
                        print(lines[x])
                    except:
                        break
                file_read.close()
        elif command=="exit":
            exit()
        else:
            print("Unknown command. Enter 'help' for a list of commands")

elif mode == "express":
    arg_count = len(sys.argv)

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
            with open(log_path,"a") as file_write:
                file_write.write(f"\n{get_datetime()} Balance set to ${sys.argv[2]}.")
                file_write.close()
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
    elif sys.argv[1] == "log":
        if arg_count>2:
            try:
                argv2 = int(sys.argv[2])
                if int(sys.argv[2])>0:
                    entries = int(sys.argv[2])
                    with open(log_path,"r") as file_read:
                        lines = file_read.readlines()
                        if len(lines)>0:
                            print("------------TRANSACTION LOG------------")
                            for x in range(int(entries)):
                                try:
                                    print(lines[x].strip("\n"))
                                except:
                                    break
                        else:
                            print("No entries in log")
                        file_read.close()
            except ValueError:
                open(log_path, 'w').close()
                print("Transaction log cleared")

        else:
            print("Please specify number of entries")
    else:
        print("Unknown command. Enter 'help' for a list of commands")

    exit()
