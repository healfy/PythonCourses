from datetime import datetime
from threading import Thread
import json
import requests
import re
from collections import OrderedDict


class DownloadThread(Thread):

    def __init__(self, cities, url):
        super(DownloadThread, self).__init__()
        self.key = cities
        self.url = url

    def run(self):
        result = requests.get(self.url)
        temp2 = re.findall(r'<div class="temp fact__temp">'
                           r'<span class="temp__value">([+-]?\d+)</span>',
                           result.text)
        requests_dict[self.key] = temp2[0]


def main():
    threads = []
    for key, url in data.items():
        thread = DownloadThread(key, url)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    with open('cities.json', 'r', encoding='utf8') as file1:
        data = json.load(file1)
        requests_dict = {}
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    result_dict = OrderedDict(sorted(requests_dict.items(), key=lambda t: t[0]))
    with open('weather1.json', 'w', encoding='utf8') as result_file:
        result_file.write(json.dumps(result_dict, ensure_ascii=False, indent=4))


