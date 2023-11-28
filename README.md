# AWS ReStart Course

This is a course for AWS restart. This course will let us earn an AWS practitioner certificate.

## Table of Content

1. [Introduction to Computing](#introduction-to-computing)
2. [Basic Computing Concepts](#basic-computing-concepts)
3. [Development Team Roles](#development-team-roles)
4. [What is Cloud Computing](#what-is-cloud-computing)
5. [Advantages of Cloud Computing](#advantages-of-cloud-computing)

## Introduction to Computing

In todays world we can't live without computing. We buy books, watch videos, and even chat with friends all through this technology called computer. All this can happen on a computer when a user have a set of **applications** and **network** connectivity. Applications, networks, and computers run the digital world.

### Application

An application is a set of instructions that run on a computer to perform a specific task. A computer program is written using code or programming languages(a language that the computer understands). Computer programs are called softwares.

There 4 main type of applications, they are:

1. Web applications
2. Mobile applications
3. Desktop applications
4. Internet of Things applications

A computer mostly consist of the hardware and software.

### Computer Network

A computer network connects multiple devices to share data and resources. Connected devices can be of different types, such as computers, printers, storage drives, and smartphones.

A network interface card, also called a network adapter, connects a computer to a computer network. It uses a cable that is connected to a hub or switch.A wired network card uses an Ethernet cable to connect a computer to the network. A wireless network card uses a Wi-Fi signal instead.

## Basic Computing Concepts

### What is a server?

A server is a computer that provides data or services to other computers. A server provides a response to a request from a client computer over a network.

A server resides in a data center. A data center is a physical location that is used to host computer systems and associated components such as networks, storage devices, and power supplies.

Traditionally, organizations owned their data centers. The equipment was on premises at a location that the company owned. The company are the one who buys, installs, configures, and manages all the hardware and software in your own facility. You are responsible for installation, maintenance, and numerous other costs. You also must hire the staff who are responsible for the maintenance of the hardware, software, and the facility itself.

The cloud model provides another option: a cloud services provider buys the hardware and infrastructure software in their own facility. They manage and maintain it with their own personnel. You bring your application or workload to run on their servers and pay for the services that they offer.

### Virtual machines

A virtual machine is a software based computer that runs on a physical computer. The VM provides computing capabilities by accessing the physical resources of the host through a software layer, which is called a hypervisor. The hypervisor shares the host’s physical resources—such as its CPU, memory, disk drives, and networking capabilities—among the VMs that run on the host. A VM can run its own operating system, and multiple VMs can run on a single host.

VMs facilitate computing in the cloud. In the AWS Cloud, the core service that offers computing capabilities as virtual machines is the Amazon Elastic Compute Cloud (Amazon EC2).

### Software development lifecycle

The software development life cycle (SDLC) is a process that is used to produce software in a disciplined and organized way.

At a high level, the purpose of each phase can be described by the following questions and actions:

- **Plan:** What is the problem, and what resources do you need to solve it?

- **Analyze:** What do you want from a solution?

- **Design:** How will you built what you want?

- **Develop:** Build what you have designed.

- **Test:** Did you get what you want?

- **Implement:** Start to use what you built.

- **Maintain:** Improve what you built.

The SDLC is repeated over the lifetime of an application. It is used to create, update, fix, and maintain the application over a period of time.

## Development Team Roles

To complete the SDLC in a timely manner development often takes place in teams, and each team has their specific roles that they are doing.

- **Project Manger**
  - Is responsible for developing a project plan
  - Recruits staff to fulfill other roles
  - Leads and manages the project team
  - Assigns tasks to different team members
  - Determines a timeline for the project
  - Provides updates to upper management

- **Analyst**
  - Is sometimes called the business analyst or requirements analyst
  - Defines the purpose for each project
  - Gathers requirements from leadership, clients, and users
  - Organizes requirements into tasks for developers and quality assurance (QA) to use for implementation and testing

- **Quality Assurance**
  - Creates a list of tests that verify function, usability, efficiency, maintainability, and portability for each new requirement
  - Maintains the list of tests that are needed to verify the behavior for each previously released feature
  - Runs all tests and investigates any failures
  - Documents the steps to replicate bugs or issues in the application for the developer
  - Assists in creating the acceptance criteria, which are the performance criteria that are used to measure successful completion of the application

- **Software Developer**
  - Writes the code that makes up the application according to the specifications that the analyst provides
  - Maintains previous versions of the application if they are still supported
  - Runs initial test cases to ensure that the product works
  - Writes code to fix and address bugs or other issues that are reported to them

- **Database Administrator**
  - Maintains the data that is needed in the application
  - Is responsible for planning, maintaining, and configuring access to that data and for ensuring the availability of enough computing resources to make an application work correctly
  - Secures the data in the database
  - Backs up data (and restores data as needed)
  - Is responsible for database performance and optimization

## What is Cloud Computing

### Understanding cloud computing

Cloud computing is the on-demand delivery of compute power, database, storage, applications and other IT resources, with a pay as you go model of pricing.

In its most basic definition, the cloud is a computer that is located somewhere else, accessed through the internet, and used in some way. The cloud comprises server computers in large data centers in different locations around the world. When you use a cloud service like Amazon Web Services (AWS), you use the computers that AWS owns.  With cloud computing, organizations can consume on-demand computing and storage resources instead of building, operating, and improving infrastructure on their own.

### Traditional computing model

**Infrastructure as hardware:** In a traditional computing model infrastructure is thought of as hardware. And every company needs to manage their own resources, space, maintainers and scaling of these hardwares. Hardware solutions are physical. They require space, staff, physical security, planning, and upfront costs.

Also in a traditional model a company must guess their highest theoretical maximum peaks so that they can provide their services without fear of their systems not being able to handle the load.

What if their application or service blows up one day(just like chatGPT)? Then they will need to physically buy new hardware, rack and stack them. This process can be really expensive.

And what if their application also losses some users? This means that their systems would be underutilized, thus there would be a lot of space and compute power left which is not being used. So maybe they'll unstack their hardware and sell it, which will also cost time and money to do.

So basically in a traditional computing model companies must go through the time, effort, and costs that are needed to make all necessary changes to their systems.

### Cloud computing model

**Cloud computing model:** With cloud computing we thing of and use our infrastructures as softwares. If your needs change, your software can change more quickly, cost-effectively and with less adjustments than your hardware.

With cloud computing companies can spin up servers they need instead of thinking about the highest theoretical maximum peaks, and as their services grow they can scale up or down automatically based on their requirements. And also with cloud computing you get the choice of choosing services you want, as in compute power, storage, or database.

With AWS, you don’t need to anticipate your hardware needs ahead of time and then order, install, and set it up at your data center. You also don’t need to undergo a long procurement cycle. With a few clicks, you can provision exactly what you need, and it is available to you in a few minutes. You can provision and terminate resources as necessary on AWS instead of paying for hardware when you are not using it. You can treat resources as temporary and disposable, free from the inflexibility and constraints of a fixed and finite IT infrastructure.

### Cloud service models

There are 3 basically cloud service models, and they are:

1. Infrastructure as a service (IaaS). More control examples include AWS and GCP
2. Platform as a service (PaaS). Medium control, examples include Vercel and Netlify
3. Software as a service (SaaS). Less to no control, examples include Facebook and Youtube

**Infrastructure as a service:** With this model companies manage their own servers and the operating system they use on the server. In general the cloud provider service will not have access to your server.

**Platform as a service:** With this model someone else manages the underlying infrastructure including the server and the type of OS used. PaaS also provides a framework for developers that they can build on to create customized applications.

**Software as a service:** With this model you handle your own files, whiles the provider handles everything from data centers, to servers, to networks, to storage, to maintenance and patching. The user only handles how they would use the software. You are provided with a complete product that the service provider runs and manages. Facebook and Dropbox are examples of SaaS. You manage your Facebook contacts and Dropbox files, and the service providers manage the systems.

| Cloud Service Model | Applications | Data | Middleware | Runtime | OS | Virtualization | Servers | Storage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| On premises | You manage | You manage | You manage | You manage | You manage | You manage | You manage | You manage |
| IaaS | You manage | You manage | You manage | You manage | You manage | Others manage | Others manage | Others manage |
| PaaS | You manage | You manage | Others manage | Others manage | Others manage | Others manage | Others manage | Others manage |
| SaaS | Others manage | Others manage | Others manage | Others manage | Others manage | Others manage | Others manage | Others manage |

This table shows who manages each component (Applications, Data, Middleware, Runtime, OS, Virtualization, Servers, Storage) in different cloud service models (On premises, IaaS, PaaS, SaaS).

### Cloud computing deployment models

There are three main cloud computing deployment models that represents the cloud environments where you can deploy your applications.

- **Cloud (all-in-cloud)** is a cloud-based application that is fully deployed in the cloud. All parts of the application run in the cloud.

- **Hybrid deployment** is a way to connect infrastructure and applications between cloud-based resources and existing resources that are not in the cloud.

- **On-premises cloud** is when you run a cloud infrastructure from your own data center.

The table below dives into the differences between cloud deployments and on-premises cloud deployments

| Type of Infrastructure | Upfront Investment | Ongoing Costs | Flexibility | Capacity | Geographic Reach |
| --- | --- | --- | --- | --- | --- |
| Cloud | No upfront investment | Low ongoing costs | Flexible and agile | Scalable capacity | Global reach on demand |
| Private (on-premises) cloud | Large initial purchase | Labor, patches, and upgrade cycles | Fixed capacity | Long procurement and setup | Limited geographic regions |

This table shows the comparison between different types of infrastructures (Cloud, and Private (on-premises) cloud) in terms of upfront investment, ongoing costs, flexibility, capacity, and geographic reach.

### What can you do in the cloud?

- Application hosting
- Backup and storage
- Content delivery
- Websites
- Enterprise IT
- Databases

## Advantages of Cloud Computing

- How does cloud computing benefit you?
  - Cloud computing gives you access to servers, storage, databases, and a broad set of application services over the internet. Cloud storage is a good example of cloud computing.
- If you have a business, how can cloud computing benefit your business?
  - Cloud computing or cloud services providers like Amazon Web Services (AWS) provide rapid access to flexible and low-cost IT resources
- Why are so many companies interested in moving to the cloud?
  - Companies are moving to the cloud because it presents many benefits including cost savings because you pay only for the resources that you use.This slide provides answers to the questions posed on the previous slide.Next, you explore the major reasons why so many companies are moving to the cloud.

### Why are so many companies moving to the cloud?

1. Trading fix expenses for variable (pay as you go) expenses, when it comes to infrastructure.
2. Benefits from massive economy of scale, because many people are using AWS it brings down the cost of operations at AWS so this reduction in cost is passed on the users of AWS which results in lower pay-as-you-go prices.
3. Reduce guessing capacity. With on-prem model you either get underutilized servers or over burdened servers, with cloud computing you can scale up or down as needed.
4. With cloud computing you don't guess much about your maximum peaks in terms of usage. In traditional model it's either you buy too much and waste money or buy too less and have downtimes.
5. Increase your speed and agility. In cloud computing spinning up a server is just a matter of click away, and this leads to provisioning of servers to your developers really fast, something that can take up to weeks.
6. No more expenses for running and maintaining data centers. With cloud computing companies can focus on their core business goal and not about installing and managing servers.
7. Going global in minutes. With cloud computing you can provision servers at different locations around the globe that is closer to your users therefore reducing latency between your users devices and the server.
