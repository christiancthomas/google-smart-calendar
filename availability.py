from auth import auth
import pytz
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
## FreeBusy test


def availability():
    """
    availability returns an object that defines when events are already scheduled during a defined timerange.
    returns dict of a list of dicts for a given calendar
    example: myemail@gmail.com {'busy': [{'start': '2022-12-14T08:00:00-06:00', 'end': '2022-12-14T10:15:00-06:00'}]}
    """
    # TODO: update function for dynamic daterange support

    print('\nstarting availability()...\n')
    try:
        creds = auth()
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

        # This event should be returned by freebusy
        print('\nstarting freebusy...\n')
        tz = pytz.timezone('US/Central')
        the_datetime = tz.localize(datetime.datetime(2022, 12, 14, 0))
        the_datetime2 = tz.localize(datetime.datetime(2022, 12, 24, 0))
        body = {
        "timeMin": the_datetime.isoformat(),
        "timeMax": the_datetime2.isoformat(),
        "timeZone": 'US/Central',
        "items": [{"id": 'christian.thomas@gamesight.io'}]
        }

        eventsResult = service.freebusy().query(body=body).execute()
        cal_dict = eventsResult[u'calendars']
        for cal_name in cal_dict:
            print(cal_name, cal_dict[cal_name])

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    availability()