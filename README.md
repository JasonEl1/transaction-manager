# transaction-manager

A simple python command line tool to keep track of your transactions, intended to be used for cash transactions.

### Quick setup (MacOS)

Open the `transaction-manager` folder and enter this command:

`bash alias.sh`

this will create an alias in your ~/.zshrc file. You can then use the name of your alias followed by a command. The rest of this guide will assume a chosen alias name of `cash`.

### How to use transaction-manager:

enter `cash` (or alternative chosen alias) into the terminal, followed by the appropriate number of arguments, depending on the specific command. After execution of the specified command, the tool will close automatically.

### Commands:

```
help -> display a list of commands
get -> get current account balance
set <balance> -> set new account balance
add <amount> -> add specified <amount> to account balance
remove <amount> -> remove specified <amount> from account balance
note <message> -> add note to transaction log
log <entries> -> get last <entries> transaction log entries
log clear -> clear all entries from transaction log
```
