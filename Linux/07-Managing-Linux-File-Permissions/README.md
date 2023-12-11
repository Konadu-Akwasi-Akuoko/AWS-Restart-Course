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

```bash
chmod 764 file_2
```

- **Symbolic mode:** Use a combination of letters and symbols to add permissions or to remove any set permissions.

```bash
chmod g+w file_1
```

## Using the `ls -l` command to view permissions

The `ls -l` command is used to print out (view) the file's or directory's permissions details. Option `–l` shows the file or directory, size, modified date and time, file or folder name, and owner of a file and its permissions. The following is an example of an output of a `ls -l` command

```bash
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

```bash
-`rwx`------
```

In the above example the `rwx` represents the user permissions of a file.

## Group identity

Group members are granted permissions of the group to a file or directory.

```bash
-rwx`r-x`--
```

In the above example the `r-x` represents the group permissions of a file.

## Other identity
