import httplib2
import oauth2client
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools

class Calendar:
    """Stores data to make Google Calendar API happy"""
    secret_path = ""
    application_name = ""
    credentials = ""
    http = ""
    service = ""

    def __init__(self, secret_path, application_name):
        """Instantiate Calendar, keep track of secret path"""
        self.SCOPES = 'https://www.googleapis.com/auth/calendar'
        self.CREDENTIALS_DIR = "credentials/"
        self.secret_path = secret_path
        self.application_name = application_name

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        if not os.path.exists(self.CREDENTIALS_DIR):
            os.makedirs(self.CREDENTIALS_DIR)
        credential_path = os.path.join(self.CREDENTIALS_DIR,'calendar.json')
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.secret_path+'/client_secret.json', self.SCOPES)
            flow.user_agent = self.application_name
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)

        return credentials

    def set_calendar_vars(self):
        self.credentials = self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=self.http)
        print type(self.service)
