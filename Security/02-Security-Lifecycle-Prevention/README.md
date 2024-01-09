# Security Lifecycle: Prevention

## Prevention in the security life cycle

Prevention is the first and arguably the most important phase of the security lifecycle. It offers the opportunity to proactively stop threats from becoming breaches through the implementation of security controls.

In the prevention stage, you:

- **Identify the assets to be protected:** You build an inventory of the networking devices, computers, applications, and other physical and digital resources that you must protect.
- **Assess asset vulnerability:** You examine each asset in the inventory and determine the type and level of protection that the asset needs.
- **Implement countermeasures:** For each asset to be protected, you implement security controls to prevent attacks against the asset from being successful.

## Identifying assets

You must know what resources are in your computing environment so that you can protect them. Therefore, the first step in prevention is to create an inventory of your computing assets. This inventory can be extracted from existing design documents, such as network topology diagrams, architecture diagrams, and other system documentation. The list should provide a clear understanding of what components are in your environment. It also should convey what their key properties are (for example, the IP address of network devices) and how they relate to each other.

Various tools can help you in this task. For example, for network discovery:

- You can use the `ping` command to determine the IP address of hosts in your environment and their reachability.
- You can use the open-source `Nmap` utility to discover the available hosts on a network and gather important information such as the services that they’re running.

In the AWS Cloud, the AWS Systems Manager service provides an inventory function that you can use to list the managed instances in your account. For each instance, the service can identify key information, such as the instance’s IP address and operating system and the applications installed on the instance.

## Assessing asset vulnerability

As soon as you have identified your list of assets, you can perform a vulnerability assessment on each one of them. The goal of vulnerability assessment is to search for security weaknesses or potential exposures so that you can implement countermeasures against them. It involves analyzing the asset’s security posture by asking questions relevant to the asset type, its intended use, and its desired level of protection.

Example questions to ask by asset type include the following:

- **The host assessment:** evaluates how vulnerable servers are to attacks.
  - Which ports are open?
  - Which devices are exposed to the public?
- **The network assessment:** evaluates the accessibility of networks and network devices.
  - Which applications are running?
  - Which services are running?
  - Are security patches up to date?
- **The data assessment:** examines the level of protection for data traveling through the system (data in transit) and data stored in the system (data at rest). It protects this data from the perspective of the confidentiality, integrity, and availability (CIA) triad.
  - Does the source code contain security vulnerabilities?
- **The application assessment:** evaluates the security vulnerability in an application’s source code.
  - Is data in transit and at rest adequately protected?

