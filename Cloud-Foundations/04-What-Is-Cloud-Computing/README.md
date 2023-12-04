# What is Cloud Computing

## Understanding cloud computing

Cloud computing is the on-demand delivery of compute power, database, storage, applications and other IT resources, with a pay as you go model of pricing.

In its most basic definition, the cloud is a computer that is located somewhere else, accessed through the internet, and used in some way. The cloud comprises server computers in large data centers in different locations around the world. When you use a cloud service like Amazon Web Services (AWS), you use the computers that AWS owns.  With cloud computing, organizations can consume on-demand computing and storage resources instead of building, operating, and improving infrastructure on their own.

## Traditional computing model

**Infrastructure as hardware:** In a traditional computing model infrastructure is thought of as hardware. And every company needs to manage their own resources, space, maintainers and scaling of these hardwares. Hardware solutions are physical. They require space, staff, physical security, planning, and upfront costs.

Also in a traditional model a company must guess their highest theoretical maximum peaks so that they can provide their services without fear of their systems not being able to handle the load.

What if their application or service blows up one day(just like chatGPT)? Then they will need to physically buy new hardware, rack and stack them. This process can be really expensive.

And what if their application also losses some users? This means that their systems would be underutilized, thus there would be a lot of space and compute power left which is not being used. So maybe they'll unstack their hardware and sell it, which will also cost time and money to do.

So basically in a traditional computing model companies must go through the time, effort, and costs that are needed to make all necessary changes to their systems.

## Cloud computing model

**Cloud computing model:** With cloud computing we thing of and use our infrastructures as softwares. If your needs change, your software can change more quickly, cost-effectively and with less adjustments than your hardware.

With cloud computing companies can spin up servers they need instead of thinking about the highest theoretical maximum peaks, and as their services grow they can scale up or down automatically based on their requirements. And also with cloud computing you get the choice of choosing services you want, as in compute power, storage, or database.

With AWS, you don’t need to anticipate your hardware needs ahead of time and then order, install, and set it up at your data center. You also don’t need to undergo a long procurement cycle. With a few clicks, you can provision exactly what you need, and it is available to you in a few minutes. You can provision and terminate resources as necessary on AWS instead of paying for hardware when you are not using it. You can treat resources as temporary and disposable, free from the inflexibility and constraints of a fixed and finite IT infrastructure.

## Cloud service models

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

## Cloud computing deployment models

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

## What can you do in the cloud?

- Application hosting
- Backup and storage
- Content delivery
- Websites
- Enterprise IT
- Databases
