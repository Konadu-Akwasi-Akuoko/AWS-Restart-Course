# AWS Shared Responsibility Model

| Responsibility | Customer | AWS |
| --- | --- | --- |
| Customer data | Yes | No |
| Applications, AWS Identity and Access Management (IAM) | Yes | No |
| Client-side data encryption and authentication | Yes | No |
| Network-side encryption and data protection, integrity, identity | Yes | No |
| AWS foundational services | No | Yes |
| Compute | No | Yes |
| Storage | No | Yes |
| Database | No | Yes |
| Networking | No | Yes |
| AWS Global Infrastructure | No | Yes |
| Availability Zones | No | Yes |
| Regions | No | Yes |
| Edge locations | No | Yes |

This table represents the shared responsibility model between the customer and AWS. The customer's responsibility includes customer data, applications, client-side data encryption and authentication, and network-side encryption and data protection, integrity, identity. On the other hand, AWS is responsible for foundational services, compute, storage, database, networking, and global infrastructure including availability zones, regions, and edge locations.

As the above table shows AWS Shared Responsibility Model is a concept that divides responsibilities between AWS and the customer.

## AWS security responsibilities: Security of the cloud

AWS is responsible for the security of the cloud. Thus under the shared responsibility model, AWS operates, manages, and controls the components. These components range from the host operating system and virtualization layer down to the physical security of the facilities where the services operate. This also means that AWS is responsible for protecting the global infrastructure that runs all of the services that are offered in the AWS Cloud.

AWS handles the security of the physical infrastructure that hosts your resources. Some of these are:

1. **Physical security** of data centers with controlled, need-based access, located in nondescript facilities.
2. **Hardware infrastructure**,which includes servers, storage devices, and other appliances that AWS services rely on.
3. **Software infrastructure** that hosts the operating systems, service applications, and virtualization software.
4. **Network infrastructure**,which includes routers, switches, load balancers, firewalls, and cabling.
5. **Virtualization infrastructure**, including instance isolation.

## Customer security responsibility: Security in the cloud

Though AWS secures and maintains the cloud infrastructure, customers are responsible for security of everything that they put in the cloud. These steps include selecting the instance OS, securing the application, configuring security groups and firewalls, and managing the network configuration and user accounts.

When customers use AWS services, they maintain complete control over their content. Customers are responsible for managing critical content security requirements, including the following:

- Which content they choose to store on AWS
- Which AWS services are used with the content
- Which country that content is stored in
- The format and structure of that content and whether it is masked, anonymized, or encrypted
- Who has access to that content and how those access rights are granted, managed, and revoked

Customers retain control of the security that they choose to protect their data,
environment, applications, AWS Identity and Access Management (IAM) settings, and operating systems.

## Service characteristics and security responsibility

- **Infrastructure as a service (IaaS)** refers to services that provide basic building blocks for cloud IT. Cloud services that can be characterized as IaaS provide the customer with the highest level of flexibility and management control over IT resources. IaaS services are the most similar to existing on-premises computing resources that many IT departments are familiar with.

  AWS services—such as Amazon EC2—can be categorized as IaaS. Thus, the customer must perform all necessary security configuration and management tasks. Customers who deploy EC2 instances are responsible for managing the guest OS (including updates and security patches) and any application software installed on the instances. In addition, customers are responsible for configuring the security groups that AWS provided.

- **Platform as a service (PaaS)** refers to services that reduce the customer’s need to manage the underlying infrastructure (hardware, OS, and other resources). By using PaaS services, customers can focus on deploying and managing applications. Customers don’t need to worry about resource procurement, capacity planning, software maintenance, or patching.
  
  AWS services such as AWS Lambda and Amazon RDS can be categorized as PaaS because AWS operates the infrastructure layer, the operating system, and platforms. Customers only need to access the endpoints to store and retrieve data. With PaaS services, customers are responsible for managing their data, classifying their assets, and applying the appropriate permissions. However, these service act more like managed services, with AWS handling a larger portion of the security requirements. For these services, AWS handles basic security tasks, such as OS and database patching, firewall configuration, and disaster recovery (DR).

- **Software as a service (SaaS)** comprises services that provide centrally hosted software typically accessible through a web browser, mobile app, or application programming interface (API). With SaaS offerings, customers don’t need to manage the infrastructure that supports the service.
