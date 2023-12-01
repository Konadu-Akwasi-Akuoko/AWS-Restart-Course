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
