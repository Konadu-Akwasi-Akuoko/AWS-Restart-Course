# Internet Protocols (IP)

## IP

An IP (Internet Protocol) address is like your home address but for your computer when it's connected to a network or the internet. It's a unique identifier that helps computers locate and connect with each other.

There are two types of IP addresses:

1. **Local IP**: This works within a single network, like your home or office network.
2. **Global IP**: This works over the entire internet and is needed to find a system online.

Just like your home address can change when you move, an IP address can also change. It's a fluid value. So, in simple terms, an IP address is your computer's address in the digital world.

We can use IP addresses to identify devices. Also we can use port numbers to identify endpoints.Supports subnetting to subdivide a network.

## IP addresses

An IP address uniquely identifies a device on a network. Each device on a network has an IP address, and it serves two main functions:

- It identifies a host and a network.
- It is also used for location addressing.

An IP address can be static or dynamic. Also it can be made public or private, in the sense that if it is public, other people on the internet can visit your public IP address.

## Private and Public IP addresses - OSI model

An IP address works in layer 3(networking) of the OSI model. IP addresses can be assigned to devices in a dynamic or static way. IP addresses can also be made public or private. The IP address is very important for trouble shooting. Why?

1. You might have experience latency, where a site or application is taking a long time to load, possibly to the point that it times out. In corporate settings, latency is a big deal, and finding out exactly where and what is causing it can save time and money. When troubleshooting latency, at layer 3, there is a command called traceroute where it provides a report on the path the packet takes from source to destination, each server is called a hop, and it checks for packet loss as well.
2. You might come across an issue where a server is not responding to requests, could it be layer 3 related? Or layer 4? Starting at the bottom and working your way up will assist in a solid troubleshooting method. Checking the Physical aspects first at layer 1 if possible, understanding what operates at layer 2, and working your way up to layer 3 IP addresses.
3. Understanding how, where, and what works at each layer will assist you in troubleshooting basic networking issues.

## Layer 3 of the OSI model

Layer 2 (data link) establishes the connection between two nodes. These nodes have the physical components that use a MAC address. This needs to be translated to a logical address. At layer 3 (network), this translation between logical and physical takes place.

## Private and Public IP addresses

Sure, let's break it down:

**Private IP addresses** are like your home phone number. They are only known and used within your home (or in this case, your private network). Just like you can't call your home phone from a different city, computers outside your network can't reach your computer using its private IP address. There are certain ranges of these private IP addresses, which are set by a guide called RFC 1918. These ranges are:

- 10.0.0.0 to 10.255.255.255
- 172.16.0.0 to 172.31.255.255
- 192.168.0.0 to 192.168.255.255

**Public IP addresses**, on the other hand, are like your home's street address. They are unique and can be used to locate your home (or in this case, your network) from anywhere in the world. So, if a computer knows your network's public IP address (like 54.239.28.85), it can send information to your network from anywhere on the internet. This is similar to how anyone who knows your home address can send you a letter from anywhere in the world.

All in all, private IP addresses are used for communication within a network, while public IP addresses are used for communication over the internet.

## IP addresses - IPv4

An IP address is a unique identifier for a device on a network, following the IPv4 standard. It's made up of four numbers (0-255), separated by periods, forming a 32-bit binary number. Each of these numbers is an 8-bit binary number, so the total is 32 bits. The IP address identifies both the network and the specific device on that network.

For example, consider the IP address 10.100.20.5. Here, '10' is an 8-bit number, '100' is another 8-bit number, '20' is the third 8-bit number, and '5' is the final 8-bit number. Together, they add up to a 32-bit number. The 'network portion' of the IP address is the number assigned to your network, while the 'host portion' is the number assigned to each device (or 'host') on that network.

For example, let’s consider an IP address 192.168.1.100 with a subnet mask 255.255.255.0. Here, the first three numbers (192.168.1) form the network portion, and the last number (100) forms the host portion. This is because the subnet mask 255.255.255.0 has '1’s for the first three numbers and '0’s for the last number.

