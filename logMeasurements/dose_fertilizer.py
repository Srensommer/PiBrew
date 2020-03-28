from datetime import datetime, timedelta
from threading import Timer
import megaApi


class TimeChecker:
    mega: megaApi.MegaApi
    time = datetime.today()
    # 5 min delay
    timer_max_delay = 60*5
    
    def __init__(self, time):
        self.time = time
        self.fertilize_time_controller()

    @classmethod
    def dosing_version(cls, time, mega):
        cls.time = time
        cls.mega = mega

    def fertilize_time_controller(self):
        now = datetime.today()
        next_time = now.replace(
            day=now.day,
            hour=self.time.hour,
            minute=self.time.minute,
            second=self.time.second,
            microsecond=0
        )
        secs = (next_time - now).total_seconds()
        if secs <= self.timer_max_delay:
            if secs < 0:
                secs += timedelta(days=1).total_seconds()
            else:
                t = Timer(self.timer_max_delay, self.fertilize)
                t.start()
                return

        self.wait_longer()

    def wait_longer(self):
        print("wait longer")
        t = Timer(self.timer_max_delay, self.fertilize_time_controller)
        t.start()

    def fertilize(self):
        print("Fertilize")
        if self.mega:
            self.mega.relay_timed(1, 2)
        t = Timer(self.timer_max_delay, self.fertilize_time_controller)
        t.start()
