from datetime import datetime, timedelta


class Fecha:
    def __init__(self, dateStr, format="%d-%m-%Y"):
        self.date = datetime.strptime(dateStr, format)

    def addDay(self, days):
        self.date = self.date + timedelta(days=days)

    def toString(self, format="%d-%m-%Y"):
        return self.date.strftime(format)

