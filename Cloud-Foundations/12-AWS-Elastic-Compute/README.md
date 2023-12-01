# AWS Elastic Compute

Amazon Web Services (AWS) provides multiple services to build a solution. Some of those services provide the foundation to all solutions, which are also known as the core services. And Amazon Elastic Compute is also part of these core services.

AWS offers several compute options to meet different needs. Key runtime compute choices can be grouped into four categories of cloud computing models, and they are:

1. Virtual machines(VMs)
2. Containers
3. Platform as a Service(PasS)
4. Serverless

In addition, you can use specialized solutions to address specific compute use cases.

- **Virtual machines:**
  - **Amazon Elastic Compute Cloud(Amazon EC2):** It provides secure and resizable virtual servers in the cloud.
  - **Amazon Lightsail:**  It provides virtual private servers to run workloads in a cost-effective way. The Lightsail service allows users to provision pre-configured cloud servers like LAMP, WordPress, or Node.js to quickly set up the application architecture without having to install the software manually, unlike EC2.
- **Containers Category**
  - **Amazon Elastic Container Service(Amazon ECS):** With this service you can run Docker container applications on AWS.
- **PaaS Category**
  - **AWS Elastic Beanstalk:** It is a solution that runs web applications and services that are developed in languages such as Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.
- **Serverless Category**
  - **AWS Lambda:** a serverless compute solution that runs Java, Go, PowerShell, Node.js, C#, Python, or Ruby code.
  - **AWS Fargate:** provides a serverless compute platform for containers.
- **Specialized solutions**
  - **AWS Outposts:** provides a way to run AWS infrastructure and services on premises.
  - **AWS Batch:** is a service that runs batch jobs at any scale.

The service you select solely depends on your needs and the amount of control you wants, because virtual machines and container-based services provide more control over your infrastructure. They also allow for higher degrees of customization. PaaS and serverless services help you focus more on your application and less on infrastructure.

## Amazon EC2

**Amazon Elastic Compute Cloud (Amazon EC2)** provides on-demand, scalable computing capacity in the cloud. It allows users to rent virtual computers on which to run their own computer applications.

Use cases for Amazon EC2 incudes:

- Application servers
- Web servers
- Database servers
- Game servers
- Mail servers
- Media servers
- Catalog servers
- File servers
- Computing servers
- Proxy servers

## Amazon EC2 overview

The EC2 in Amazon EC2 stands for Elastic Compute Cloud:

- **Elastic** refers to the fact that you can automatically increase or decrease the number of servers that you run to support an application.
- **Compute** refers to actions that require compute resources, including processing power (CPU) and memory (RAM).
- **Cloud** refers to the fact that the EC2 instances that you run are hosted in the cloud.

Amazon EC2 provides virtual machines in the cloud. This service gives you full administrative control over the Microsoft Windows or Linux operating system (OS) that runs on the instance. Most server OSs are supported, including Windows 2008, 2012, 2016, and 2019; Red Hat; SUSE; Ubuntu; and Amazon Linux.

An OS that runs on a virtual machine is often called a guest OS to distinguish it from the host OS. The host OS is directly installed on any server hardware that hosts one or more virtual machines.

With Amazon EC2, you can launch any number of instances of any size into any Availability Zone anywhere in the world in minutes.

## Launching an EC2 instance

The first time that you launch an EC2 instance, you will likely use the AWS Management Console Launch Instance Wizard.

**The Launch Instance Wizard** simplifies launching an instance. For example, if you choose to accept all the default settings, you can skip most of the steps that are provided by the wizard and launch an EC2 instance in a few clicks.

However, for most deployments, you will want to modify the default settings so that the servers you launch are deployed in a way that matches your specific needs.

