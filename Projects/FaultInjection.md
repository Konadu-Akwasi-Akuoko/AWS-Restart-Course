# AWS Fault Injection Service

## Introduction to AWS Fault Injection Service

With AWS Fault Injection Service (AWS FIS), you can run controlled experiments on your AWS resources to test their resilience and reliability. AWS FIS is a fully managed service that lets you inject faults into your workloads without requiring any code changes or complex setup.

Fault injection is based on the principles of chaos engineering. One way to apply chaos engineering is to use fault injection, which deliberately introduces errors into a system to test its resilience.

## What is chaos engineering? Principles chaos engineering

From Wikepedia: "Chaos engineering is the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production"

What does this mean?

Chaos engineering is the practice of intentionally injecting faults into a system to test its resilience. The goal is to identify potential failure points and correct them before they cause an actual outage or other disruption.

There are many ways to create chaos in a system, but the most important thing is to have a plan. Without a plan, it's easy to create more problems than you solve. When creating your plan, you'll need to decide what you want to test and how you're going to do it. You can then start experimenting once you have a plan.

You can then start creating events and by creating these events in a controlled non-production environment (NB: not in a production enviroment, but rather a test enviroment), you can test how your system reacts and identify any potential problems.

Once you've identified potential failure points, you can start working on mitigating them. This might involve adding monitoring or logging to help identify issues when they occur or changing your design to make it more resilient to failures.

### Which companies use Chaos Engineering?

Here are a handful of companies that have embraced chaos engineering to proactively prevent outages and disruptions:

- Netflix (Chaos Monkey)
- Amazon (AWS Fault Injection Service)
- Google (Google DiRT - Google Disaster Recovery Testing)
- Facebook (Azure Chaos Studio)

One of the most notable examples of chaos engineering was implemented by Netflix. Netflix encouraged its engineers to develop recovery mechanisms to bolster its platform. Particularly, Netflix implemented Chaos Monkey when they migrated their systems from physical server warehouses to the cloud.

Chaos Monkey was designed to “terminate” their servers during business hours, keeping their engineers on their toes to fix these issues immediately. This enabled Netflix to proactively learn about the vulnerabilities of transmitting their streaming services over the cloud and accelerate their problem-solving process in real-time.

As a result of these efforts, Netflix was able to avoid major outages and solidify its reputation as one of the best streaming giants.

## Running experiments in AWS FIS

There are some steps you need to follow when running tests in AWS fault injection service.

1. **Create an Experiment Template**: The first step is to create an experiment template. This template is the blueprint of your experiment and contains the actions, targets, and stop conditions for the experiment.

2. **Start an Experiment**: After creating an experiment template, you can use it to start an experiment. An experiment is finished when one of the following occurs: all actions in the template completed successfully, a stop condition is triggered, an action cannot be completed because of an error (for example, if the target cannot be found), or the experiment is stopped manually.

3. **Monitor Your Experiment**: You can monitor your experiment using any of the following features: view your experiments in the AWS FIS console, view Amazon CloudWatch metrics for the target resources in your experiments or view AWS FIS usage metrics, and enable experiment logging to capture detailed information about your experiment as it runs.

4. **View Your Experiments**: You can view the progress of a running experiment, and you can view experiments that have completed, stopped, or failed. Stopped, completed, and failed experiments are automatically removed from your account after 120 days.

5. **Schedule Your Experiments**: You can schedule your experiments as a one-time task or recurring tasks using Amazon EventBridge.

To apply the steps you've mentioned to an AWS Auto Scaling group and check if it launches new EC2 instances when one is terminated without cause, you would do the following:

1. **Create an Experiment Template**: In AWS FIS, create an experiment template that targets your Auto Scaling group. The action should be to terminate an instance, and the stop conditions should be set according to your needs¹.

2. **Start an Experiment**: Start the experiment using the template you created. This will terminate an instance in your Auto Scaling group¹.

3. **Monitor Your Experiment**: Monitor the experiment using the AWS FIS console and Amazon CloudWatch. You can view metrics for your Auto Scaling group to see if a new instance is launched after one is terminated¹.

4. **View Your Experiments**: After the experiment is completed, you can view the details in the AWS FIS console. This includes whether the experiment was successful and what actions were taken¹.

5. **Schedule Your Experiments**: If you want to regularly test the resilience of your Auto Scaling group, you can schedule experiments to run at regular intervals using Amazon EventBridge¹.

To check if a new EC2 instance is launched when one is terminated, you can monitor the `GroupTotalInstances` metric in CloudWatch for your Auto Scaling group. This metric represents the total number of instances in the group, so if a new instance is launched when one is terminated, the value of `GroupTotalInstances` should remain constant.

Remember, running these experiments will have real effects on your AWS resources, so it's recommended to test in a pre-production environment first.

## Actions, Targets, and Stop conditions

In the context of AWS Fault Injection Service (FIS), actions, targets, and stop conditions are key components of an experiment³:

1. **Actions**: Actions are the activities performed on an AWS resource during an experiment¹. They represent the faults or disruptions that you want to inject into your system. For example, an action could be to terminate an EC2 instance or to introduce latency into an API call¹.

2. **Targets**: Targets are the AWS resources on which the actions are performed³. They define the scope of the experiment. For example, a target could be a specific EC2 instance, a set of instances in an Auto Scaling group, or a Lambda function³.

3. **Stop Conditions**: Stop conditions are mechanisms to stop an experiment if it reaches a defined threshold². This threshold is defined as an Amazon CloudWatch alarm². If a stop condition is triggered during an experiment, AWS FIS stops the experiment². This provides a safety mechanism to prevent experiments from causing excessive impact on your system².

These components work together to define and control the behavior of your fault injection experiments in AWS FIS³. Remember, running these experiments will have real effects on your AWS resources, so it's recommended to test in a pre-production environment first³.

## Benefits of AWS FIS

AWS Fault Injection Service (FIS) offers several benefits:

1. **Improve Resilience and Performance**: AWS FIS helps you uncover hidden bugs, monitor blind spots, and discover performance bottlenecks in your applications¹. By creating real-world conditions, you can observe how your application responds to disruptive events and use this information to improve the performance and resiliency of your applications².

2. **Controlled Experiments**: AWS FIS provides the controls and guardrails that you need to run experiments safely on your AWS workloads². It allows you to define specific conditions to stop an experiment or roll back to the pre-experiment state¹.

3. **Ease of Use**: AWS FIS simplifies the process of setting up and running controlled fault injection experiments across a range of AWS services¹. You can run experiments in minutes using pre-built scenarios from the FIS Scenario Library¹.

4. **Insights**: AWS FIS provides superior insights by generating real-world failure conditions, such as impaired performance of different resources¹. This helps you better understand how your system behaves under different conditions¹.

5. **Integration**: AWS FIS can be integrated with your delivery pipeline, allowing you to repeatedly test the impact of fault actions, such as injecting task-level container failures, as part of your software delivery process¹.

- Confident Engineers Build Better Systems
