# transaction-manager
A simple python command line tool to keep track of your transactions. Intended to be used for cash transactions.

### How to add alias to command line: (MacOS)

Open the terminal and enter this command:

`vim ~/.zshrc`

You can replace `vim` with the alias of any other text editor you wish to use.

Once editing the file, insert the following line:

`alias cash="python3 /Users/yourusername/downloads/transaction-manager/transactions.py`

Note that this is the default download location but you can edit this line to suit your preferences. You can also change the alias name from `cash` to anything else you want it to be.

Save the file and restart the terminal. Entering `cash` into the terminal will start the command line script.

### How to use transaction-manager:

**There are two ways to use transaction-manager : `normal` mode and `express` mode**

`normal` mode:

enter `cash` (or alternative chosen alias) into the terminal and the tool will start. You will be greeted with a welcome message and will have the option to enter as many commands as you would like before using the `exit` command to close the tool. The `help` command is also available to display a list of valid commands.

***

`express` mode:

enter `cash` (or alternative chosen alias) into the terminal, followed by either one or two arguments. The number of arguments required depends on the specific commands. See the list of commands below for all valid commands available for use in `express` mode. After execution of the specified command, the tool will close itself automatically.

### Commands:

```
help -> display a list of valid commands
get -> get current account balance
set <balance> -> set new account balance
add <amount> -> add specified amount to account balance
remove <amount> -> remove specified amount from account balance
exit -> close transaction-manager
```

**Note that `exit` command is not available in `express` mode.**