As you analyze the security vulnerability of an asset, you should consider the potential threats. It is often useful to know the common types of threats that have 9
been identified in the industry for the asset’s type. One resource that provides such information is the [Common Vulnerabilities and Exposures (CVE) website](https://cve.mitre.org/). The CVE website is an online resource that lists publicly disclosed cybersecurity vulnerabilities.

Automated tools, such as database scanners and application scanners, are available to help identify both existing and potential security vulnerabilities. When they detect a known vulnerability, some of the scanning tools point to the corresponding CVE entry.

## Implementing countermeasures

After you have analyzed and determined the security requirements of your assets, establish a security strategy, and implement security controls to protect your assets.

A best practice is to implement a security strategy that uses multiple layers of security. Each layer provides a specific type of protection, including protecting networks, systems, data, and user identity.

## Layered security model

An effective security prevention strategy protects valuable assets by using a layered defense model. By implementing **multiple layers** of security, an attacker would have to penetrate all of the layers in order to gain access to the protected asset.

Some security layers are:

- **Perimeter security:** Secures the perimeter networks by using controls such as firewalls or an intrusion prevention system (IPS)
- **Network security:** Prevents unauthorized network access by using network access control lists (network ACLs), for example
- **Endpoint security:** Uses software such as an antivirus program to protect a host
- **Application security:** Protects applications with specialized firewalls, and monitoring and scanning tools
- **Data security:** Protects access to data through identity and access management

## Layered defense example: Castle

As an example of a layered defense, consider the architecture of a castle. The castle might have a moat as its first level of defense. The castle also includes an outer wall, an inner wall, and finally, the keep, where the protected assets reside. Each layer must be defeated in order for an attacking army to reach the keep and take the castle. Similarly, companies implement many layers of defense on their systems to make the systems more difficult to breach.

## Layered defense example: OSI model

The OSI model provides another example of how security can be implemented in layers.

- **Physical layer:** Network devices and equipment are protected from physical access to keep intruders out.
- **Data link layer:** Filters are applied to network switches help prevent attacks based on media access control (MAC) addresses.
- **Network and transport layers:** Implementing firewalls and access control lists (ACLs) helps to mitigate unauthorized access to internal systems.
- **Session and presentation layers:** By using authentication and encryption methods, you can prevent unauthorized data accesses.
- **Application layer:** Solutions, such as virus scanners and an IDS, help protect applications.

## Network hardening measures

The first layer of security prevention measures focuses on protecting the network. This protection can be achieved through **network discovery hardening** and **network security architecture hardening**.

The goal of **network discovery hardening** is to prevent an attacker from discovering, exploring, or mapping the network. Unfortunately, the same tools that network administrators use to explore or map networks can compromise network security if malicious entities are allowed to use them. (Examples of these tools include `ping` and `Nmap`.) As a result, network discovery tools should be blocked because they can be used to exploit network systems.

Another effective network hardening action is to close network ports that are not used because they present open doors for attackers to come in. In addition, you can use your asset inventory list to identify and enforce the list of devices that are allowed on your network. If a device that is not on the allow list appears on your network, you can immediately investigate and take proper action.

**Hardening the security architecture** of your network is another important prevention measure. For example, you can use firewalls in your network topology to protect resources such as web servers and database servers. A firewall permits only a certain type of traffic (based on protocol and source IP address) to come into the protected resource. You can also use segments to break down the network so that critical resources run in their own segment, which gives them additional protection.

## System hardening measures

The next layer of security prevention measures addresses protecting the hosts that run your services and applications or that store your data. This security layer is known as systems hardening.

- **Applying OS patches and security updates on a regular basis:** As OS vendors identify known vulnerabilities, they publish patches to correct them. It is important that you apply these patches when they become available in order to prevent vulnerabilities at the OS level from being exploited.
- **Removing unused applications and services:** Unused or older versions of applications and services might sometimes expose security vulnerabilities that can be maliciously exploited. By uninstalling them, you not only eliminate the potential security exposure but also free up the runtime and storage resources that they consume
- **Monitoring and controlling configuration changes:** Ideally, all configuration changes that you make to a system are performed using an automated tool that enforces best practice change control policies and procedures. You should also monitor all configuration changes so that you can always answer the important questions of, Who changed what, where, and when?

## Data security controls

Data security is the next layer of prevention measures in the layered secured model. It focuses on protecting data through the use of various control mechanisms, including the following:

- **Encrypting data in transit and data at rest:** Encryption protects the confidentiality of information. For example, a digital certificate can be used to encrypt messages between a sender and a receiver.
- **Using data integrity checking tools:** For example, use a hashing tool to generate a unique value based on the content of a data file before a sender transmits the file. When the receiver receives the file, the same hashing tool is used to generate the value again. If both the before and after transmission values are the same, the data file’s integrity has not been compromised.
- **Using role-based access control:** Access control affects the availability of information. It ensures that data is made available only to users that are authorized to access the data.

## Identity management

The last layer of security prevention measures is identity management. Identity management defines rules that specify who has access to specific information (authentication) and what they can do with it (authorization). Examples of identity management controls include the following:

- **Use the principle of least privilege to control access to resources:** You should grant users the permission to access only the resources that they are authorized to.
- **Set up a policy that enforces password strength and password expiration:** Passwords are a mechanism that is used for authentication. A good password policy prevents passwords from being easily guessed and requires them to be changed on a periodic basis.
- **Use the principles of authentication, authorization, and accounting (AAA):** In addition to authentication and authorization controls, auditing measures should also be put in place. Accounting involves tracking and logging activities within a system. It's crucial for auditing purposes, allowing organizations to understand who did what, when, and why. These measures are implemented by capturing resource usage information, and they facilitate security auditing.
