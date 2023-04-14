from datetime import timedelta, date
import datetime as dt

hrs_in_day = 24
dt_today = date.today() 
dt_birthday = dt.date(1987,2,17)

days_from_birthday = dt_today - dt_birthday

print(days_from_birthday.days)
hrs_lived = (days_from_birthday.days * hrs_in_day)

print(hrs_lived)
