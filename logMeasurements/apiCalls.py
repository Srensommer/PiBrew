from util import time_stamp_print
import requests

post_to_server = True


class ApiCalls:
    host = 'https://hansenbrew.dk/'

    def __init__(self, url):
        self.url = url

    def post_log_to_server(self, data):
        if post_to_server:
            posted = False
            while not posted:
                try:
                    x = requests.post(self.host + self.url, data=data, timeout=10)
                    posted = True
                    if 200 <= x.status_code < 300:
                        return True
                    return False

                except requests.exceptions.Timeout:
                    time_stamp_print("Post to server - timeout")
                except requests.exceptions.RequestException as e:
                    time_stamp_print("Post to server - ConnectionError", e)
        return True
