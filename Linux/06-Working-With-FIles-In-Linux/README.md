# Working With Files In Linux

## The `hash` command

The `hash` command in Linux is used to remember or report the full pathnames of commands that have been previously executed. It is a built-in command in many shell environments like bash, zsh, and more.

When you execute a command in the shell, the system searches for the command in directories specified in the `PATH` environment variable. Once it finds the command, it stores the command's full pathname in a hash table to quickly locate it next time.

Here are some common usages of the `hash` command:

- `hash`: Running the command with no arguments will display a list of remembered commands.
- `hash -r`: This will reset or clear the hash table.
- `hash command_name`: This will add `command_name` to the list of remembered commands.

For example, if you have a command named `my_command`, you can add it to the hash table with `hash my_command`. Now, whenever you run `my_command`, the shell will use the hashed location, speeding up the command's execution.

Some command options are as follows.

- d: Deletes the location for `commandName` from the hash table
- l: Displays output in a format that can be used as input to another command
- p: Sets `pathName` as the the full path location for `commandName`
- r: Empties the hash table
- t: Displays the location of commandName

## The `cksum` command

The `cksum` command in Linux is used to calculate a Cyclic Redundancy Check (CRC) checksum and the byte count of a file. This checksum can be used to verify the integrity of files or data. The command reads each specified file, or standard input if no files are specified, and outputs a CRC checksum and byte count for each file.

The `cksum` command is particularly useful when you've downloaded a file or received a file through some other means and want to verify that the file has not been corrupted during the transfer. Most vendors offer a checksum (or a checksum-like code) corresponding to the file being downloaded. If the file doesn't behave in the expected way, users can recompute the file's checksum using the `cksum` command and compare it with the original checksum provided by the vendor to see if the file is intact.

The usage of this command is quite simple. You just pass the file name as an argument to the `cksum` command, and it will print the corresponding CRC checksum and the number of bytes in the file. Here's an example:

```bash
cksum file1
```

So the first number in the output is the checksum, the second number is the number of bytes, and the third entity is the input file name.

While the `cksum` command provides a simple way to check file integrity, it's worth noting that the CRC checksum calculated by the `cksum` command is not cryptographically secure. It is sufficient to protect against accidental corruption, but it would be possible for an attacker to deliberately alter the file in a way that does not change the checksum. Therefore, for more security-critical applications, other commands that provide cryptographically secure checksums, such as `sha256sum`, might be more appropriate.

## The `find` command

.
The `find` command in Linux is used to search and locate the list of files and directories based on conditions you specify for files that match the arguments. `find` can be used in a variety of conditions such as search by name, search by owner, search by group, search by type, search by permissions, search by date, search by size, and more.

The basic syntax of the `find` command is:

```bash
find [where to start searching from] [expression determines what to find] [-options] [what to find]
```

Remember that the `find` command can be very resource-intensive if used on a large area of the filesystem, especially the root directory (/), because it recursively searches through all directories and subdirectories.

The `-type` flag in the `find` command in Linux is used to specify the type of file that you want to search for.

- `-type f`: This flag is used to find regular files. When you use this flag, the `find` command will only return regular files (not directories, links, etc.).

- `-type d`: This flag is used to find directories. When you use this flag, the `find` command will only return directories.

Here are some examples:

- To find all regular files in the current directory, you can use:

  ```bash
  find . -type f
  ```

- To find all directories in the current directory, you can use:

  ```bash
  find . -type d
  ```

These flags can be very useful for narrowing down your search to a specific type of file.

## Find options

The `find` command in Linux is quite versatile and comes with a variety of options or flags that you can use to refine your search. Here are some of the most commonly used ones:

1. `-name`: This flag is used to search for files by their name. For example, `find . -name "filename"` would search for a file named "filename" in the current directory and its subdirectories.

2. `-iname`: This is similar to `-name`, but it ignores case. For example, `find . -iname "filename"` would match "Filename", "FILENAME", "filename", etc.

3. `-type`: This flag is used to specify the type of file to search for. For example, `find . -type f` would search for regular files, while `find . -type d` would search for directories.

