import datetime

class ScheduleTime():

    TIMEZONE = "PST"

    def __init__(self, hour:int, minute:int):
        self.time = datetime.datetime.combine(datetime.datetime.today(), datetime.time(hour, minute))
        self.time -= datetime.timedelta(hours=1, minutes=15)
    
    def __iter__(self):
        return self

    def __next__(self):
        self.time += datetime.timedelta(hours=1,minutes=15)
        lower = self.time
        upper = self.time + datetime.timedelta(hours=1, minutes=15)
        return f"{lower.strftime('%I:%M%p' + ' ' + self.TIMEZONE)}-{upper.strftime('%I:%M%p' + ' ' + self.TIMEZONE)}"