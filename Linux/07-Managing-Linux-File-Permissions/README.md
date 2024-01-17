# Managing Linux File Permissions

## Linux permission types

In Linux, the term permissions refers to how someone can use a file or directory.

Files and directories in a Linux system have the following three permissions:

- **Read(r):** The read permission gives the control to open and read a file. For example, the read permission on a directory lets you print out the file's content.
- **Write(w):** The write permission gives the user control to change the file's content. For example, the write permission on a directory gives the control to add, remove, and rename files that are stored in the directory. A user might have write permission on a file that is stored in a directory but does not have write permission for the directory itself. In that case, the user can change the file contents. However, the user cannot rename or remove the file from the directory.
- **Execute(x):** In Linux, you must have this permission to run a program. If the permission is not set, a user can see or change the program code (if read and write permissions are set) but not run it.

**NB:`d` in file permissions is a directory, a file or folder can have a `d` or `-`, the `d` means that item is a directory, and `-` means that item is a file**

## Permission modes

Linux uses two modes to configure permissions.

- **Absolute mode:** Use numbers to represent file permissions. This mode is the most commonly used to set permissions. An example is

```sql
chmod 764 file_2
```

- **Symbolic mode:** Use a combination of letters and symbols to add permissions or to remove any set permissions.

```sql
chmod g+w file_1
```

## Using the `ls -l` command to view permissions

The `ls -l` command is used to print out (view) the file's or directory's permissions details. Option `–l` shows the file or directory, size, modified date and time, file or folder name, and owner of a file and its permissions. The following is an example of an output of a `ls -l` command

```sql
drwxr-xr-x  2 akwasi_akuoko akwasi_akuoko     4096 Dec  5 10:20 Downloads
drwxr-xr-x  3 akwasi_akuoko akwasi_akuoko     4096 Dec  6 09:17 SS
-rw-r--r--  1 akwasi_akuoko akwasi_akuoko       53 Dec  6 09:44 introtovim.md
drwxr-xr-x 15 akwasi_akuoko akwasi_akuoko     4096 Dec  5 15:34 neovim
drwxr-xr-x  6 akwasi_akuoko akwasi_akuoko     4096 Dec  5 15:12 nvim-linux64
-rw-r--r--  1 akwasi_akuoko akwasi_akuoko 11053358 Oct  9 20:51 nvim-linux64.tar.gz
-rwxr--r--  1 akwasi_akuoko akwasi_akuoko 11183296 Dec  5 14:48 nvim.appimage
drwxr-xr-x  2 akwasi_akuoko akwasi_akuoko     4096 Dec  4 09:57 projects
drwx------  3 akwasi_akuoko akwasi_akuoko     4096 Dec  4 09:59 snap
```

The `drwxr-xr-x` is the file permissions, we are talking about, the first `akwasi_akuoko` of the output is the user's name, and the second `akwasi_akuoko` is the group's name, note these may change depending on who and where the `ls -l` command is run.

## Understanding the differences

Files and directories in a Linux system assign three types of ownership. And they are

- **User:** A user can create a new file or directory. The file's ownership is set to the user ID of the user who created the file.
- **Group:** A user group can contain multiple users. Users who belong to that group will have the same Linux group permissions to access the file. Every file is also associated with one group name, which is called the group owner.
- **Other:** Other ownership means that the user did not create the file and does not belong to a user group that could own the file.

## User or owner directory

The owner of the file is displayed to the right of where the permissions are displayed. The file owner controls permissions, and the permissions are set for the owner and apply to that user identity or name.

```sql
-`rwx`------
```

In the above example the `rwx` represents the user permissions of a file.

## Group identity

Group members are granted permissions of the group to a file or directory.

```sql
-rwx`r-x`---
```

In the above example the `r-x` represents the group permissions of a file.

## Other identity

Any user who is not the owner and not a member of an associated group is part of other for purposes of permissions.

```sql
-rwx---`rw-`
```

In the above example the `rw-` represents the group permissions of a file.

## Default permissions

- The root account: This is the user account that has full control over the system, also known as superuser. It can execute any command, access all files and directories, and change any settings. This account has the highest level of permissions.

- Non-root users: These are regular user accounts that do not have the same level of access as the root account. They have restrictions on what they can do, particularly when it comes to making system-wide changes.

- `sudo` command: This is a command that allows non-root users to execute commands with the privileges of the root user. It stands for "superuser do". When a user precedes a command with `sudo`, they are requesting to execute that command as the root user.

- One-off command: This refers to a command that is executed only once. By using `sudo`, a non-root user can run a one-off command with root privileges.

- Prompted to enter the account user's password: When a non-root user attempts to use `sudo`, they will be asked to enter their password. This is a security measure to confirm that the user has the necessary permissions to execute the command as the root user.

## The `chown` command

The `chown` command in Linux stands for "change owner", and it allows you to change the user and/or group ownership of a file or directory.

In Linux, every file and directory is assigned to an owner and a group. The owner has certain permissions over the file or directory, such as the ability to read, write, and execute it. Groups are used to organize users and manage their permissions collectively.

The `chown` command is particularly useful in scenarios where administrators need to grant or revoke access to specific resources. You can use it to change the owner of a file, directory, or symbolic link.

The basic syntax of the `chown` command is as follows:

```sql
chown [options] new_owner[:new_group] file(s)
```

- `options`: Optional flags that modify the behavior of the `chown` command.
- `new_owner[:new_group]`: The new owner and optionally the new group. If `new_group` is omitted, only the owner is changed.
- `file(s)`: The file or files for which ownership is to be changed.