4. `-size`: This flag is used to search for files by their size. For example, `find . -size +1M` would search for files larger than 1 megabyte.

5. `-mtime`: This flag is used to search for files modified within a certain number of days. For example, `find . -mtime -7` would search for files modified within the last 7 days.

6. `-user`: This flag is used to search for files owned by a certain user. For example, `find . -user username` would search for files owned by "username".

7. `-group`: This flag is used to search for files belonging to a certain group. For example, `find . -group groupname` would search for files belonging to "groupname".

8. `-perm`: This flag is used to search for files with certain permissions. For example, `find . -perm 644` would search for files with 644 (rw-r--r--) permissions.

9. `-exec`: This flag is used to execute a command on each file found. For example, `find . -type f -exec rm {} \;` would delete all regular files in the current directory and its subdirectories.

10. `-maxdepth`: This flag is used to limit the depth of directory traversal. For example, `find . -maxdepth 1 -name "filename"` would search for "filename" only in the current directory.

Remember to replace the placeholders (like "filename", "username", "groupname") with your actual search terms.

## Actions that are used with the `find` command

The `find` command can perform actions on the files that match the search criteria. Some examples are as follows.

- `fprint fileName`: Writes the output of the command to the specified file name
- `exec commandName`: Runs the specified command on the returned file or files
- `delete`: Deletes the returned file or files

## The `grep` command

The `grep` command in Linux is a powerful tool used to search and filter text. The name `grep` stands for "global regular expression print". This command searches files for specific patterns of characters and prints the lines where matches are found.

Here are some commonly used options or flags with the `grep` command:

1. `-i`: This flag makes the search case-insensitive. For example, `grep -i "searchterm" file` would match "searchterm", "SearchTerm", "SEARCHTERM", etc.

2. `-v`: This flag inverts the search, returning lines that do not match the pattern. For example, `grep -v "searchterm" file` would return all lines that do not contain "searchterm".

3. `-r` or `-R`: These flags make the search recursive, meaning it will search in the current directory and its subdirectories. For example, `grep -r "searchterm" .` would search for "searchterm" in all files in the current directory and its subdirectories.

4. `-l`: This flag returns the names of files where the search term is found, instead of the actual lines. For example, `grep -l "searchterm" *` would return the names of all files in the current directory that contain "searchterm".

5. `-n`: This flag adds line numbers to the output, showing you where in each file the search term was found. For example, `grep -n "searchterm" file` would return lines containing "searchterm", along with the line numbers.

6. `-w`: This flag searches for whole words, not parts of words. For example, `grep -w "search" file` would match "search" but not "research" or "searching".

7. `-c`: This flag counts the number of lines that match the pattern. For example, `grep -c "searchterm" file` would return the number of lines in "file" that contain "searchterm".

8. `-e`: This flag allows you to specify multiple search patterns. For example, `grep -e "pattern1" -e "pattern2" file` would return lines in "file" that contain either "pattern1" or "pattern2".

Remember to replace "searchterm", "pattern1", "pattern2", and "file" with your actual search terms and file names.

Here's the basic syntax of the `grep` command:

```bash
grep [options] pattern [file...]
```

- `options`: These are flags that modify the behavior of the `grep` command. I mentioned some of these in the previous message.
- `pattern`: This is the search term or regular expression you're looking for.
- `file`: This is the file (or files) you're searching in. If no file is specified, `grep` will search the standard input.

Here are some examples of how to use the `grep` command:

- To search for the pattern "hello" in a file named `file.txt`, you would use:

```bash
grep "hello" file.txt
```

- To perform a case-insensitive search for "hello" in `file.txt`, use the `-i` option:

```bash
grep -i "hello" file.txt
```

- To search for "hello" in `file.txt` and display line numbers with the matching lines, use the `-n` option:

```bash
grep -n "hello" file.txt
```

- To search for lines that do not contain "hello" in `file.txt`, use the `-v` option:

```bash
grep -v "hello" file.txt
```

- To search for the whole word "hello" (not part of a word like "helloing" or "ohello") in `file.txt`, use the `-w` option:

```bash
grep -w "hello" file.txt
```

