Project Overview:
The License System Project was aimed at securing BEL's proprietary software through a structured and secure license management mechanism. The system ensures that only authorized users can activate and access software by generating and verifying cryptographic license keys.

📌 Key Responsibilities & Features:

Cryptographic Key Generation
Developed a secure mechanism to generate public and private RSA keys used for signing and validating licenses. Ensured confidentiality and integrity during the license lifecycle.

License Creation & Signing
Implemented functionality to create license files containing metadata (user info, expiry date, hardware binding, etc.) and digitally sign them using private keys.

License Verification Module
Designed a module to validate license files on software startup. Verified digital signatures, expiration dates, and device binding to prevent unauthorized access or tampering.

GUI Integration (Windows Forms)
Built a user-friendly GUI for license input, activation status, and error display using Windows Forms. Ensured seamless integration with backend validation logic.

Hardware Binding
Integrated system to bind licenses to specific hardware identifiers (like MAC address or CPU ID) for enhanced protection against license sharing.

Secure Storage & Logging
Used local encrypted storage (SQLite or file-based) to store activation records. Included audit logs for failed/successful validation attempts.

🎯 Outcome & Impact:

Strengthened software protection by preventing piracy, cloning, and misuse.

Improved control over software distribution and activation monitoring.

Delivered a scalable license validation framework adaptable to future projects and software tools used at BEL.

✅ Skills Gained:

Software protection and encryption techniques

Licensing architecture and secure software deployment

Practical understanding of RSA, digital signatures, and secure key storage

Integration of cryptographic logic into real-world applications

