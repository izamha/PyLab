import datetime as dt

# Store today's date in a variable, today
today = dt.date.today()
# Format my own date
yesterday = dt.date(2021, 2, 14)

print(today)
# Get the month of today
print('Year:', today.year, 'Month:', today.month, 'Day:', today.day)
print(f"{yesterday:%A, %B %d %Y}")

# Working with time -- datetime.time()
almost_midnight = dt.time(23, 59, 59, 999999)
print('Almost midnight:', almost_midnight)

# As of now
right_now = dt.datetime.now()
print('Right now', right_now)

'''
Get the timespan
We use the datetime.timedelta()
'''
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day

print('Days in between:', days_between)
