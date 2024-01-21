# transaction-manager
A simple python command line tool to keep track of your transactions. Intended to be used for cash transactions.

### Quick setup (MacOS)

Open the `transaction-manager` folder and enter this command:

`bash alias.sh`

this will create an alias named `cash` in your ~/.zshrc file. You can then use `cash` followed by a command or just `cash` alone use the transaction manager.

### How to use transaction-manager:

**There are two ways to use transaction-manager : `normal` mode and `express` mode**

`normal` mode:

enter `cash` (or alternative chosen alias) into the terminal and the tool will start. You will be greeted with a welcome message and will have the option to enter as many commands as you would like before using the `exit` command to close the tool. The `help` command is also available to display a list of valid commands.

***

`express` mode:

enter `cash` (or alternative chosen alias) into the terminal, followed by either one or two arguments. The number of arguments required depends on the specific commands. See the list of commands below for all valid commands available for use in `express` mode. After execution of the specified command, the tool will close itself automatically.

### Commands:

**`normal` and `express` modes:**
```
help -> display a list of valid commands
get -> get current account balance
```
***
**`normal` mode only:**
```
exit -> close transaction-manager
set -> set new account balance
add -> add specified amount to account balance
remove -> remove specified amount from account balance
log -> output recent transaction log entries
```
***
**`express` mode only:**
```
set <balance> -> set new account balance
add <amount> -> add specified <amount> to account balance
remove <amount> -> remove specified <amount> from account balance
log <entries> -> get last <entries> transaction log entries
log clear -> clear all entries from transaction log
```
