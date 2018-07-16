import asyncio
import sys
from aiohttp import ClientSession
from datetime import datetime
from threading import Thread
import json
import requests
import re
from collections import OrderedDict


start_time = datetime.now()

with open('cities.json', 'r', encoding='utf8') as file1:
    data = json.load(file1)
    result_dict = {}
    for key, value in data.items():
        result = requests.get(value)
        temp = re.findall(r'<div class="temp fact__temp">'
                          r'<span class="temp__value">([+-]?\d+)</span>',
                          result.text)
        result_dict[key] = temp[0]

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

with open('weather.json', 'w', encoding='utf8') as result_file:
    result_file.write(json.dumps(result_dict, ensure_ascii=False, indent=4))


with open('cities.json', 'r', encoding='utf8') as file1:
    data = json.load(file1)
    requests_dict = {}


async def call_url(city, url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            try:
                request_data = await response.text()
                temp1 = re.findall(
                    r'<div class="temp fact__temp">'
                    r'<span class="temp__value">([+-]?\d+)</span>',
                    request_data)
                requests_dict[city] = temp1[0]
            except TimeoutError:
                return url

start_time = datetime.now()

futures = [call_url(city, url) for city, url in data.items()]

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.wait(futures))

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))

result_dict = OrderedDict(sorted(requests_dict.items(), key=lambda t: t[0]))

with open('weather3.json', 'w', encoding='utf8') as result_file:
    result_file.write(json.dumps(result_dict, ensure_ascii=False, indent=4))


class DownloadThread(Thread):

    def __init__(self, cities, url):
        super(DownloadThread, self).__init__()
        self.key = cities
        self.url = url

    def run(self):
        result1 = requests.get(self.url)
        temp2 = re.findall(r'<div class="temp fact__temp">'
                           r'<span class="temp__value">([+-]?\d+)</span>',
                           result1.text)
        requests_dict[self.key] = temp2[0]


def main():
    threads = []
    for cities, url in data.items():
        thread = DownloadThread(cities, url)
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

