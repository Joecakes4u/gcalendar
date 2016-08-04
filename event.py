class Event:
    """Class which handles event generation and list events"""

    def __init__(self):
        """Instantiate Event"""
        import datetime
        import httplib2
        import oauth2client
        from oauth2client import client
        from oauth2client import tools

    def get_events(max_results, service):
        """Gets events by making Calendar API call"""
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        eventsResult = service.events().list(
          calendarId='primary', timeMin=now, maxResults=max_results, singleEvents=True,
          orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        if not events:
          print('No upcoming events found.')
        for event in events:
          start = event['start'].get('dateTime', event['start'].get('date'))
          print(start, event['summary'])

    def create(http, credentials, service, summary, location, description, start_dt, end_dt, rec_freq, rec_count, time_z='America/Los_Angeles'):
        """Create event creation request, make request, confirm request sent"""

        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_dt,
                'timeZone': time_z,
            },
            'end': {
                'dateTime': end_dt,
                'timeZone': time_z,
            },
            'recurrence': [
                'RRULE:FREQ='+rec_freq+';COUNT='+rec_count
            ],
            'attendees': [
                # implement if this is ever necessary. Ex:
                # {'email': 'lpage@example.com'},
                # {'email': 'sbrin@example.com'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        print("Event created: "+str(event.get('htmlLink')))
