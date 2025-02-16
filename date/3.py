from datetime import datetime
current_time = datetime.now()
without_microseconds = current_time.replace(microsecond=0)
print(without_microseconds)