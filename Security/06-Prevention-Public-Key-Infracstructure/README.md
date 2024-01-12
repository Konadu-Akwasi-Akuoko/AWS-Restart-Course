# Prevention: Public Key Infrastructure

## Security lifecycle: Prevention - Data security

- Prevention: Is the first line of defense
- Detection: Occurs when prevention fails
- Response: Describes what you do when you detect a security threat
- Analysis: Completes the cycle as you identify lessons learned and implement new measures to prevent the issue from occurring again in the future

Public key infrastructure is on the **prevention level**

## Public key infrastructure

Public key infrastructure (PKI) is a collection of technologies that are used to apply cryptography principles to transfer information securely between two entities. It is based on a practical distribution and implementation of keys, with a set of tools to achieve confidentiality, integrity, non-repudiation, and authenticity.

PKIs are used to implement the encryption of public keys but also to manage public-key-associated certificates. Certificates are digital documents that are used in PKI to prove the ownership of a public key. Certificates contain information about the entity that provided and verified the certificate, the entity to which the certificate belongs, and the public key.

The entity that issues the certificate is called the issuer or the certificate authority. The entity that receives the certificate is called the subject.

## Enabling trust

Trust is achieved through the exchange of public keys that validate and identify the parties. Public keys are attached to the certificate that a certificate authority (CA) issues.

## PKI components

- The certificate authority is the entity that delivers the certificate.
- Certificates are documents that contain information about the certificate issuer, the entity that receives the certificate (subject), and the public key.
- Revocation lists are lists that contain certificates that have been invalidated, which means that these certificates cannot be trusted anymore.
- Registration authorities are entities (organizations or companies) that verify requests for certificates. If a request is valid, they tell the certificate authority to provide a certificate.
- Entities are organizations or companies that are asking for certificates or verifying that the certificate is not on a revocation list.
- Certificate templates are models that are used for the certificates.

A user submits a registration request to the registration authority server. The request is transmitted to the certificate authority server. A verification is performed with a revocation list to verify that the certificate is still valid and is not on the revocation list. After the certificate is verified, the certificate authority server sends the certificate to the entity that requested the registration.

## Certificate authorities

CAs are entities that deliver digital certificates, which ensure that a website is secure. An example of certificate authority is Google Trust Services (GTS) and Let's encrypt

CAs issue other types of documents, including the following:

- **Certificate practices statement (CPS):** A CPS defines practices, standards, and algorithms that the CA uses. A CA might publish this document on their website. You can use the information to compare services that CAs offer.
- **Certificate policy:** The certificate policy defines the rules that customers of a CA must follow. The rules include payment requirements, permissible practices (for example, whether you can use it for gambling content), and revocable offenses. Examples of revocable offenses include committing criminal activities or failing to inform the CA of changes that you made to your identity.

## Root CAsand subordinate CAs

Root CA:

- Is at the top of the hierarchy and initializes it
- Stores the root CA keys–Is isolated and kept offline
- Is not directly involved in servicing entities (standalone)

## Internal CAs vs. external CAs


