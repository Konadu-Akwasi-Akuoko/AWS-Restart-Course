# Prevention: Network Hardening

## What is network hardening?

**Network hardening** concerns the protection of a computer network and its resources from unauthorized access, misuse, modification, or destruction. It is designed to preserve the usability and integrity of a network and the data that flows through the network. Network hardening combines **policies and procedures** with **hardware and software solutions** to achieve this goal.

Network hardening is typically achieved through two primary preventive actions: **network discovery hardening** and **network architecture security hardening**.

## Network security threats

A network security threat is any attempt to expose, alter, disable, or gain unauthorized access to an organization’s network. Its purpose is to steal data or perform a malicious activity. They occur when an attacker discovers the layout and resources on a network and exploits a vulnerability. As soon as an attacker gains access to the network, they can, for example, install malware on unprotected devices. They can disable a server or flood the network with so many requests that it becomes unusable (a denial of service [DoS] attack).

Network attacks start by discovering information about a network and then exploiting a vulnerability in the network. Therefore, identifying vulnerabilities that expose the network to a discovery or exploration attack is critical.

Types of network security discovery threats include the following:

- Network mapping
- Port scanning
- Traffic sniffing

## Network mapping

Network mapping is a technique that attackers use to discover the topology of a network. By using network discovery commands and tools, they can collect valuable information. This information can include the devices and hosts on the network and the paths that can be used to reach them. In the end, attackers can create a map of your network environment.

Attackers typically use the same tools that are available to network administrators to identify and map resources on a network. These tools include the `ping` and `traceroute` commands, and the open-source `Nmap` network exploration and security auditing utility.

## Network mapping tools example: `ping` and `traceroute`

The `ping` command returns:

- The IP address of the specified host if it can be reached
- A timeout if the host does not respond within a specified time
- Unknown host if the host does not exist

The `traceroute` command prints:

- The route that IP packets take to reach the specified host
- The IP address of each host that is encountered along the route
- Asterisks if a host along the route does not respond within a specified time (request timeout)

## Port scanning

Port scanning sends packets sequentially to ports on a host to determine which ports are open.

Port scanning is a method that attackers use to determine which protocols and services are available on a host. It tries to sequentially establish a connection to each port on a host to find open ports and identify which services are running.

## Port scanning tool example: `Nmap`

You can use Nmap to determine which IP protocols are supported by a network device or host.

```bash
nmap konadu.dev
```

`sudo nmap konadu.dev` will run an `nmap` scan with root privileges on the host `konadu.dev`. The scan will return information such as what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and other characteristics.

## Traffic sniffing

Traffic sniffing exposes the information that is traveling through a network.

Traffic sniffing, also known as packet sniffing, is a technique that attackers use to see the data flowing through a network. They watch the packets that pass through a network interface card (NIC) or network device. Any sensitive data that is not encrypted (such as clear text passwords) will be visible and can be collected for malicious use. For example, traffic sniffing can be used for man-in-the-middle attacks.

Protocol analyzer tools are typically used for traffic sniffing because you can use them to watch and store all traffic that goes through a network. Wireshark is an example of an open-source network protocol analyzer.

## Preventing network discovery

The goal of network discovery hardening is to keep attackers off the network.

To protect against network mapping and port scanning, restrict the use of, or disable, network discovery protocols, such as:

- Internet Control Message Protocol (ICMP)
- Simple Network Management Protocol (SNMP)

To protect against traffic sniffing, consider the following measures:

- **Disable promiscuous mode on NICs:** When a NIC is configured to run in promiscuous mode, it reads all packets that pass through the network. All packets are read, regardless of whether the NIC was the packet’s intended destination or not. If an attacker is able to sniff the traffic on that NIC, they would be able to see all the traffic on the network.
- **Use switches instead of hubs in a network:** A switch can mitigate sniffing attacks because it will forward packets to only the intended destination port. This port is identified in the packet. A hub broadcasts all incoming packets to all of the destination ports connected to it. For this reason, today (in 2022), the use of hubs
in networks is extremely rare.
- **Encrypt sensitive data in transit:** A hardware device or software can be used to encrypt the data that flows through your network. You will learn more about protecting data in a subsequent module.

