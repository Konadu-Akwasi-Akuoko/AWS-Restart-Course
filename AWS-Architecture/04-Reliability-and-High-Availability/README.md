# Reliability and High Availability

## Reliability

Reliabilityis the probability that an entire system (including all hardware, firmware, and software) will satisfactorily function for a specified period of time. Reliability is a measure of how long the item performs its intended function.

There are two common measures of reliability. The first one is the mean time between failure (or MTBF), which is the total time in service divided by the number of failures. The second one is the failure rate, which is the number of failures divided by the total time in service.

For example, when you purchase a vehicle, you purchase a system, or a collection of subsystems, that must work together for the vehicle to be considered reliable. The reliability of each of the subsystems—including the cooling, the ignition, and the brakes—is a part of determining the reliability of the vehicle. So, if you try to start the vehicle and the ignition fails, reliability is negatively impacted. Keep in mind that reliability is based on the entire system functioning as designed.

## Reliability compared to availability

Reliability is a measure of how long a resource performs its intended function.

Reliability is closely related to availability. Reliability is a measure of how long a resource performs its intended function. In contrast, availability is a measure of the percentage of time that the resources are in an operable state.

When you look at Amazon Web Services (AWS) services, you might see numbers like 99.99 percent. Those numbers refer to the availability,or the percentage of time that a system or application is correctly performing the operations expected. A common shorthand refers to only the number of 9s. For example, five 9s is 99.999 percent available.

## High availability (HA)

| Number of 9s | Percentage of Uptime | Maximum Downtime Per Year | Equivalent Downtime Per Day |
|--------------|----------------------|---------------------------|-----------------------------|
| One 9        | 90%                  | 36.5 days                 | 2.4 hours                   |
| Two 9s       | 99%                  | 3.65 days                 | 14 minutes                  |
| Three 9s     | 99.9%                | 8.77 hours                | 1.4 minutes                 |
| Four 9s      | 99.99%               | 52.6 minutes              | 8.6 seconds                 |
| Five 9s      | 99.999%              | 5.25 minutes              | 0.86 seconds                |

Availability specifically refers to the amount of time that your system is in a functioning condition. In general terms, your availability is referred to as 100 percent minus your system's downtime.

High availability (HA) is about ensuring that your application's downtime is minimized as much as possible without the need for human intervention. It does not consider availability to be a series of replicated physical components. Instead, HA considers availability to be a set of system-wide, shared resources that cooperate to guarantee essential services. HA combines software with open standard hardware to minimize downtime by quickly restoring essential services when a system, component, or application fails. Though the restore actions are not instantaneous, services are restored rapidly, often in less than 1 minute.

Because events that can disrupt your system's availability are never entirely predictable, there are always ways to make an application more available. However, keep in mind that improving availability usually leads to increased cost. When considering how to make your environment more available, it is important to balance the cost of the improvement with the benefit to your users.

## HA goals

- Systems are generally functioning and accessible.
- Downtime is minimized.
- Minimal human intervention is required.

HA is a concept that regards the entire system. Its goal is to help ensure that your systems are always functioning and accessible and that downtime is minimized as much as possible without needing human intervention.

## HA: Prime factors

The following factors contribute to HA:

- Fault tolerance, recoverability, and scalability are the prime factors that determine the overall availability of your application. Fault tolerance is often confused with high availability. Fault tolerance refers to the built-in redundancy of an application's components and its ability to remain operational even if some of that system’s components fail. Fault tolerance relies on specialized hardware to detect a hardware fault and instantaneously switch to a redundant hardware component. This redundancy applies whether the failed component is a processor, memory board, power supply, I/O subsystem, or storage subsystem. The fault-tolerant model does not address software failures, which is by far the most common reason for downtime.
- Scalability is a question of how quickly your application's infrastructure can respond to increased capacity needs. Its goal is to ensure that your application is available and performs within your required standards. It does not guarantee availability, but it is one part of your application's availability.
- Recoverability is often overlooked as a component of availability. If a natural disaster makes one or more components unavailable or destroys your primary data source, can you restore service quickly and without lost data?

## On-premises HA compared to HA on AWS

Traditionally, ensuring HA in your local data centers can be expensive. Building overhead costs and system maintenance can add up quickly depending on the level of availability required. Maintaining highly available servers not located in the same Region can also be expensive.

Traditionally, ensuring HA in your local data centers can be expensive. Building overhead costs and system maintenance can add up quickly depending on the level of availability required. Maintaining highly available servers not located in the same Region can also be expensive.