So, in an IP address, the network portion identifies the specific network, and the host portion identifies the specific device (or ‘host’) on that network. The exact division between the network and host portions can vary depending on the subnet mask.

## IP addresses - IPv6

IPv6 standard extends the range of IPv4 addresses by a factor of 1,028. It uses a group of hexadecimal numbers that are separated by eight colons. The extra digits in IPv6 allow an expanded number of available addresses. Each decimal value now allows for 16 bits instead of the 8 bits that IPv4 provided. IPv4 provided an estimated 4.2 billion addresses, IPv6 provides around 340 trillion, trillion, trillion addresses to keep up with today’s growing list of internet of things (IoT) devices.

## IP addresses - dynamic and static

IP addresses can be assigned to devices in a dynamic or static way.A device with a static address has an IP address that does not change. Static addresses are useful for devices like servers or printers that devices connect to often. A device with a dynamic address has an assigned IP address that can change.

Dynamic address are useful when devices like a work-assigned laptop leave the work network and then connect to the user’s home network.

## IP addresses – EC2 instances

With staticIP addresses, whether a machine or EC2 instance is turned off and back on, the IP address will stay the same. It will not change. If the instance is used as a server, the best address to assign it is a static IP address, also known as an Elastic IP address (EIP).

With dynamicIP addresses, when a machine or EC2 instance is turned off, the IP address will change.

## IP addresses – summary

Public or private IP addresses:

- Public IP address can be accessed over the internet. Its globally unique IP address that is assigned to a computing device that must access the internet.
- Private IP address cannot be accessed from the internet. Example: the application and database servers in your data center are assigned private IP addresses because you might not want other devices to know about these servers.

## IP addresses –special purpose

When a network is assigned a range of IP addresses, such as 10.0.0.0-10.255.255.255, a few addresses have a special purpose. They are not assigned as host addresses.

- The default router address is typically the second address in the range: 10.0.0.1.
- The broadcast address is the last address in the range: 10.255.255.255

## Converting IP addresses to binary

To understand IP addressing, you can convert the number into binary. A binary number is expressed in the base-2 numeral system, and it consists of only zeroes and ones:

| Bit Position | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary Power | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| Decimal Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

- The value of 0 or 1 is known as a binary digit, or bit.
- In an IPv4 address, each of the four numbers between the dots is an 8-bit binary number. This means the entire address is a 32-bit binary number.

## Port numbers

A device might send or receive data from multiple devices at the same time. A port number, in combination with an IP address, enables the device to determine the exact source or destination of the data, which is also known as the endpoint.

An example is to think of a port number like an extension to a phone number. You might have the number to the hospital (IP), but you will need the extension (or port) in order to get to the exact office (endpoint) you are trying to reach.

Common Port number examples:

- Port 22: SSH (Secure Shell)
- Port 53: DNS (Domain Name System)
- Port 80: HTTP (Hypertext Transfer Protocol)
- Port 443: HTTPS (Hypertext Transfer Protocol Secure)
- Port 3389: RDP (Remote Desktop Protocol)
- Port 3000: React default port
- Port 4200: Angular default port

Common Port number examples:Port 22: SSH (Secure Shell)Port 53: DNS (Domain Name System)Port 80: HTTP (Hypertext Transfer Protocol)Port 443: HTTPS (Hypertext Transfer Protocol Secure)Port 3389: RDP (Remote Desktop Protocol).

## Port number example

When a port is blocked by a firewall, or if using a VPC it can be blocked by an AWS service like a Security Group or Network Access Control List, the source will not be able to send or receive traffic depending on the rules. Essentially ports can be blocked or allowed to certain traffic for security reasons.

When troubleshooting issues, you can use commands such as netstat, ss, and telnet. These commands are used at layer 4 of the OSI, but some can be used at layer 7

- The command `netstat` confirms established connections, so if a port is blocked, it will not show as a established connection.
- The command `telnet` confirms TCP connections to a web server, note, that this can also be used at layer 7 in the OSI model
- The command `ss` is very similar to netstat, however, it confirms IPv4 connections only.
