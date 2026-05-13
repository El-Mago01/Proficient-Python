import csv

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

with open('timesheet.rtf', 'rb') as rtffile:
     content = rtffile.read()


for month in months:
    filename = 'timesheet_' + month + '23.rtf'
    with open(filename, 'wb') as rtffile:
        rtffile.write(content)
