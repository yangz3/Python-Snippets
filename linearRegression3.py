from numpy import arange,array,ones#,random,linalg
from os import listdir
import numpy as np
import csv
import math
from pylab import plot,show
from scipy import stats
from pylab import *

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
count = 0
countAll = 0
for fn in fnList:
    if fn.endswith(".csv"):
        with open("./rawData/" + fn, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
        
            for row in reader:
                countAll +=1

                if row[19] == "NoneFeedbacks":
                    if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                        timeNoneFeedbacks.append(float(row[8]))
                        idNoneFeedbacks.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1
                                                           

                elif row[19] == "LinePhysicalLeadingEdge":
                    # count sum time
                    if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                        timeLinePhysicalLeadingEdge.append(float(row[8]))
                        idLinePhysicalLeadingEdge.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1                       
                elif row[19] == "LinePhysicalBackground":
                    if int(row[7]) == 1 : # only compute data when user successed on the first drop trial
                        timeLinePhysicalBackground.append(float(row[8]))
                        idLinePhysicalBackground.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1                                
                elif row[19] == "LinePhysicalCenter":
                    if int(row[7]) == 1 : # only compute data when user successed on the first drop trial
                        timeLinePhysicalCenter.append(float(row[8]))
                        idLinePhysicalCenter.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1

                elif row[19] == "LineTTLeadingEdge":
                    # count sum time
                    if int(row[7]) == 1 : # only compute data when user successed on the first drop trial
                        timeLineTTLeadingEdge.append(float(row[8]))
                        idLineTTLeadingEdge.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1             
                elif row[19] == "LineTTBackground":
                    if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                        timeLineTTBackground.append(float(row[8]))
                        idLineTTBackground.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1
                        
                elif row[19] == "LineTTCenter":
                    if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                        timeLineTTCenter.append(float(row[8]))
                        idLineTTCenter.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1

                elif row[19] == "FillPhysicalTarget":
                    if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                        timeFillPhysicalTarget.append(float(row[8]))
                        idFillPhysicalTarget.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1
                        
                elif row[19] == "FillTTTarget":
                    if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                        timeFillTTTarget.append(float(row[8]))
                        idFillTTTarget.append(math.log(((1.0*int(row[4])/int(row[5])) + 1) , 2))
                        count+=1
## put indent to view user's data individually

print count
print countAll

## None  result
x1 = np.array(idNoneFeedbacks)
y1 = timeNoneFeedbacks
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(x1,y1)
line1 = slope1*x1+intercept1

## Pysical  result
x2 = np.array(idLinePhysicalLeadingEdge)
y2 = timeLinePhysicalLeadingEdge
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2,y2)
line2 = slope2*x2+intercept2

x3 = np.array(idLinePhysicalBackground)
y3 = timeLinePhysicalBackground
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(x3,y3)
line3 = slope3*x3+intercept3

x4 = np.array(idLinePhysicalCenter)
y4 = timeLinePhysicalCenter
slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(x4,y4)
line4 = slope4*x4+intercept4

## TT result
x5 = np.array(idLineTTLeadingEdge)
y5 = timeLineTTLeadingEdge
slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(x5,y5)
line5 = slope5*x5+intercept5

x6 = np.array(idLineTTBackground)
y6 = timeLineTTBackground
slope6, intercept6, r_value6, p_value6, std_err6 = stats.linregress(x6,y6)
line6 = slope6*x6+intercept6

x7 = np.array(idLineTTCenter)
y7 = timeLineTTCenter
slope7, intercept7, r_value7, p_value7, std_err7 = stats.linregress(x7,y7)
line7 = slope7*x7+intercept7

## Fill result
x8 = np.array(idFillPhysicalTarget)
y8 = timeFillPhysicalTarget
slope8, intercept8, r_value8, p_value8, std_err8 = stats.linregress(x8,y8)
line8 = slope8*x8+intercept8

x9 = np.array(idFillTTTarget)
y9 = timeFillTTTarget
slope9, intercept9, r_value9, p_value9, std_err9 = stats.linregress(x9,y9)
line9 = slope9*x9+intercept9

print("NoneFeedbacks: " + str(slope1))
print("LinePhysicalLeadingEdge: " + str(slope2))
print("LinePhysicalBackground: " + str(slope3))
print("LinePhysicalCenter: " + str(slope4))
print("LineTTLeadingEdge: " + str(slope5))
print("LineTTBackground: " + str(slope6))
print("LineTTCenter: " + str(slope7))
print("FillPhysicalTarget: " + str(slope8))
print("FillTTTarget: " + str(slope9))

subplot(3,1,1)
plot(x1,line1,'r-',x1,y1,'ro', x2,line2,'g-',x2,y2,'go', x3,line3,'b-',x3,y3,'bo', x4,line4,'m-',x4,y4,'mo')
subplot(3,1,2)
plot(x1,line1,'r-',x1,y1,'ro', x5,line5,'g-',x5,y5,'go', x6,line6,'b-',x6,y6,'bo', x7,line7,'m-',x7,y7,'mo')
subplot(3,1,3)
plot(x1,y1,'ro', x8,line8,'g-',x8,y8,'go', x9,line9,'b-',x9,y9, 'bo', x1,line1,'r-')
show()
