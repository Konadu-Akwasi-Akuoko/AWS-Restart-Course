# AWS S3

Amazon S3 is a managed cloud storage solution that you can use to store data as objects in a bucket.

Objects can be almost any data file, such as documents, images, or videos. When you add objects to a bucket, you must give them a unique name, which is called an object key. Amazon S3 is object-level storage, this means if you want to change a part of a file, you must make the change and then re-upload the entire modified file.

Buckets are logical containers for objects. You can have one or more buckets in your account. For each bucket, you can control access regarding who can create, delete, and list objects in the bucket. You can view access logs for the bucket and its objects, and you can choose the geographical region where Amazon S3 stores the bucket and its contents.

## Amazon S3 features

- Amazon S3 holds trillions of objects and regularly peaks at millions of requests per second, and it can hold virtually any amount of files.
- By default, none of your data is shared publicly. You can also encrypt your data in transit and choose to turn on server-side encryption on your objects.
- By default, data in Amazon S3 is stored redundantly across multiple facilities and multiple devices in each facility.
- Amazon S3 also provides low-latency access to the data over the internet by Hypertext Transfer Protocol (HTTP) or Secure HTTP (HTTPS), so you can retrieve data anytime from anywhere.
-Bucket names are universal and must be unique across all existing bucket names in Amazon S3.

## Amazon S3 storage classes

- **Amazon S3 Standard:** Amazon S3 Standard is designed to provide high-durability, high-availability, and high-performance object storage for frequently accessed data. And it delivers low latency and high throughput. The use cases of S3 standard include cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics. The data is also stored in redundantly in 3 or more availability zones.

- **Amazon S3 Intelligent-Tiering:** Amazon S3 Intelligent-Tiering storage class is designed to optimize costs. It automatically moves data to the most cost-effective access tier without affecting performance or operational overhead. For a small monthly monitoring and automation fee per object, Amazon S3 monitors access patterns of the objects in Amazon S3 Intelligent-Tiering. It moves the objects that haven’t been accessed for 30 consecutive days to the Infrequent Access tier. If an object in the Infrequent Access tier is accessed, it is automatically moved back to the Frequent Access tier. It doesn’t charge retrieval fees when you use it. Also, it doesn’t charge additional fees when objects are moved between access tiers.

- **Amazon S3 Standard-Infrequent Access (Amazon S3 Standard-IA):** The Amazon S3 Standard-IA storage class is used for data that is accessed less frequently but requires rapid access when needed. Amazon S3 Standard-IA is designed just like Amazon S3 Standard. With these benefits, it also offers a low per-GB storage price and per-GB retrieval fee. But you can store objects in Amazon S3 Standard-IA for any length of time. However, it’s important to note that S3 Standard-IA has a minimum storage duration charge of 30 days. This means that if you delete an object before 30 days, you will still be charged for the full 30 days. And it also works well as a data store for disaster recovery (DR) files.

- **Amazon S3 One Zone-Infrequent Access (Amazon S3 One Zone-IA):** Amazon S3 One Zone-IA is for data that is accessed less frequently but requires rapid access when needed. Unlike other Amazon S3 storage classes, which store data in at least three Availability Zones, Amazon S3 One Zone-IA stores data in one Availability Zone. Amazon S3 One Zone-IA works well for customers who want a lower-cost option for infrequently accessed data, but don’t require the availability and resilience of Amazon S3 Standard or Amazon S3 Standard-IA.You can also use it as cost-effective storage for data that is replicated from another AWS Region by using Amazon S3 Cross-Region Replication.

- **Amazon Simple Storage Service Glacier (Amazon S3 Glacier):** Amazon S3 Glacier is a secure, durable, and low-cost storage class for data archiving. To keep costs low but suitable for varying needs, Amazon S3 Glacier provides three retrieval options that range from a few minutes to hours, with varying prices. In the context of Amazon S3 Glacier, retrieval refers to the process of accessing and restoring your data from the Glacier storage. This is typically done when you need to access or use the data that has been archived in Glacier. The time it takes to retrieve your data can vary based on the retrieval option you choose. Amazon S3 Glacier provides three retrieval options:

  1. **Expedited retrievals** that typically complete in 1–5 minutes.
  2. **Standard retrievals** that typically complete in 3–5 hours.
  3. **Bulk retrievals** that return large amounts of data typically in 5–12 hours

  You can upload objects directly to Amazon S3 Glacier.

- **Amazon S3 Glacier Deep Archive (Amazon S3 Glacier Deep Archive):** Amazon S3 Glacier Deep Archive is the lowest-cost storage class for Amazon S3. It supports long-term retention and digital preservation for data that might be accessed once or twice in a year. All objects that are stored in Amazon S3 Glacier Deep Archive are replicated and stored across at least three geographically dispersed Availability Zones. In retrieving your data after uploading it will be made available to you within a 12-hour time frame.

