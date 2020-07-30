from time import sleep
from shared.util.util import timestamp_print
import requests
from subprocess import check_output

post_to_server = True


def wait_for_wifi():
    while True:
        wifi_ip = check_output(['hostname', '-I'])
        if wifi_ip is not None:
            return
        timestamp_print("No internet")
        sleep(5)


class ApiCalls:
    host = 'https://hansenbrew.dk/'

    def __init__(self, url):
        self.url = url

    def post_log_to_server(self, data):
        if post_to_server:
            posted = False
            while not posted:
                wait_for_wifi()
                try:
                    x = requests.post(self.host + self.url, data=data, timeout=10)
                    print(str(x.status_code))
                    posted = True
                    if 200 <= x.status_code < 300:
                        return True
                    return False
                    
                except requests.exceptions.Timeout:
                    timestamp_print("Post to server - timeout")
                except requests.exceptions.RequestException as e:
                    timestamp_print("Post to server - ConnectionError" + e)
        return True
