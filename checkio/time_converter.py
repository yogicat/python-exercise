def time_converter(time):
    hours = int(time[:2])
    suffix = ' a.m.'

    if hours >= 0 and hours < 12:

    return str(hours) + time[2:] + suffix


print(time_converter('14:30'))
print(time_converter('00:00'))
