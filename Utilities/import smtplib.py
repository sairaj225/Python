import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From']    = "foo@YOUR_DOMAIN_NAME"
msg['To']      = "bar@example.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('postmaster@YOUR_DOMAIN_NAME', '3kh9umujora5')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