## Access teh data anywhere

You can access Amazon S3 through theAWS Management Console, AWS Command Line Interface (AWS CLI), or AWS Software Development Kits (SDKs). Additionally, you can access the data in your bucket directly by using REST-based endpoints, which support Hypertext Transfer Protocol(HTTP) or Secure HTTP (HTTPS) access.

## Amazon S3 bucket and object URL structure

- Bucket URL: `https://s3-ap-northeast-1.amazonaws.com/[bucket name]/`
- Object: `https://s3-ap-northeast-1.amazonaws.com/[bucket name]/[Preview2.mp4]`

In the above example, Amazon S3 was used to create a bucket in the Tokyo Region, which is identified in AWS by its Region code: `ap-northeast-1`.

The example shows how the URL for a bucket is structured. The Region code is first, followed by `amazonaws.com`, and then followed by the bucket name.

Amazon S3 refers to files as objects. As soon as you have a bucket, you can store virtually any number of objects inside it. An object consists of data and any metadata that describes that file.

To store an object in Amazon S3, you upload the file that you want to store into a bucket. When you upload a file, you can set permissions (and metadata) on the data.

In this example, the object `Preview2.mp4` is stored inside the bucket. The URL for the file includes the object name at the end, thus `Preview2.mp4`.

## Redundancy in Amazon S3

When you create a bucket in Amazon S3, it is associated with a specific AWS Region. Whenever you store data in the bucket, it is redundantly stored across multiple AWS facilities in your selected Region.

## Seamless scaling

Amazon S3 automatically manages the storage behind your bucket even when your data grows. Because of this system, you can get started immediately and have your data storage grow with your application needs.

## Common use cases for Amazon S3

The flexibility to store a virtually unlimited amount of data—and to access that data from anywhere—makes Amazon S3 suitable for various scenarios, including the following:

- Location for application data. Amazon S3 is one of the best ways to store application data, especially data generated by users. The content can be fetched directly over the web through `http` and `https`, your application doesn’t need serve that content.

- For static web hosting, S3 buckets can serve your website’s static content, including Hypertext Markup Language (HTML), Cascading Style Sheets (CSS), JavaScript, and other files.

- The high durability of Amazon S3 makes it a good candidate to store backups of your data. Also S3 is highly available and it also have disaster recovery capabilities.

- You might have data that you plan to analyze by using various big data tools. The scalable storage and performance of Amazon S3 make it a good candidate for the staging or long-term storage of this data.

## Amazon S3 pricing

| Pay for only what you use | You do not have to pay for the following |
| --- | --- |
| GBs per month | Transfer in to Amazon S3 |
| Transfer out to other Regions | Transfer out from Amazon S3 to Amazon CloudFront or Amazon EC2 in the same Region |
| PUT, COPY, POST, LIST, and GET requests | |

With Amazon S3, specific costs might vary, depending on the Region and the specific requests that are made. You pay for only what you use, including GBs per month; transfer out of other Regions; and PUT, COPY, POST, LIST, and GET requests.

As a general rule, you pay for only transfers that cross the boundary of your Region. You don’t pay for transfers in to Amazon S3 or for transfers out from Amazon S3 to Amazon CloudFront edge locations in that same Region.

## Amazon S3 cost estimation

When you estimate the costs of Amazon S3, you must consider the following factors:

- **Storage class type:**
  - **Standard storage** is designed to provide 11 9s of durability and four 9s of availability. This means that the system is designed to be operational and accessible 99.99% of the time, which translates to approximately 52.56 minutes of downtime per year.
  - **Standard –Infrequent Access (S-IA)** can reduce your costs by storing less frequently accessed data at slightly lower levels of redundancy than Amazon S3 Standard Storage. Standard –Infrequent Access is designed to provide the same 11 9s of durability as Amazon S3, with three 9s of availability in a given year.
- **Amount of storage:**
  - You should also consider the number and size of objects that are stored in your S3 buckets and the type of storage.
- **Requests:**
  - Consider the number and type of requests. GET requests incur charges at different rates than other requests, such as PUT and COPY requests.
    - A GET request retrieves an object from Amazon S3. You must have READ access to use this operation.
    - A PUT request adds an object to a bucket. You must have WRITE permissions on a bucket to add an object to it.
    - A COPY request creates a copy of an object that is already stored in Amazon S3. A COPY operation is the same as performing a GET and then a PUT.

- **Data transfer**
  - Consider the amount of data that is transferred out of the Amazon S3 Region.
  - Remember that data transfer in is free, but you will be charged for data transfer out.
