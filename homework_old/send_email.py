import smtplib

gmail_user = 'python_courses@fksis.by'
gmail_password = 'python2018course'

sent_from = 'Sender'
to = ['anton@fksis.by', 'dmitry-datsyk@yandex.by']
subject = 'First email'
email_text = 'Message <b>1</b>'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except Exception as error:
    print(error)
