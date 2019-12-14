from datetime import date,timedelta
import datetime

today = date.today()
day = today - timedelta(5)
print(day)