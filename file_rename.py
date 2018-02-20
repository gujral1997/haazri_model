# renames all folders in copied_dataset to sequential whole numbers
import os

FList = os.listdir(os.getcwd())
FListC = FList[0:]

m = 0
for i in FListC:
    fileExtension = os.path.splitext(i)[1]
    os.rename(i,str(m)+fileExtension)
    m = m+1
