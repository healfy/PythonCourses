import json
import requests
import re
from datetime import datetime


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



