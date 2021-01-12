#-*- coding: utf-8 -*-
import csv
from time import time

from Data.Keyword import keywords
from TotalScan.Save import hash_save
from TotalScan.Search import *
from thread import *

#========Main========
day = input('ex)2020-01-01, Date :')

OPTION_DAYS.append(" fs:"+day+"00:00:00+ fs:"+day+"23:59:59-")

print('''
[+] [Scan Type]
[+] 1) UTF-8(filename) Type Scan
[+] 2) UTF-8 Type + All EML File Type Scan
[+] 3) All Scan
      ''')

OPTION_SCAN_TYPE.append(input('[+] Select Number : '))

#Start_Timer
start = time()

#Thead
Tasker(KeywordSearch, 8, keywords)

#End_Timer
end = time()
print('%.3f seconds' % (end-start))

#Hash Save(.txt)
hash_save()

#Meta Save(.csv)
f_csv = open(CSV_PATH,'w', encoding='utf-8-sig', newline='')
w_csv = csv.writer(f_csv)
for row in RESULT:
    w_csv.writerow(row)
f_csv.close()

print('\nend...')
#====================
