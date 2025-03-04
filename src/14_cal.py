"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

currentMonth = datetime.now().month
currentYear = datetime.now().year


def calendar1(list1=[currentMonth,currentYear]):
    month = currentMonth
    year = currentYear
    if len(list1) == 1:
        month = int(list1[0])
        c = calendar.TextCalendar(calendar.SUNDAY)
        cal = c.formatmonth(year, month)
        print(cal)
    elif len(list1) == 2:
        month = int(list1[0][1])
        year = int(list1[1][:-1])
        c = calendar.TextCalendar(calendar.SUNDAY)
        cal = c.formatmonth(year, month)
        print(cal)



# calendar1([1, 2020])
# calendar1([1])
# calendar1([])
y = []

try:
    y = str(input('month and year (1,2020): ')).split(',')
except SyntaxError:
    print('bad data')


calendar1(y)
