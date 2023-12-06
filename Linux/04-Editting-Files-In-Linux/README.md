# Editing Files in Linux

## Introduction to Vim

You must be able to edit text files with tools specific to the command line interface (CLI). Most Linux configurations are held in text files, so you must be able to modify text files to modify the system configuration.

Vim is the default text editor for nearly all Linux distributions. Vim is an implementation of Vi. Depending on the Linux distribution, you might find Vi or Vim. A basic understanding if this tool is essential.

## Vim modes

Vim has no menu buttons.

- Vim uses two different modes that react differently to keystrokes.
  - Command mode: Keystrokes issue commands to Vim.
  - Insert mode: Keystrokes enter content into the text file.

## The command mode

| Keystroke  | Effect  |
|------------|---------|
| x  | Delete the character at the cursor  |
| G  | Move the cursor to the bottom of the file  |
| gg  | Move the cursor to the top of the file  |
| 42G  | Move the cursor to line 42 of the file  |
| /keyword  | Search the file for a keyword  |
| y  | Yank text (cut)  |
| p  | Put text (paste)  |
| i  | Move to insert mode  |

## More Vim commands

| Command  | Effect  |
|----------|---------|
| ZZ  | Save changes and exit vim  |
| X  | Delete the character at the cursor  |
| Dd  | Delete the line at the cursor  |
| U  | Undo the last command  |
| /g  | Global  |
| :s/old/new/g  | Globally find old and replace with new  |
| O  | Enter the insert mode and create a line below the cursor  |
| A  | Enter the insert mode and enter the text after the cursor  |
| h, j, k, l  | Move cursor left, down, up and right  |

## The insert mode

- Enter i.
- Enter your text.
- Press ESC to exit the insert mode.

## Quiring and saving

From command mode, press `:` to get a command prompt for Ex mode

| Common command  | Effect  |
|-----------------|---------|
| :w  | Writes file (save)  |
| :q  | Quits vim  |
| :wq  | Writes files and then quit vim  |
| :wq!  | Writes files and forces quit  |
| :q!  | Quits vim without saving changes  |

## Most common vim commands

| Command  | Effect  |
|----------|---------|
| i  | Enter insert mode  |
| ESC  | Enter command mode  |
| :  | Enter Ex mode  |
| :wq  | Save and quit  |
| :q!  |  Quit without saving changes  |

## Get help in vim

Vimtutor is a command to enter in the shell that opens a Vim documentation. Other commands must be entered inside Vim, such as the following:

- Press `ESC` and enter `:help` to get general help, and then enter `:q` to exit the help page.
- Press `ESC` and enter `:help ‘textwidth’` to go directly to the part of the documentation that mentions the word `textwidth`. Enter `:q` to exit the documentation.
- Enter `useradd`, press `ESC`, and enter `K` to get help about the `useradd` command. Then enter `q` to exit the help page.

## The GNU nano text editor

Nano is a common text editor in Linux, that is preinstalled on most linux distros

## Common nano commands

| Command  | Effect  |
| CTRL + X  | Quit nano  |
| CTRL + O  | Save the file  |
| CTRL + K  | Cut text  |
| CTRL + U  | Paste text  |
| CTRL + G  | Get help  |

## More nano commands

| Command | Effect |
| --- | --- |
| ^G | Display help text |
| ^O | Write the current file to disk |
| ^W | Search for a string or a regular expression |
| ^V | Move to the next screen |
| ^K | Cut the current line and store it in buffer |
| ^U | Display the position of the cursor |

## Other nano commands

| Command | Effect |
| --- | --- |
| ^ | Go to the line and column number |
| ^W | Replace a string or a regular expression |
| ^M-^W | Copy the current line and store it in the cutbuffer |
| ^E | Move to the end of the current line |
| ^M-, | Move to the previous file |
| ^M-. | Switch to the next file |

## The gedit text editor

gedit is a GUI text editor, it have menu buttons available