1. **Select an Amazon Machine Image(AMI)**

    An AMI is a template that is used to create an EC2 instance (which is a virtual machine, or VM,that runs in the AWS Cloud). Is a template that is used to create an EC2 instance (which is a virtual machine, or VM,that runs in the AWS Cloud). AMI is all about the type of OS and the third party apps that will be automatically installed.

    An AMI includes the following components:
    - A template for the root volume of the instance. A root volume typically contains an OS and everything that was installed in that OS (applications, libraries, and so on). Amazon EC2 copies the template to the root volume of a new EC2 instance, and then starts it.
    - Launch permissions that control which AWS accounts can use the AMI
    - A block device mapping that specifies the volumes to attach to the instance (if any) when it is launched

    You can choose from many AMIs:
    - **Quick Start:** AWS offers several prebuilt AMIs for launching your instances. These AMIs include many Linux and Windows options.- - **My AMIs:** These AMIs are AMIs that you created.
    - **AWS Marketplace:** The AWS Marketplace offers a digital catalog that lists thousands of software solutions. These AMIs can offer specific use cases to help you get started quickly.
    - **Community AMIs:** These AMIs are created by people all around the world. AWS does not check these AMIs, so use them at your own risk. Community AMIs can offer many different solutions to various problems, but use them with care. Avoid using them in any production or corporate environment.

    Here re some benefits of using AMIs

    - Repeatability
      - Use an AMI to launch instances repeatedly with efficiency and precision
    - Reusability
      - Instances that are launched from the same AMI are identically configured.
    - Recoverability
      - You can create an AMI from a configured instance as a restorable backup.
      - You can replace a failed instance by launching a new instance from the same AMI.
2. **Select an instance type**

    Now it's time to choose an instance type, Amazon EC2 provides a selection of instance types that are optimized to fit different use cases. The compute type you choose determines your memory(RAM), processing power(CPU), disk space and disk type(storage), and your network performance.

    Instance type categories include general-purpose, compute-optimized, memory-optimized, storage-optimized, and accelerated computing instances. Each instance type category offers many instance types to choose from, which help you scale your resources to the requirements of your target workload.

    **EC2 instance type and naming sizes:**

    Let's take a look at this EC2 instance name and try to understand it: `t3.large`

      - T is the family name, which is then followed by a number. Here, that number is 3. The number is the generation number of that type. For example, a T3 instance is the third generation of the T family.
      - The next part of the name is the size portion of the instance. When you compare sizes, it’s important to note the coefficient portion of the size category. For example, a t3.2xlarge has twice the virtual CPU (vCPU) and memory of a t3.xlarge. The t3.xlarge has, in turn, twice the vCPU and memory of a t3.large.
      - Network bandwidth is also tied to the size of the EC2 instance. If you run jobs that are network intensive, you might need to increase the instance specifications to meet your needs. T3 family mostly uses EBS storage, EBS refers to Amazon Elastic Block Store (Amazon EBS), which this module discusses later.

    **Instance type use cases:**

    Instance types vary in several ways, including CPU type, CPU or core count, storage type, storage amount, memory amount, and network performance.

    | Instance Type | Use Case |
    | --- | --- |
    | General Purpose (a1, m4, m5, t2, t3) | Broad |
    | Memory Optimized (c4, c5) | High performance |
    | Accelerated Computing (f1, g3, g4, p2, p3) | Machine learning |
    | Storage Optimized (d2, h1, h3) | Distributed file systems |

    Let's consider a few instance type in more details:
      - T3 instances provide burstable performance general-purpose instances that provide a baseline level of CPU performance, with the ability to burst above the baseline. Use cases for this type of instance include the following:
        - Websites and web applications
        - Development environments
        - Build servers
        - Code repositories
        - Microservices
        - Test and staging environments
        - Line-of-business applications
      - C5 instances are optimized for compute-intensive workloads. They deliver cost-effective high performance at a low price per compute ratio. Use cases include the following:
        - Scientific modeling
        - Batch processing
        - Ad serving
        - Highly scalable multiplayer gaming
        - Video encoding
      - R5 instances are optimized for memory-intensive applications. Use cases include the following:
        - High-performance databases
        - Data mining and analysis
        - In-memory databases
        - Distributed web-scale in-memory caches
        - Applications that perform real-time processing of unstructured big data
        - Apache Hadoop or Apache Spark clusters
        - Other enterprise applications

      **Instance type network features:**

      Each instance type provides a documented network performance level. For example, an a1.medium instance will provide up to 10 Gbps, but a p3dn.24xlarge instance provides up to 100 Gbps. Choose an instance type that meets your requirements.

      When you start up multiple new EC2 instances on Amazon's cloud service (Amazon EC2), the system tries to spread them out across the physical machines that it runs on. This is done to reduce the chance of them all going down at the same time if there's a problem with the hardware.

      However, if you have a group of these virtual computers that need to work closely together, you might want them to be located closer to each other to reduce the time it takes for them to communicate and increase the amount of data they can send to each other.

      Amazon EC2 allows you to do this using something called "placement groups". You can specify that a group of instances should all be located in the same area (known as an Availability Zone).

