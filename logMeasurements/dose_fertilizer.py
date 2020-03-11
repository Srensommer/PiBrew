from datetime import datetime, timedelta
from threading import Timer


class TimeChecker:
    time = datetime.today()
    # 15 min delay
    timer_max_delay = 60*15
    
    def init(self, time):
        self.time = time
        self.fertilize_time_controller()

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
        t = Timer(self.timer_max_delay, self.fertilize_time_controller)
        t.start()
