# course-python-mega

Application: Static Website

Framework: Flask

Inputs: 
TBD - website_blocker.py, /private/etc/hosts
Outputs: TBD - /private/etc/hosts


Prerequisites:
1. A host file for Mac, must be in: /private/etc/hosts/
2. A host file for Win, must be in: c:\Windows\System32\drivers\etc
3. Getting the script running on a Mac
    a. Since the host file is running in a location where admin permission is needed. Need to run at terminal window.
    b. Open terminal window at the script folder
    c. Type: sudo python3 website_blocker.py
    d. Enter password.
    e. Script should be running.

Description:
This project will update the hosts file on Mac during working hours adding websites that should not be visted. When outside working hours then the websites will be removed and will be accessible.

It will:
- use the datetime oject
- open a text document for read/write
