from datetime import datetime 
date1 = datetime.fromisoformat(input("Input date1: "))
date2 = datetime.fromisoformat(input("Input date2: "))
difference = abs((date2 - date1).total_seconds())
print(difference)