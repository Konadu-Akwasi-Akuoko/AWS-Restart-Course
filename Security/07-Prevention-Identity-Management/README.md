# Prevention: Identity Management

## Security lifecycle: Prevention - Data security

- Prevention: Is the first line of defense
- Detection: Occurs when prevention fails
- Response: Describes what you do when you detect a security threat
- Analysis: Completes the cycle as you identify lessons learned and implement new measures to prevent the issue from occurring again in the future

Identity management is on the **prevention level**

## What is identity management?

Identity management is the active administration of subjects, objects, and their relationships regarding access permissions.

With identity management, users (or any type of identity) receive appropriate access to the resources that they need at the correct level and appropriate time. By implementing identity management, systems remain scalable as they identify and grant access to resources.

## Identity management principles

Authentication, authorization, and accounting are the core tasks that are performed in identity management.

Consider the case of a visitor who tries to gain physical access to a company’s facilities:

- **Identification:** The visitor must first prove that they are who they say they are by showing a picture identification to the receptionist.
- **Authentication:** The receptionist authenticates the visitor’s identity by comparing the picture to the person who is standing in front of them.
- **Authorization:** To specify that the person is expected and should be allowed into the facilities, the receptionist calls the contact person to grant access to the visitor. The receptionist might also do the following actions:
  - Issue a visitor’s badge
  - Require that the company contact escort the visitor into the facilities as proof to other employees of the visitor’s authorization
- **Accounting:** The visitor is required to sign a visitors’ log. The visitor provides the following information in the log:
  - Name
  - Date and time they arrived and departed
  - Number of their visitor’s badge
  - Name of their contact
  - Reason for their visit

## AAA example login process

Identification, authentication, authorization, and accounting (IAAA) are common security steps that are enforced when a user logs into a system.

The following information is an example of a login principle:

A cloud engineer uses an identification card (ID) that their company issued to log in to the company computer. This card is used to identify the cloud engineer, and the engineer must be **authenticated** by inputting a password. After identification and authorization are complete, the engineer is granted access to the **authorized** services and folders that the engineer is allowed to work on. Every time the engineer logs in and out of the computer, **accounting** is taking place.

## Authentication factors

The three types of authentication factors are something you know, something you have, and something you are. Every authenticator has one or more authentication factors.

**Multi-factor authentication (MFA)** is an authentication method that requires multiple methods or ways of authentication. For example, you log into a bank website with your password, and MFA is enabled. It might ask you for something that you have, such as your phone number. MFA is asking you for something that you know and something that you have.

## Authentication factors: Something you know

Passwords, passphrases, and personal identification numbers (PINs) are examples of authentication factors. These factors are simpler to implement, but they are also the least secure.

## Authentication factors: Something you have

Authenticate by using something that you physically possess. Using something that you have is a more secure way to authenticate. This method is often implemented as a second-factor authentication system after you have provided something that you know.

## Authentication factors: Something you are

Biometric devices are used to validate something that you are. Biometric devices authenticate based on a human property.

Using an authentication mechanism that validates a unique human property, such as a fingerprint or a retinal pattern, is the most complex and expensive solution. However, the authentication can be highly reliable when it is configured well.

## Personally identifiable information (PII)

Personally identifiable information (PII) is a type of data that, when used alone or with other relevant data, identifies an individual. PII might contain direct identifiers, such as passport information, race, ethnicity, or date of birth.

Even if individuals have the same name and possibly the same birth date, they would not have the same government identification number. In this way, PII can identify something unique about an individual among a group of people.

Why is PII important?

PII needs to be protected because it is something that only the individual can uniquely identify. Passwords can be cracked and systems can be hacked, but PII is something that cannot be cracked. Therefore, it is important to keep it in a safe place.

PII can fall under all three authentication factors:

- Something you know: Government identification number
- Something you have: Bank card
- Something you are: Fingerprint

## Authentication: Password policies

When you use password authentication, controlled password management is critical. The most basic way to manage password authentication is to define a policy with password parameters or rules.

A basic or common policy might have the following parameters:

- Minimum number of characters: for example, eight
- Password complexity: none or at least one capital letter
- Maximum password age: none

An example password for this policy is `Password`.

This password and policy make this password extremely vulnerable to attacks such as dictionary and rainbow table attacks. A good policy might have the following parameters:

- Minimum number of character: Passwords must be at least 12 characters.
- Password complexity: Passwords must contain at least one capital letter, one number, and a symbol.
- Maximum password age: After 45 days, passwords expire, and the last 10 passwords cannot be used again.

An example password for this policy is `Pa$$w0rd123!14`

## Dictionary attacks

When you define password rules, you must understand the types of attacks that password authentication can be subject to. One type of attack is a dictionary attack. A dictionary attack attempts to systematically enter each word in the dictionary as a password until it finds a match. Countermeasures for dictionary attacks include enforcing a strong password policy and locking out access after a fixed number of unsuccessful attempts.

Another type of password authentication attack is a rainbow table attack, which uses precomputed hashes of text passwords. These precomputed hashes are compared against stolen hashes to find their corresponding password.

A password hash is a unique encrypted value. This password hash is produced by taking the value of the text password and transforming it by using an algorithm. The algorithm always produces the same hashed value for a given input value. The rainbow table lists the plain-text value of encrypted passwords specific to a given hash algorithm. Thus, the text password value of a password can easily be determined when a match on the hash value is found.

## Password managers

- Operate over a centralized authentication system
- Improve security by requiring extra login steps
- Allow password resets
- Manage services that are used with specific credentials
- Store personal passwords on a local system

## Group accounts

Do not use group accounts. To harden authentication, as a best practice, avoid the use of group accounts because they provide no accountability. With group accounts, multiple groups can authenticate at the same time.

## Single sign-on (SSO)

With single sign-on (SSO), users log in once and gain access to different applications without the need to re-enter login credentials for each application.

## AWS Single Sign-On

AWS SSO includes the following features:

- **One-click SSO access to AWS accounts:** AWS SSO has integrated applications and custom SAML 2.0 based applications, which gives the AWS SSO console quick one-click access to authorized users.
- **Ability to create and manage users and groups with AWS SSO:** You can create users and groups within AWS SSO in the console for easy access to granting permissions. AWS SSO is also compatible with the AWS Directory Service for Microsoft Active Directory.
- **Compatibility with common cloud applications:** Because AWS SSO is compatible with commonly used cloud applications, cloud administrators don’t need to learn how to administer SSO services to different applications. AWS SSO can be integrated with applications that are noted in the AWS documentation.
- **Compatibility with existing IAM roles, users, and policies:** Using AWS SSO will have no impact on existing IAM roles, users, or policies.

## Federated users

Federated users is a form of single sign-on. One account is used for multiple services.

Federated users is a type of SSO implementation that is used between web identities. It uses a token to verify user identity between distinct systems.

With SSO, individuals can sign into different networks or services by using the same group or personal credentials. For example, by using SSO, you can use your Google account credentials to sign into Facebook.

## Amazon Cognito

It is an Amazon service that provides user management, authentication, and authorization for your web and mobile apps. You can use Amazon Cognito by signing in with a user name and password through a third-party website.

Here is how Amazon Cognito works to authenticate and grant access to an AWS service:

1. First, the user signs in through what is called a user pool and receives a user token after they get authenticated.
2. The application will then exchange the user pool token for an AWS credential through the identity pool.
3. For the final step, the user can now use the AWS credentials to access AWS services.

User pools have the following characteristics:

- Can federate through a third-party identity provider
- Function as a user directory for Amazon Cognito
- Give users the ability to sign up or sign in through a web or mobile app by using Amazon Cognito
- Provide SSO, customizable user interface (UI), social sign-in options, user directory management, and MFA

## How IAM works

AWS Identity and Access Management (IAM) is a service that helps you securely control access to AWS resources by using authentication and authorization.

- Authentication: Use IAM to control who can sign in
- Authorization: Use IAM to control who has access to resources

When the user signs in to the AWS console, the principal is authenticated as the AWS account root user or an IAM entity (user or role). The principal then sends a request to AWS, which contains information about the principal itself, the action it wants to perform, environment data, and resources. After the request is sent, AWS uses policies stored as JavaScript Object Notation (JSON) documents to check whether the user is authorized for the request. As soon as the user is authenticated and authorized and AWS approves the request, the user is allowed to create, delete, and edit resources. The policy defines the actions that the principal is allowed to take on the resources.

A principal is a person that is either the AWS account root user or IAM user or role that makes requests to AWS.

Authentication happens when the principal signs in to AWS by using their AWS credentials.

A request contains the following log of information: Resources:

- **The AWS resource object being accessedPrincipal:** The (user or role) sending the request
- **Environment data:** IP address, user agent, enabled status, time of day, and user agent
- **Resource data:** Data that pertains to the resource (for example, a tag on an Amazon Elastic Compute Cloud [Amazon EC2] instance)

Authorization is stored in AWS as JSON documents, which AWS uses as values to check for policies that apply to these requests. These requests are either allowed or denied. Action is when the user is authenticated, authorized, and request approved, and the user will then be allowed to create, delete, and edit resources. A policy holds what the principal or user is allowed to create, delete, or edit.
