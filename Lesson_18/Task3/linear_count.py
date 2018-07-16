from datetime import datetime


def writer(array):
    result = []
    for number in array:
        result.append(number ** (10**6))
    return result


start_time = datetime.now()

print(writer([6, 7, 8, 9]))

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))
