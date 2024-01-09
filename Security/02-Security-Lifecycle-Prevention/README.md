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


