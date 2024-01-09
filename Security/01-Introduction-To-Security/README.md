# Introduction To Security

## Security strategy

Security strategy defines the following:

- **What security measures to implement:** This is achieved through security controls.
- **When to implement security measures:** This is defined in a security lifecycle.

## Security strategy for the cloud

Security strategy for the cloud defines the following:

- **What security measures to implement:** This is achieved through security controls.
- **When to implement security measures:** This is defined in a security lifecycle.
- Who is responsible for implementing the different security measures.

## AWS Cloud security shared responsibility model

In the AWS Cloud, the shared responsibility model indicates who is responsible for implementing security measures. In this model, AWS is responsible for security OF the cloud, and the customer is responsible for the security IN the cloud.

AWS handles the security of the physical infrastructure that hosts your resources, which includes the following:

- **Data centers:** These centers are secured with controlled, need-based access and are located in nondescript facilities. In addition, security guards protect them 24 hours a day, 7 days a week.- - - **Network infrastructure:** This infrastructure includes routers, switches, load balancers, firewalls, and cabling. It is protected with nearly continuous network monitoring at external boundaries, secure access points, redundant infrastructure, and intrusion detection.
- **Virtualization infrastructure:** Each compute instance is isolated from other instances.

Customers are responsible for the security of everything they put in the cloud. In particular, the customer is responsible for managing the security of their data, including the following:

- Which country that data is stored in
- Whether or not the data is encrypted
- Who has access to the data, and how those access rights are granted, managed, and revoked

## What are security controls?

Security controls are measures that protect against threats and eliminate vulnerabilities.

There are three types of security controls: preventive, detective, and corrective. For each type of control, you can implement **physical**, **technical**, and **administrative security measures** to ensure information confidentiality, integrity, and availability.

- A preventative security control protects a system from security threats before they can happen.
- A detective security control helps find a vulnerability early or quickly alert when a breach has happened.
- A corrective security control remediates a security breach.

Each type of control provides protection in three different security areas: physical, administrative, and technical.

- A physical control is a device or object, such as a security camera.
- An administrative control is usually a policy or a procedure that must be followed.
- A technical control is usually some software that provides security functions.

| Control type  | Physical                                                         | Administrative                                             | Technical                                               |
|---------------|------------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------|
| Preventative  | Card reader devices to allow access to a building                | Corporate policy stating that all employees must swipe their individual cards to access the building             | Software to collect data from card readers and monitor building access traffic                                  |
| Detective     | Metal detector at an airport to detect weapons                    | Control procedures that require a report when a system is changed                                                 | Antivirus software that runs scans on regular basis     |
| Corrective    | Backup generator in a data center that turns on automatically if the power is interrupted   | Business continuity plan that details how to keep the business running if a system is compromised                | Antivirus software that removes malware when it is detected                                                   |

For the preventative security control type, a card reader device that allows access to a building is an example of a physical control. To complement this control, a corporate policy should exist requiring that all persons who access the building swipe their individual cards to enter and exit. This is an example of a administrative preventative control. Finally, a software application that collects and monitors the data from the card readers is as an example of a technical preventative security control.

Typically, when implementing a security control, start by controlling the physical access to the resource if possible and applicable. Then, establish policies and procedures that describe how to define, set up, and manage the security of the resource. Finally, use a technical control to enforce secure access and usage of the resource.

## Acceptable Use Policy (AUP)

An Acceptable Use Policy (AUP) is a document outlining rules and guidelines for using an organization's IT resources, such as networks, devices, and software. It defines acceptable and prohibited behaviors, aiming to protect assets, ensure security, and maintain a productive work environment.

The AUP typically covers areas such as:

- **Acceptable use**: Defines what constitutes acceptable use of the organization’s IT resources.
- **Prohibited use**: Details the behaviors that are not allowed.
- **System and network activities**: Addresses the use of system resources.
- **Email and communication activities**: Sets standards for email and other forms of communication.
- **Software and intellectual property**: Discusses the use of software and respect for intellectual property rights.
- **Confidentiality**: Emphasizes the importance of maintaining confidentiality.

The AUP is usually enforced by the owner or manager of a website, network, online service, or larger computer infrastructure. Violations of the AUP can lead to disciplinary actions. Regularly updating this policy in line with technological advancements and regulatory changes will further enhance its effectiveness in safeguarding your organization’s assets and reputation.

## Security life cycle

An effective security strategy addresses security in stages of a lifecycle. These stages consist of prevention, detection, response, and analysis. Note that the first three stages correspond to the three types of security controls.

- **In the prevention stage,** you identify the assets to be protected, assess their vulnerabilities, and implement measures to remove any discovered vulnerability.
- **In the detection stage,** you implement monitoring solutions to quickly identify and generate alerts if a breach is detected.
- **In the response (or corrective) stage,** you perform the corrective tasks to eliminate the breach and restore normal operations.
- **In the analysis stage,** you review the steps used to resolve the issue and identify any lessons learned. If necessary, you update your security policies and procedures to make adjustments based on the result of the analysis.
