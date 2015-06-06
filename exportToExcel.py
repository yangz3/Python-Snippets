from os import listdir
import csv
import math


timeNoneFeedbacks = [] 
timeLinePhysicalLeadingEdge = [] 
timeLinePhysicalBackground = [] 
timeLinePhysicalCenter = [] 
timeLineTTLeadingEdge = [] 
timeLineTTBackground = [] 
timeLineTTCenter = []
timeFillPhysicalTarget = []
timeFillTTTarget = []

idNoneFeedbacks = [] 
idLinePhysicalLeadingEdge = [] 
idLinePhysicalBackground = [] 
idLinePhysicalCenter = []
idLineTTLeadingEdge = [] 
idLineTTBackground = [] 
idLineTTCenter = []
idFillPhysicalTarget = []
idFillTTTarget = []

fnList = listdir("./rawData/")
print fnList

with open('./filteredExcelFriendlyData/toExcel.csv', 'wb') as csvfile:
    ewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    ewriter.writerow(["subjectiveNum", "distance", "width", "timesOfTrial", "timeUsed", "ID=log2(A/W+1)", "feedbackType"])

    for fn in fnList:
        if fn.endswith(".csv"):
            with open("./rawData/" + fn, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                
                
                count = 0
                for row in reader:
                    ewriter.writerow([fn[0], row[4], row[5], row[7], row[8][1:], math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2), row[19]])
                    
