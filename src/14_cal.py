"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
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

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

args = sys.argv

if len(args) == 1:
  month = datetime.today().month
  year = datetime.today().year
  calendar.prmonth(year, month)
elif len(args) == 2:
  month = int(args[1])
  year = datetime.today().year
  calendar.prmonth(year, month)
elif len(args) == 3:
  month = int(args[1])
  year = int(args[2])
  calendar.prmonth(year, month)
else:
  print("ERROR")

# today = datetime.now()
# current_month = today.month
# current_year = today.year
# time = today.time()

# tc = calendar.TextCalendar(calendar.SUNDAY)

# valid_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# if len(args) == 1:
#   tc.prmonth(current_year, current_month)
# elif len(args) == 2:
#   print(type(args[1]))
#   if(int(args[1]) == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12):    
#     print('this passed the if statment')
#     month_input = int(args[1])
#     tc.prmonth(current_year, month_input)
#   else:
#     print("This format is not recognized. Try: '14_cal.py month year'")
# elif len(args) == 3:
#   month_input = int(args[1])
#   year_input = int(args[2])
#   tc.prmonth(year_input, month_input)
# else:
#   print("This format is not recognized. Try: '14_cal.py month year'")