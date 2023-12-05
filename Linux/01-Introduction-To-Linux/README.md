# Introduction to Linux

## Hardware and operating systems

Hardware refers to a computer’s physical components, such as its central processing unit (CPU), memory, storage drive, and network card.

Software is the collection of applications and programs that are installed on the computer. One key type of software that computers require is an operating system. An operating system manages a computer’s hardware and software resources and runs applications.

## The linux operating system

Linux is an open source operating system distributed under the terms of the **Gnu is Not Unix (GNU)** and **General Public License (GPL)**. It provides the core functionality of an operating system, called a kernel, and users can modify and expand it, so today there are many distributions of Linux available.

With Linux, multiple people can use the same computer at the same time and can run multiple applications simultaneously. It also supports network functionality and provides system tools and utilities to increase usability.

## Linux history and benefits

Linux was created by Linux Torvalds in 1991. Linux is very stable and does not experience frequent system freezes that requires the computer to restart, because of this it's a good candidate for being a server operating system and also a desktop operating system.

## Distributions

A Linux **distribution** is a packaged version of Linux that a group of individuals or a company develops. It includes the core operating system functionality (kernel) and additional complementary tools and software applications.

Distributions are typically downloaded but can also be installed by using various media and formats, some of these include compact disk (CD), Universal Serial Bus (USB)device, and downloadable International Standardization for Organization (ISO)image.

Examples of Linux distribution include Amazon Linux 2, Red Hat Enterprise Linux (RHEL), Debian, and Ubuntu.

## Major components of Linux

The major components of a Linux distribution consist of a kernel, daemons, applications, data files, and configuration files.

## The Linux kernel

The kernel refers to the core component of an operating system. It controls everything in the operating system, including the allocation of CPU time and memory storage to running programs, and access to peripheral devices.

## Functions of the Linux kernel

The Linux kernel manages the running of multiple applications and the sharing of resources among multiple users. It also controls the interface to the input/output (I/O) devices that are connected to the computer, and it manages files and directories.

## Daemons

A daemon is computer program that runs in the background and is not under the control of an interactive user. It typically provides a service to other running programs.Examples of daemons include the following:

- **syslogd:** When system or user applications generate messages, the syslogd daemon captures the messages and stores them to a file, which is called a log.
- **sshd:** The sshd daemon handles Secure Shell (SSH) connections to the computer. This type of connection uses encryption to secure the communication between the client and the server.

In retrospect, a Linux daemon is like a personal assistant that's always ready to work in the background, without needing any direct interaction from you.

Imagine you're a manager in an office. You have a lot of tasks that need to be done, like answering emails, scheduling meetings, and so on. But you also have an assistant. This assistant constantly checks your email for you, organizes your meetings, and performs other tasks without you having to ask them each time. They're always running in the background, making sure everything goes smoothly.

In the Linux world, a daemon is just like this assistant. It's a type of program that runs in the background, away from direct user interaction. For example, there's a daemon that manages your printer jobs, another one that adjusts your system clock, and so on. These daemons start up when your system boots and quietly do their work in the background, just like the assistant in our analogy. They're an essential part of making sure your Linux system runs smoothly.

## Applications

An application, is a computer program that provides functions that help users perform a type of task or activity.

## Data files

A file contains information, or data, that the user has created or captured. Files can be of different types depending on the type of data that they contain. A program can process the data in a file. Files are also typically grouped in directories for organizational purposes.

A file has a name that uniquely identifies it. The format of a complete file name consists of an optional **directoryName**, the actual **fileName**, and an optional extension. **A period precedes the extension.** Something like `/pictures/dog.gif`.

## Configuration files

A Linux configuration file is a special type of file that stores initial settings or important values for a system program. These values configure the behavior of the associated program or capture the data that the program uses. For example, the `/etc/group` configuration file contains the list of authorized users for the system.

Some configuration files are used to run a set of commands when the system is started or when the user logs in. With these commands, theLinux environment can be customized to the specific preferences of the user. Configuration file names use a common set of extensions, including `.cnfand` `.conf`.

## How to interface: CLI compared with GUI

