# AWS ReStart Course

This is a course for AWS restart. This course will let us earn an AWS practitioner certificate.

## Table of Content

1. [Introduction to Computing](#introduction-to-computing)
2. [Basic Computing Concepts](#basic-computing-concepts)
3. [Development Team Roles](#development-team-roles)
4. [What is Cloud Computing](#what-is-cloud-computing)
5. [Advantages of Cloud Computing](#advantages-of-cloud-computing)
6. [What is AWS](#what-is-aws)
7. [AWS Infrastructure Overview](#aws-infrastructure-overview)

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

## What is AWS

### Web services

AWS offers 3 models of cloud computing services, and they are IaaS, PaaS, and Saas. And the basic building blocks of cloud IT include:

- network features
- compute
- data storage space

 Almost everything that you can do with a traditional on prem infra can be done with AWS in the cloud.

### What are web services?

A web service is any piece of technology that makes itself available on the internet. Web services happen over a network with a request and response to and from the server. The standard language that web services use for request and response are Extensible Markup Language(XML) or Javascript Object Notation(JSON) which connects users to Application Programming Interfaces(API).

### AWS services

AWS is a secure cloud service provider with many services that let businesses scale and grow.

Because it is an on-demand service, companies can access compute, data storage, and networking infrastructure over the internet.

An example of how a company use AWS:

A database application is being built using various Amazon Web Services (AWS).

1. Customers send data to **Amazon Elastic Compute Cloud (EC2)** instances, a service in the Compute category.
2. The EC2 servers batch the data in 1-minute increments and add an object per customer to **Amazon Simple Storage Service (S3)**, which is the chosen AWS storage service.
3. A nonrelational database like **Amazon DynamoDB** is used to power the application and build an index to find all the objects from a given customer collected over a certain time period.
4. These services might be run inside **Amazon Virtual Private Cloud (VPC)**, a service in the networking category.

This shows how you can select and combine different AWS services from various categories to build a solution, in this case, a database application. However, the solutions that you build can also be quite complex.

### Choosing  a service

AWS has a lot of services, but what you choose solely depends on your business goals and your technology requirements.

Here is an example of some services that AWS offers:

| Community Services | Storage Services | Management and Governance Services | Database Services | Security, Identity, and Compliance Services | Networking and Content Delivery Services | AWS Cost Management Services |
|---|---|---|---|---|---|---|
| AWS Lambda | Amazon S3 | Amazon CloudWatch | Amazon DynamoDB | Amazon Cognito | Amazon VPC | AWS Budgets |
| Amazon Elastic Beanstalk | Amazon Glacier | AWS Trusted Advisor | Amazon RDS | AWS Shield | Amazon Route 53 | AWS Cost Explorer |
| Amazon EC2 Auto Scaling | Amazon EBS | AWS CloudTrail | Amazon Redshift Aurora | AWS WAF | Amazon CloudFront | |
| Amazon ECS | | AWS Artifact | | AWS KMS | Elastic Load Balancing | |

Each row represents a different service offered by AWS under the respective category. For example, under "Community Services", you have AWS Lambda, Amazon Elastic Beanstalk, Amazon EC2 Auto Scaling, and Amazon ECS.

### Three ways to interact with AWS

- **AWS management console:** an easier to use gui for managing AWS services
- **AWS CLI:** a command line interface that you can use to manage AWS services
- **AWS SDK:** these SDKs give the privilege for users to access AWS services directly in their code

### AWS cloud adoption framework

The AWS cloud adoption framework helps companies to adopt the cloud efficiently and effectively. The AWS cloud adoption framework helps companies to align their people, process, and technology which helps them migrate their infra to the cloud.

### AWS documentation

The AWS docs help you find user guides, developer guides, API references, tutorials and more. Each tool and SDK in the AWS web services also has it's own docs.

## Fundamentals of AWS Pricing

### AWS pricing model

AWS have major three major drivers of cost: **compute**, **storage**, and **outbound data transfer**

In most cases you won't be charged for inbound data transfer, thus it means communication or the sending of data between AWS services in the same region will not be billed. But sometimes there is an exception to this rule.

Outbound data transfer is aggregated across services and then charged at the outbound data transfer rate. This charge appears on the monthly statement as **AWS Data Transfer Out**.

### How do you pay for AWS?

AWS is a pay as you go service, thus you pay for what you use. This utility style payment includes:

- Pay for what you use.
- Pay less when you reserve.
- Pay less when you use more.
- Pay even less as AWS grows.

- **Pay for what you use:** With AWS you pay for only web services you use, and there are no upfront costs or contracts that a user is being locked into, it's only pay as you go. Also if you think you don't need a service again it can be terminated.

- **Pay less when you reserve:** For certain services like Amazon EC2 and Amazon RDS companies or users can let Amazon reserve a space or capacity for them, and when it is reserved they pay less than when it is on demand or when it is a pay-as-you-go model. Reserve instances are in 3 options
  1. **All upfront reserved instance(AURI)**, this is when you pay for the full reserved instance, and it contains the most discount.
  2. **Partial upfront reserved instance(PURI)**, this is when you make partial payment for a reserved instance, and it gives the lower discounts with the ability to spend less upfront.
  3. **No upfront reserved instance(NURI)**, this is when you don't make any initial payment upfront but you tell Amazon to reserve you an instance, this model get's the lowest discount.

- **Pay less by using more:** Services such as Amazon S3, Amazon EBS, and Amazon EFS have tiered pricing, thus the more you use the less you pay. For these services they are measured using pay per GB, so the more GB you use the less you pay.

- **Pay less as AWS grows:** As AWS grows they also lower pricing for their services. Since 2006 Amazon has lowered their price 75 times as they continue to grow.

### Custom pricing

If none of the AWS pricing models work for your project, custom pricing is available for high-volume projects with unique requirements.

### AWS free tier

To help new AWS customers get started in the cloud, AWS offers a free usage tier (the AWS Free Tier) for new customers for up to 1 year. The AWS Free Tier applies to certain services and options.

### Services with no charge

AWS offers some services that have no charges:

1. Amazon virtual private cloud (Amazon VPC)
2. AWS identity and access management (IAM)
3. Consolidated billing
4. AWS elastic beanstalk
5. AWS cloud formation
6. Amazon EC2 auto scaling
7. AWS OpsWorks

### AWS pricing calculator

The AWS pricing calculator helps us estimate monthly billings of AWS services. With the pricing calculator you can add, modify, remove services from your bill, to see how you'll pay.

The AWS calculator can help you estimate monthly service costs, identify opportunities for reductions, use templates to model solutions to compare services and deployments models. The calculator also show common user samples and usage

### The cost of ownership

If a company wants to save a lot of money it is encouraged that they use cloud services instead of on premises infrastructure. Because with the on premises infrastructure a company needs to buy equipments, hire people to manage these equipments, and do a whole lot of stuff to maintain and look after the on premises infrastructure. But sometimes companies would want to measure between on premises infra and using cloud infra. How would they do that?

**Total cost of ownership(TCO):** is a financial estimate to help identify direct and indirect costs of a system. Use TCO to compare the costs of running an entire infrastructure environment or specific workload on premises as compared to the AWS Cloud. Budget and build the business case for moving to the cloud.

When you compare an on-premises solution and a cloud solution, it’s essential to assess the actual costs of both options. With the cloud, most costs are upfront and can be calculated. Cloud providers give transparent pricing based on different usage metrics such as RAM, storage, and bandwidth. Pricing is frequently fixed per unit of time.After you understand how pricing works, you can calculate costs based on several different usage estimates.

## AWS Infrastructure Overview

The **AWS Global Infrastructure** is designed and built to deliver a flexible, reliable, scalable, and secure cloud computing environment with high-quality global network performance.

The AWS global infra consists of three main elements, they are regions, availability zones, and point of presence. AWS infra spans 84 availability zones in 26 geographical regions around the world.

### AWS data centers

AWS data centers is the foundation for AWS services. A data center is the physical location where the data is stored and the processing occurs.

### AWS availability zones

Each availability zone is made up of one or more data centers that are designed for fault isolation. They are designed for fault isolation.

Availability Zones are interconnected with other Availability Zones by using high-speed private links. Users can choose their own availability zones.

Fault tolerance design helps to ensure that if a fault (an error or failure) occurs in one data center, it doesn’t impact the others. This way, even if there’s a problem in one data center, the others can continue to operate normally, providing a high level of reliability and availability for AWS services. This is particularly important for applications that require high availability and fault tolerance.

You are responsible for selecting the Availability Zones where your systems will reside. Systems can span across multiple Availability Zones. AWS recommends replicating across Availability Zones for resiliency. You should design your systems to survive temporary or prolonged failure of an Availability Zone if a disaster occurs. Distributing applications across multiple Availability Zones helps them remain resilient in most failure situations, including natural disasters or system failures.

### AWS regions

An AWS Region is a physical geographical location in the world where AWS has multiple Availability Zones. To achieve fault tolerance and stability, Regions are isolated from each other.

When you store data in a specific Region, it’s not replicated outside that Region. AWS never moves your data out of the Region that you put it in. It’s your responsibility to replicate data across Regions if your business needs require it.

### Selecting a region

You should consider a few factors when you select the optimal Region or Regions where you store data and use AWS services.

One essential consideration is **data governance** and legal requirements. Local laws might require that certain information be kept within geographical boundaries.

 Also it’s generally desirable to run your applications and store your data in a Region that is as close as possible to the user and systems that will access them. This will help you **reduce latency**.

 Finally, there is some variation in the cost of running services, which can depend on which Region you choose. For example, as of this writing, the per-hour cost to run a t3.medium Amazon Elastic Compute Cloud (Amazon EC2) On-Demand Linux Instance in the US East (Ohio) Region might differ from running the same instance in the Asia Pacific (Tokyo) Region.

 In summary, when you select a Region, you should consider which Region offers the services that you need and where it’s located.

### Points of presence

A PoP is where end users access AWS services through either the Amazon CloudFront or the Amazon Route 53 services.

As of August 2020, the global AWS infrastructure contained 216 PoPs, consisting of 205 edge locations and 11 Regional edge caches located in most of the major cities around the world. These PoPs serve requests for CloudFront and Route 53.

CloudFront is a content delivery network (or CDN) used to distribute content to end users to reduce latency. Route 53 is a Domain Name System (DNS) service. Requests going to either one of these services will be routed to the nearest edge location automatically.

Regional edge caches, used by default with CloudFront, are used when you have content that is not accessed frequently enough to remain in an edge location. Regional edge caches absorb this content and provide an alternative to the content having to be fetched from the origin server.

### AWS Infrastructure Features

An Availability Zone is a data center or collection of data centers. Availability Zones are connected with low-latency, high-throughput, highly redundant networking. Availability Zones are physically distinct. Each one has equipment like uninterruptible power supplies, cooling equipment, backup generators, and security, to help ensure uninterrupted operations.

AWS Regions provide multiple physically separated, isolated Availability Zones. An AWS Region contains two or more Availability Zones.

This infrastructure has several valuable features:

- First, it is elastic and scalable. This means that resources can dynamically adjust to increases or decreases in capacity requirements. The infrastructure can also rapidly adjust to accommodate growth.
- Second, this infrastructure is fault tolerant, which means it has built-in component redundancy so that it can continue operations despite a failed component.
- Finally, it requires minimal to no human intervention while providing high availability with minimal downtime.
