import requests
import numpy as np
import re


def task_1(array_1, array_2):
    mat1 = np.matrix(array_1, dtype=np.float)
    mat2 = np.matrix(array_2, dtype=np.float)
    a = mat1 + mat2
    b = a.T
    c = np.rot90(mat2, k=3)
    d = b * c
    e = np.matrix([d.max(), d.min()]).mean()
    f = d[1:-1, 1:-1]
    if len(array_1) % 2 == 0:
        g = d[(len(array_1)//2)-1, (len(array_1)//2)-1]
    else:
        g = d[len(array_1)//2, len(array_1)//2]

    return a, b, c, d, e, f, g


def task_2(money):
    url = 'http://www.nbrb.by/API/ExRates/Rates/' + money + '?ParamMode=2'
    result = requests.get(url).json()
    return round(float(1/(result['Cur_OfficialRate']/result['Cur_Scale'])), 2)


def task_3():
    result = requests.get('https://yandex.by/pogoda/minsk')
    temp = re.findall(r'<div class="temp fact__temp">'
                      r'<span class="temp__value">([+-]?\d+)</span>',
                      result.text)
    return int('{}'.format(temp[0]))