You can use either the CLI or GUI based on your preference. But the CLI is the most preferred one.

## The `shell`

hen you use the CLI, the shell that you select defines the list of commands and functions that you can run. A shell interprets the command that you type and invokes the appropriate kernel component that runs the command. Some of these shell environments that works on Linux are `bash`, `zsh`, `csh`, and `fish` shells.

## Shell types

There are different shell types, but the only one you need to know for Linux is the Bash Shell. As we said some of them are `sh`, `bash`, and `ksh`.

## Manual pages

The primary source of Linux documentation is the manual pages or the man pages. They contain a description of the purpose, syntax, and options for a Linux command.

You access the man pages by using the `man` command, like `man git`, will give you documentation about git.

## The `man` command

The man command displays documentation information for the command that you specify as its argument. This information includes the following:

- **Name:** The name and a brief description of the purpose of the command
- **Synopsis:** The syntax of the command
- **Description:** A detailed description the command’s usage and functions
- **Options:** An explanation of the command’s options

## Command features of the `man` command

The documentation that is displayed for a command will typically consist of many pages. To navigate through the pages, use the following keyboard keys:

- **Up arrow or Down arrow key:** Scrolls up or down one line, respectively
- **Page-up or Page-down key:** Scrolls up or down one page, respectively
- **Space bar:** Scrolls down one page

You can also search a command’s man page by using the forward slash (/) character: `/<searchString>` To exit the manual pages, enter `q`.

## Sources of major distributions

A Linux distribution includes the Linux kernel and the tools, libraries, and other software applications that the vendor has packaged. Some of the most important ones are:

- **Fedora:** Red Hat, an IBM company, mainly sponsors this distribution. Fedora is used to develop, test, and mature the Linux operating system. Fedora is the source of the commercially distributed RHEL from which the Amazon Linux 2 and CentOS distributions are derived.
- **Debian:** ThisLinux distribution adheres strongly to the free software principles of open source. The Ubuntu distribution is derived from Debian, and the British company Canonical Ltd. maintains it.
- **OpenSUSE:** The German company SUSE sponsors this distribution, which is used as the basis for the company’s commercially supported SUSE Enterprise Linux offering.

## Amazon Linux 2

Amazon Linux 2 is the latest Linux operating system that AWS offers. It is designed to provide a stable, secure, and high-performance runtime environment for applications that run on Amazon Elastic Compute Cloud (Amazon EC2). It supports the latest EC2 instance type features and includes packages that facilitate integration with AWS.

Amazon Linux 2 enhances security by automatically applying critical or important security updates when an instance is booted.

## Cent OS

CentOS (or Community Enterprise Operating System)is a free Linux distribution and is functionally compatible with its upstream source, RHEL. As of December 2020, Red Hat has cancelled any further development for CentOS Linux and replaced it with CentOS Stream.

## Additional info

- SSH is a network protocol that provides a secure way to access a computer. To connect to a host by using SSH, you need an SSH client. MacOS or Linux usually gives you access to an SSH client directly from the terminal. On Windows, you can use a tool that is called PuTTY, which has a graphical interface. The SSH connection usually uses port 22. The security group that is linked to the EC2 instance opens up this port.

- Linux instances come with a default user.•For the Amazon Linux 2 instance that you will use, the default user is ec2-user. To connect to the instance, you need a private key that is automatically generated for you. The format of the key is the `.pem` format, which stands for Privacy Enhanced Mail. On Windows. PuTTY uses a slightly different format, the `.ppk` (which stands for PuTTY private key) format. PuTTYgen is a tool that can convert a `.pem` key into a `.ppk` key.

- After you launch an EC2 instance, you can connect to it and use it the way you'd use a computer sitting in front of you.Depending on the computer system, you have two ways to access the EC2 instance.
  - The first way to connect is by using a client called PuTTY.PuTTYis an open-source SSH and telnet client .PuTTY allows you to connect to your instance from a Windows machine.
  - If you are using a macOS or Linux machine, you access the EC2 instance differently. If you are using a Mac or Linux computer, it most likely includes an SSH client by default.You can check for an SSH client by entering `ssh` at the command line.
