# References
#   https://youtu.be/JRCJ6RtE3xU
#   https://docs.python.org/3/library/smtplib.html

import smtplib
import csv

CLASS_FILENAME  = 'class.csv'
EMAIL_ADDRESS   = 'johndoe@gmail.com'
EMAIL_PASSWORD  = 'password'
EMAIL_CLIENT    = 'smtp.gmail.com'
EMAIL_SMTP_PORT = 587

# Open the classList file that has been formatted and saved as CSV
with open(CLASS_FILENAME) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name     = row[0] # Column 1, Student Name
        username = row[1] # Column 2, Linux Lab Username
        email    = row[2] # Column 3, Student email
        password = row[3] # Column 4, Initial Password (email address before the @)
        done     = row[4] # This column can be used to skip rows that have already been sent
        
        # Skip over blank lines
        if (username != "") and (done == ""):
            # Print the current student's information to the terminal
            print(f'Name: {name}, Username: {username}, Password: {password}, Email: {email}')
    
            #--- Start Final - Comment out this section until you are ready to send the messages
            # Open the smtp connection
#             with smtplib.SMTP(EMAIL_CLIENT, EMAIL_SMTP_PORT) as smtp:
#             
#                 smtp.ehlo()     # initialize the connection
#                 smtp.starttls() # start encryption
#                 smtp.ehlo()     # initialize encrypted connection
#                 
#                 smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # login
            #--- End Final
            
            # --- Start Debug - For debugging using this smtp connection
            with smtplib.SMTP('localhost', 1025) as smtp:
            # run the following command in the terminal to start the local email host
            #  python3 -m stmpd -c DebuggingServer -n localhost:1025
            #  or
            #  python -m stmpd -c DebuggingServer -n localhost:1025
            # --- End Debug

                # Populate the message
                subject = 'Linux Lab Credentials'
                body = f'Hello {name},\nBelow are your initial username and password for the BYU-I Linux Lab\n'
                body += 'If you have already logged into the Linux Lab, you may ignore this email.\n'
                body += f'Username: {username}\n'
                body += f'Password: {password} or Temple4dpc\n\n'
                body += 'Please contact your instructor with any issues.\n'
                body += 'Do Not replay to this email.\n\n'
                body += 'Best Regards,\nBro. Dennett\n'
                
                # Format the message for sending
                msg = f'Subject: {subject}\n\n{body}'
                
                #send the message
                smtp.sendmail(EMAIL_ADDRESS, email, msg)
    
    
    