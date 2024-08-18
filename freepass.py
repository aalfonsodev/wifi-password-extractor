import subprocess
import os

# Create a file
password_file = open('passwords.txt', "w")
password_file.write("Check the passwords below:\n\n")
password_file.close()

# Lists
wifi_files = []
wifi_name = []
wifi_password = []

# Use Python to execute this Windows command as if it were being executed from CMD
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

# Grab current directory
path = os.getcwd()

# Do the magic
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if '<name>' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if '<keyMaterial>' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)

# Write the results to the passwords.txt file
with open('passwords.txt', 'a') as password_file:
    for i in range(len(wifi_name)):
        password_file.write(f"Wi-Fi Name: {wifi_name[i]}\nPassword: {wifi_password[i]}\n\n")


