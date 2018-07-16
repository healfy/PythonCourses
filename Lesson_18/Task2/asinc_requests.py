import asyncio
from collections import OrderedDict
from aiohttp import ClientSession
import json
import re
from datetime import datetime

with open('cities.json', 'r', encoding='utf8') as file1:
    data = json.load(file1)
    requests_dict = {}


async def call_url(key, url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            try:
                request_data = await response.text()
                temp = re.findall(
                    r'<div class="temp fact__temp">'
                    r'<span class="temp__value">([+-]?\d+)</span>',
                    request_data)
                requests_dict[key] = temp[0]
            except TimeoutError:
                return url

start_time = datetime.now()

futures = [call_url(key, url) for key, url in data.items()]


loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.wait(futures))

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))

result_dict = OrderedDict(sorted(requests_dict.items(), key=lambda t: t[0]))

with open('weather3.json', 'w', encoding='utf8') as result_file:
    result_file.write(json.dumps(result_dict, ensure_ascii=False, indent=4))