- To search for "hello" in all `.txt` files in the current directory, you could use:

```bash
grep "hello" *.txt
```

- To search for "hello" in all files in the current directory and its subdirectories, use the `-r` (or `-R`) option:

```bash
grep -r "hello" .
```

## Differences between `grep` and `find`

Sure, here's a comparison of the `find` and `grep` commands in Linux in a markdown table:

| Aspect | `find` Command | `grep` Command |
| --- | --- | --- |
| Purpose | Used to search and locate the list of files and directories based on conditions you specify for files that match the arguments. | Used to search and filter text within files. It searches files for specific patterns of characters and prints the lines where matches are found. |
| Search Scope | Searches for files and directories in the file system. | Searches for specific text within files. |
| Search Criteria | Can use a variety of criteria including name, type, size, modification time, permissions, etc. | Uses patterns, regular expressions, or specific text strings as search criteria. |
| Case Sensitivity | By default, the `find` command is case sensitive but can be made case insensitive using the `-iname` option. | By default, the `grep` command is case sensitive but can be made case insensitive using the `-i` option. |
| Recursive Search | Can search recursively through directories and subdirectories. | Can also search recursively with the `-r` or `-R` option. |
| Output | Outputs the paths of files or directories that match the search criteria. | Outputs the lines of text that match the search criteria, along with the file names. |

## The `diff` command

The `diff` command in Linux is used to compare the contents of two files line by line. It's a very useful tool for viewing the differences between files, especially for tasks like debugging source code or identifying changes in configuration files.

The basic syntax of the `diff` command is as follows:

```bash
diff [options] file1 file2
```

Here, `file1` and `file2` are the two files you want to compare. The `options` parameter can include various flags to modify the behavior of the `diff` command. For example, the `-y` option can be used to output differences side by side, and the `-i` option can be used to ignore case differences.

Here's an example of how you might use the `diff` command:

```bash
diff file1.txt file2.txt
```

This command will output the lines that are different between `file1.txt` and `file2.txt`. If a line is present in `file1.txt` but not in `file2.txt`, it will be prefixed with `<`. Conversely, if a line is present in `file2.txt` but not in `file1.txt`, it will be prefixed with `>`.

Please note that `diff` does not work for binary files, it's intended for text files like source code, configuration files, etc.

## Links and inode

In Linux, a link is a reference to a file or a directory. There are two types of links: hard links and symbolic (or soft) links.

1. **Hard Links**: A hard link is essentially a mirror of the original file. Both the original file and the hard link share the same inode (the data structure that stores information about the file like its size, owner, etc.). This means that even if you delete the original file, the hard link will still have access to the content of the file. Hard links cannot span different file systems or volumes and cannot reference directories.

2. **Symbolic (Soft) Links**: A symbolic link, on the other hand, is a file that points to another file or directory. It's similar to a shortcut in Windows. Unlike a hard link, a symbolic link does not contain the data in the target file. It simply points to another entry somewhere in the file system. This means that if you delete the original file, the symbolic link will be broken and will not work. Symbolic links can span different file systems and can reference directories.

An **inode** (index node) is a data structure in a Unix-style file system that describes a file-system object such as a file or a directory. Each inode stores the attributes and disk block locations of the object's data. File-system object attributes may include metadata (times of last change, access, modification), as well as owner and permission data.

Directories are lists of names assigned to inodes. A directory contains an entry for itself, its parent, and each of its children. There is a specific inode for each file and directory in the file system, but a single file can be linked to multiple locations in the file system, which is how hard links work.

## Hard link

- Points to the original file’s inode
- Cannot reference a directory
- If the original file is deleted, its data still exists until the hard link is deleted

The syntax for creating a hard link is:

```bash
ln source_file link_name
```

Here, `source_file` is the file you want to create a link to, and `link_name` is the name of the new hard link. For example:

```bash
ln file1.txt link_to_file1
```

This command creates a hard link named `link_to_file1` to `file1.txt`.

## Symbolic link

- Points to an original file name or a hard link
- Can point to a directory
- If the original file is deleted, the soft link is broken until you create a new file with the original name

The syntax for creating a symbolic link is:

