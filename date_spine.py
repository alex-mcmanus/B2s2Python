from datetime import datetime
from datetime import timedelta

start = input('Pick a start date in a proper format or bad things will occur ')
end = input('Pick and end date in proper format or bad things will occur')

start = datetime.strptime(start, "%Y-%m-%d")
end = datetime.strptime(end, "%Y-%m-%d")

while start <= end:
    print(start)
    start = start + timedelta(days=1)