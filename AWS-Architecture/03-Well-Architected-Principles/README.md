# Well-Architected Principles

## Well-Architected design principles

The AWS Well-Architected Framework identifies a set of general design principles to facilitate good design in the cloud:

- Stop guessing your capacity needs.
- Test systems at production scale.
- Automate to make architectural experimentation easier.
- Provide for evolutionary architectures.
- Drive architectures by using data.
- Improve through game days.

## Stop guessing your capacity needs

In a traditional environment, the company would have to estimate the number of customers who will be visiting, purchasing, and interacting with the environment.

In a cloud environment, you do not need to guess your infrastructure capacity needs. Start with as much or as little capacity as you need, and scale up and down automatically as your need changes. You can achieve this flexibility by monitoring demand and system usage. You can also automate the addition or removal of resources to maintain the optimal level for satisfying demand.

With a cloud environment, the company would be able to set workload thresholds, which would initiate increases or decreases in resources to match demand (scaling). By staying as close to the real amount as possible, the company is more efficient in expenditures and resource utilization.

## Test systems at production scale

In a traditional, non-cloud environment, it is usually cost-prohibitive to create a duplicate environment that is used only for testing. Consequently, most test environments are not tested at live levels of production demand.

In the cloud, you can create a duplicate a environment on demand, complete your testing, and then decommission the resources. You pay for the test environment only when it is running. Therefore, you can simulate your live environment for a fraction of the cost of testing on premises.

## Automate

On-premises environments have separate structures and components that require more work to automate with no common API for all parts of your infrastructure.

You can use automation to create and replicate your systems at low cost with little manual effort. You can track changes to your automation, audit the impact, and revert to previous parameters when necessary.

## Provide for evolutionary architectures

In a traditional environment, architectural decisions are often implemented as a static, one-time events, with a few major versions of a system during its lifetime. As a business and its context continue to change, these initial decisions might hinder the system’s ability to meet changing business requirements.

In the cloud, the capability to automate and test on demand lowers the risk of impact from design changes. In this way, systems can evolve over time so that businesses can take advantage of new innovations as a standard practice.

## Drive architectures by using data

In a traditional, non-cloud environment, architectural choices are often made according to organizational defaults instead of through a data-driven approach. You generally cannot generate datasets that would help you to make informed decisions, so you might use models and assumptions to size your architecture.

In the cloud, you can collect data on how your architectural choices affect the behavior of your workload. In this way, you can make fact-based decisions about how to improve your workload. Your cloud infrastructure is code, so you can use that data to inform your architecture choices and improvements over time.

## Improve through game days

In a traditional environment, you would exercise your runbook only when something bad happened in production.

In the cloud, you can test how your architecture and processes perform by regularly scheduling game days to simulate events in production. This process will help you understand where you can make improvement. It can also help develop organizational experience in dealing with events.
