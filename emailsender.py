import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = <name>
email['to'] = <recipient email>
email['subject'] = <subject>

email.set_content(html.substitute({'name': 'TinTin'}), 'html') #if you want only text use: email.set_content(<message>)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(<email username>, <email password>)
	smtp.send_message(email)
	print('All done')
