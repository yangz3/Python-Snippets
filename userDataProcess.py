import csv
import pylab as P
from numpy import arange,array,ones#,random,linalg
from os import listdir
import numpy as np
import csv
import math
from pylab import plot,show
from scipy import stats
from pylab import *

fnList = listdir("./rawData/")
print fnList

Time_noneFeedbacks = 0
Time_linePhysicalLeadingEdge = 0
Time_linePhysicalCenter = 0
Time_linePhysicalBackground = 0
Time_lineTTLeadingEdge = 0
Time_lineTTCenter = 0
Time_lineTTBackground = 0
Time_lineTTFill = 0

Counter_noneFeedbacks = 0
Counter_linePhysicalLeadingEdge = 0
Counter_linePhysicalCenter = 0
Counter_linePhysicalBackground = 0
Counter_lineTTLeadingEdge = 0
Counter_lineTTCenter = 0
Counter_lineTTBackground = 0
Counter_lineTTFill = 0

errorCounter1 = 0
errorCounter2 = 0
errorCounter3 = 0
errorCounter4 = 0
errorCounter5 = 0
errorCounter6 = 0
errorCounter7 = 0
errorCounter9 = 0


Time_linePhysicalFill = 0
Counter_linePhysicalFill = 0
errorCounter8 = 0

