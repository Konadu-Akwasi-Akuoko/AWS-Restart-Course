# Amazon DynamoDB

## Relational and nonrelational NoSQL databases: Comparison

- Relational databases
  - Data is stored in tables by using predefined columns of specific data types.
  - Relationships can be defined between tables by using table foreign keys.
  - Better performance is achieved by adding compute or memory capacity to a single database server.
- Non-relational NoSQL databases
  - Data is stored in tables with a flexible column structure.
  - Each item stored in a table can have a different number and type of data elements.
  - Better performance is achieved by adding a new server to an existing pool of database servers.

## DynamoDB is a NoSQL database

Dynamo DB is a fully managed, serverless, key-value NoSQL database that does the following:

- Improves performance by keeping data in memory
- Keeps data secure by encrypting data at rest
- Protects data with backups and automated copying of data between AWS Regions

DynamoDB offers the following advantages:

- Fully managed service: AWS manages all of the underlying compute and storage needed to store your data.
- Scalability: DynamoDB automatically adds more compute and storage capacity as your data grows.
- **Redundancy:** DynamoDB copies your data across multiple AWS Regions to avoid data loss.
- **Recoverability:** DynamoDB can restore your data from automatic backup operations.•Low latency:Data can be read from a DynamoDB table in a few milliseconds.
- **Security:** You can use DynamoDB with AWS Identity and Access Management (IAM) to control access to DynamoDB tables.
- **Flexibility:** DynamoDB can store several types of data, and each record can have varying numbers and types of data. JSON is one popular way to store data in DynamoDB.

## Key concepts: Tables

- Tables In DynamoDB:
  - Similar to relational database systems, DynamoDB stores data in tables.
  - The table name and primary key must be specified at table creation.
  - Each DynamoDB table has at least one column that acts as the primary key.
- The primary key is the only data that is required when storing a row in a DynamoDB table. Any other data is optional.

## Key concepts: Attributes

- A column in a DynamoDB table is called an attribute.
  - An attribute represents a fundamental data element, something that does not need to be broken down any further.
  - An attribute is similar in concept to table columns or fields in a relational database.
- A primary key can consist of one or two attributes.

## Key concepts: Items

- An item is a group of attributes that is uniquely identifiable among all of the other items.
  - Each item consists of one or more attributes.
  - Each item is uniquely identified by its primary key attribute.
  - This concept is similar to a table row in a relational database.
- The number and type of non-primary key attributes can be different for each item in a table.

## Key concepts: Primary keys

- Simple primary key
  - The primary key consists of one attribute.
  - The attribute is called the partition key or hash key.
- Composite primary key
  - The primary key consists of two attributes.
  - The first attribute is the partition key or hash key.
  - The second attribute is the sort key or range attribute.

## Key concepts: Partitions

- DynamoDB tables store item data in partitions.
  - Table data is partitioned and indexed by the primary key.
  - Each table has one or more partitions.
  - New partitions are added as data is added to the table.
  - Tables whose data is distributed evenly across multiple partitions generally deliver the best performance.
- The partition in which an item’s data is stored is determined by its primary key attribute.

## Key concepts: Storing items in partitions

When choosing the partition to store the data, DynamoDB applies a function to the partition key attribute of the primary key. In the case of the Friends table, the primary key is a simple primary key. Therefore, the partition key attribute is the same as the primary key, which is FriendID.

The value that the function returns will be in either Partition 1or Partition 2 depending on the value for the FriendIDattribute.

## Key concepts: Storing attributes in partitions

When choosing the partition to store the data, DynamoDB applies a function to the partition key attribute, FriendID. In this case, the function chooses Partition 2to store Zhang’s data.

Notice that two additional attributes are being stored for Zhang, more than were stored for Martha. These extra attributes do not present a problem. If an item has a primary key value, DynamoDB permits each item to have different numbers and types of attributes.

## Using global tables

- Using the global table option creates a DynamoDB table that is automatically replicated across your choice of AWS Regions worldwide.
  - Deliver fast, local read and write performance for global applications.
  - Your applications can stay highly available in the unlikely event of isolation or degradation of an entire AWS Region.
- Global tables eliminate the difficult work of replicating data between Regions and resolving update conflicts between copies.

The DynamoDB global tables feature provides high availability and scalability across Regions. A global table is a collection of one or more DynamoDB tables, which must all be owned by a single AWS account.The tables in the collection are also known as replica tables. Each replica stores the same set of data items. When you create a global table, you specify the AWS Regions where you want the table to be available. DynamoDB performs all of the necessary tasks to create identical tables in these Regions. It automatically performs ongoing copying of data to all of the tables to keep their contents in sync.DynamoDB global tables work well for large-scale applications with globally dispersed users by accessing the replica that is closest to them.
