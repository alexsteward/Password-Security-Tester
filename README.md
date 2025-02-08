## **Password Security Tester**

### **Description**  
  The **Password Vulnerability Tester** is a tool I built to demonstrate how vulnerable certain password hashing algorithms can be to brute-force attacks. The tool works by taking a hashed password (created using common algorithms like MD5, SHA-1, or SHA-256) and attempting to "crack" it by trying different combinations until it finds the original password. By inputting a hashed password, selecting the hash algorithm, and setting a maximum password length, the tool simulates a basic password attack, showing how attackers might exploit weak hashing methods.  
  
  This project is designed with education in mind, helping users understand how vulnerable hashes can be and why using stronger passwords and more secure algorithms is essential for protecting sensitive data.  

> **⚠️ Disclaimer:** This tool is meant solely for ethical testing in controlled environments. It should only be used with explicit permission on systems you own or have authorization to test.

##  **Features**  
  - Supports multiple hash types: MD5, SHA-1, and SHA-256.  
  - Customizable brute-force limit: Define a maximum password length for cracking attempts.  
  - Simple to use: Input a hash, choose an algorithm, and start the cracking process.  
  - Demonstrates vulnerabilities in password hashing algorithms, highlighting the need for secure practices.  

##  **Tools, Languages, and Libraries Used**  
  - **Python** – Primary programming language used for building the tool.  
  - **hashlib** – Python's built-in library for handling hashing algorithms.  
  - **time** – Used for calculating and displaying the duration of the brute-force process.  
  - **Visual Studio Code (VSCode)** – Development environment used for coding and testing.
