from datetime import datetime


def time_stamp_print(string_to_print):
    print("%s: %s" % (datetime.now(), string_to_print))
