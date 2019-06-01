def time_converter(time):
    hours, mins = map(int, time.split(':'))

    hours = hours % 12 if hours % 12 != 0 else 12
    suffix = 'p.m.' if hours >= 12 else 'a.m'

    return f"{hours}:{mins} {suffix}"


print(time_converter('14:30'))
print(time_converter('00:00'))