3. **Specify network settings**
  
    When you want to start a new virtual computer (an EC2 instance) on Amazon's cloud service (Amazon EC2), you first need to choose a blueprint (an AMI) and a size (an instance type). Then, you need to decide where in the world this virtual computer will    be located (the Region). Make sure you're looking at the right Region in the Amazon EC2 console before you start.

    If you start your virtual computer in a default virtual private cloud (VPC), which is like a private section of the cloud just for you, Amazon will automatically give it a public IP address. This is like a phone number for the internet, allowing your virtual computer to talk to other computers.

    However, if you start your virtual computer in a non-default VPC, it won't get a public IP address automatically. Whether it gets one depends on the settings of the subnet, which is like a smaller section within your VPC.

    By default, virtual computers in a non-default subnet won't get a public IP address. But you can change this in two ways. First, you can change the settings of your subnet. Second, you can choose whether to enable or disable the public IP address feature when you start your virtual computer. This will override the subnet's settings.

4. **Attach an IAM role (optional)**

    It is common to use EC2 instances to run an application that must make secure API calls to other AWS services. To support these use cases, AWS gives you the ability to attach an AWS Identity and Access Management (IAM) role to an EC2 instance. Without this feature, you might be tempted to place AWS credentials on an EC2 instance for an application on that instance to use. However, you should never store AWS credentials on an EC2 instance. This practice is highly insecure. Instead, attach an IAM role to the EC2 instance. The IAM role then grants permissions to make API requests to the applications that run on the EC2 instance.

    An instance profile is a container for an IAM role. If you use the AWS Management Console to create a role for Amazon EC2, the console automatically creates an instance profile and gives it the same name as the role. When you use the Amazon EC2 console to launch an instance with an IAM role, you can select a role to associate with the instance. In the console, the list that displays is actually a list of instance profile names.

    You can use an IAM role to grant permissions to an application that runs on an EC2 instance. The application must access a bucket in Amazon Simple Storage Service (Amazon S3).

    You can attach an IAM role when you launch the instance, but you can also attach a role to an already-running EC2 instance. When you define a role that can be used by an EC2 instance, you define which accounts or AWS services can assume the role. You also define which API actions and resources the application can use after it assumes the role. If you change a role, the change is propagated to all instances that have the role attached to them.

5. **User data script (optional)**

    When you create your EC2 instances, you have the option of passing user data to the instance. User data can automate the completion of installations and configurations at instance launch. For example, a user data script might patch and update the instance's operating system, fetch and install software license keys, or install additional software. When using a Linux EC2 instance you can choose to run:

    ```bash
    #!/bin/bash
    sudo apt update -y
    sudo apt upgrade -y
    sudo apt install wget
    ```

    This means that every time the EC2 instance starts, it'll upgrade and update all packages on the system, and also install wget onto the system.

    For a Microsoft Windows instance, the user data script should be written in a format that is compatible with a Command Prompt window (batch commands) or with Windows PowerShell.

    When the EC2 instance is created, the user data script will run with AWS account root user privileges during the final phases of the boot process. On Linux instances, it is run by the cloud-init service. On Microsoft Windows instances, it is run by the EC2Config or EC2Launch utility.

    By default, user data runs only the first time that the instance starts. However, if you want your user data script to run every time the instance is booted, you can create a Multipurpose Internet Mail Extensions (MIME)multipart file user data script. (This process is not common.)

