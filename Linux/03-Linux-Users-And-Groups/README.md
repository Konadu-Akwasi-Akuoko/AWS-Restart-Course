# Linux Users and Groups

## User accounts

- User accounts represent users on the system.
- User information can be stored locally or on another server accessible through a network.
- When information is stored locally, Linux stores it in the `/etc/passwd` file.
- Best practice is to assign one user per account.

`tail` is a command that displays the last lines of a file. By default, it displays the last 10 lines, but you can adjust the number of lines using the `–n` option. For example,the following command displays the last five lines: `tail –n 5 /etc/passwd`.

## The `/etc/passwd` file

Linux stores the accounts in the `/etc/passwd` file. The `passwd` file contains registered users on the system.It is formatted as a colon-separated file that contains the following information:

- User name
- Encrypted password
- User ID
- User’s group ID
- Full name of the user
- Home directory of the user
- The shell that is used after login

## Default user accounts

- Default system accounts are created during the installation of Linux and services.
- For example, a root user account is created during the installation, which allows administration of the system.

`head` is the complementary command of tail. It displays the first 10 lines of a file by default. You can adjust the number of lines by using the `–n` option: For example, the following command displays the first five lines: `head –n 5 /etc/passwd`.

## The `useradd` command

- Creates the user account
- Creates a home directory for the user in /home
- Defines account defaults

`grep` is a command that searches for a string in a file. For example, the following command displays all occurrences of the string `mmajor` in the file `/etc/passwd`:

```bash
grep mmajor /etc/passwd
```

### The `useradd` command options

| Option | Description | Example |
| --- | --- | --- |
| -c | Comment | useradd -c "new employee" jdoe |
| -e | Account expiration | useradd -e 2025-01-01 jdoe |
| -d | Home directory path | useradd -d /users/jdoe jdoe |

## The `usermod` command

This command is used to modify or change parts of or a whole existing user account.

## The `userdel` command

- Deletes a user account
- Uses the -r option to also delete the user's home directory

## The `passwd` command

- User passwords are set with the `passwd` command.
- You must enter the password twice.
- Users can reset their own passwords, and the root user can reset any user password.
- No characters are echoed to the screen when the password is set.

## What are groups

- A group is a set of accounts.
- Groups are a convenient way to associate user accounts with similar security needs.
- For example, it is easier to grant permissions to a group of four users than to grant permissions individually to each of four users individually.
-The storage location for groups is the `/etc/group` file.

## The `etc/group` file

The `etc/group` is the storage location for groups.

## The `groupadd`, `groupmod`, and `groupdel` commands

| Option | Description | Example |
| --- | --- | --- |
| groupadd | Creates a new group | groupadd/group |
| groupmod | Modifies an existing group | groupmod -n new_group old_group |
| groupdel | Deletes an existing group | groupdel/group |

### Add user to a group

- The `usermod` command adds the user `mmajor` to the groups `hr` and marketing: `usermod -aG hr,marketing mmajor`
- The `gpasswd` command adds the user `jdoe` to the marketing group: `gpasswd -a jdoe marketing`
- To append a user to a group without removing them from other groups, use the `usermod` command with `-aG` options

## The `gpassword` command

| Option | Description |
| --- | --- |
| -a, --add | Add USER to GROUP |
| -d, --delete | Remove USER from GROUP |
| -M, --members USER1,USER2,... | Set the list of members of GROUP |
| -A, --administrators ADMIN1,ADMIN2,... | Set the list of administrators for GROUP |

The command `gpasswd-a jdoe ec2-user` adds the user `jdoe` to the `ec2-user` group. The command `gpasswd–M smartinez, rroe ec2-user` sets the list of members of the `ec2-user` group to `smartinez`, `rroe`.

## User permissions levels

| Root user | Standard user |
| --- | --- |
| Access any file | Access any files if given permission to do so |
| Change any file | Control any files that the user owns |
| Control services | Limited access to manage the system |
| Manage hardware |  |
| Manage the Linux kernel |  |
| Manage software |  |

## Use caution with `root`

- Do not log in to the system with administrative permissions
- Log in as a standard user, and then elevate permissions only when necessary
- The root user is a powerful Linux account; mistakes can make the system inoperable
- The root user command prompt ends with `#`
- The standard user command prompt ends with `$`

## The `su` command

- Log in as a standard user, and then elevate permissions to accomplish administrative tasks.
- Be careful to exit the root context.

| Command   | Description   |
|-----------|---------------|
| sudo su root  | Switches to root with the current user's environment  |
| sudo su - root    | Switches to root with the root's environment  |

## The `/etc/sudoers` file

- Delegate specific commands to specific users by adding them to `/etc/sudoers`
- The syntax is `users hosts=(user:group) commands`
- Examples:
  - Allow members of the users group to shut down the local host:

  ```bash
  %users localhost=/usr/sbin/shutdown -r now
  ```

  - Allow members of the devs group all actions from any host without requiring any password:

   ```bash
   %devs    ALL=(ALL)    NOPASSWD: ALL
   ```

  - Delegate specific commands to specific users by adding them to the `/etc/sudoers` file

## Using `sudo`

`sudo` requires the password of the current user whereas `su` requires the password of the substitute account.

Both of the following commands can be used to add a user:

```bash
[student01@server00 ~]$ sudo useradd user20
```

- Requires the password of student01
- student01 must be a sudoers

```bash
[student01@server00 ~]$ su adminuser
[adminuser@server00 student01]$ useradd user20
```

- `student01` must know the password of the `adminuser` (could be root or another user with administrative privileges)
- `sudo` is a safer method to run commands because it does not require a password exchange (`student01` does not need to know the password of `adminuser`).

## The `sudo` command

Use `-lU` options to see your delegated `sudo` permissions.

## The `sudo` logs

- The use of `sudo` permissions is logged at `/var/log/messages`
- A command that is run with sudo permissions is logged at `/var/log/secure`

## The `su` command versus the `sudo` command

- The `su` command activates full administrative permissions.
  - Used when all administrative permissions are needed
  - Users are prompted for the root password
- The `sudo` command activates only delegated permissions.
  - Is used to delegate a specific administrative task to a specific standard user
  - Users are prompted for their own password

## AWS Identity and Access Management (IAM)

IAM as the tool to centrally manage access. It determines who can launch, configure, manage, and remove resources. It provides control over access permissions for people and for systems or other applications that might make programmatic calls to AWS resources.

A policy is a document that you can attach to a user or a group of users and define the permission to access resources. Examples of such permissions might include administrator access to Amazon Relational Database Service (Amazon RDS) or read-only access to Amazon Simple Storage Service (Amazon S3).

Access to IAM can be done through:

- AWS Management Console, a web interface via a browser
- AWS Command Line Interface (AWS CLI), a command line interface accessible by using a Linux shell or Windows command line
- AWS software development kits (SDKs) available for many languages, including Java, Python, JavaScript
