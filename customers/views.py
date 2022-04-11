from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def import_contacts(request):
    """
    Uses allauth Google credentials token to make a
    connection to the user Google Contacts and copy
    the details into the Customers model
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    google_token = SocialToken.objects.get(account__user=request.user)
    creds = Credentials(
        token=google_token.token,
        refresh_token=google_token.token_secret,
        client_id=google_token.app.client_id,
        client_secret=google_token.app.secret,
        scopes=SCOPES
        )
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        # else:
        #     flow = InstalledAppFlow.from_client_secrets_file(
        #         'credentials.json', SCOPES)
        #     creds = flow.run_local_server(port=0)
        # # Save the credentials for the next run
        # with open('token.json', 'w') as token:
        #     token.write(creds.to_json())

    try:
        service = build('people', 'v1', credentials=creds)

        # Call the People API
        print('List 10 connection names')
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=10,
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            if names:
                name = names[0].get('displayName')
                print(name)
    except HttpError as err:
        print(err)
