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

List_dates = []
List_dates_stables = []
d1 = datetime.date(yyyy, m, dd) # release-candidate date
d2 = datetime.date(yyyy, mm, dd) # release date
diff = d2 - d1
for i in range(diff.days + 1):
    List_dates.append((d1 + datetime.timedelta(i)).isoformat())
print(List_dates)
header = []
data = []
release = "ocata"
finaldata = ["change-ID", "change_number", "url", "project", "branch", "created", "closed", "status",
             "subject", "description", "#revisions", "#reviewers", "#added_lines", "#deleted_lines", "#files",
             "#inline_comments", "#messages", "discreption_length", "duration_in_hours", "files", "messages",
             "at_least_one_puppet", "Phase"
             ]
InputDataset = "link to all code reviews data of OpenStack\\Openstack-data.csv"
Output = "an empty csv file\\"+release+".csv"
with open(InputDataset, 'r', encoding="utf8") as csvinput:
    mycsv = csv.reader(csvinput)
    data.append(finaldata)
    for col in mycsv:
        branch = col[4]
        if "branch" in branch:
            data.append(col)
        elif "stable/"+release in branch:
            created = col[5]
            d = re.search('.*-.*?-.*\s', created).group(0)
            # print(d)
            nospacesdate = d.replace(" ", "")
            if str(nospacesdate) > "release-date format yyyy-mm-dd":
                col.append("post-release")
            if str(nospacesdate) < "release-date format yyyy-mm-dd":
                print(str(nospacesdate))
                col.append("release-candidate")
            data.append(col)
            # print(data)
        elif "master" in branch:
            created = col[5]
            d = re.search('.*-.*?-.*\s', created).group(0)
            for dates in List_dates:
                if dates in d:
                    col.append("development")
                    data.append(col)

# write

# print(data)
with open(Output, 'w+', encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in range(len(data)):
        writer.writerow(data[i])
