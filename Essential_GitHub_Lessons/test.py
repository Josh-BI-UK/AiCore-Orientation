from datetime import timedelta, date
import datetime as dt
from dateutil.relativedelta import relativedelta

hrs_in_day = 24
dt_today = date.today() 
dt_birthday = dt.date(1987,2,17)

delta_today_bday = relativedelta(dt_today, dt_birthday)

days_from_birthday = dt_today - dt_birthday


yrs_lived = delta_today_bday.years
mths_lived = yrs_lived * 12
days_lived = days_from_birthday.days
hrs_lived = (days_lived * hrs_in_day)

print(f"Hours Lived: {hrs_lived:,}\n")
print(f"Days Lived: {days_lived:,}\n")
print(f"Months Lived: {mths_lived:,}\n")
print(f"Years Lived: {yrs_lived:,}\n")
print(f"Life Time: {delta_today_bday.years} years, {delta_today_bday.months} months, {delta_today_bday.days} days\n")
