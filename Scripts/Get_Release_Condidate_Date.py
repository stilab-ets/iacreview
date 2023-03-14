import csv

import sys, ctypes as ct
import re

csv.field_size_limit(int(ct.c_ulong(-1).value // 2))
List_Dates = []
Final_List_Dates = []
Final_List_Dates_Strings = []
Final_List_Dates_NoSpace = []
input = "url to release code review data"
with open(input, 'r', encoding="utf8") as csvinput:
    mycsv = csv.reader(csvinput)
    for col in mycsv:
        # START WITH STABLES BRANCHES

        branch = col[4]
        created = col[5]

        if "stable/release-name" in branch:
            List_Dates.append(created)

for date in List_Dates:
        d = re.findall('.*-.*?-.*\s', date)
        # print(d)
        Final_List_Dates.append(d)
for d in Final_List_Dates:
        Date = " "

        # return string
        Date = Date.join(d)
        # print(Date)
        Final_List_Dates_Strings.append(Date)

    # print(Final_List_Dates_Strings)
for d in Final_List_Dates_Strings:
        nospaces = d.replace(" ", "")
        Final_List_Dates_NoSpace.append(nospaces)

    # print(Final_List_Dates_NoSpace)
    ## SORT dates from old to recent

import datetime

dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in Final_List_Dates_NoSpace]
dates.sort()
sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
print(len(sorteddates))
print(sorteddates)
print(sorteddates[0], sorteddates[-1])