It is also important to protect networks from discovery tools and mechanisms because of the security risks that these tools present. One of the most effective ways to do so is to block or restrict the use of the discovery protocols that these tools use. The most common network discovery tools use the Internet Control Message Protocol (ICMP). For example, the ping and `traceroute` commands and the `nmap` utility use ICMP.  Tools that use the Simple Network Management Protocol (SNMP) can also expose detailed network data. Network operators typically use them to monitor and manage the devices on a network. If the use of SNMP tools is not securely controlled, attackers can exploit them. By restricting the use of or disabling network discovery protocols, you can prevent attackers from getting crucial information about your network.

To help network discovery hardening in the AWS Cloud, you can use the Amazon Inspector service. This service provides functions to discover network exposure vulnerabilities.

## Amazon Inspector: Network reachability assessment

Amazon Inspector scans Amazon Elastic Compute Cloud (Amazon EC2) instances for open network paths and other network reachability issues and provides guidance about restricting access that is not secure.

You can use Amazon Inspector to analyze the accessibility of critical ports and generate findings about the exposure of each port. These findings highlight network configurations that might be overly permissive or that might allow for potentially malicious access. Amazon Inspector also attaches a severity level for each finding that it reports. The severity of a network reachability vulnerability is determined by the service, ports, and protocols that are exposed and by the type of open path.

## Other network discovery countermeasures

Another way to prevent the discovery of a network is to monitor for symptoms that point to such an activity. For example, if an unknown IP address appears on the network, it can indicate that an attacker has successfully connected to the network. You can use your inventory of the allowed hosts of a network to perform this check.

Likewise, if you detect that ports are being scanned sequentially, it can mean that an unauthorized port scan is in progress. You can use an intrusion prevention system (IPS) to monitor such conditions and alert you when they arise.

You should also limit remote administration access. Specifically, you should limit the following:

- **Who** is permitted to have administrative access
- **How** the devices are accessed (for example, which protocols can be used)
- **Where** the devices are accessed (for example, remote administration from the internet is strictly prohibited)

Implement an administrative policy that defines authentication, authorization, and accounting (AAA) rules to protect the access to network devices. This policy should include rules for the following:

- To assign different levels of access permission to different administrative roles
- To log access, commands, and changes to network devices
- To enforce change control procedures

## What is network architecture hardening?

Network architecture hardening increases the security of a network through design improvements.

Network architecture hardening is achieved through the following:

- Adding security components to the network
  - Network firewalls
  - Intrusion prevention systems (IPSs)
- Segmenting a network
  - Creating private subnets
  - Using network access control lists (network ACLs)

## Network firewall

A network firewall is a hardware or software component that filters incoming and outgoing traffic in a network to prevent unauthorized access. It allows or blocks data packets into the network based on rules that you specify. These rules use the information in the packet to determine whether to allow the packet to pass. This information includes the packet’s source IP address, destination IP address, source port number, destination port number, and port type (protocol).

The number and placement of firewalls depend on your network topology and security requirements. They will be influenced by factors such as the number of devices, type of devices, access requirements, and vulnerability risk.

## Network firewall example

The network firewall is placed in front of web servers and at the entry point of traffic into a corporate network. In this way, you can protect assets in the intranet, the trusted internal network, from requests that come from the untrusted public internet.

## Network firewall best practices

- Block all traffic first, and then gradually permit authorized traffic. In this way, you apply the best practice principle of least privilege.
- Log all exceptions. By recording all filtering decisions, including packet rejections, you can capture data that can be analyzed later to detect possible patterns of attack.
- Position firewalls at the junction points of the network as close to the traffic source as possible. In this way, you can identify and stop bad traffic before it reaches deep into your network.
- Supplement network firewalls with application firewalls. An application firewall filters the communication into and out of an application and provides an additional layer of access protection.

