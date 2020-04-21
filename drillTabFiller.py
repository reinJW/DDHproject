'''drillTabFiller.py

module of functions that fills a drill data table with sufficient data to be used in QGIS for hole
trace plotting ... the base case only uses a very simple 2 line input text file

14-04-2020 imported and methods run in DDHmain

It needs to be expanded ... more methods

'''

import os
import math

def read(aString):
    '''reads a user specified 2 line  text file ... returns list of lists ...'''

    valuList =[]
    fileObj = open(aString,'r')
    lineList = fileObj.readlines()
    lines = len(lineList)
    for i in range(lines):
        items = lineList[i].split()
        valuList.append(items)
    return valuList

def assign(aList):

''' reads 2 lines into a list of lists of parameters ... these are all global variables
there might be an easier way of doing this '''

    # variables from the first line ...
    global name0, order0, fRom0, to0, dist0, dip0, azi0, ddist0, x0, y0, z0

    name0 = aList [0][0]                # string [row] [column]
    order0 = int(aList [0][1])        # integer
    fRom0 = float(aList [0][2])     # float 1 decimal place
    to0 = float(aList [0][3])           
    dist0 = float(aList [0][4])       
    dip0 = float(aList [0][5])        
    azi0 = float(aList [0][6])         
    ddist0 = float(aList [0][7])     
    x0 = float(aList [0][8])            # float to 4 decimal places
    y0 = float(aList [0][9])            
    z0 = float(aList [0][10])          

    # variables from the next line ...
    global name1, order1, fRom1, to1, dist1, dip1, azi1, ddist1, x1, y1, z1

    name1 = aList [1][0]                # string [row] [column]
    order1 = int(aList [1][1])        # integer
    fRom1 = float(aList [1][2])     # float to 1 decimal place
    to1 = float(aList [1][3])           # float to 1 decimal place
    dist1 = float(aList [1][4])       # float to 1 decimal place
    dip1 = float(aList [1][5])        # float to 1 decimal place
    azi1 = float(aList [1][6])         # float to 1 decimal place
    ddist1 = float(aList [1][7])     # float to 1 decimal place
    x1 = float(aList [1][8])            # float to 4 decimal places
    y1 = float(aList [1][9])            # float to 4 decimal places,
    z1 = float(aList [1][10])          # float to 4 decimal places

def check(interval):

    '''trying to set a comsistent interval for plotting  and this only checks to see
    if data needs to be inserted ... thorough checking is required for data integrity  ...

        - for example

        - a hole is missing starting UTM coordinates ...
        - there is no starting azimuth or dip directions ...
        - inconsistencies in hole distance measurements '''
    
    if fRom1 > fRom0 + interval:
        return True
    else:
        return False

def count(interval):
    start = to0
    end = fRom1
    numInt = 1
    while start < end:
        start += interval
        numInt += 1
    return numInt

def dipInc(numInt):
    dipIN = float((dip1-dip0)/numInt)   
    return dipIN

def azInc(numInt):
    aziIN = float((azi1-azi0)/numInt)   
    return aziIN

def insert(numInt):

    global tabArray

    tabArray = []
    
    line0 = (name0+', '+str(order0)+', '+str(fRom0)+', '+str(to0)+', '
    +str(dist0)+', '+str(dip0)+', '+str(azi0)+', '+str(round(ddist0,4))+', '
    +str(round(x0,4))+', '+str(round(y0,4))+', '+str(round(z0,4))) # the first given line ...
    tabArray.append(line0)

    '''set the next line starting variables ...'''
    tName =  name0           # string
    tOrder = order0 + 1     # integer
    tFrom = to0                   # float 1 decimal
    tTo = tFrom + 10           # float 1 decimal ... change +10 to variable
    tDist = tTo - tFrom       # float 1 decimal .... 
    tDip = dip0 + dipInc(numInt)
    tAzi = azi0 + azInc(numInt)

    tDelta = round(tDist *  math.cos(math.radians(tDip)),4)
    tx = x0 + round(tDelta * math.sin(math.radians(azi0)),4)
    ty = y0 + round(tDelta * math.cos(math.radians(azi0)),4)
    tz = z0 + round(tDist * math.sin(math.radians(dip0)),4)
   
    for i in range(numInt): # iterates from 0 to 7 = 8 times ... increment the variables
        '''write string here ...'''

        forString = (tName+', '+str(tOrder)+', '+str(tTo)+', '+str(tTo)+', '+str(tDist)+', '+str(round(tDip,1))+', '
                    +str(round(tAzi,1))+', '+str(tDelta)+', '
                    +str(round(tx,4))+', '
                    +str(round(ty,4))+', '
                    +str(round(tz,4))) # round in the calculations?
                    # iterates from 0 to 7 = 8 times

        tabArray.append(forString)

        '''increment variables here ...'''
        tOrder += 1
        tFrom = tTo
        tTo += 10.0
        tDist = tTo - tFrom # the same value

        tx += round(tDelta * math.sin(math.radians(tAzi)),4)
        ty += round(tDelta * math.cos(math.radians(tAzi)),4)
        tz += round(tDist * math.sin(math.radians(tDip)),4)

        tDip += dipInc(numInt+1)
        tAzi += azInc(numInt+1)
        tDelta = round(tDist *  math.cos(math.radians(tDip)), 4) # uses prevoius azi value
        
    line1 = (name1+', '+str(order1+1)+', '+str(fRom1)+', '+str(to1)+', '
    +str(dist1)+', '+str(dip1)+', '+str(azi1)+', '+str(round(ddist1,4))+', '
    +str(round(x1,4))+', '+str(round(y1,4))+', '+str(round(z1,4))) # the last line ...
    tabArray.append(line1)

def outCSV(outFile):
    with open(outFile,'w') as fileObj:
        for line in tabArray:
            fileObj.write('%s\n' % line)
    fileObj.close()
