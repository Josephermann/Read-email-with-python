from imap_tools import MailBox
from imap_tools import MailBox
import os
from settings import config
import rarfile
from pathlib import Path

params = config()

def emailLoader(dateJ:str,configuration:dict, path:str):
    '''
    Cette fonction telecharge les pieces jointes reçues par mail
    params: Elle prend trois parametres, la date du jour, la configuration des adresses mails et le dossier de destination
    return: Elle retourne les pieces jointes dans un dossier specifié en parametre
    '''

    with MailBox(params['IMAP_URL']).login(params['USER_MAIL'],params['PASSWORD']) as mailbox:
        for msg in mailbox.fetch('TEXT "ITOP SERVICE REPORT" ON {}'.format(dateJ)):
            if msg.from_ == params['CONTACT_MAIL']:   
                for att in msg.attachments:
                    print(att.filename, att.content_type)
                    with open('../data_storage/log_file.txt', 'a') as f:
                        f.write(f'\n======== date :{dateJ}========\n content :{att.content_type}\n files name:{att.filename}')

                    with open(os.path.join(path,att.filename), 'wb') as f:
                        f.write(att.payload)


def extractFile(input_path:str):
    
    elements = os.listdir(path=input_path)
    for file in elements:
        if file.endswith('.rar'):
            file_path = os.path.join(input_path,file)
            rar = rarfile.RarFile(file_path)
            rar.extractall(path=input_path)
            del file
            del file_path
            del rar


