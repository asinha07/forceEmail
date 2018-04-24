import smtplib
import time
import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "YOUR_EMAIL_ID" + ORG_EMAIL
FROM_PWD    = "PASSWORD"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password):
    smtpserver='smtp.gmail.com:587'
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = str(header) + str(message)
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def readmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    date = msg['date']
                    if email_from == 'THE FUCKER"S EMAIL':
                        sendemail(FROM_EMAIL,[to_email_list],email_subject,msg,FROM_EMAIL,FROM_PWD);
                        print 'From : ' + email_from + '\n'
                        print 'Subject : ' + email_subject + '\n'
                        print 'Date: '+date

    except Exception, e:
        print str(e)

if __name__ == 'main':
    readmail()
