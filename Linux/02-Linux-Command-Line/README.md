# Linux Command Line

## The login prompt

All Linux sessions begin with the login process (default authentication process). Linux sessions start with the user entering their user name at the prompt. The login prompt is used to authenticate (prove the user’s identity) before using a Linux system. But note when the password is typed it does not display any text.

The user name is checked against the `/etc/.psswd` file, which is stored in the `/etc` directory. The file represents an individual user account and contains the following fields separated by colons (:)

1. User name or login name
2. Encrypted password
3. User ID
4. Group ID
5. User description
6. User’s home directory
7. User’s login shell

## The login workflow

Sure, here's a simplified explanation:

When you log into a Linux system, it needs to verify your username and password. It does this by checking two files: `/etc/passwd` for your username and `/etc/shadow` for your password.

The username you enter is compared with the usernames in the `/etc/passwd` file. If it finds a match, it then checks the password.

The password check is a bit more complicated. In the past, passwords were stored in the `/etc/passwd` file, but for security reasons, they've been moved to a separate file called `/etc/shadow`. So, when you enter your password, it's actually checked against the `/etc/shadow` file.

One thing to note is that Linux is case-sensitive, which means it treats lowercase and uppercase letters as different characters. So, a username like "salazar" is not the same as "Salazar". To avoid confusion, it's best to stick with lowercase letters for your username.

Lastly, the username field can only hold a maximum of 32 characters. Anything beyond that will be cut off.

After logging in the user is presented with a command prompt. The user’s current working directory will be their home directory.

## Anatomy of the command prompt

The default shell in Linux is Bash, which provides the command prompt. The Linux command prompt or command line is a text interface to your Linux computer. It is commonly referred to as the shell, terminal, console, or prompt. The default shell contains the user name, and the user's home directory has the same name as the user (which it does by default). Although this format is common, it is changeable and not always consistent in different Linux distributions.

## Command syntax example

Most commands in Linux follow syntax rules. Depending on the command, the syntax comprises the command itself, an option, and an argument. The best way to describe the command syntax is as follows:

```bash
man -i whoami
```

- `Command:` What you want Linux to do
- `Option:` Modifies the command
- `Argument:` What the command acts on

## The `whoami` command

In Linux, it's used to show the current user's user name when the command is invoked. A use case for this command would be to use it after you log in as UserA. Then, switch users and run commands as another user to see the context.

## The `id` command

This command helps identify the user and group name and numeric IDs (UID or group ID) of the current user or any other user on the server. This command displays the user and group information for each specified USER or (when USER is omitted) for the current user.

## The `hostname` command

This command displays the TCP/IP hostname. The `hostname` is used to either set or display the system's current host, domain, or node name. Many networking programs use hostnames to identify the system.

## The `uptime` command

This command indicates how long the system has been up since the last boot.

## The `date` command

This command can display the current time in a given forma.It can also set the system date.

## The `cal` command

The `cal` command is used to display a calendar. If no arguments are specified, the current month is displayed.

## The `clear` command

The `clear` command is used to clear the terminal screen. This command, when ran, clears all text on the terminal screen and displays a new prompt.

## The `echo` command

The `echo` command places specified text on the screen. It is useful in scripts to provide users with information as the script runs. It directs selected text to standard output or in scripts to provide descriptions of displayed results.

## The `history` command

Bash keeps a history of each user's commands in a file in that user's home directory. The `history` command views the history file.

## The `touch` command

The `touch` command can be used to create, change, or modify timestamps on existing files.Also, the `touch` command is used to create a new empty file in a directory.

## The `cat` command

The `cat` command is used to show contents of files and outputs it to the standard output. This command is useful to administrators because Linux configurations are held in text files.

## Standard input `–stdin` command

"Standard input" (often abbreviated as `stdin`) is a way that a program gets information. This could be from a user typing in information or from a file. In the world of programming, we often refer to these sources of information as "file handles".

In Linux, `stdin` is represented by the number `0`. So when you see `0`, think "this is where my program is getting its information from".

The `cat` command is a common command in Linux that reads data from `stdin` and outputs it. In the example `cat 0<myfirstscript`, the `cat` command is being told to read its information from the file `myfirstscript` instead of the keyboard input from a user.

The `<` symbol is what's doing the redirecting here. It's saying "don't get your information from the keyboard like you usually do, get it from `myfirstscript` instead".

So, in simple terms, `cat 0<myfirstscript` is a command that tells your computer "display the contents of the file `myfirstscript` on the screen".

## Standard output  `-stdout` command

"Standard output", often abbreviated as `stdout`, is a way that a program sends information out. This could be text that you see in the terminal after running a command.

In Linux, `stdout` is represented by the number `1`. So when you see `1`, think "this is where my program is sending its information to".

The `ls -l` command is a common command in Linux that lists the detailed contents of the current folder. By default, the output is sent to the terminal screen (the standard output).

But what if you want to save this output to a file instead of just displaying it on the screen? That's where the `>` symbol comes in. It's used to redirect the output to a file.

So, in the example `ls -l 1>folder.txt`, the `ls -l` command is being told to send its output to the file `folder.txt` instead of the terminal screen.

In simple terms, `ls -l 1>folder.txt` is a command that tells your computer "list the detailed contents of the current folder and save it to the file `folder.txt`".

### Getting to know more about the standard input and standard output

The standard input and output command using `0<, 1>` in Linux is a way of telling the shell where to get the input from and where to send the output to. The `0<` means to read the input from a file or another command, and the `1>` means to write the output to a file or another command. For example, if you want to run a program called `myprog` that takes a number as input and prints its square as output, you can use the following command:

```bash
myprog 0< input.txt 1> output.txt
```

This command will read the number from a file called `input.txt` and write the square to a file called `output.txt`. You can also use the symbols `<` and `>` instead of `0<` and `1>`, as they are the default file descriptors for standard input and output. For example, the same command can be written as:

```bash
myprog < input.txt > output.txt
```

The standard input and output command using `0<, 1>` in Linux is useful when you want to automate tasks or process large amounts of data without typing or displaying them on the screen. You can also combine multiple commands using pipes (`|`) and redirections (`<`, `>`, `>>`) to create complex workflows. For more information, you can check out these web pages:

## Standard error `–stderr` command

"Standard error", often abbreviated as `stderr`, is a way that a program sends out error messages. This could be error messages that you see in the terminal after running a command.

In Linux, `stderr` is represented by the number `2`. So when you see `2`, think "this is where my program is sending its error messages to".

The `find / -name "*" -print` command is a common command in Linux that searches for files in a directory hierarchy. If it encounters any errors (like files it doesn't have permission to read), those errors are sent to `stderr`.

But what if you don't want to see these error messages? That's where the `2>/dev/null` part comes in. It's used to redirect the error messages to a special place called `/dev/null`, often referred to as the "black hole" of Linux because anything written to it is discarded and disappears.

So, in the example `find / -name "*" -print 2>/dev/null`, the `find` command is being told to send its error messages to `/dev/null` instead of the terminal screen.

In simple terms, `find / -name "*" -print 2>/dev/null` is a command that tells your computer "search for files and print the results, but if you encounter any errors, don't show them to me".

## Bash tab completion

In Bash tab completion, the tab key automatically completes commands and file or directory names. The Bash tab saves time and provides greater accuracy. To use this feature, you must enter enough of the command or file name for it to be unique.

## Best practice: history and tab completion

For history and Bash tab completion, best practices include the following:

- Develop the habit of using both of these features to make usage of command line faster.
- Use the features of Bash to work smarter, not harder.
