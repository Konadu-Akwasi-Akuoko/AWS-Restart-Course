# Prevention: Data Security

## Security lifecycle: Prevention - Data security

- Prevention: Is the first line of defense
- Detection: Occurs when prevention fails
- Response: Describes what you do when you detect a security threat
- Analysis: Completes the cycle as you identify lessons learned and implement new measures to prevent the issue from occurring again in the future

Data security is on the **prevention level**

## Confidentiality, integrity, and availability (CIA)

Information must be protected to ensure its confidentiality, integrity, and availability.

- **Confidentiality:** Is private data protected to prevent unauthorized access?
- **Integrity:** Are measures in place to ensure that data has not been tampered with and is correct and authentic?
- **Availability:** Are authorized users able to access the data when they need it?

## Data in motion compared to data at rest

It is important to secure sensitive data while it travels through networks and systems (data in motion). It is also important to secure this data when it is stored on a device (data at rest).

## Cryptography

**Cryptography** is the discipline that embodies the principles and techniques for providing data security, including confidentiality and data integrity.

**Encryption** is the process of using a code, called a cipher, to turn readable data into unreadable data for another party. The cipher contains both algorithms to encrypt and to decrypt the data.

A **key** is a series of numbers and letters that the algorithm uses to encrypt and decrypt data. Only the owners of the keys can encrypt and decrypt data.

Cryptography is the discipline that embodies the principles and techniques for providing data security, including confidentiality and data integrity. It is a collection of practices that take advantage of modern computing techniques. It provides a level of confidentiality and integrity of the information to secure and maintain access to sensitive information. Cryptography is not encryption; encryption is a piece of it.

## Practical uses

Data at rest encryption:

- **File system encryption:** Using Windows New Technology File System (NTFS), you can encrypt a single file or an entire set of files.
- **Drive encryption:** Encrypt an entire drive and its contents. Examples include BitLocker and VeraCrypt. VeraCrypt is a free solution for open-source drive encryption.

Data in motion encryption:

- **Secure Sockets Layer (SSL)/Transport Layer Security (TLS):** These protocols are used to secure data that is being transmitted across the wire. When you go to a secure website with `https` at the beginning of the URL, the `s` signifies SSL. TLS is the successor to SSL.
- **Kerberos:** Kerberos is an encryption technology that is used to encrypt all communications between two devices.
- **IP Security (IPsec):** This protocol was introduced as an integral component of the Internet Protocol version 6 (IPv6) and borrowed for use with Internet Protocol version 4 (IPv4). Both IPs provide the logical connection between network devices by providing identification for each device. The IPsec is used to secure virtual private networks (VPNs).
- **Instant messaging or secure email:** In addition to using TLS to secure the communication between a client and a server, you might also want to secure the message itself. Secure/Multipurpose Internet Mail Extensions (S/MIME) and Pretty Good Privacy (PGP) are two protocols that are used for this purpose.

## Encryption

The goal of encryption is to achieve data confidentiality.

The three types of encryption are symmetric, asymmetric, and hybrid, which the following slides explain further.

## Symmetric encryption

Symmetric encryption uses the same key to encrypt and decrypt the data. The key is a shared secret between the sender and the receiver. Symmetric encryption is fast and reliable and is used for bulk data.

Symmetric encryption is used for payment applications, to encrypt databases, and to verify the identity of the sender of a message in messaging applications.

Security standards that use symmetric encryption include the following:

- **Advanced Encryption Standard (AES):** The US National Institute of Standards and Technology (NIST) established this standard. It replaces the previous Triple Data Encryption Algorithm (3DES) standard. The AES has three fixed 128-bit block ciphers with cryptographic key sizes of 128 bits, 192 bits, and 256 bits. A block cipher is a key and algorithm that are applied to a block of data immediately. With AES, the key size is unlimited whereas the block size maximum is 256 bits. For example, Amazon Elastic File System (Amazon EFS) uses an AES-256 encryption algorithm to encrypt data at rest.
- **International Data Encryption Algorithm (IDEA):** This standard was created and patented in Switzerland and is free for noncommercial use. It uses a block cipher with a 128-bit key.
- **Twofish:** This public domain encryption algorithm is slower than AES.
- **TLS and SSL:** These protocols use symmetric encryption for data exchange.

## Asymmetric encryption

Asymmetric encryption uses both a private key and a public key (a key pair) to encrypt and decrypt the data. Every user in the conversation has a key pair. Asymmetric encryption is more complex and much slower than symmetric encryption. However, it provides more capabilities in the way that keys are managed.

Asymmetric encryption is used to encrypt emails or create digital signatures.

Security standards that use asymmetric encryption include the following:

