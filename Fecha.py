from datetime import datetime, timedelta


class Fecha:
    # Wrapper of date. It has util methods for dates
    # Receive a date as String. Lets specify format
    def __init__(self, date_str, date_format="%Y-%m-%d %H:%M:%S"):
        self.date = datetime.strptime(date_str, date_format)

    # add_day: int -> None
    # add a day in the date. It can be negative
    def add_day(self, days):
        self.date = self.date + timedelta(days=days)

    def to_string(self, date_format="%d-%m-%Y"):
        return self.date.strftime(date_format)