6. **Specify storage**

    When you launch an EC2 instance, you can configure storage options. For example, you can configure the size of the root volume where the guest OS is installed. You can also attach additional storage volumes when you launch the instance. Some AMIs are also configured to launch more than one storage volume by default to provide storage that is separate from the root volume.

    For each volume that your instance will have, you can specify the size of the disks, the volume types, and whether the storage will be retained if the instance is terminated. You can also specify if encryption should be used.

    **Amazon EC2 storage options:**

    Amazon Elastic Block Store (Amazon EBS) is a high-performance durable block storage service that is designed to be used with Amazon EC2. It is used for both throughput-intensive and transaction-intensive workloads. With Amazon EBS, you can choose from four different volume types to balance the optimal price and performance.

      - **Amazon EBS:** Amazon Elastic Block Store (Amazon EBS) is a high-performance durable block storage service that is designed to be used with Amazon EC2. It is used for both throughput-intensive and transaction-intensive workloads. With Amazon EBS, you can choose from four different volume types to balance the optimal price and performance. You can change volume types or increase volume size without disrupting your critical applications, so you can have cost-effective storage when you need it.

      - **Amazon EC2 Instance Store:** Amazon EC2Instance Store provides ephemeral (or temporary) block-level storage for your instance. This storage is located on disks that are physically attached to the host computer. Instance Store works well when you must temporarily store information that changes frequently, such as buffers, caches, scratch data, and other temporary content. When a running instance of your EC2 is stopped, or crashes the data in this file system will be lost permanently, so don't use it as the root file system or to store important files.

      - **Amazon Elastic File System:** Amazon Elastic File System (Amazon EFS) provides a scalable, fully managed elastic Network File System (NFS) file system for use with AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting applications. It grows and shrinks automatically as you add and remove files, which reduces the need to provision and manage capacity to accommodate growth.

      - **Amazon S3:** Amazon Simple Storage Service (Amazon S3) is an object storage service that offers scalability, data availability, security, and performance.

    **Example storage options:**

    **Scenario 1:**
    Instance 1 has its operating system and possibly other data stored on Amazon EBS. It also has two additional storage volumes attached to it. One is a 500-GB EBS storage volume, and the other is an Instance Store volume. If this instance is stopped and then started again, the operating system and any data stored on the EBS volumes will remain intact. However, any data stored on the Instance Store volume will be lost.

    **Scenario 2:**
    Instance 2 has its operating system stored on an Instance Store volume. This instance  cannot be stopped using an Amazon EC2 API call, it can only be terminated. If the  instance is terminated, all data stored on the Instance Store volume, including the  operating system, will be lost. You wouldn't be able to start the instance again.

    If you need to preserve your data and operating system even when the instance is stopped, then **Scenario 1** is the best option. However, if you're okay with losing your data and operating system when the instance is terminated, then **Scenario 2** could work for you. But remember, for valuable, long-term data, it's recommended to use more durable data storage like Amazon EBS, Amazon EFS, or Amazon S3.

7. **Add tags:**

    A tag is a label that you assign to an AWS resource. Each tag consists of akeyand an optional value, both of which you define. With tags, you can categorize AWS resources (such as EC2 instances) in different ways. For example, you might tag instances by purpose, owner, or environment.

8. **Security group settings:**

    Asecurity groupacts as a virtual firewall that controls network traffic for one or more instances. When you launch an instance, you can specify one or more security groups. Otherwise, the default security group is used.

    You can add rules to each security group. Rules allow traffic to or from the security group’s associated instances. You can modify the rules for a security group at any time. The new rules will be automatically applied to all instances that are associated with the security group. When AWS decides whether to allow traffic to reach an instance, all the rules from all the security groups that are associated with the instance are evaluated. When you launch an instance in a VPC, you must either create a new security group or use one that already exists in that VPC. After you launch an instance, you can change its security groups.

    When you define a rule, you can specify the allowable source of the network communication (inbound rules) or destination (outbound rules). The source can be an IP address, an IP address range, another security group, a gateway VPC endpoint, or anywhere `*` (which means that all sources will be allowed). By default, a security group includes an outbound rule that allows all outbound traffic. You can remove the rule and add outbound rules that only allow specific outbound traffic. If your security group has no outbound rules, no outbound traffic that originates from your instance is allowed.

    Network access control lists (network ACLs) can also be used as firewalls to protect subnets in a VPC.

9. **Identify or create the key pair:**

    When you're setting up a new virtual computer (an EC2 instance) on Amazon's cloud service, you go through a process where you choose various settings. Once you've done that, you get a chance to review everything before you start the instance.

    At this point, you're asked to choose a key pair. This is a set of two keys: a public key, which is used to encrypt data, and a private key, which is used to decrypt it. This system allows you to securely access your instance without needing a password.

    You can either use a key pair that you've already created, or you can create a new one. If you create a new key pair, make sure to download and save the private key, because you won't get another chance to do so.

    To connect to a Microsoft Windows instance, use the private key to obtain the administrator password.Then log in to the EC2 instance's Windows Desktop by using RemoteDesktop Protocol (RDP). To establish an SSH connection from a Windows machine to an EC2 instance, you can use a tool such as PuTTY, which will require the same private key.

    With Linux instances, the public key content is placed on the instance at boot time. An entry is created in ~/.ssh/authorized_keys. To log in to your Linux instance (for example, by using SSH), you must provide the private key when you establish the connection.