For example, if you want to change the owner of a file named `file1.txt` to a user named `mary`, you would use:

```sql
chown mary:root file1.txt
```

This command changes the ownership of `file1.txt` to the user `mary`, and the group to `root`. The group ownership of the file would remain unchanged.

## The `chmod` command

The `chmod` command in Linux is used to change the access permissions of a file or directory. It stands for "change mode". This command allows you to specify who can read, write, or execute a file.

The basic syntax of the `chmod` command is as follows:

```sql
chmod [options] mode file(s)
```

- `options`: Optional flags that modify the behavior of the `chmod` command.
- `mode`: The new permissions that you want to apply to the file(s). This can be represented in symbolic mode (using letters) or in numeric mode (using numbers).
- `file(s)`: The file or files for which permissions are to be changed.

Here are some examples of how to use the `chmod` command:

- To give the owner read, write, and execute permissions, and only read and execute permissions to everyone else, you can use:

  ```sql
  chmod 755 filename
  ```

- To only give the owner read, write, and execute permissions, and no permissions to everyone else, you can use:

  ```sql
  chmod 700 filename
  ```

- To give everyone read, write, and execute permissions, you can use:

  ```sql
  chmod 777 filename
  ```

- To give the owner and group read and write permissions, and only read permissions to everyone else, you can use:

  ```sql
  chmod 664 filename
  ```

- To remove all permissions from a file, you can use:

  ```sql
  chmod 000 filename
  ```

Remember, the first digit of the mode represents the permissions for the owner, the second digit represents the permissions for the group, and the third digit represents the permissions for everyone else. Each digit is a combination of read (4), write (2), and execute (1) permissions. For example, a mode of 755 represents read, write, and execute (7) for the owner, and read and execute (5) for the group and everyone else.

## `chmod` command in symbolic mode

The `chmod` command in Linux allows you to change the permissions of a file or directory using symbolic notation. The symbolic mode of `chmod` is more intuitive and flexible compared to the numeric (or octal) mode.

In symbolic mode, you specify a set of expressions that define who you want to give permissions to and what those permissions are. The format used in symbolic mode is `[ugoa...][[+-=][rwxXst]...]`. Here is what the symbols mean:

- `u` stands for the user who owns the file (user permissions).
- `g` stands for other users in the file's group (group permissions).
- `o` stands for other users not in the file's group (other permissions).
- `a` stands for all users.

If none of these are given, the effect is as if 'a' were given, but bits that are set in the umask are not affected.

The operations are as follows:

- `+` adds the specified permissions to the existing permissions of the file.
- `-` removes the specified permissions from the existing permissions of the file.
- `=` sets the permissions of the file exactly as specified, which means it removes any existing permissions not listed.

The permissions you can set are:

- `r` allows the file to be read.
- `w` allows the file to be written to or modified.
- `x` allows the file to be executed (or in the case of a directory, accessed).

Here are some examples of using the `chmod` command in symbolic mode:

- `chmod u+x filename`: This command gives the user (u) execute (x) permission on the file.
- `chmod g-w filename`: This command removes write (w) permission from the group (g).
- `chmod a+r filename`: This command gives all users (a) read (r) permission on the file.
- `chmod u=rwx,g=rx,o=r filename`: This command gives the user (u) read, write, and execute permissions, gives the group (g) read and execute permissions, and gives others (o) only read permission.

## `chmod` in absolute mode

The `chmod` command in Linux is used to change the access permissions of a file or directory in absolute mode. The term 'absolute mode' refers to the use of numeric (or octal) values to represent file permissions.

The basic syntax of the `chmod` command in absolute mode is:

```sql
chmod [options] mode file(s)
```

- `options`: Optional flags that modify the behavior of the `chmod` command.
- `mode`: The new permissions that you want to apply to the file(s), represented as a three-digit number (in octal).
- `file(s)`: The file or files for which permissions are to be changed.

Each digit in the mode represents the permissions for a different kind of user:

- The first digit represents the permissions for the user who owns the file (user permissions).
- The second digit represents the permissions for other users in the file's group (group permissions).
- The third digit represents the permissions for all other users (other permissions).

Each digit is a combination of read (4), write (2), and execute (1) permissions. For example, a mode of 755 represents read, write, and execute (7) for the user, and read and execute (5) for the group and others.

Here are some examples of how to use the `chmod` command in absolute mode:

- To give the owner read, write, and execute permissions, and only read and execute permissions to everyone else, you can use:

  ```sql
  chmod 755 filename
  ```

- To only give the owner read, write, and execute permissions, and no permissions to everyone else, you can use:

  ```sql
  chmod 700 filename
  ```

- To give everyone read, write, and execute permissions, you can use:

  ```sql
  chmod 777 filename
  ```

- To give the owner and group read and write permissions, and only read permissions to everyone else, you can use:

  ```sql
  chmod 664 filename
  ```

- To remove all permissions from a file, you can use:

  ```sql
  chmod 000 filename
  ```

In summary, the `chmod` command in absolute mode provides a way to manage file and directory permissions in Linux using numeric values.

## Best practices for managing file permissions

- Do not use chmod777.It grants read, write, and execute permissions to every user.
- Follow the principle of least permissions. Give the least number of users the least amount of file access at first, and grant more access only when the user has a need.
- Limit file names to alphanumeric characters, dots, and dashes.- -
- Remember that some characters have special functions.
