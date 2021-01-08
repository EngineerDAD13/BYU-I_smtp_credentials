# BYU-I_smtp_credentials
Python Script for sending Student's Linux Lab credentials over smtp

This script reads the class.csv file and can send an email to each student with their username and password.

To use the script a valid stmp capable email address, password, smtp server id and port number are needed. 
These values can be populated into the global parameters at the top of the script. 

The committed version of the script is in debug mode and will only send the email messages to a localhost email client.
The localhost email client can be setup using one of the following commands
python3 -m smtpd -c DebuggingServer -n localhost:1025
python -m smtpd -c DebuggingServer -n localhost:1025

Uncomment the line between the #--- Start Final and #--- End Final tags and Comment out the #--- Debug lines to enable sending the emails.

The class.csv needs to be formatted as a csv from the output of classList as run for the class as shown in the class_example.csv.
The first 3 Columns are unchanged.
The 4th column is the password
The 5th column can be used to mark students that have already been sent the email. entering anything into the 5th column will cause that row to be skipped.
