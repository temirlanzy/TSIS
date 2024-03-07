#Exercise 1(Task 4) Write a Python program to subtract five days from current date.
import datetime
current_datetime = datetime.datetime.now()
five_day_timedelta = datetime.timedelta(days=5)
date_five_days_ago = current_datetime - five_day_timedelta
print(date_five_days_ago)

#Exercise 2(Task 4) Write a Python program to print yesterday, today, tomorrow.
import datetime
now = datetime.datetime.now()
past_date = now - datetime.timedelta(days=1)
future_date = now + datetime.timedelta(days=1)
print("Now:", now)
print("Yesterday:", past_date)
print("Tomorrow:", future_date)

#Exercise 3(Task 4) Write a Python program to drop microseconds from datetime.
import datetime
current_time = datetime.datetime.now()
time_without_microseconds = current_time.replace(microsecond=0)
microseconds = current_time.strftime("%f")
print(time_without_microseconds)
print(microseconds)

#Exercise 4(Task 4) Write a Python program to calculate two date difference in seconds.
import datetime
date_string1 = input()
date_string2 = input()
datetime1 = datetime.datetime.strptime(date_string1, "%Y-%m-%d %H:%M:%S")
datetime2 = datetime.datetime.strptime(date_string2, "%Y-%m-%d %H:%M:%S")
difference_in_seconds = abs((datetime1 - datetime2).total_seconds())
print(difference_in_seconds)