# wifi-password-extractor
- This Python script is designed to extract Wi-Fi profiles and their corresponding passwords from a Windows machine. The script utilizes the netsh command to export Wi-Fi profiles and then parses the generated XML files to retrieve the Wi-Fi names and passwords.

## How It Works

## Creating the Output File:
The script begins by creating a text file named passwords.txt. This file will store the retrieved Wi-Fi names and passwords.

## Executing the netsh Command:
- The script uses the subprocess module to execute the netsh wlan export profile key=clear command. This command exports all saved Wi-Fi profiles on the machine into XML files in the current directory.

## Parsing the XML Files:
- The script scans the current directory for files that start with "Wi-Fi" and end with ".xml".
- It then opens each XML file and reads through the lines to find the Wi-Fi names and passwords.
- Wi-Fi names are found between <name> and </name> tags.
- Wi-Fi passwords are found between <keyMaterial> and </keyMaterial> tags.
- The extracted names and passwords are stored in the wifi_name and wifi_password lists, respectively.

## Writing to the Output File:
- Finally, the script writes the retrieved Wi-Fi names and passwords into the passwords.txt file.

## Requirements:
- This script is designed to run on a Windows machine.
- Python 3.x is required to execute the script.

## Usage
- Clone the repository or download the script.
- Open a terminal or command prompt in the directory containing the script.

## Run the script using Python:
```bash
python wifi_password_extractor.py
```
- The script will create a file named passwords.txt in the same directory with the extracted Wi-Fi names and passwords.

**Disclaimer**
This script is intended for educational purposes only. Use it responsibly and only on networks where you have permission to access the passwords. Unauthorized access to networks is illegal and unethical.

**License**
Feel free to customize further based on your specific needs!
