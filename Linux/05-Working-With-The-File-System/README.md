# Working With The File System

## Everything in Linux is a file

In linux commands, hardware, and directories are represented as files. Most system configurations are in files.

Files allow for transparency. Drives, processes, and other elements are all represented as files. They can be browsed and accessed for information (for example, `ls /proc` gives you access to processes).

## Files

`ls` command with the option `–l` can list the `ls` command configuration file because it is also a file.

The `ls` command can be used with other commands to create a search condition for `.txt` documents. Something like `ls | grep .txt`, this will find all files with the `.txt` in the file name.

## Linux file names and extensions

Files in linux are:

- They are case sensitive.
- They must be unique within the directory.
- They should not contain /or spaces.

Although file extensions in Linux are optional, it's recommended we always use consistent extensions.

## File systems

The file system organizes how files are stored on the hard drive. A file is located inside a directory.

## File system hierarchy  standard (FHS)

The Linux File System Hierarchy, also known as the Filesystem Hierarchy Standard (FHS), defines the directory structure and directory contents in Unix-like operating systems, including Linux. Here's a brief overview:

- `/` (Root): The primary hierarchy root and root directory of the entire file system hierarchy.
- `/bin`: Contains essential command binaries that need to be available in single-user mode.
- `/boot`: Contains boot loader files, e.g., kernels, initrd.
- `/dev`: Contains essential device files.
- `/etc`: Host-specific system-wide configuration files.
- `/home`: Home directories for all users to store their personal files.
- `/lib`: Libraries essential for the binaries in /bin/ and /sbin/.
- `/media`: Temporary mount directory for removable media.
- `/mnt`: Temporarily mounted file systems.
- `/opt`: Contains add-on applications from individual vendors.

Please note that all files and directories appear under the root directory `/`, even if they are stored on different physical or virtual devices.

| Directory | Function |
| --- | --- |
| / | Root of file system |
| /dev | Devices |
| /etc | Configuration files |
| /home | Standard users' home directories |
| /media | Removable media |
| /mnt | Network drives |
| /root | Root user home directory |
| /var | Log files, print spool, network services |

## Understanding command syntax with the `ls` command

The `ls` command displays a list of files in a directory.

- Different colors represent different types of files.
- `ls` command lists the content of the current directory.
- `ls dir` command lists the content of the `dir` directory.

## `ls` command options and examples

| Option | Description  |
|--------|--------------|
| -l  | Long format (shows permissions)  |
| -h  | File sizes reported in a human-friendly format  |
| -a  | Shows all files, including hidden files  |
| -R  | Lists subdirectories  |
| --sort=extension or -X  | Sorts alphabetically by file extension  |
| --sort=size or -S  | Sorts by file size  |
| --sort=time or -t  | Sorts by modification time  |
| --sort=version or -v  | Sorts by version number  |

## `more` command

- Used to view file contents that don't fit on one screen.
- Loads entire contents of files before displaying results
- Can only scroll down
- Can be used in conjunction with other commands: `cat file.txt | more`

**Usage:**

```sql
more [-options] [-num] [+/pattern] [+linenum] [file_name]
```

This is what the command means

- Options:
  - d: Displays information about how to navigate at the bottom of the screen
  - f: Prevents line wrap
  - p: Clears the screen before displaying the content
  - s: Squeezes multiple blank lines into one line
- num: Number of lines to display
- /pattern: String to find in the file
- linenum: The line number where the content starts to display
- file_name: Name of the file to display the content of

## `less` command

- Displays file contents that don't fit on one screen
- Can scroll up and down through content
- Loads faster than more because `less` doesn’t load every page before it displays results
- Used mostly for large files

**Usage:**

```sql
less [OPTIONS] filename
```

Use Q to quit.

- Options:
- -N: Shows line numbers
- -X: Displays the content after the last command and does not clear the screen when exiting
- +F: Watches for file content changes

## `head` command

- Displays the first 10 lines of a file by default
- Can display multiple files
- When the head command is used in conjunction with the `-n` option, you can specify the number of lines to display.

## `tail` command

- Displays the last 10 lines of a file by default
- Use the tail command with the `-n` option to specify the number of lines to display.

## `cp` command

- The `cp` command copies files and directories.
- By default, the `cp` command overwrites existing files that have the same name.Example: `cp <file-name> <destination>`

**Usage:**

```sql
cp folderA/srcfile folderB/destfile
```

- Copies the `srcfile` that is located in `folderA` to folderB and names it `destfile`

```sql
cp folderA/srcfile folderB/
```

- Copies the `srcfile` that is located in `folderA` to `folderB`(and both files have the same name)

```sql
cp  folderA/srcfile folderB/ folderC/destfile
```

- Copies the `srcfile` that is located in `folderA` to `folderB` and to `folderC` with the name `destfile`

| Option | Description |
| --- | --- |
| cp -a | Force copy |
| cp -i | Interactive – Ask before overwrite |
| cp -l | Link files instead of copy |
| cp -n | No follow symbolic links |
| cp -R | Recursive copy (including hidden files) |
| cp -u | Update – Copy when source is newer than destination |
| cp -v | Verbose – Print informative messages |

## `rm` command

The `rm` command deletes files.

**Usage:**

```sql
rm [OPTIONS] filename(s)
```

- Options:
  - d: Removes a directory; the directory must be empty: `rm –d dir`
  - r: Allows you to remove a non-empty directory: `rm –r dir`
  - f: Never prompt user (useful when deleting a directory with many files)
  - i: Prompts the user for confirmation for each file
  - v: Display the names of deleted files
- If a file is write protected, a prompt will ask the user for confirmation.•Several files can be removed at once.
- If you want to remove a complete directory, use the –r and –f option: `rm –rf dir`
- You can use a regular expression: `rm *.png` removes all files that end with .png.

## `mkdir` command

The `mkdir` command creates new directories.

## `mv` command

The `mv` command moves a file from one directory to another.

The `mv` command renames a file if the source and destination are the same

## `rmdir` command

The `rmdir` command deletes existing empty directories: `rmdir <DirectoryName>`

If a directory isn’t empty, use `rm -r <DirectoryName>`. This command removes a directory and all of its contents.

## `pwd` command

Output of the `pwd` command: Absolute path to your current location in the file system

## Paths

Paths define directories to be traversed to get to a particular resource. In a graphical user interface (GUI), you navigate by opening directories. In a command line interface (CLI), you also navigate through directories, but you specify them by name.

## Types of Paths

- **Absolute paths:** An absolute path is the complete path to the resource from the root of the file system. Example: `/home/userA/Documents/projects`
- **Relative paths:** A relative path is the path to the resource from the current directory. Example: `Documents/projects` or `./Documents/projects`

## `cd` command

The change directory or `cd` command is used to move from one directory to another.
