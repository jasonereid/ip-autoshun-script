import csv

list = ['var1''var2''var3''var4''var5''var6''var7''']
fields = ['ip','date','priority']

# open the csv to import new ips in read mode
with open('ip-list.csv','r') as ip_List:
    read_List = csv.reader(ip_List)
    for fields in read_List:
        print(fields)
        list = fields
# divide up the csv
#o = csv.reader(c)
#for row in o:
#    print(row)
# close out the csv
#c.close()
print(list)
# get current list average priority
# ip, date, priority
# get current list by date, drop older than 30 days

# get new IP info

# check if new ip priority is higher than list average

# if new IP priority is higher than average and date is less than 30 days, add to list
# drop lowest priority if there are more than 10 ips


