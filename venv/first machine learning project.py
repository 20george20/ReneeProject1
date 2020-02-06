import csv

datafile = open('Animal-Usage_pg2.csv','r')
datafile2 = open('Animal-UsageNPND.csv', 'r')
datafile3 = open('Animal-UsageWPWD.csv', 'r')
datareader = csv.reader(datafile)
datareader2 = csv.reader(datafile2)
datareader3 = csv.reader(datafile3)

dataWPND = []
dataWPWD = []
dataNPND = []
score = 0

for row in datareader:
    dataWPND.append(row)
for row in datareader2:
    dataNPND.append(row)
for row in datareader3:
    dataWPWD.append(row)
def getScore(row):
    score = int(dataWPND[row][11].replace(",",""))*3 + int(dataWPWD[row][11].replace(",",""))*2 + int(dataNPND[row][11].replace(",",""))
    return score
def getMaxScore():
    max = 0
    for row in dataWPND:
        if getScore(row) > max:
            max = getScore(row)
    return max
def getList():
    list1 = []
    for i in range(1, 54):
        list2 = []
        list2.append(dataNPND[i][0])
        list2.append(getScore(i))
    list1.append(list2)
    list1.sort(key=lambda x:x[1], reverse=True)
    print "The top 10 worst States for animal testing are listed below"
    for r in range(1, 10):
        print list2[r][1]




