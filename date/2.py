from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
x = date.today()
tomorrow = date.today() + timedelta(days=1)
print(yesterday)
print(x)
print(tomorrow)