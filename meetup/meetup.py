import calendar
import datetime
import regex

def meetup_day(year, month, day, label):
    week = list(calendar.day_name)

    try: delta = int(regex.findall(r'\d', label)[0])
    except IndexError: delta = -1 if label == "last" else 1

    # itermonthdays will return 0's if a day isn't present in a month. We need
    # to remove those 0's from the list!
    for d in filter((0).__ne__, calendar.Calendar().itermonthdays(year, month)):
        if label == "teenth" and (d < 13 or d > 19): continue
        if datetime.date(year, month, d).weekday() == week.index(day):
            date = datetime.date(year, month, d)
            delta -= 1
        if delta == 0: break

    if delta > 0: raise ValueError("Day is not exisiting")
    return date
