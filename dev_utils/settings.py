# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

def config():

	USER_MAIL = os.environ.get("USER_MAIL")
	PASSWORD = os.environ.get("PASSWORD")
	IMAP_URL = os.environ.get("IMAP_URL")
	CONTACT_MAIL = os.environ.get("CONTACT_MAIL")

	return {'USER_MAIL':USER_MAIL, 'PASSWORD':PASSWORD, 'IMAP_URL':IMAP_URL, 'CONTACT_MAIL':CONTACT_MAIL}