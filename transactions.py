###   version 0.3.0   ###

import subprocess
import sys
from datetime import datetime
from os import system
from os.path import exists
import os


fullpath = os.path.abspath(__file__)
name_len = len(os.path.basename(__file__))
temppath = fullpath[:-name_len]

balance_path = f"{temppath}/balance.txt"
log_path = f"{temppath}/transaction-log.txt"

open(log_path, 'a').close()


try:
    current_balance = float(open(balance_path, "r").read())
except:
    print(f"Creating personal file at {balance_path}...")
    with open(balance_path, 'w') as file_write:
         file_write.write("0.00")
         file_write.close()

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
    print("set <amount> -> set new balance")
    print("add <amount> -> add funds")
    print("remove <amount> -> remove funds")
    print("note <message> -> add note to transaction log")
    print("log <entries> -> get most recent transaction log entries")
    print("log clear -> clear all transaction log entries")
    print("-------------")

def print_balance():
    bal = current_balance
    bal = '%.2f' % bal
    print(f'Your  balance is ${bal}')

def add_amount(amount):
    with open(balance_path,"w") as file_write:
        file_write.write(str(current_balance+amount))
        amount = '%.2f' % amount
        print(f'added ${str(amount)} to balance')
        file_write.close()
    with open(log_path,"a") as file_write:
        file_write.write(f"\n{get_datetime()} Added ${amount} to balance.")
        file_write.close()

def remove_amount(amount):
    file_write = open(balance_path,"w")
    amount = float('%.2f' % amount)
    file_write.write(str(current_balance-amount))
    print(f'removed ${str(amount)} from balance')
    file_write.close()

    with open(log_path,"a") as file_write:
        file_write.write(f"\n{get_datetime()} Removed ${'%.2f' % amount} from balance.")

def print_transaction_log(entries):
    with open(log_path,"r") as file_read:
        lines = file_read.readlines()
        lines = list(reversed(lines))
        if len(lines)>0:
            print("------------TRANSACTION LOG---------------")
            for x in range(int(entries)):
                try:
                    print(lines[x].strip("\n"))
                except:
                    break
            print("------------------------------------------")
        else:
            print("No entries in log")
        file_read.close()


arg_count = len(sys.argv)
if arg_count > 1:
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
                amount = '%.2f' % amount
            print(f"Balance set to ${amount}")
            with open(log_path,"a") as file_write:
                file_write.write(f"\n{get_datetime()} Balance set to ${'%.2f' % float(sys.argv[2])}.")
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
    elif sys.argv[1] == "note":
        message = sys.argv[2]
        if arg_count>2:
            with open(log_path,"a") as file_write:
                file_write.write(f"\n{get_datetime()} {message}")
                file_write.close()
            print(f"Logged: '{message}'")
        else:
            print("No note entered")
    elif sys.argv[1] == "log":
        entries = 0
        if arg_count>2:
            type = ""
            try:
                arg = int(sys.argv[2])
                type = "int"
            except ValueError:
                type = "str"
            if type=="int":
                if int(sys.argv[2])>0:
                    entries = int(sys.argv[2])
                print_transaction_log(entries)
            elif type=="str" and sys.argv[2] == "clear":
                open(log_path, 'w').close()
                print("Transaction log cleared")
        else:
            entries = 10
            print_transaction_log(entries)
    else:
        print("Unknown command. Enter 'help' for a list of commands")
else:
    print(f"Try entering a command")

    exit()
