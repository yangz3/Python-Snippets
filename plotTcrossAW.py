import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
timeNoneFeedbacks = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width
timeLinePhysicalLeadingEdge = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width
timeLinePhysicalBackground = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width
timeLinePhysicalCenter = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width

errorRateNoneFeedbacks = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width
errorRatePhysicalLeadingEdge = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width
errorRatePhysicalBackground = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width
errorRatePhysicalCenter = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 5 distances * 3 width


with open('./XiyangData/LinesNone.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        
        if row[19] == "NoneFeedbacks":
            indexDistance = int(row[4])/128 - 1 #0-4
            indexWidth = int(math.log(int(row[5])/25,2)) #0-2
            
            if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                timeNoneFeedbacks[indexDistance][indexWidth] += int(row[8][1:])
            else:
                errorRateNoneFeedbacks[indexDistance][indexWidth] += 1
                

        elif row[19] == "LinePhysicalLeadingEdge":
            indexDistance = int(row[4])/128 - 1 #0-4
            indexWidth = int(math.log(int(row[5])/25,2)) #0-2

            # count sum time
            if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                timeLinePhysicalLeadingEdge[indexDistance][indexWidth] += int(row[8][1:])

            # count number of error
            else: 
                errorRatePhysicalLeadingEdge[indexDistance][indexWidth] +=1


        elif row[19] == "LinePhysicalBackground":
            indexDistance = int(row[4])/128 - 1 #0-4
            indexWidth = int(math.log(int(row[5])/25,2)) #0-2
            
            if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                timeLinePhysicalBackground[indexDistance][indexWidth] += int(row[8][1:])
            else:
                errorRatePhysicalBackground[indexDistance][indexWidth] +=1

        elif row[19] == "LinePhysicalCenter":
            indexDistance = int(row[4])/128 - 1 #0-4
            indexWidth = int(math.log(int(row[5])/25,2)) #0-2
            
            if int(row[7]) == 1: # only compute data when user successed on the first drop trial
                timeLinePhysicalCenter[indexDistance][indexWidth] += int(row[8][1:])
            else:
                errorRatePhysicalCenter[indexDistance][indexWidth] +=1


## time need to divide 5 and error rate need to divide 75 ##
for row in xrange(5):
    for col in xrange(3):
        timeNoneFeedbacks[row][col] = timeNoneFeedbacks[row][col]/5.0
        timeLinePhysicalLeadingEdge[row][col] = timeLinePhysicalLeadingEdge[row][col]/5.0
        timeLinePhysicalBackground[row][col] = timeLinePhysicalBackground[row][col]/5.0
        timeLinePhysicalCenter[row][col] = timeLinePhysicalCenter[row][col] /5.0
        errorRateNoneFeedbacks[row][col] = errorRateNoneFeedbacks[row][col] / 75.0
        errorRatePhysicalLeadingEdge[row][col] = errorRatePhysicalLeadingEdge[row][col] / 75.0
        errorRatePhysicalBackground[row][col] = errorRatePhysicalBackground[row][col] / 75.0
        errorRatePhysicalCenter[row][col] = errorRatePhysicalCenter[row][col] / 75.0

timeNoneFeedbacks_draw = []
timeLinePhysicalLeadingEdge_draw = []
timeLinePhysicalBackground_draw = []
timeLinePhysicalCenter_draw = []


errorRateNoneFeedbacks_draw = []
errorRatePhysicalLeadingEdge_draw  = []
errorRatePhysicalBackground_draw  = []
errorRatePhysicalCenter_draw  = []

for row in xrange(5):
    for col in xrange(3):
        timeNoneFeedbacks_draw.append(timeNoneFeedbacks[row][col])
        timeLinePhysicalLeadingEdge_draw.append(timeLinePhysicalLeadingEdge[row][col])
        timeLinePhysicalBackground_draw.append(timeLinePhysicalBackground[row][col])
        timeLinePhysicalCenter_draw.append( timeLinePhysicalCenter[row][col])
        errorRateNoneFeedbacks_draw.append(errorRateNoneFeedbacks[row][col])
        errorRatePhysicalLeadingEdge_draw.append(errorRatePhysicalLeadingEdge[row][col])
        errorRatePhysicalBackground_draw.append(errorRatePhysicalBackground[row][col])
        errorRatePhysicalCenter_draw.append(errorRatePhysicalCenter[row][col])


## plot ##
# evenly sampled time at 200ms intervals
t = np.arange(0., 15., 1.)

print len(t)
print len(timeNoneFeedbacks_draw)

# red dashes, blue squares and green triangles
plt.subplot(2,1,1)
plt.plot(t, timeLinePhysicalLeadingEdge_draw, '-gs', t, timeLinePhysicalBackground_draw, '-bs', t, timeLinePhysicalCenter_draw, '-ys', t, timeNoneFeedbacks_draw, '-rs', linewidth=2.0, label = "timeUsed")
plt.subplot(2,1,2)
plt.plot(t, errorRatePhysicalLeadingEdge_draw, '-gs', t, errorRatePhysicalBackground_draw, '-bs', t, errorRatePhysicalCenter_draw, '-ys', t, errorRateNoneFeedbacks_draw, '-rs', linewidth=2.0, label = "errorRate")
plt.show()




            
            
