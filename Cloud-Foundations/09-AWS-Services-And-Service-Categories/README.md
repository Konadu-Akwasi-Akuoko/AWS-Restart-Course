# AWS Services and Service Categories

## AWS service categories

AWS offers a broad set of cloud-based services in many product or service categories. Each category also consist of one or more services. Some of these main services are:

- AWS Cost Management
- Compute
- Containers
- Database
- Management and Governance
- Networking and Content Delivery
- Security, Identity, and Compliance
- Storage

This means that if you want to use a compute service, AWS have one or more services under the compute service category, something like an EC2 instance.

## Storage service category

AWS storage services provide cloud storage services, some of them are:

- **Amazon Simple Storage (Amazon S3)** is an object storage service that offers scalability, data availability, security, and performance. Use it to store and protect any amount of data for websites and mobile apps.

- **Amazon Elastic Block Store (Amazon EBS)** is high-performance block storage that is designed for use with Amazon EC2 for both throughput-intensive and transaction-intensive workloads. It is used for various workloads, such as relational and non-relational databases, enterprise applications, containerized applications, big data analytics engines, file systems, and media workflows.
  - “Throughput-intensive” workloads are those that require a lot of data to be moved around quickly. This could be something like streaming video, where you’re constantly sending large amounts of data.

  - “Transaction-intensive” workloads, on the other hand, are those that require a lot of read/write operations, often with smaller amounts of data. This could be something like a database, where you’re constantly reading and writing small bits of data.

- **Amazon Elastic File System (Amazon EFS)** provides a scalable, fully managed elastic Network File System (NFS) file system for AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes, growing and shrinking automatically as you add and remove files.
  - Amazon EFS uses the Network File System (NFS) protocol, which is a standard for accessing files over a network.

- **Amazon Simple Storage Glacier** is a secure, durable, and low-cost Amazon S3 cloud storage class for data archiving and long-term backup. It is designed to deliver 99.999999999 percent of durability.

## Compute service category

AWS compute services provide cloud compute services, some of them are:

- **Amazon Elastic Compute Cloud (Amazon EC2)** provides resizable compute capacity as virtual machines in the cloud.

- **Amazon EC2 Auto Scaling** gives you the ability to automatically add or remove EC2 instances according to conditions that you define.

- **AWS Elastic Beanstalk** is a service provided by Amazon Web Services (AWS) that simplifies the process of deploying and scaling web applications and services. AWS Elastic Beanstalk takes your web application and deploys it on the AWS cloud. It also automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring, which makes it easier for you to deliver your web application to users.

- **AWS Lambda** gives you the ability to run code without provisioning or managing servers. You pay for only the compute time that you consume, so you won’t be charged when your code isn’t running.

## Container service category

AWS provides a range of services to help you manage and deploy your containerized applications, some of them are:

- **Amazon Elastic Container Service (Amazon ECS)** is a highly scalable, high-performance container orchestration service that supports Docker containers.

- **Amazon Elastic Container Registry (Amazon ECR)** is a fully managed Docker container registry that facilitates storing, managing, and deploying Docker container images.

- **Amazon Elastic Kubernetes Service (Amazon EKS)** facilitates deploying, managing, and scaling containerized applications that use Kubernetes on AWS.

- **AWS Fargate** is a compute engine for Amazon ECS that you can use to run containers without managing servers or clusters.

## AWS database service category

AWS database services provide cloud database services, some of them are:

- **Amazon Relational Database Service (Amazon RDS)** facilitates setting up, operating, and scaling a relational database in the cloud.

- **Amazon Aurora** is a relational database that is compatible with MySQL and PostgreSQL.

- **Amazon Redshift** gives you the ability to run analytic queries against petabytes of data that is stored locally in Amazon Redshift. You can also run queries directly against exabytes of data that are stored in Amazon S3.

- **Amazon DynamoDB** is a key-value and document database that delivers single-digit millisecond performance at any scale with built-in security, backup and restore, and in-memory caching.

## Networking and content delivery service category

AWS Networking and Content Delivery services provide a broad set of options for connecting and delivering applications, services, and data across different environments.

- **Amazon Virtual Private Cloud (Amazon VPC)** gives you the ability to provision logically isolated sections of the AWS Cloud.

- **Elastic Load Balancing** automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions.

- **Amazon CloudFront** is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and application programming interfaces (APIs) to customers globally.

- **Amazon Route 53** is a scalable, cloud Domain Name System (DNS) web service. It is designed to give you a reliable way to route end users to internet applications. Route 53 translates names (like <www.example.com>) into the numeric IP addresses (like 192.0.2.1) that computers use to connect to each other.

- AWS Direct Connect provides a way to establish a dedicated private network
connection from your data center or office to AWS. Using AWS Direct Connect can reduce network costs and increase bandwidth throughput.

- AWS Client VPN provides a secure private tunnel from your network or device to the AWS global network.

## Security, identity, and compliance service category

The Security, Identity, and Compliance service category in AWS is a collection of services designed to help you protect your data, manage access, and comply with regulations.

- **AWS Identity and Access Management (IAM)** gives you the ability to manage access to AWS services and resources securely. By using IAM, you can create and manage AWS users and groups.

- **AWS Organizations** permits you to restrict what services and actions are allowed in your accounts.

- **Amazon Cognito** gives you the ability to add user sign-up, sign-in, and access control to your web and mobile apps.

- **AWS Artifact** provides on-demand access to AWS security and compliance reports and select online agreements.

- **AWS Key Management Service** (AWS KMS) provides the ability to create and manage keys.

- **AWS Shield** is a managed distributed denial of service (DDoS) protection service that safeguards applications running on AWS.

## AWS cost management service category

The AWS Cost Management service category is a suite of tools and services provided by Amazon Web Services (AWS) to help you understand, manage, and optimize your costs on AWS.

- **AWS Cost and Usage Report** contains the most comprehensive set of AWS cost and usage data available. It includes additional metadata about AWS services, pricing, and reservations.

- **AWS Budgets** provides the ability to set custom budgets that alert you when your costs or usage exceeds (or will likely exceed) your budgeted amount.

- **AWS Cost Explorer** has an easy-to-use interface that you can use to visualize, understand, and manage your AWS costs and usage over time.

## Management and governance service categories

Amazon Management and Governance services are a suite of tools and services provided by Amazon Web Services (AWS) that help customers manage and govern their AWS resources.

- **AWS Management Console** provides a web-based user interface for accessing your AWS account.
- **AWS Config** provides a service that helps you track resource inventory and changes.
- **Amazon Cloud Watch** gives you the ability to monitor resources and applications.
- **AWS Auto Scaling** provides features that you can use to scale multiple resources to meet demand.
- **AWS Command Line Interface (AWS CLI)** provides a unified tool to manage AWS services.
- **AWS Trusted Advisor** helps you optimize performance and security.AWS Well-Architected Tool provides help in reviewing and improving your workloads.AWS CloudTrail tracks user activity and API usage.
