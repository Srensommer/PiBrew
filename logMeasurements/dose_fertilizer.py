import datetime


class TimeChecker:
    last_day_dosed = 0

    def should_fertilize(self):
        t = datetime.datetime.today()
#       if 10 > t.hour > 9 and t.minute and self.last_day_dosed != t.today():
        if 13 < t.hour < 14 and t.minute and self.last_day_dosed != t.today():
            self.last_day_dosed = t.today()
            print ("Fertilize")
            return True
        return False
