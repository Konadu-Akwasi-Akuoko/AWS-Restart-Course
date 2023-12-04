# What is AWS

## Web services

AWS offers 3 models of cloud computing services, and they are IaaS, PaaS, and Saas. And the basic building blocks of cloud IT include:

- network features
- compute
- data storage space

 Almost everything that you can do with a traditional on prem infra can be done with AWS in the cloud.

## What are web services?

A web service is any piece of technology that makes itself available on the internet. Web services happen over a network with a request and response to and from the server. The standard language that web services use for request and response are Extensible Markup Language(XML) or Javascript Object Notation(JSON) which connects users to Application Programming Interfaces(API).

## AWS services

AWS is a secure cloud service provider with many services that let businesses scale and grow.

Because it is an on-demand service, companies can access compute, data storage, and networking infrastructure over the internet.

An example of how a company use AWS:

A database application is being built using various Amazon Web Services (AWS).

1. Customers send data to **Amazon Elastic Compute Cloud (EC2)** instances, a service in the Compute category.
2. The EC2 servers batch the data in 1-minute increments and add an object per customer to **Amazon Simple Storage Service (S3)**, which is the chosen AWS storage service.
3. A nonrelational database like **Amazon DynamoDB** is used to power the application and build an index to find all the objects from a given customer collected over a certain time period.
4. These services might be run inside **Amazon Virtual Private Cloud (VPC)**, a service in the networking category.

This shows how you can select and combine different AWS services from various categories to build a solution, in this case, a database application. However, the solutions that you build can also be quite complex.

## Choosing  a service

AWS has a lot of services, but what you choose solely depends on your business goals and your technology requirements.

Here is an example of some services that AWS offers:

| Community Services | Storage Services | Management and Governance Services | Database Services | Security, Identity, and Compliance Services | Networking and Content Delivery Services | AWS Cost Management Services |
|---|---|---|---|---|---|---|
| AWS Lambda | Amazon S3 | Amazon CloudWatch | Amazon DynamoDB | Amazon Cognito | Amazon VPC | AWS Budgets |
| Amazon Elastic Beanstalk | Amazon Glacier | AWS Trusted Advisor | Amazon RDS | AWS Shield | Amazon Route 53 | AWS Cost Explorer |
| Amazon EC2 Auto Scaling | Amazon EBS | AWS CloudTrail | Amazon Redshift Aurora | AWS WAF | Amazon CloudFront | |
| Amazon ECS | | AWS Artifact | | AWS KMS | Elastic Load Balancing | |

Each row represents a different service offered by AWS under the respective category. For example, under "Community Services", you have AWS Lambda, Amazon Elastic Beanstalk, Amazon EC2 Auto Scaling, and Amazon ECS.

## Three ways to interact with AWS

- **AWS management console:** an easier to use gui for managing AWS services
- **AWS CLI:** a command line interface that you can use to manage AWS services
- **AWS SDK:** these SDKs give the privilege for users to access AWS services directly in their code

## AWS cloud adoption framework

The AWS cloud adoption framework helps companies to adopt the cloud efficiently and effectively. The AWS cloud adoption framework helps companies to align their people, process, and technology which helps them migrate their infra to the cloud.

## AWS documentation

The AWS docs help you find user guides, developer guides, API references, tutorials and more. Each tool and SDK in the AWS web services also has it's own docs.