for fn in fnList:
    if fn.endswith(".csv"):
        with open("./rawData/" + fn, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            for row in reader:
                if row[19] == "NoneFeedbacks":
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_noneFeedbacks +=1
                        Time_noneFeedbacks += int(row[8])
                    else:
                        errorCounter1 +=1
                        

                elif row[19] == "LinePhysicalLeadingEdge":
           
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_linePhysicalLeadingEdge +=1
                        Time_linePhysicalLeadingEdge += int(row[8])
                    else:
                        errorCounter2 +=1
                    
                elif row[19] == "LinePhysicalBackground":
          
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_linePhysicalBackground += 1
                        Time_linePhysicalBackground += int(row[8])
                    else:
                        errorCounter3 +=1
                    
                elif row[19] == "LinePhysicalCenter":

                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_linePhysicalCenter +=1
                        Time_linePhysicalCenter += int(row[8])
                    else:
                        errorCounter4 +=1

                elif row[19] == "LineTTLeadingEdge":
           
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_lineTTLeadingEdge +=1
                        Time_lineTTLeadingEdge += int(row[8])
                    else:
                        errorCounter5 +=1
                    
                elif row[19] == "LineTTBackground":
          
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_lineTTBackground += 1
                        Time_lineTTBackground += int(row[8])
                    else:
                        errorCounter6 +=1
                    
                elif row[19] == "LineTTCenter":

                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_lineTTCenter +=1
                        Time_lineTTCenter += int(row[8])
                    else:
                        errorCounter7 +=1
                        
                elif row[19] == "FillTTTarget":
           
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_lineTTFill +=1
                        Time_lineTTFill += int(row[8])
                    else:
                        errorCounter9 +=1
                        
                elif row[19] == "FillPhysicalTarget":
                    if int(row[7]) == 1 and int(row[6]) == 1: # only compute data when user successed on the first drop trial
                        Counter_linePhysicalFill +=1
                        Time_linePhysicalFill += int(row[8])
                    else:
                        errorCounter8 +=1


Average_noneFeedbacks = Time_noneFeedbacks*1.0/Counter_noneFeedbacks
Average_linePhysicalLeadingEdge =  Time_linePhysicalLeadingEdge*1.0/Counter_linePhysicalLeadingEdge
Average_linePhysicalBackground = Time_linePhysicalBackground*1.0/Counter_linePhysicalBackground
Average_linePhysicalCenter = Time_linePhysicalCenter*1.0/Counter_linePhysicalCenter

Average_lineTTLeadingEdge =  Time_lineTTLeadingEdge*1.0/Counter_lineTTLeadingEdge
Average_lineTTBackground = Time_lineTTBackground*1.0/Counter_lineTTBackground
Average_lineTTCenter = Time_lineTTCenter*1.0/Counter_lineTTCenter

Average_lineTTFill = Time_lineTTFill*1.0/Counter_lineTTFill
Average_linePhysicalFill = Time_linePhysicalFill*1.0/Counter_linePhysicalFill

    
ErrorRate_noneFeedbacks = 1-(Counter_noneFeedbacks/(75.0*9))
ErrorRate_linePhysicalLeadingEdge = 1-(Counter_linePhysicalLeadingEdge/(75.0*9))
ErrorRate_linePhysicalBackground = 1-(Counter_linePhysicalBackground/(75.0*9))
ErrorRate_linePhysicalCenter = 1-(Counter_linePhysicalCenter/(75.0*9))
ErrorRate_lineTTLeadingEdge = 1-(Counter_lineTTLeadingEdge/(75.0*9))
ErrorRate_lineTTBackground = 1-(Counter_lineTTBackground/(75.0*9))
ErrorRate_lineTTCenter = 1-(Counter_lineTTCenter/(75.0*9))
ErrorRate_lineTTFill = 1-(Counter_lineTTFill/(75.0*9))
ErrorRate_linePhysicalFill = 1-(Counter_linePhysicalFill/(75.0*9))


nameList = ["NoneFeedbacks: " , "LinePhysicalLeadingEdge: " ,"LinePhysicalBackground: " , "LinePhysicalCenter: ", \
            "LineTTLeadingEdge: ", "LineTTBackground: " , "LineTTCenter: ", "FillTTTarget: ","FillPhysicalTarget: "]
valueList = [Average_noneFeedbacks,Average_linePhysicalLeadingEdge,Average_linePhysicalBackground,Average_linePhysicalCenter,\
             Average_lineTTLeadingEdge,Average_lineTTBackground,Average_lineTTCenter,Average_lineTTFill,Average_linePhysicalFill]

combineList = zip(nameList, valueList)


print 
print "NoneFeedbacks: " + str(Average_noneFeedbacks)
print "LinePhysicalLeadingEdge: " + str(Average_linePhysicalLeadingEdge)
print "LinePhysicalBackground: " + str(Average_linePhysicalBackground)
print "LinePhysicalCenter: " + str(Average_linePhysicalCenter)
print "LineTTLeadingEdge: " + str(Average_lineTTLeadingEdge)
print "LineTTBackground: " + str(Average_lineTTBackground)
print "LineTTCenter: " + str(Average_lineTTCenter)
print "FillTTTarget: " + str(Average_lineTTFill)
print "FillPhysicalTarget: " + str(Average_linePhysicalFill)
print
print "NoneFeedbacks: " + str(ErrorRate_noneFeedbacks)
print "LinePhysicalLeadingEdge: " + str(ErrorRate_linePhysicalLeadingEdge)
print "LinePhysicalBackground: " + str(ErrorRate_linePhysicalBackground)
print "LinePhysicalCenter: " + str(ErrorRate_linePhysicalCenter)
print "LineTTLeadingEdge: " + str(ErrorRate_lineTTLeadingEdge)
print "LineTTBackground: " + str(ErrorRate_lineTTBackground)
print "LineTTCenter: " + str(ErrorRate_lineTTCenter)
print "FillTTTarget: " + str(ErrorRate_lineTTFill)
print "FillPhysicalTarget: " + str(ErrorRate_linePhysicalFill)


##x1= np.array(xrange(9))
##y1=[Average_noneFeedbacks, Average_linePhysicalLeadingEdge, Average_linePhysicalBackground, Average_linePhysicalCenter,
##    Average_lineTTLeadingEdge, Average_lineTTBackground, Average_lineTTCenter,
##    Average_lineTTFill, Average_linePhysicalFill]
##
##x2= np.array(xrange(9))
##y2=[ErrorRate_noneFeedbacks, ErrorRate_linePhysicalLeadingEdge, ErrorRate_linePhysicalBackground
##, ErrorRate_linePhysicalCenter,ErrorRate_lineTTLeadingEdge, ErrorRate_lineTTBackground, ErrorRate_lineTTCenter, ErrorRate_lineTTFill, ErrorRate_linePhysicalFill]
##
##
##subplot(2,1,1)
##plot(x1,y1,'ro')
##subplot(2,1,2)
##plot(x2,y2,'ro')
##show()
            
