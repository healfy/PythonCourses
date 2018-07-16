def task_1(array1):
    return {i for i in array1 if i % 2 == 0 and i != 0}


def task_2(array2):
    return dict([[i[0], [a for a in i]]for i in array2])


def task_3(array3):
    return sorted(list(set([b for i in array3 for a in i for b in a])), reverse=True)


def task_4(date1, date2):

    from datetime import datetime, timedelta
    assert isinstance(date1, datetime) and isinstance(date2, datetime)
    if isinstance(date1, datetime) and isinstance(date2, datetime):
        days = abs((date1 - date2)).days
        seconds = (date1 - date2).seconds
        minutes = seconds / 60
        hours = minutes / 60
        weeks = days // 7
        if date1.year - date2.year != 0:
            y = (date1.year - date2.year) * 12 + (date1.month - date2.month)
            if date1.month - date2.month > 0:
                number_of_month = y
                return number_of_month
            elif date1.month - date2. month < 0:
                number_of_month = y - 1
                return number_of_month
            elif date1.month == date2.month:
                if date1.day - date2.day > 0:
                    number_of_month = y
                    return number_of_month
                elif date1.day - date2.day < 0:
                    number_of_month = y - 1
                    return number_of_month
                elif date1.day == date2.day:
                    if date1.hour - date2.hour > 0:
                        number_of_month = y
                        return number_of_month
                    elif date1.hour - date1.hour < 0:
                        number_of_month = y - 1
                        return number_of_month
                    elif date1.hour - date1.hour == 0:
                        if date1.minute - date2.minute > 0:
                            number_of_month = y
                            return number_of_month
                        elif date1.minute - date2.minute < 0:
                            number_of_month = y - 1
                            return number_of_month
                        elif date1.minute - date2.minute == 0:
                            if date1.second - date2.second >= 0:
                                number_of_month = y
                                return number_of_month
                            elif date1.second - date2.second < 0:
                                number_of_month = y - 1
                                return number_of_month
        else:
            if date1.month - date2.month > 0:
                if date1.day - date2.day > 0:
                    if date1.hour - date2.hour > 0:
                        if date1.minute - date2.minute > 0:
                            if date1.second - date2.second >= 0:
                                number_of_month = date1.month - date2.month
                                return number_of_month
                else:
                    return 0
            else:
                return 0
        return seconds,days,minutes,hours,weeks