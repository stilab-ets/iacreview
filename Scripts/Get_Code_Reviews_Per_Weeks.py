import csv
import os
import re
import sys, ctypes as ct
import re
from itertools import groupby

import pandas
import pandas as pd

csv.field_size_limit(int(ct.c_ulong(-1).value // 2))
import pandas
import pandas as pd

from datetime import date
import datetime

from cffi.backend_ctypes import xrange

Final_List_Dates = []
Final_List_Dates_Strings = []
Final_List_Dates_NoSpace = []
List_days = []
List_weeks = []
List_dates_stables = []
List_Number_Of_CR_IN_Weeks = []
AnsibleFiles = []
FinalAnsibleFiles = []
release = "ocata"
AnsibleFilesList = "link to found IaC files"
with open(AnsibleFilesList, 'r', encoding="utf8") as f:
    # mycsv=next(csv.reader(f))
    mycsv = csv.reader(f)
    for col in mycsv:
        status = col[1]
        if status != "":
            AnsibleFiles.append(status)
# print(AnsibleFiles)
AnsibleFiles.pop(0)
# print(AnsibleFiles)
for file in AnsibleFiles:
    FinalAnsibleFiles.append(file.split("\n"))
# print(FinalAnsibleFiles)
Flat_FinalAnsibleFiles = [item for subfile in FinalAnsibleFiles for item in subfile]
List_Dates = []
data = []
finaldata = []
List_files=[]
List_final_files=[]
d1 = datetime.date(2020, 5, 14) # First CR date in development phase
d2 = datetime.date(2021, 6, 14)  # Last CR date in post-release phase
outputFile = "An empty csv file"+release+".csv"
InputDataset = "link to each release code reviews data\"+release+".csv"
with open(InputDataset, 'r', encoding="utf8") as csvinput:
    mycsv = csv.reader(csvinput)
    ANSIBLE_EXIST = False
    Puppet_EXIST = False
    for col in mycsv:
        branch = col[4]
        files = col[19]
        status = col[7]
        cycle = col[22]
        ID = col[1]
        created = col[5]

        ### TEST IF IAC FILE EXISTS FOR ""ALL"" CR
        pat = r'\'(.*?)\''
        List_Files = re.findall(pat, files)
        ANSIBLE_EXIST = False
        Puppet_EXIST = False
        if List_Files:
            for path in List_Files:
                for i in Flat_FinalAnsibleFiles:
                    ##IF ANSIBLE
                    if i.__contains__(path):
                        # print(i)
                        ANSIBLE_EXIST = True
                        break

                filename, file_extension = os.path.splitext(path)
                if file_extension == ".pp":
                    # print(file_extension)
                    Puppet_EXIST = True
        if ANSIBLE_EXIST == False  and (
                "development" in cycle or "post-release" in cycle or "release-candidate" in cycle) and Puppet_EXIST == False:
                #and ("development" in cycle or "post-release" in cycle or "release-candidate" in cycle):  # and status == "MERGED":

            List_Dates.append(created)

                # i need to add number of file and date of CR together so they will be sorted together. Add them in set
            print(len(List_Files))
            List_files.append(len(List_Files))

print(List_Dates)
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
# print(len(sorteddates))
print(sorteddates)

diff = d2 - d1
# print(diff)
# for i in range(diff.days + 6):
#     List_weeks.append((d1 + datetime.timedelta(i)).isoformat())
# print(List_weeks)
List_weeks.append(d1)
for i in range(diff.days):
    d1 = d1 + datetime.timedelta(days=6)
    List_weeks.append(d1)
    if d1 > d2:
        break
print(List_weeks)
nb = 0
for i in range(len(List_weeks) - 1):
    List_days.clear()
    nb = 0
    value = List_weeks[i:i + 2]
    diff = value[1] - value[0]

    # print(diff, value[1] , value[0])
    for r in range(diff.days + 1):
        List_days.append((value[0] + datetime.timedelta(r)).isoformat())
    # print(value)

    if i > 0:
        List_days.pop(-1)
    # print(List_days)
    for s in List_days:

        for t in sorteddates:
            if t == s:
                # print('yes')
                nb += 1
    List_Number_Of_CR_IN_Weeks.append(nb)
    # print(value)
print(List_Number_Of_CR_IN_Weeks)
List_WEEKS = []
for t in List_weeks:
    List_WEEKS.append(t.isoformat())
print(List_WEEKS)
List_WEEKS.pop(-1)
CRWeeks = pd.DataFrame({'NB_NONIAC_CR_IN_Weeks': List_Number_Of_CR_IN_Weeks})
Weeks = pd.DataFrame({'Weeks': List_WEEKS})
# # pd.concat([Revisions,Reviewer,AddedLines,DeletedLines,Files,InlineComments,Messages,DescriptionLength,TimeToMerge,Churn],axis=1).to_csv(outputFile, index = False)
pd.concat([CRWeeks, Weeks], axis=1).to_csv(outputFile, index=False)
