# auto-IP shun system

import csv

# open the csv
c = open('ips.csv','r')

# divide up the csv
o = csv.reader(c)
for r in o:
    print(r)
c.close()

# get current list average priority

# get current list by date, drop older than 30 days

# get new IP info

# check if new ip priority is higher than list average

# if new IP priority is higher than average and date is less than 30 days, add to list
# drop lowest priority if there are more than 10 ips



