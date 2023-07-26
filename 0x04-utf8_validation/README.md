# 0x04. UTF-8 Validation

In this project, I implement a method to determine if a given data set represents a valid UTF-8 encoding. As a Software Engineer at Holberton School, I ensure that the code adheres to the PEP 8 style and is written in Python 3.4.3, with all files being executable and ending with a new line. The project is aimed at handling characters in UTF-8, which can vary in length from 1 to 4 bytes. The data set provided will be represented as a list of integers, where each integer represents 1 byte of data, and I focus on handling the 8 least significant bits of each integer. Through this project, I aim to ensure the accurate validation of UTF-8 encoded characters and their compliance with the specified requirements.

## Tasks

### 0. UTF-8 Validation (mandatory)

Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Usage

```bash
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$

carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$

## Repository

- GitHub repository: [alx-interview](https://github.com/chibwesamuel/alx-interview)
- Directory: 0x04-utf8_validation
- File: 0-validate_utf8.py


