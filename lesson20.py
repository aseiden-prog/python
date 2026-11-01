def times_10(number):
    return number * 10
def times_100(number):
    return times_10(times_10(number))
print(times_100(6))