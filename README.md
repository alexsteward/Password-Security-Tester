# Password Cracker Tool

## Overview
This **Password Cracker Tool** allows you to crack hashes generated by popular algorithms like **MD5**, **SHA-1**, and **SHA-256**. By inputting a hashed password, selecting the hash type, and specifying a maximum password length, the tool attempts to find the original plaintext password through brute-force cracking using a list of potential passwords.

## Features
- **Supports Multiple Hash Types**: MD5, SHA-1, and SHA-256.
- **Customizable Cracking Limit**: Define the maximum password length to control the range of brute-forcing.
- **Efficient Cracking**: Uses a brute-force method to generate potential password combinations based on the provided `passwords.txt` file.

## Tools, Languages, and Libraries Used
- **Python** – Primary programming language used for the tool.
- **Visual Studio Code (VSCode)** – Development environment for building and testing the code.
- **hashlib** – Python's built-in library for generating and checking hash values.
- **time** – Used for calculating and displaying cracking duration.


## Skills Learned
- **Hashing Algorithms:** Working with MD5, SHA-1, and SHA-256 to understand their structures and weaknesses.
- **Brute-Force Cracking:** Implementing a brute-force method to generate potential passwords and crack hashes.
- **Python Scripting:** Using Python for file handling, hashing, and performing computational tasks efficiently.

## How to Use
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/password-cracker.git
   cd password-cracker

2. Create passwords.txt file in same directory
3. Install needed dependencies (pip install -r requirements.txt)
4. Run the script: python cracker.py --hash <your_hash> --type <md5|sha1|sha256> --max-length <number>


               (EX: python cracker.py --hash d41d8cd98f00b204e9800998ecf8427e --type md5 --max-length 5)

