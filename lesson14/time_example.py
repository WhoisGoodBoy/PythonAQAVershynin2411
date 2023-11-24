import time
import datetime
'''

a = time.time()

count = 0
while count < 10000000:
    count +=1

time.sleep(3)

finish = time.time()

print(f'execution time = {finish - a}')



print(datetime.datetime.now())
print(datetime.datetime(year=2022, month=9,day=22,hour=4,minute=5,second=2))
today = datetime.datetime.now()
print(today.day)
print(today.year)
monday = datetime.date(2023, 11,20)
monday_datetime = datetime.datetime(2023,11,20)
print(monday.weekday())
time_now = datetime.time(20,22,50)
print(time_now.hour)
five_days_delta = today - monday_datetime
print(five_days_delta)
five_days_in_a_future = today+five_days_delta
print(five_days_in_a_future)
ten_days_delta = datetime.timedelta(days=10,hours=5)
ten_days_in_the_future = today + ten_days_delta
print(ten_days_in_the_future)
print(five_days_in_a_future>ten_days_in_the_future)
print(today<ten_days_in_the_future)
print(ten_days_delta>five_days_delta)
start = datetime.datetime.now()
count = 0
while count < 10000000:
    count +=1
finish = datetime.datetime.now()
print(finish-start)
'''
finish = datetime.datetime.now()
timestamp_now = finish.timestamp()
print(timestamp_now)
timestamp_1_day_delta = 86400
tomorrow_timestamp = timestamp_now+timestamp_1_day_delta
tomorrow = datetime.datetime.fromtimestamp(tomorrow_timestamp)
print(tomorrow)
formated_time = datetime.datetime.strptime('2023-24-11 21:06:59', '%Y-%d-%m %H:%M:%S')
print(formated_time)
formated_time = formated_time-datetime.timedelta(10)
ten_days_before = formated_time.strftime('%d/%m/%Y, %H:%M:%S')
print(ten_days_before)

formatted_am_time = formated_time.strftime('%d/%m/%y, %I:%M:%S:%p')
print(formatted_am_time)



