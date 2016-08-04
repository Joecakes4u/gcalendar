from Event import Event
from Calendar import Calendar

def main():
    """program entrypoint, handles args and objects"""
    calendar = Calendar(".", "Joe's Calendar")
    calendar.set_calendar_vars()
    event = Event()
    event.create(
        calendar.http,
        calendar.credentials,
        calendar.service,
        "Test",
        "Test Location",
        "Test description",
        "2016-08-5T09:09:00:00-07:00",
        "2016-08-5T09:010:00:00-07:00",
        "DAILY",
        "3"
    )
    event.get_events(10, calendar.service)

if __name__ == "__main__":
    main()
