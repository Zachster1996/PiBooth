""" 
Enka High School Make Club
PhotoBooth Core Functions Class 
"""

import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.multiport import MIMEMultiport
from email.mime.application import MIMEApplication
import email.encoders as encoders

def load_config(config_file):
	config_file_stream = open(config_file, 'r')
	config_entries = config_file_stream.readlines()
	config_file_stream.close()
	return config_entries

def take_picture(delay, file_name):
	os.system("raspistill -n -t %(delay) -o %(file_name)" % locals())
	
def send_email(options):
	msg = MIMEMultipart()
	msg['Subject'] = options['subject']
	msg['From'] = options['from']
	msg['To'] = options['to']
	# TODO: add message code

	attachment_file = open(options['attachment_filename'], 'rb')
	attachment = MIMEApplication(attachment_file.read())
	attachment_file.close()

	attachment.add_header('Conent_disposition', 'attachment; filename="%s"' % options['attachment_filename'])
	msg.attach(part)
	server = smtplib.SMTP(options['SMTP'])
	server.starttls()
	server.login(options['username'], options['password'])
	server.sendmail(options['from'], options['to'], msg.as_string())
	server.quit()

