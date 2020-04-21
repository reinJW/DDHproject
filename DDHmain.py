'''DDHmain.py

module that is the main procedure that imports ...

drillTabFiller.py, and
fileDia.py

that contain methods that open and save user selected files and process data to generate
data that can be plotted in QGIS as drill hole traces on surface and possibly in x-section

only works on a csv file consiting of 2 lines 

NEXT

1. make it work on data in more than 2 lines ... with a header ...
2. need a better data structure ... class  DDHTable?
3. modify drillTabFiller to include more methods ...

'''

import drillTabFiller as dTF        # a module
import fileDia as fD                      # another module               

''' 04-19-2020 ... 62 and I've finally used modules ...

1. create a method to use on data consisting of more than two lines 

2. define Class DDH to instantiate table objects for further processing? '''

## Main ##

fileString = fD.openFile()           # returns path & file string
fileList = dTF.read(fileString)    # reads file selected by user as a list
dTF.assign(fileList)                     # global variable assignment
lines = dTF.count(10)                 # determined number of lines for a 10 m interval
nArray = dTF.insert(lines)         # inserts required lines to complete file
fileString = fD.saveFile()            # returns path and file for user selected output
dTF.outCSV(fileString)                # writes the file
