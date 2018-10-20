#File project.py
#Written by: Jonathan Colbert
#Section: 500
#Email: Colbert1500@tamu.edu
#Description: Reads in a log file from the internet and returns informationself.
from urllib.request import urlretrieve
import time
import datetime
from datetime import date
import operator
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = "logfile.log"
urllib.request.urlretrieve(URL_PATH, 'logfile.log')
count = 0;count01 = 0;count02 = 0;count03 = 0
count04 = 0;count05 = 0;count06 = 0;count07 = 0
count08 = 0;count09 = 0;count10 = 0;count11 = 0
count12 = 0;weekcount = 0;daycount = 0
unsuccessful = 0.0;redirected = 0.0
fileNames = {}
errorData = []
years = []
yearcount = 0
infile = open(LOCAL_FILE)
outfile01 = open('Jan.txt', 'w'); outfile02 = open('Feb.txt', 'w')
outfile03 = open('Mar.txt', 'w'); outfile04 = open('Apr.txt', 'w')
outfile05 = open('May.txt', 'w'); outfile06 = open('Jun.txt', 'w')
outfile07 = open('Jul.txt', 'w'); outfile08 = open('Aug.txt', 'w')
outfile09 = open('Sep.txt', 'w'); outfile10 = open('Oct.txt', 'w')
outfile11 = open('Nov.txt', 'w'); outfile12 = open('Dec.txt', 'w')

flag = True
# while(flag):
# #     flag = False
#     try:
for line in (infile):
    count += 1;
    dateFull = re.findall('[-*-].*\[([^:]*)'  , line)
     # fileName = re.findall('"[A-Z]{3,5} (.*) HTTP.+\"',line)
    # statusCode = re.findall("(\d{3}).*/",line)
    # status = str(statusCode)
    # code = status[2]
    # #print(status)
    # if code == '3':
    #    print(code)
     #
     # print("Date: ",dateFull[0])
    dateEdit = str(dateFull)
     # day = dateEdit[0:2]
     # month = dateEdit[3:6]
    year = dateEdit[5:8]
    # if (count == 3):
    # #     print(dateEdit)
    #     print(year)
    # years.append(year)
    # #print(years[count-1])
    # yearS = (years[count-2])
    # #print(yearS)
    # if yearS == '1994':
    #     print("yay")
    # if yearS != year:
    #     print("ya")
    # if (years[count - 1]) != '1994':
    #     print(count - 1)
    #     yearcount += 1
    #     print (years[count-1])

    #print(month)
    if (year == "Jan"):
        outfile01.write(line); count01 += 1
    elif (year == "Feb"):
        outfile02.write(line); count02 += 1
    elif (year == "Mar"):
        outfile03.write(line); count03 += 1
    elif (year == "Apr"):
        outfile04.write(line); count04 += 1
    elif (year == "May"):
        outfile05.write(line); count05 += 1
    elif (year == "Jun"):
        outfile06.write(line); count06 += 1
    elif (year == "Jul"):
        outfile07.write(line); count07 += 1
    elif (year == "Aug"):
        outfile08.write(line); count08 += 1
    elif (year == "Sep"):
        outfile09.write(line); count09 += 1
    elif (year == "Oct"):
        outfile10.write(line); count10 += 1
    elif (year == "Nov"):
        outfile11.write(line); count11 += 1
    elif (year == "Dec"):
        outfile12.write(line); count12 += 1
    else:
        errorData.append(line)
############################################################################
    if bool(re.match('.*[3][0-9][0-9]',line)):
    	redirected += 1
    elif bool(re.match('.*[4][0-9][0-9]',line)):
    	unsuccessful += 1
    else:
    	errorData.append(line)
#     except IndexError:
#         errorData.append(line)
# flag = False
#really should of naked that better
file = line.split(" ")
for i in range(len(file)):
	if file[i] == '"GET' and i+1 < len(file):
		filename = file[i+1]
		if filename in fileNames:
			fileNames[filename] += 1
		else:
			fileNames[filename] = 1
# For instance,
#
# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(1))
#
# sorted_x will be a list of tuples sorted by the second element in each tuple. dict(sorted_x) == x.
#
# And for those wishing to sort on keys instead of values:
#
# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(0))
#
# In Python3 since unpacking is not allowed [1] we can use
#
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_by_value = sorted(x.items(), key=lambda kv: kv[1])
sorted_Names = sorted(fileNames.items(),key = operator.itemgetter(1))

outfile01.close();outfile02.close();outfile03.close()
outfile04.close();outfile05.close();outfile06.close()
outfile07.close();outfile08.close();outfile09.close()
outfile10.close();outfile11.close();outfile12.close()
infile.close()

print("1.Total requests:           %d"%count)
print("January:                    ",count01)
print("February:                   ",count02)
print("March:                      ",count03)
print("April:                      ",count04)
print("May:                        ",count05)
print("June:                       ",count06)
print("July:                       ",count07)
print("August:                     ",count08)
print("September:                  ",count09)
print("October:                    ",count10)
print("November:                   ",count11)
print("December:                   ",count12)
print("Average requests per week:    %d"%((count/2)/52))
print("Average requests per day:      %d"%((count/2)/365))
print("3.Unsuccessful attempts:        %d%%"%(unsuccessful/count*100))
print("4.Redirected requests:          %d%%"%(redirected/count*100))
print("5.Most requested file:   ", sorted_Names[-1])
print("6.Many files were requested only once. To many to list in a proper manner. ")
