from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.services.auth import auth

def create():
    event = {
    # 'summary': 'Google I/O 2022',
    # 'location': '800 Howard St., San Francisco, CA 94103',
    # 'description': 'A chance to hear more about Google\'s developer products.',
    # 'start': {
    #     'dateTime': '2022-12-25T09:00:00-07:00',
    #     'timeZone': 'America/Los_Angeles',
    # },
    # 'end': {
    #     'dateTime': '2022-12-25T17:00:00-07:00',
    #     'timeZone': 'America/Los_Angeles',
    # },
    # 'recurrence': [
    #     'RRULE:FREQ=DAILY;COUNT=2'
    # ],
    # 'attendees': [
    #     {'email': 'lpage@example.com'},
    #     {'email': 'sbrin@example.com'},
    # ],
    # 'reminders': {
    #     'useDefault': False,
    #     'overrides': [
    #     {'method': 'email', 'minutes': 24 * 60},
    #     {'method': 'popup', 'minutes': 10},
    #     ],
    # },
    }

    event = {
        'summary': '',
        'start': {},
        'end': {}
    }

    print('\nstarting create()...\n')
    try:
        creds = auth()
        service = build('calendar', 'v3', credentials=creds)
        event['summary'] = input('Event name: ')
        event['start']['dateTime'] = input('Event start time YYYY-MM-DDTHH:MM:SS-HH:MM: ')
        event['end']['dateTime'] = input('Event end time YYYY-MM-DDTHH:MM:SS-HH:MM: ')
        timezone = input('Event timezone (format like: America/Los Angeles): ')
        event['start']['timeZone'] = timezone
        event['end']['timeZone'] = timezone
        event['location'] = input('Event location (optional): ')
        event['description'] = input('Event description (optional): ')

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    create()
