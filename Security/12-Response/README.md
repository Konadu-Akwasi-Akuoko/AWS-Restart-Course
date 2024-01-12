# Response

## Security lifecycle: Response

- Prevention: Is the first line of defense
- Detection: Occurs when prevention fails
- Response: Describes what you do when you detect a security threat
- Analysis: Completes the cycle as you identify lessons learned and implement new measures to prevent the issue from occurring again in the future

Response is the third phase of the security life cycle

## Event response

| Step | Action | Notification Type |
|------|--------|-------------------|
| 1    | Event occurs | Automatic notification |
| 2    | Investigate event | Administrator gives manual notifications |
| 3    | Respond and remediate | Administrator gives manual notifications |
| 4    | Notify dependent stakeholders | Administrator gives manual notifications |
| 5    | Act to prevent this type of event from happening again in the future | - |

- What immediate action do you take?
- Whom do you notify?
- How do you ensure that the business can keep running in a reduced capacity?
- How can you ensure that this situation will not happen again or at least that it will be less likely to happen in the future?
- How do you get back to a normal situation?

## Event investigation process

- When a security alert is activated, the alert must be verified because false positives can happen, especially with a system such as an automated intrusion detection system (IDS).
- If the alert is verified, then the event must be investigated. What is the scope of the attack?
- The first step to respond to the attack is to contain infected elements if there are any, such as hosts infected by a virus. Then, block access to network addresses.
- Notify the departments or the teams that will be affected that they might have limited access to the systems that they use. Stakeholders might be customers that won’t be able to use a website.
- Recover to get back to business as soon as possible: add security rules, rebuild infected systems, recover data, and take other appropriate steps.
- Finally, see whether there is a way to strengthen the system to avoid another attack or recover faster. You can also implement new procedures for the team in case of an attack.

You cannot plan for every conceivable disaster. However, you can demonstrate due diligence by identifying and documenting the types of disasters that present a real threat to your business. The unexpected event can be a minor inconvenience, or it could result in the end of your organization. If you fail to plan for these potential events, you plan to fail.

## BCP and DRP

A critical aspect of managing a business is creating strategies to prepare for any event that will disrupt the way the business normally works.

Two strategies or processes are important:

- BCP: How to run the business in a reduced capacity
- DRP: How to recover from an outage or loss and return to a normal situation as quickly as possible

## Planning business continuity

A BCP lists different disaster scenarios. It describes what the business will do to keep critical services and functions running when a disaster or disruption occurs. For example, it could be an interruption of service or destruction of hardware.

The BCP accomplishes the following actions:

- Lists different disaster scenarios and what the business will do to keep business running as usual.
- Keeps the business running in a reduced form over a period of time.

The BCP is not activated during an outage.

## Planning disaster recovery

The DRP is a strategy that helps the business recover from disasters and unplanned incidents.

- **Primary goal:** Restore business functionality quickly and with minimum impact.
- **Security goal:** Do not lower the level of controls or safeguards that are in place.
- **Follow-on goal:** Prevent this threat, exploit, or disaster from happening again.

- Recovery time objective (RTO): How quickly does the business need to be back up?
- Recovery point objective (RPO): How much time and data can the business afford to lose?

As the values of these parameters decrease, backup strategies and other recovery mechanisms become more expensive or complex. However, RTO and RPO have decreased over time as technology has evolved.

The following are possible security goals:

- A business might implement different corrective measures for access control based on the impact of the disaster or disruption. However, the business should implement security access controls to the same level of restriction before the disruption.
- If access controls are not implemented to the same level, the business must not permit access or use of resources.

Disaster recovery is the process of preparing for and recovering from a disaster. Examples include earthquakes or floods, technical failures such as power or network loss, and human actions such as inadvertent or unauthorized modifications. Minimizing the downtime of the systems involves two important objectives:

- Recovery time objective (RTO): The maximum acceptable delay between the interruption of service and restoration of service. The RTO determines an acceptable length of time for service downtime.
- Recovery point objective (RPO): The maximum acceptable amount of time since the last data recovery point. The RPO is directly linked to how much data will be lost and how much will be retrieved.

## RPO compared to RTO

The main focus of RPO is on data. RPO represents the point in time, before disruption, when data can be recovered (given the most recent backup copy of the data) after the disruption. RPO is a factor of how much data loss the business can tolerate during the recovery process.

In short, RPO is concerned with the following questions:

- How much data can the business lose before the business suffers?
- How much time between data backups can elapse without causing severe harm if a disaster occurs?
  - This answer is based on fixed intervals of data backups.
  - The more time that elapses, the more money the business loses.

RPO is easier to implement than RTO because RPO affects only the data layer of your infrastructure.

RTO represents the time that the system can be down before a business can’t maintain business continuity and the business suffers. The sooner a business must get back online, the costlier it will be. Recovery involves the entire business infrastructure.

**Work recovery time (WRT)** involves recovering or restoring data, testing processes, and then making the system live for production. It corresponds to the time between systems and resource recovery, and the start of normal processing.

The **maximum tolerable downtime (MTD)** is the sum of the RTO and the WRT. In other words, MTD = RTO + WRT.

MTD is the total time that a business can be disrupted after a disaster without causing any unacceptable consequences from a break in business continuity. Include the MTD value as part of the BCP and DRP.

## Disaster recovery options

The following list contains different types of backup solutions:

- Backup(can be traditional tape storage)
  - Is used for the entire business infrastructure
  - Focuses on long-term data of the business
  - Is cost-effective but not time-effective
- Replication
  - Snapshot-based:
    - Writes only changed data since the last snapshot
  - Continuous:
    - Uses synchronous, asynchronous, or near-synchronous•Focuses on resuming to normal operations quickly
    - Offers more granular recovery points
- Pilot light
  - The minimal version of an environment is always running in the cloud.
  - Configure and run the most critical elements of your system.
  - When recovery is needed, rapidly provision a complete production environment around the critical core.
  - Infrastructure elements include database servers and other significant data.

## Cost balancing

The key thing here is that the faster you want to get back up the higher the cost.

The longer a disruption is permitted to continue, the more costly it can be to the business and its operations. A tradeoff exists between speed of recovery and cost.

The answer is not the same for all systems. For example, an employee database can probably be down for a couple of days, but the ecommerce site can be down for only minutes.

Amazon Simple Storage Service (Amazon S3) is a cloud storage service that can back up data with different levels of restoration speed and cost.
