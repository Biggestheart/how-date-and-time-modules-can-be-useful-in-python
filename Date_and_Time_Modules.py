'''

The program shows the use of date and time module for manipulating and formatting dates and times. 

'''


import time
import datetime

print("Time in seconds since epoch:")
print(time.time())

print("\nCurrent date and time:")
print(datetime.datetime.now())

print("\nFormatting the current date and time using strftime():")
print(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

print("\nOr formatting it like this:")
print(datetime.datetime.now().strftime("%d-%m-%y and %H:%M"))

print("\nCurrent Year:")
print(datetime.datetime.now().strftime("%Y"))

print("\nCurrent Month of the year:")
print(datetime.datetime.now().strftime("%B"))

print("\nWeek number of the year:")
print(datetime.date.today().strftime("%W"))

print("\nWeekday of week:")
print(datetime.date.today().strftime("%w"))

print("\nDay of the year:")
print(datetime.datetime.now().strftime("%j"))

print("\nDay of the month:")
print(datetime.datetime.now().strftime("%d"))

print("\nDay of the week:")
print(datetime.datetime.now().strftime("%A"))

print("\nTime tuple for local time:")
print(time.localtime(time.time()))

print("\n Formatting it in readable form:")
print(time.asctime( time.localtime(time.time()) ))

print("\nWeekday of a certain date:")
my_date=datetime.date(1996,7,19) #yyyy-mm-dd.
print(my_date.strftime("%A"))