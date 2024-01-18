# Amazon Relational Database Service (Amazon RDS)

## Amazon RDS defined

Amazon RDS is a managed database service that sets up and operates a relational database in the cloud.

Running an unmanaged, standalone relational database can be time-consuming and have limited scope. To address these challenges, AWS provides a service that sets up, operates, and scales the relational database without any ongoing administration. Amazon RDS provides cost-efficient and resizable capacity while automating time-consuming administrative tasks.

Amazon RDS frees you to focus on your applications so that you can give them the performance, high availability, security, and compatibility that they need. With Amazon RDS, your primary focus is your data and optimizing your application. In short Amazon RDS is a PaaS.

## Amazon RDS use cases

| Web and Mobile Applications | Ecommerce Applications | Mobile and Online Games |
|----------------------------|-----------------------|------------------------|
| High throughput            | Low-cost database     | Rapid growth capacity  |
| Massive storage scalability| Data security         | Automatic scaling      |
| High availability          | Fully managed solution| Database monitoring    |

## DB Instance

A DB instance is an isolated database environment that runs in the cloud. It is the basic building block of Amazon RDS.

## Amazon RDS DB instances

The basic building block of Amazon RDS is the DB instance. A DB instance is an isolated database environment. It can contain multiple user-created databases, and you can access it by using the same tools and applications that you use with a standalone database instance. The resources in a database instance are determined from its database instance class, and the type of storage is determined from the type of disks.

Database instances and storage differ in performance characteristics and price so that you can customize your performance and costs to the needs of your database. When you choose to create a DB instance, you must first specify which database engine to run. Amazon RDS currently supports the following databases:

- MySQL
- Aurora
- Microsoft SQL Server
- PostgreSQL
- MariaDB
- Oracle

## Amazon RDS backup

- Because Amazon RDS is a fully managed service, one task that it automatically performs is the periodic backup of a DB instance. The entire instance is backed up to a storage volume snapshot during a specified backup window. It is retained according to a specified backup retention period. The first snapshot of a DB instance contains the full data. Subsequent snapshots are incremental and contain only the data that changed since the most recent snapshot.
- Optionally, you can back up a database instance manually by creating a snapshot.

## Creating a DB instance in Amazon RDS

You can create a DB instance in Amazon RDS in two ways. The management console offers an Easy Create method and a Standard method.

- If you choose to use the Easy Create method, the configuration options are based on Amazon best practices. You can specify a DB engine and instance size and can choose an identifier.
- You also have an opportunity to select Standard to create your instance. You determine or choose your configurations.

## How to create a DB instance

MySQL example

1. In the Configuration section, choose MySQL.
2. Complete the remaining steps that are needed to answer the required configuration questions, and then choose Create.
3. Depending on the DB instance class and the amount of storage, it can take up to 20 minutes before the new instance is available.

## High availability with Multi-AZ deployment: Replication

One of the main features of AmazonRDS is that you can configure a database instance with high availability by using a Multi-AZ deployment. This configuration automatically generates a standby copy of the database instance in another Availability Zone in the same virtual private cloud (VPC). After you make the initial full copy, transactions are synchronously replicated to the standby copy. Running a database in multiple Availability Zones can enhance availability during planned system maintenance. It can help protect your database against database failure and disruptions to Availability Zones.

## High availability with Multi-AZ deployment: Failover

If the primary database instance fails, Amazon RDS automatically brings the standby database instance online as the new primary instance. Requests from both applications are then directed to the new primary instance. The requesting applications use the Amazon RDS Domain Name System (DNS) endpoint to reference the database by name. As a result, the failover happens without needing to change the application code. Also, notice that no data loss occurs because of the synchronous replication.

## Amazon RDS read replicas and scaling

In addition to a high availability configuration, Amazon RDS offers other ways of providing scalability. For example, you can create read replicas for MySQL, MariaDB, PostgreSQL, and Aurora. Updates to the source DB instance are asynchronously copied to the read replica instance.

You can then reduce the load on your source DB instance by routing read queries from your applications to the read replica. You can also use read replicas to scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads.

Read replicas can also be promoted to become the primary DB instance. However, because it uses asynchronous replication, this option requires manual action. Read replicas can be created in a different Region from the primary DB instance. This feature can direct reads to a read replica in a geographic area that is closer to the user. Thus, it can help satisfy disaster recovery (DR) requirements or reduce latency.

## Amazon RDS scaling

You can also increase the capacity of a database server by changing its instance class or storage capacity. By changing the instance class, you can increase the CPU and memory that are available to the instance. By modifying the allocated storage, you can increase storage capacity without incurring downtime.

- Instance class
  - Change instance class to increase computation and memory capacity
- Storage capacity
  - Scale storage for existing instances.
  - Increase storage capacity without incurring downtime.

**NB: Note that changing an instance class requires downtime.**

## Aurora defined

Aurora is part of the managed database service Amazon RDS. Aurora is a relational database engine. A database engine is a service for storing, processing, and securing data.

Some of the benefits of Aurora include the following:

1. Aurora uses the same code, tools, and applications as existing MYSQL and PostgreSQL databases.
2. Aurora includes a high-performance storage subsystem. Its database engine is customized to take advantage of that fast distributed storage.
3. An Aurora DB has clusters that consist of one or more DB instances and a cluster volume that manages the data for those DB instances.

## An AuroraDB cluster

An Aurora DB cluster consists of one or more DB instances and a cluster volume that manages the data for those DB instances.

What is an Aurora cluster volume?

An Aurora cluster volume is a virtual database storage volume that spans multiple Availability Zones. Each Availability Zone has a copy of the DB cluster data.

## Contents of an AuroraDB cluster

Two types of DB instances make up an Aurora DB cluster.

- **Primary DB instance**
  - The primary DB is the main instance. The instance allows read and write operations and allows for data modification.
- **Aurora Replica**
  - The Aurora Replica connects to the same storage volume as the primary DB instance and supports only read operations.

## Aurora use cases

- Enterprise applications
  - Compared to commercial databases, Aurora can help cut down your database costs by 90 percent or more while improving the database’s reliability and availability
- Software as a service (SaaS)applications
  - The Aurora managed database offering provides benefits to SaaS applications. SaaS companies can focus on building high-quality applications without worrying about the underlying database that powers the application.
- Online and mobile gaming
  - Because web and mobile games are built to operate at very large scale, they require a database with high throughput and massive storage scalability.Aurora provides enough room for future growth.
