import oauth2client
import os
from oauth2client import client
from oauth2client import tools

class Calendar:
"""Stores data to make Google Calendar API happy"""

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    CREDENTIALS_DIR = "credentials/"

    def __init__(self, secret_path, application_name):
    """Instantiate Calendar, keep track of secret path"""
        self.secret_path = secret_path
        self.application_name = application_name

    def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    if not os.path.exists(CREDENTIALS_DIR):
        os.makedirs(CREDENTIALS_DIR)
    credential_path = os.path.join(CREDENTIALS_DIR,'calendar.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(secret_path, SCOPES)
        flow.user_agent = application_name
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials