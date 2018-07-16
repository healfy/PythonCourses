#
import re
import requests

response = requests.get('http://tut.by/')
result = str(response.content)
temp = re.findall(r'<span class="weather">([+-]\d+)', result)
print(temp)