- **Rivest-Shamir-Adleman (RSA):** This method employs an algorithm based on prime number factorization. Thus, deducing an RSA key takes a significant amount of time and processing power. This encryption method is the standard for important data, especially data that is transmitted over the internet.
- **Diffie-Hellman (DH):** DH is a key exchange method of cryptographic keys over a public channel. This method uses numbers that are raised to specific powers to produce encryption keys.
- **ElGamal:** This method uses an algorithm based on the DH method.•TLS, SSL, and Secure Shell (SSH) –These protocols use asymmetric encryption to establish the connection and create the session, and symmetric encryption for data exchange.

## Comparison of encryption methods

| Criteria | Symmetric | Asymmetric |
| --- | --- | --- |
| Encryption | Fast and straightforward | Complex and time-consuming |
| Process speed | Fast (even large amounts of data) | Slow |
| Keys | One key: 128 or 256 bits | Two keys: length can be 2048 bits or higher |
| Level of security | Is extremely secure; the risk of compromise if the shared key is lost | Provides additional security services; the key is not shared |
| Manageability | Becomes complex with more keys | Includes an easy-to-manage key system |
| Security services provided | Only confidentiality | Non-repudiation, authentication, and more |
| Use cases | Is used to securely transmit large amounts of data, or encrypt databases | Is used for authentication or digital signatures |

The algorithms that are used for symmetric encryption are less complex than the ones for asymmetric encryption. Therefore, symmetric encryption is used when speed matters, such as when transmitting data in bulk. The downside is that the secret key that is used for encryption must be shared between senders and recipient. This method poses a security risk if one of the parties were to lose the key.

Asymmetric encryption is newer and is considered to be more secure than symmetric encryption because different keys are used for the encryption and decryption processes. The private key is not shared; only the recipient possesses it. However, it is more complex to process.

## Hybrid Encryption

Hybrid approaches are often used for encryption. Examples include:

- The TSL protocol or messaging applications that you use on your phone use both symmetric and asymmetric encryptions.
- The session is created by using asymmetric encryption, and symmetric encryption is used for the duration of the session.

A hybrid encryption approach uses both symmetric encryption and asymmetric encryption to protect the data further.

## AWS CloudHSM and AWS KMS

A hardware security module (HSM) is a special hardened and tamper-resistant device to create and manage keys. They must meet some specific, highly secure standard such as FIPS-140-2.

There are two types of HSM:

- AWS CloudHSM:
  - Is a service that is primarily intended to support customer-managed applications that are specifically designed to use HSMs for compliance obligations
  - Is fully managed
  - Offers the possibility to export keys to other available HSMs
- AWS Key Management Service (AWS KMS):
  - Is fully managed.
  - Is integrated with AWS services to simplify the process of using your keys to encrypt data across your AWS workloads.
  - Can store keys in the default key store or connect to AWS CloudHSM to store keys in its key store. This technique helps satisfy compliance obligations to use HSMs while providing the AWS service integrations of AWS KMS.

## What is data integrity?

Data integrity means ensuring that the data remains accurate and consistent when it is stored or travels over a network.

In general, hashes are used to verify the integrity of files that are downloaded from a website.

Hashing and encryption are two very different processes:

- Encryption is a two-way process. An encrypted file can be decrypted by a third party that has the right key.
- Hashing is a one-way encryption to create a signature of the file.

## Ensuring data integrity with hashing

Hashing is a technique that is used to ensure data integrity.

Hashing uses a function that reads the data in a message or file and generates a unique text string value from the data. This text string value is known as a hash value or message digest. If you hash copies of the same file with the same hashing function, it will always produce the same hash value. In this way, you can verify that the content of file has not changed (for example, after it has been transmitted through a network). Hashing functions typically employ standard algorithms such as Secure Hash Algorithm version 1 (SHA1) and Message Digest version 5 (MD5). In general, hashes are used to verify the integrity of files that are downloaded from a website.

## Principles of permissions

A permission grants a specific type of access to a resource (for example, write access to a file). Permissions are classified into two types: discretionary(based on identity or other criteria) and role-based(based on an assigned role).

A permission is assigned to a subject (a person, device, or system) to give the subject the resource access ability defined by the permission.

## Discretionary access control

In a discretionary access control (DAC) type, individuals are assigned a level of access to a resource. The level of access information is stored in an access control list (ACL).

DAC controls the access to resources based on the identity of individuals or groups of individuals.

An ACL is made of a list of permissions: it tells which users have access to which resources and which operations they are allowed.

AWS Identity and Access Management (IAM), the AWS service that helps you securely control access to AWS resources, uses ACL to control access to resources.

## Role-based access control

In a role-based access control type, a level of access to a resource is assigned to a role. That is, permissions are distributed based on role. Individuals are then assigned to different roles as they need access to resources.

Role-based permissions are a key feature of IAM and have the following properties:

- Include a modern permissions approach that does not require a high level of interaction every time a change is needed
- Are efficient when dealing with high staff turnovers and hires for shorter-term projects and tasks
- Are very customizable
- Are used extensively in the commercial sector
- Are expanding in use because they provide a good level of granularity

For example, a company might decide to define permissions based on job role. When someone new is hired, they automatically receive all the permissions that come with the role by being placed into the appropriate role group.
