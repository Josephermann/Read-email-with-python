from settings import config
from dev_script import emailLoader, extractFile
import datetime
import os


if __name__ == "__main__":

	params = config()

	date_jour = datetime.datetime.today().strftime('%d-%b-%Y') 
	files_path = os.path.join('..','data_storage','itop')
	emailLoader(dateJ=date_jour,configuration=params, path=files_path)
	extractFile(input_path=files_path)