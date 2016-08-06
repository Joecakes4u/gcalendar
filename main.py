from Event import Event
from Calendar import Calendar

def main():
    """program entrypoint, handles args and objects"""
    calendar = Calendar(".", "Joe's Calendar")
    calendar.set_calendar_vars()
    event = Event()
    event.create(
        cal=calendar,
        summary="Test",
        location="Test Location",
        description="Test description",
        start_dt="2016-08-06T09:00:00-07:00",
        end_dt="2016-08-06T10:00:00-07:00",
        rec_freq="DAILY",
        rec_count="3"
    )
    event.get_events(10, calendar.service)

if __name__ == "__main__":
    main()
