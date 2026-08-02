Secure File Encryptor - Codveda Internship (Level 3)
1.Introduction
This project is a secure command-line tool designed to encrypt and decrypt files using industry-standard cryptographic algorithms. As part of the Codveda Technology Python Development Internship (Level 3 - Advanced), this application demonstrates the practical implementation of data security principles. It ensures that sensitive information remains confidential by converting readable data into an unreadable format, which can only be restored using a specific secret key.
2.Features
Universal File Support: Capable of handling any file type, including text documents (.txt), images (.jpg, .png), and PDFs, by processing data in binary mode.
Fernet Symmetric Encryption: Utilizes the cryptography library to provide robust, tamper-proof encryption that is difficult to break without the key.
Automatic Key Management: Generates a unique secret.key file automatically if one does not exist, ensuring a seamless user experience while maintaining security.
Smart Naming Convention: Automatically appends _encrypted to filenames during encryption and restores the original name upon decryption to prevent data confusion.
Robust Error Handling: Provides clear feedback for common issues such as missing files, incorrect keys, or corrupted data, ensuring the program never crashes unexpectedly.
3.Technology Stack & Rationale
Technology
Why We Used It
Python 3.x
Chosen for its powerful standard libraries and ease of handling binary file operations and complex logic.
Cryptography Library
Provides the Fernet class, which implements symmetric encryption. It is preferred over custom algorithms (like Caesar Cipher) because it is vetted by security experts and resistant to modern attacks.
OS Module
Used to check for file existence and handle file paths dynamically, making the script compatible with different operating systems.
Binary Mode (rb/wb)
Essential for reading and writing non-text files (like images) without corrupting their internal structure.
4.Advantages
Data Privacy: Ensures that even if a file is stolen, its contents remain inaccessible to unauthorized users.
Integrity: Fernet encryption includes a timestamp and HMAC, ensuring that the encrypted data has not been tampered with.
Simplicity: The CLI interface makes it easy for non-technical users to secure their files without needing to understand complex cryptographic concepts.
Efficiency: The encryption and decryption processes are fast, even for moderately large files, due to optimized library functions.
5.Requirements
To run this project, you need the following:
Python 3.6 or higher installed on your system.
Internet Connection (only for the initial installation of the library).
Required Library: Install the cryptography package using pip:pip install cryptography

6.How It Works (Working Mechanism)
Key Generation: Upon the first run, the script generates a 32-byte URL-safe base64-encoded key and saves it as secret.key.
Encryption Process:
The user selects a file.
The script reads the file in binary mode.
The Fernet object uses the key to transform the data into an encrypted byte string.
The result is saved as a new file with the _encrypted tag.
Decryption Process:
The user selects the encrypted file.
The script uses the same secret.key to reverse the process.
If the key matches, the original data is restored; otherwise, an error is raised.
7.Learning Outcomes
Understanding the difference between Symmetric and Asymmetric encryption.
Practical implementation of File I/O in binary mode.
Mastery of Third-party library integration (cryptography).
Adherence to Zero-Trust Security Principles by prioritizing key management.
#=============================================#
8 Code Architecture
The project follows a modular functional architecture, separating concerns into distinct logical units for better maintainability and scalability.
Component Breakdown:
Key Manager (generate_key, load_key): Handles the lifecycle of the cryptographic key. It ensures that a valid 32-byte Fernet key is always available for operations.
Encryption Engine (encrypt_file):
Reads source file in binary mode (rb).
Initializes the Fernet cipher suite with the loaded key.
Transforms plaintext bytes into ciphertext.
Writes the encrypted payload to a new file with an _encrypted suffix.
Decryption Engine (decrypt_file):
Reads the encrypted file.
Attempts to reverse the transformation using the same key.
Validates data integrity (HMAC check) before writing the restored file.
User Interface (main): A CLI-based controller that manages user input, validates file paths using the os module, and routes actions to the appropriate engine.