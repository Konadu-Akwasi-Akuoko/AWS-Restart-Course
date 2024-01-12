# Detection

## Security lifecycle: Detection

- Prevention: Is the first line of defense
- Detection: Occurs when prevention fails
- Response: Describes what you do when you detect a security threat
- Analysis: Completes the cycle as you identify lessons learned and implement new measures to prevent the issue from occurring again in the future

Detection is the second phase of the security life cycle

## The threat of malware

Malware is an application that causes harm to a computer system. It interrupts one or many of the CIA triad elements: confidentiality, integrity, or availability. Knowledge of malware, how to avoid infection, and how to respond to corrupted systems are key elements of security management.

The following are types of malware:

- **Viruses:** Viruses are programs that can corrupt or delete data and propagate themselves from one system to another.
- **Worms:** Worms are programs that spread themselves and consume resources destructively on a computer. They have no executable file and rely on application weaknesses to deploy themselves. The author of a worm can control the infected computer remotely. Worms can be difficult to isolate because they spread quickly. Examples include MyDoom, Sobig, and Stuxnet.
- **Bots:** Bots are used to control computers or launch distributed denial of service (DDoS) attacks against vulnerable systems. An example is Poison Ivy.
- **Backdoor:** A backdoor (also known as a Trojan horse) is often a secret server that steals information from the victim’s system. It allows an intruder into a system. You can know about the backdoor if you scan the system and the network to find patterns of traffic. Examples include Sub7, GirlFriend, and Zeus.
- **Rootkits:** A rootkit cloaks itself by replacing system files that can reveal its presence. It is used to retrieve information. It is difficult to identify and remove because it can become part of the operating system. Removal often requires a system reformat. An example is Hacker Defender.
- **Spyware:** Spyware jeopardizes privacy and typically comes embedded into applications that look free and interesting to use. As people are doing more finance and other personal activities online, these activities can be detected and revealed, and information can be stolen. An example is Real-time spy.
- **Adware:** Adware deploys advertising content and monitors user activity, such as visited websites. It is similar to spyware, but it focuses on ads and what a user clicks. Adware is often embedded in shareware applications. An example is Fireball.
- **Ransomware:** Ransomware locks systems or makes data unavailable until the user pays a ransom.

Malware infects a system through different methods, including the following:

- **Untrusted websites:** Untrusted websites are websites whose identity can’t be identified and might have malicious intent.
- **Removable devices:** These devices can be used to infect a system. For example, a USB device is mailed to you. You open it, and it contains a backdoor that gives remote access to your system to an unauthorized user.
- **Emails:** An email can have attachments with viruses or malware.

## What is antivirus software?

Antivirus software programs protect a computer against malware. They prevent malware from infecting a computer and also detect and remove malware that has already infected a system.

Antivirus programs are usually provided as part of modern operating systems (for example, Windows and Mac OS). They are also available for free on the internet (be careful to select a trusted source) or sold by third-party companies.

The following are some best practices when using an antivirus program:

- Regularly update your antivirus or anti-malware software.
- Frequently scan your system.
- Scan incoming communications (for example, emails and attachments).

## Intrusion detection system (IDS)

An intrusion detection system (IDS) is a hardware or software solution that monitors a network or a computer system to detect intrusions or malicious activity. When this kind of activity happens, the IDS generates alerts to notify security personnel.

An IDS can detect an attack by using different mechanisms, including the following:

- **Anomaly-based detection:** The IDS compares the current traffic pattern or system activity against established baselines for any deviation.
- **Signature-based detection:** The IDS monitors and analyzes the traffic for known patterns of attack.

There are several types of intrusion detection systems, and the type is based on where the IDS is installed in the computing environment.

## Network-based IDS and host-based IDS

An IDS usually is either a **network-based intrusion detection system (NIDS)** or a **host-based intrusion detection system (HIDS)**

- A **NIDS** monitors for attacks on the network. Therefore, it is installed on the network and inspects and analyzes all the data that travels through the network.
- A **HIDS** is installed on a server and monitors logs and critical files on the server, watching for signs of an attack.

## Amazon GuardDuty detection mechanism

GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity. It delivers detailed security findings for visibility and remediation.

When you activate GuardDuty and configure it to monitor your account, GuardDuty automatically detects threats by using anomaly detection and machine learning techniques. You can view the security findings that GuardDuty produces in the GuardDuty console or through Amazon CloudWatch Events.

GuardDuty detects unauthorized and unexpected activity in your AWS environment by analyzing and processing data from different AWS service logs. These logs include the following:

- AWS CloudTrail event logs
- Virtual private cloud (VPC) flow logs
- Domain Name System (DNS) logs

GuardDuty extracts various fields from these logs and uses them for profiling and anomaly detection.


