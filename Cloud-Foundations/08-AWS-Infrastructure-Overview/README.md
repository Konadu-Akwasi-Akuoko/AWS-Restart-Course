# AWS Infrastructure Overview

The **AWS Global Infrastructure** is designed and built to deliver a flexible, reliable, scalable, and secure cloud computing environment with high-quality global network performance.

The AWS global infra consists of three main elements, they are regions, availability zones, and point of presence. AWS infra spans 84 availability zones in 26 geographical regions around the world.

## AWS data centers

AWS data centers is the foundation for AWS services. A data center is the physical location where the data is stored and the processing occurs.

## AWS availability zones

Each availability zone is made up of one or more data centers that are designed for fault isolation. They are designed for fault isolation.

Availability Zones are interconnected with other Availability Zones by using high-speed private links. Users can choose their own availability zones.

Fault tolerance design helps to ensure that if a fault (an error or failure) occurs in one data center, it doesn’t impact the others. This way, even if there’s a problem in one data center, the others can continue to operate normally, providing a high level of reliability and availability for AWS services. This is particularly important for applications that require high availability and fault tolerance.

You are responsible for selecting the Availability Zones where your systems will reside. Systems can span across multiple Availability Zones. AWS recommends replicating across Availability Zones for resiliency. You should design your systems to survive temporary or prolonged failure of an Availability Zone if a disaster occurs. Distributing applications across multiple Availability Zones helps them remain resilient in most failure situations, including natural disasters or system failures.

## AWS regions

An AWS Region is a physical geographical location in the world where AWS has multiple Availability Zones. To achieve fault tolerance and stability, Regions are isolated from each other.

When you store data in a specific Region, it’s not replicated outside that Region. AWS never moves your data out of the Region that you put it in. It’s your responsibility to replicate data across Regions if your business needs require it.

## Selecting a region

You should consider a few factors when you select the optimal Region or Regions where you store data and use AWS services.

One essential consideration is **data governance** and legal requirements. Local laws might require that certain information be kept within geographical boundaries.

 Also it’s generally desirable to run your applications and store your data in a Region that is as close as possible to the user and systems that will access them. This will help you **reduce latency**.

 Finally, there is some variation in the cost of running services, which can depend on which Region you choose. For example, as of this writing, the per-hour cost to run a t3.medium Amazon Elastic Compute Cloud (Amazon EC2) On-Demand Linux Instance in the US East (Ohio) Region might differ from running the same instance in the Asia Pacific (Tokyo) Region.

 In summary, when you select a Region, you should consider which Region offers the services that you need and where it’s located.

## Points of presence

A PoP is where end users access AWS services through either the Amazon CloudFront or the Amazon Route 53 services.

As of August 2020, the global AWS infrastructure contained 216 PoPs, consisting of 205 edge locations and 11 Regional edge caches located in most of the major cities around the world. These PoPs serve requests for CloudFront and Route 53.

CloudFront is a content delivery network (or CDN) used to distribute content to end users to reduce latency. Route 53 is a Domain Name System (DNS) service. Requests going to either one of these services will be routed to the nearest edge location automatically.

Regional edge caches, used by default with CloudFront, are used when you have content that is not accessed frequently enough to remain in an edge location. Regional edge caches absorb this content and provide an alternative to the content having to be fetched from the origin server.

## AWS Infrastructure Features

An Availability Zone is a data center or collection of data centers. Availability Zones are connected with low-latency, high-throughput, highly redundant networking. Availability Zones are physically distinct. Each one has equipment like uninterruptible power supplies, cooling equipment, backup generators, and security, to help ensure uninterrupted operations.

AWS Regions provide multiple physically separated, isolated Availability Zones. An AWS Region contains two or more Availability Zones.

This infrastructure has several valuable features:

- First, it is elastic and scalable. This means that resources can dynamically adjust to increases or decreases in capacity requirements. The infrastructure can also rapidly adjust to accommodate growth.
- Second, this infrastructure is fault tolerant, which means it has built-in component redundancy so that it can continue operations despite a failed component.
- Finally, it requires minimal to no human intervention while providing high availability with minimal downtime.
