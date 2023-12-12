# Networking In The AWS Cloud

## Networking in the cloud

| Traditional topology          | AWS service                                             |
|------------------------------|--------------------------------------------------------|
| Data center                  | Amazon VPC                                              |
| Router                       | Route tables                                            |
| Switches (subnets)           | Subnets                                                 |
| Firewall                     | Security groups and network access control lists (network ACLs) |
| Servers and operating systems| Amazon Elastic Compute Cloud (Amazon EC2) instances     |
| Modem                        | Internet gateway                                        |

As described earlier, networking in the cloud is similar to regular networking in a data center:

- A data center as a whole most closely resembles the function of a VPC. In a VPC, you can launch multiple AWS services that are needed to create a working, scalable network. However, within a VPC, no maintenance is required, and you can create an isolated architecture within minutes. A data center involves multiple components: internet, servers, firewalls, switches, and more. Like a data center, a VPC requires the same services to operate.
- A router in a traditional environment has multiple functions, such as filtering packets, routing traffic, and storing them in a route table. In AWS, the service that most closely resembles a router is a route table, where the owner inputs routes within the VPC.
- A switch acts as a subnet and switches data as it comes in. AWS uses subnets in every architecture. Every node (EC2 instance) belongs in a subnet. Although the functions of a switch and an AWS subnet do not match, the functions of a subnet from both work the same architecturally. Subnets are used to logically isolate groups of internet protocols together.
- Firewalls block traffic based on a set of rules. AWS has security groups that block traffic at the node (Amazon EC2 level) and network ACLs that block traffic at the subnet level. These security groups also block traffic based on a set of rules.

## Amazon VPC

Amazon VPC is a service that you can use to provision a logically isolated section of the AWS Cloud. This service is called a virtual private cloud, or Amazon VPC. With an Amazon VPC, you can launch your AWS resources in a virtual network that you define.

- You can use Amazon VPC to create a private network in the AWS Cloud that uses many of the same concepts and constructs as an on-premises network.
- Just like an on-premises network, you can select IP address ranges and allocate them by creating subnets.
- All of the physical components of an on-premises network have become virtual. Instead of plugging devices in, in a virtual environment like Amazon VPC, you would attach resources to make a network.

## Why use an Amazon VPC

- It is more secure, scalable, reliable, cost-effective, and easy to use than a traditional data center.
- It replaces the need for your own data center.
- You can create multiple Amazon VPCs for testing, owning customer accounts, and more.

## Amazon VPC features

An Amazon VPC includes the following features:

- It is dedicated to an AWS account.
- It belongs to a single AWS Region.
- It can span multiple Availability Zones.
- It is logically isolated from other Amazon VPCs.
- You can create multiple Amazon VPCs in an AWS account to separate networking environments.
- You can create subnets in a VPC; however, fewer subnets are recommended to reduce the complexity of the network topology.
- Multiple Amazon VPCs can span different Availability Zones in an AWS Region.

## IP addressing in Amazon VPC

When you create a VPC, you must specify the IPv4 address range by choosing a CIDR block, such as 10.0.0.0/16.

- An Amazon VPC address range could be as large as /16 (65,536 addresses) or as small as /28 (16 addresses).
- Private IP ranges should be used according to RFC 1918.

1. **Private IP ranges should be used according to RFC 1918**: This means that the IP addresses within your Amazon VPC (Virtual Private Cloud) should be set to private IP ranges as defined by a standard called RFC 1918¹. These ranges are not routable over the internet, which helps to keep your resources secure.

2. **If private IP ranges are not used, resources within the VPC that have public IPs can get replies back from the internet that do not belong to the Amazon VPC**: If you use public IP ranges within your VPC, you might receive responses from the internet that were not intended for your VPC. This could potentially lead to confusion or security issues¹.

3. **IP addresses should not overlap with the addresses of other networks to which an Amazon VPC is connected**: To avoid confusion and ensure that each device can be accurately identified, the IP addresses within your VPC should be unique and not used in any other network that your VPC might connect to¹.

4. **The address range of the Amazon VPC cannot be changed after the VPC is created; however, a secondary VPC CIDR can be assigned to the VPC**: Once you've set up your VPC with a certain range of IP addresses, you can't change that range. However, you can add a secondary range (known as a CIDR block) if you need more IP addresses.

## Private IP address range

When an Amazon VPC is created, choose from a CIDR block from the following private IPv4 address ranges (also specified in RFC 1918):

| RFC 1918 range            | Example Amazon VPC CIDR block |
|---------------------------|-------------------------------|
| 10.0.0.0–10.255.255.255   | 10.0.0.0/16                   |
| 172.16.0.0–172.31.255.255 | 172.31.0.0/16                 |
| 192.168.0.0–192.168.255.255 | 192.168.0.0/16               |

- The smallest permitted block size is /28 and the largest is /16.
- A publicly routable CIDR block that falls outside the private range can be used; however, it is not recommended. This situation can cause issues if you are using publicly routable resources to the internet.

- RFC 1918 shows the private address space and its use case (within enterprise use). However, when the public IP address is enabled or an Elastic IP address is assigned, it gives a public IP address to the instance. This public IP address allows it to be routable on the internet regardless of the private address. This address is unique and is from the Amazon pool of IP addresses.
- It is recommended that you use the private IPv4 address range.
- When using anything outside the IPv4 address range, you run into the possibility of receiving replies from other resources that are not your own resources. These replies might be from other random sources on the internet.
- Some third-party tools can assist in calculating and creating IPv4 subnet and CIDR blocks. Try searching for “subnet calculator” or “CIDR calculator.”
- Within each subnet CIDR block, AWS reserves the first four IP addresses and the last IP address:
  - 10.0.0.0 –Network address
  - 10.0.0.1 –VPC router
  - 10.0.0.2 –Domain Name System (DNS) server
  - 10.0.0.3 –Reserved for future use
  - 10.0.0.255 –Network broadcast, not supported in the VPC, but still reserved
  - You can always add a secondary CIDR block to an Amazon VPC.

## Amazon VPC components


