# Fundamentals of AWS Pricing

## AWS pricing model

AWS have major three major drivers of cost: **compute**, **storage**, and **outbound data transfer**

In most cases you won't be charged for inbound data transfer, thus it means communication or the sending of data between AWS services in the same region will not be billed. But sometimes there is an exception to this rule.

Outbound data transfer is aggregated across services and then charged at the outbound data transfer rate. This charge appears on the monthly statement as **AWS Data Transfer Out**.

## How do you pay for AWS?

AWS is a pay as you go service, thus you pay for what you use. This utility style payment includes:

- Pay for what you use.
- Pay less when you reserve.
- Pay less when you use more.
- Pay even less as AWS grows.

- **Pay for what you use:** With AWS you pay for only web services you use, and there are no upfront costs or contracts that a user is being locked into, it's only pay as you go. Also if you think you don't need a service again it can be terminated.

- **Pay less when you reserve:** For certain services like Amazon EC2 and Amazon RDS companies or users can let Amazon reserve a space or capacity for them, and when it is reserved they pay less than when it is on demand or when it is a pay-as-you-go model. Reserve instances are in 3 options
  1. **All upfront reserved instance(AURI)**, this is when you pay for the full reserved instance, and it contains the most discount.
  2. **Partial upfront reserved instance(PURI)**, this is when you make partial payment for a reserved instance, and it gives the lower discounts with the ability to spend less upfront.
  3. **No upfront reserved instance(NURI)**, this is when you don't make any initial payment upfront but you tell Amazon to reserve you an instance, this model get's the lowest discount.

- **Pay less by using more:** Services such as Amazon S3, Amazon EBS, and Amazon EFS have tiered pricing, thus the more you use the less you pay. For these services they are measured using pay per GB, so the more GB you use the less you pay.

- **Pay less as AWS grows:** As AWS grows they also lower pricing for their services. Since 2006 Amazon has lowered their price 75 times as they continue to grow. This is also known as economies of scale.

## Custom pricing

If none of the AWS pricing models work for your project, custom pricing is available for high-volume projects with unique requirements.

## AWS free tier

To help new AWS customers get started in the cloud, AWS offers a free usage tier (the AWS Free Tier) for new customers for up to 1 year. The AWS Free Tier applies to certain services and options.

## Services with no charge

AWS offers some services that have no charges:

1. Amazon virtual private cloud (Amazon VPC)
2. AWS identity and access management (IAM)
3. Consolidated billing
4. AWS elastic beanstalk
5. AWS cloud formation
6. Amazon EC2 auto scaling
7. AWS OpsWorks

## AWS pricing calculator

The AWS pricing calculator helps us estimate monthly billings of AWS services. With the pricing calculator you can add, modify, remove services from your bill, to see how you'll pay.

The AWS calculator can help you estimate monthly service costs, identify opportunities for reductions, use templates to model solutions to compare services and deployments models. The calculator also show common user samples and usage

## The cost of ownership

If a company wants to save a lot of money it is encouraged that they use cloud services instead of on premises infrastructure. Because with the on premises infrastructure a company needs to buy equipments, hire people to manage these equipments, and do a whole lot of stuff to maintain and look after the on premises infrastructure. But sometimes companies would want to measure between on premises infra and using cloud infra. How would they do that?

**Total cost of ownership(TCO):** is a financial estimate to help identify direct and indirect costs of a system. Use TCO to compare the costs of running an entire infrastructure environment or specific workload on premises as compared to the AWS Cloud. Budget and build the business case for moving to the cloud.

When you compare an on-premises solution and a cloud solution, it’s essential to assess the actual costs of both options. With the cloud, most costs are upfront and can be calculated. Cloud providers give transparent pricing based on different usage metrics such as RAM, storage, and bandwidth. Pricing is frequently fixed per unit of time.After you understand how pricing works, you can calculate costs based on several different usage estimates.
