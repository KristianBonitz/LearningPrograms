import datetime

def add_gigasecond(moment):
    return moment + datetime.timedelta(seconds=1000000000)
