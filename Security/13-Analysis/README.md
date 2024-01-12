# Analysis

## Security lifecycle: Response

- Prevention: Is the first line of defense
- Detection: Occurs when prevention fails
- Response: Describes what you do when you detect a security threat
- Analysis: Completes the cycle as you identify lessons learned and implement new measures to prevent the issue from occurring again in the future

Analysis is the fourth phase of the security life cycle

## Confidentiality, integrity, and availability (CIA)

The CIA triad—confidentiality, integrity, and availability—is a concept that drives data security in enterprises. Confidentiality aims at keeping personal data safe and hidden from non-authorized people. Integrity consists of ensuring that data is not modified or altered throughout the process in which it is used. Finally, availability ensures that data stays available when needed for the right person.

## What is analysis?

Analysis is the final phase of the security lifecycle. In the analysis phase, you review the cause of security incidents and analyze current security controls to determine weaknesses. The objective is to improve and strengthen those controls to better protect your network, facilities, and organization.

## General guidelines for analysis

- Ensure that each threat yields a better security solution even if no breach occurred.
- Have flexibility when considering option to add to the solution.
- Maintain a testing environment to test solutions to potential threats.

When you test to simulate attacks, do so in a separate test environment that is representative of your production environment. However, be aware that you will probably not be able to do everything to protect your system. Each action that you take to protect your system (for example, limiting access to resources or reducing points of failure) will have impact (for example, slowing the network or increasing costs). You might want to find the right balance for your business instead of implementing everything that is possible.

## Types of security tests

You can conduct security testing during the analysis phase. Doing security tests in the analysis phase is useful in order to mimic what could happen if your system were under attack. Conducting security tests gives you an opportunity to implement solutions to better prepare against these attacks.

The types of testing include the following:

- **External vulnerability assessment:** A third party evaluates system vulnerabilities with little knowledge of the infrastructure and components.
- **External penetration test:** A third party with little knowledge of the system actively tries to break into the system in a controlled manner.
- **Internal review of applications and platforms:** A tester with some or full knowledge of the system validates the effectiveness of the following for known susceptibilities:
  - Controls in place
  - Applications and platforms

In the AWS Cloud, Amazon Web Services (AWS) customers are encouraged to conduct security assessments or penetration tests against their AWS infrastructure.

## Root cause analysis (RCA)

Root cause analysis (RCA) can be used to provide a clear and accurate answer to the following question: How did the breach happen?

You usually perform root cause analysis when your network underwent an attack, for example, or when you perform penetration testing to test your network’s security. As a result of that analysis, you can take actions to prevent that issue from happening again in the future.

Consider the example of a folder in which you are storing important data. One day, you realize that part of this data has disappeared. After performing a root cause analysis, you conclude that the wrong permissions were applied to this folder and that unauthorized users could access it. You must take action and modify the rules to restrict the access to the folder to prevent this from happening again.

## Risk assessment

isk is the likelihood of a threat occurring against a particular asset and the possible impact to that asset if the threat occurs. A risk assessment helps to identify and rank risk.

During a risk assessment, ask “What are the most critical assets or critical business processes that need the most protection?” There are 5 basic steps to risk assessment:

1. Identify threats
2. Identify vulnerabilities
3. Determine likelihood
4. Determine impact
5. Determine risk

## Risk response strategies

- **Risk avoidance:** Stop doing the risky activity.
- **Risk transference:** Assign the responsibility for the risk to another party.
- **Risk mitigation:** Implement a control to reduce the risk.
- **Risk acceptance:** Do nothing to reduce the risk,but monitor and plan a response.

## Monitoring and logging benefits

- Monitoring and logging can provide an effective way to govern IT.
- Monitoring and logging can aid in ensuring regulatory compliance by adhering to laws, regulations, and specifications relevant to its operations.
- Monitoring and logging can assist service level agreement (SLA) performance validation and help ensure compliance.
- Monitoring and logging can contribute to management oversight and control.

## Monitoring and logging

- Logs
  - Provide data that is used to examine IT systems and processes
  - Can be both inputs and outputs of monitoring
- Monitor logs for
  - Changes
  - Exceptions
  - Other significant events
- Records produced from monitoring become logs for further analysis.

## Use metrics

Metrics measure the success of the security program. For a security program, metrics can be both positive and negative.

## Monitoring

A company can define a set of rules that determine what or who is monitored by creating an Acceptable Use Policy (AUP) document.

## Types of monitoring

Location

- Onsite
- Remote
- Internal or external
- Outsourced

Resource

- System
- Network
- Database
- Physical
- Employee

Usage

- Usage or consumption
- Location
- Access restrictions

The types of monitoring can vary based on where the monitoring occurs and what type of resource or usage is being monitored.

## AWS monitoring services

- Amazon CloudWatch monitors resources and applications in the AWS Cloud and on-premises.
- AWS Config records and evaluates configurations of your AWS resources.
- Amazon Managed Service for Prometheus provides highly available, secure, and managed monitoring for your containers.
- Amazon GuardDuty protects your AWS accounts with intelligent threat detection.
- Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS.

## Monitoring as a service (MaaS)

In the AWS Cloud, the Amazon CloudWatch service provides monitoring for AWS Cloud resources and the applications that you run on AWS. CloudWatch Logs is capable of monitoring and storing your logs to help you better understand and operate your systems and applications.

A benefit of monitoring as a service (MaaS) is that these types of services can provide real-time application and system monitoring. For example, CloudWatch Logs can track the number of errors that occur in your application logs. It can then send you a notification whenever the rate of errors exceeds a threshold that you specify.

## Devices that might be monitored

- Router
- Switch
- Firewall
- Wireless access point (AP)
- Printer
- Virtual private network (VPN)
- CameraCard reader
- Laptop
- Phone
- Tablet
- Vehicle

## Monitoring policy

When you develop a monitoring policy, ask the following questions:

- What should you monitor?
- How closely should you monitor?
- How often should you monitor?
- Who does the monitoring?
- Do you outsource monitoring?
  - Data retention monitoring
  - Access to monitoring tools
  - Remote monitoring
- Who watches the watchers?
  - Policy
  - Regulations

## Retention policy for monitoring

A monitoring policy should also specify how long different types of data are retained.

## Monitoring your data with Amazon Macie

Amazon Macie is a fully managed data security and data privacy service. It uses machine learning and pattern matching to discover and protect your sensitive data in AWS.

As organizations manage growing volumes of data, identifying and protecting their sensitive data at scale can become increasingly complex, expensive, and time-consuming. Amazon Macie automates the discovery of sensitive data at scale and lowers the cost of protecting your data.

## Logging policy

- Define a logging policy to identify what will be logged and how logs are managed.
- Ensure that both the logging policy and infrastructure support a cohesive and integrated enterprise solution.

## Protection of log information

It is important to protect log information from unauthorized access and to back up logs regularly. To ensure that analysis results are correct, keep the clocks on all log servers accurate and synchronized.

- Keep logs on the original device, a log server, or both.
- Control physical and logical access to a log server.
- Log backup and recovery processes.
- Follow a retention policy.
- Check timestamps.

## AWS logging services

- AWS CloudTrail monitors and records account activity across your AWS infrastructure, which gives you control over storage, analysis, and remediation actions.
- AWS Config is a service that you can use to assess, audit, and evaluate the configurations of your AWS resources.
- Amazon Virtual Private Cloud (Amazon VPC) Flow Logs is a feature that you can use to capture information about the IP traffic to and from network interfaces in your VPC.
