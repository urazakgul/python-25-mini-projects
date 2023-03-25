# Bu proje, kullanıcının bilgisayarından e-posta (Outlook) göndermesine izin veren bir program oluşturmayı içerir.
# (This project involves creating a program that allows the user to send emails (Outlook) from their computer.)

#Python'da Outlook kullanarak mail göndermek için bilgisayarınızda Outlook'un kurulu olması gerekiyor.
#In order to send emails using Outlook in Python, you need to have Outlook installed on your computer.

import win32com.client as client

# Start Outlook
outlook = client.Dispatch('Outlook.Application')

# Create a new email
email = outlook.CreateItem(0)

# Set the recipients
email.To = 'receiver_mail_address'

# Set the subject
email.Subject = 'Test Email'

# Set the body
email.Body = 'Hello,\n\nThis is a test message.'

# Add attachment (optional)
email.Attachments.Add('C:/...')

# Send the email
email.Send()