from datetime import datetime, timedelta
from threading import Timer


class TimeChecker:
    time = datetime.today()
    
    def init(self, time):
        print(1)
        self.time = time
        delay_time = self.find_seconds_to_Next()
        t = Timer(delay_time, self.fertilize)
        t.start()


    def find_seconds_to_Next(self):
        print(2)
        x = datetime.today()
        next_time = x.replace(day=x.day, hour=self.time.hour, minute=self.time.minute, second=self.time.second, microsecond=self.time.microsecond)
        delta_time = next_time - x
        secs = delta_time.total_seconds()
        if (secs < 0):
            secs += timedelta(days=1).total_seconds()
        print(secs)
        return secs


    def fertilize(self):
        print(3)
        print("Fertilize")
        delay_time = self.find_seconds_to_Next()
        t = Timer(delay_time, self.fertilize)
        t.start()