```bash
ln -s source_file link_name
```

Here, `source_file` is the file (or directory) you want to create a link to, and `link_name` is the name of the new symbolic link. The `-s` option tells `ln` to create a symbolic link. For example:

```bash
ln -s file1.txt symlink_to_file1
```

This command creates a symbolic link named `symlink_to_file1` to `file1.txt`.

Remember, if the source file is deleted, the hard link will still work, but the symbolic link will be broken.

## The `tar` command

The `tar` command in Linux stands for tape archive, and it's used to create, maintain, modify, and extract files that are archived in the tar format. It's a very versatile tool that allows you to group together a bunch of files and directories, preserve their structure and permissions, and compress them if needed.

Here is the basic syntax of the `tar` command:

```bash
tar [options] [archive-file] [file or directory to be archived]
```

## Common `tar` options

- `options`: These are flags that modify the behavior of the `tar` command. Some common options include:
  - `-c`: Create a new archive.
  - `-x`: Extract files from an archive.
  - `-v`: Verbosely list the files processed.
  - `-f`: Allows you to specify the name of the archive.
  - `-z`: Compress the archive using gzip.
  - `-j`: Compress the archive using bzip2.
- `archive-file`: This is the name of the tar file that you want to create or extract.
- `file or directory to be archived`: These are the files or directories that you want to add to the archive.

Here are some examples of how to use the `tar` command:

- To create a tar archive file named `archive.tar` containing a directory named `dir1`, you would use:

  ```bash
  tar -cvf archive.tar dir1
  ```

- To extract the files from `archive.tar`, you would use:

  ```bash
  tar -xvf archive.tar
  ```

- To create a gzipped tar archive named `archive.tar.gz`, you would use:

  ```bash
  tar -cvzf archive.tar.gz dir1
  ```

- To extract a gzipped tar archive named `archive.tar.gz`, you would use:

  ```bash
  tar -xvzf archive.tar.gz
  ```

## The `gzip` command

The `gzip` command in Linux is used to compress **files**. The name `gzip` stands for GNU zip. The resulting compressed files typically have the `.gz` extension.

The basic syntax of the `gzip` command is:

```bash
gzip [options] [file...]
```

Here, `file...` represents one or more files that you want to compress. The `options` parameter can include various flags to modify the behavior of the `gzip` command. For example, the `-k` option can be used to keep (i.e., not delete) input files during compression or decompression, and the `-d` option can be used to decompress files.

Here are some examples of how to use the `gzip` command:

- To compress a file named `file1.txt`, you would use:

  ```bash
  gzip file1.txt
  ```

  This command replaces `file1.txt` with a compressed version named `file1.txt.gz`.

- To keep the original file while compressing, you would use the `-k` option:

  ```bash
  gzip -k file1.txt
  ```

  This command creates a compressed file named `file1.txt.gz` and leaves the original `file1.txt` file untouched.

- To decompress a file, you would use the `-d` option:

  ```bash
  gzip -d file1.txt.gz
  ```

  This command replaces `file1.txt.gz` with its decompressed version `file1.txt`.

## The `zip` and `unzip` commands

The `zip` and `unzip` commands in Linux are used to compress (zip) and decompress (unzip) files and directories. They are similar to the `gzip` and `gunzip` commands, but they work on zip files instead of gzip files.

Here's how you can use these commands:

**zip:**

The `zip` command is used to compress files and directories into a zip file. The basic syntax is:

```bash
zip [options] archive_name file_or_directory_to_compress
```

For example, to compress a directory named `dir1` into a zip file named `archive.zip`, you would use:

```bash
zip -r archive.zip dir1
```

In this command, the `-r` option tells `zip` to operate recursively, which means it will include all the files and subdirectories inside `dir1`.

**unzip:**

The `unzip` command is used to extract the contents of a zip file. The basic syntax is:

```bash
unzip archive_name
```

For example, to extract the contents of a zip file named `archive.zip`, you would use:

```bash
unzip archive.zip
```

This command will create a directory with the same name as the zip file (minus the `.zip` extension) and extract all the files and directories from the zip file into this new directory.