Another network firewall best practice is to use firewalls to create different network zones in your environment. Each zone provides a different level of network security based on the number and type of firewalls that protect them. In this way, you can place a network resource in the zone that best meets its security needs. Here are some zones where you can place firewalls:

- The internet zone represents an uncontrolled area because it is unsecure.
- The perimeter zone is secured by one firewall and is considered partially controlled. It serves as a buffer between two zones with different trust levels.
- The internal, or intranet, zone is considered fully controlled because it is secured by two firewalls.

## AWS security groups

In the AWS Cloud, security groups act like a built-in firewall for virtual servers (EC2 instances). By filtering traffic to an instance, a security group provides control over which traffic to allow into an instance. Security groups are associated with the network interfaces on an instance.

To control the access to an instance, you configure a security group rule. You can define rules that allow inbound or outbound traffic. You cannot define deny rules. Rules are based on the protocol, port number, and source or destination IP address of the traffic.

Security groups are stateful: if you allow a certain type of traffic into an instance, the same type of traffic is allowed out of the instance. This rule applies regardless of any outbound rules. Conversely, if a particular type of traffic is allowed out of an instance, it is also allowed into the instance regardless of any inbound rules.

## Intrusion prevention system (IPS)

An IPS is a network security component that identifies and prevents threats. An IPS prevents threats by analyzing packets and blocking or changing them. It monitors the network for malicious incidents and acts to prevent these malicious threats from affecting the system.

An IPS can detect an attack by using different mechanisms, including the following:

- Anomaly-based detection: The IPS compares the current traffic pattern against established baselines for any deviation.
- Signature-based detection: The IPS monitors and analyzes the traffic for known patterns of attack.

## IPS example: AWS Network Firewall

AWS Network Firewall is a service that facilitates the deployment of essential network protections to virtual private clouds (VPCs) on AWS. Its IPS provides active traffic flow inspection with real-time network and application layer protections against vulnerability exploits and brute force attacks.

Network Firewall uses a signature-based detection engine that matches network traffic patterns to known threat signatures. Its criteria for matching include packet anomalies and packet attributes such as byte sequences.

You use rules to define the criteria used for inspecting traffic and for handling packets and traffic flows that match the inspection criteria. For example, you can choose to drop or pass a packet or all packets in a traffic flow based on the inspection criteria.

## Segmenting a network

Network segmentation, also called **subnetting**, is another technique for enhancing the security of a network. Subnetting is the process of taking a large network and dividing it into smaller networks. Each smaller network is called a subnet and is assigned a contiguous subset of the IP address range of the large network. Each subnet can then be secured to meet the specific needs of the resources that it will host.

For example, in an organization with multiple office locations, each location might provide a different service and have different security requirements. Therefore, the organization might want to create individual subnets for each location so that they can apply different levels of security to the different subnets.

Other benefits of subnetting include the following:

- **Easier network management:** Each subnet represents a smaller unit that can be managed and configured independently and without affecting other subnets.
- **Improved network performance:** Having multiple subnets relieves the traffic congestion in a network. Traffic is routed more efficiently because traffic destined for a device within a subnet stays in that subnet.

## Network access control list (network ACL)

A network ACL acts as a firewall to control inbound and outbound traffic. It is typically implemented on a switch or a router and controls the traffic based on rules that you define.

A network ACL acts as a firewall to control inbound and outbound traffic. It is typically implemented on a switch or a router and controls the traffic based on rules that you define.

A network ACL is stateless, which means that the inbound and outbound rules are independent of each other.If a type of request traffic is allowed inbound, you must explicitly define an outbound rule for the same type to allow the response traffic.

In the AWS Cloud, a network ACL is used to protect a subnet inside a VPC. You can define allow or deny rules based on the protocol, port number, and source or destination IP address of the traffic.

## Layered security model for a VPC on AWS

Network ACLs and security groups provide multiple levels of network security to protect an instance.

1. Network ACLs protect at the subnet level.
2. Security groups protect at the instance level.
