#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime,timedelta
import calendar

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_obj= list()
    i=0
    for each_time in (t1,t2):
        day,date,month,year,time,utc = each_time.split()
        date_form = datetime(int(year),list(calendar.month_abbr).index(month),
                     int(date),int(time[:2]),int(time[3:5]),int(time[-2:]))
        utc_time = timedelta(hours = int(utc[1:3]),minutes= int(utc[-2:]))
        if utc[0] == '+':
            date_form = date_form - utc_time
        else:
            date_form = date_form + utc_time
        date_obj.append(date_form)
        i+=1
    #print(max(date_obj),min(date_obj))
    return str((int(timedelta.total_seconds(max(date_obj) - min(date_obj)))))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
