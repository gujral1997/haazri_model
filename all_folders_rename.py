import os

cwd = os.getcwd()
cwd += '/copied_dataset'
FList = os.listdir(cwd)
os.chdir(cwd)
FListC = FList[0:]
n = 0
for j in range(0,len(FListC)):
    new_cwd =cwd+'/'+str(n)
    new_FList = os.listdir(new_cwd)
    new_FListC = new_FList[0:]
    os.chdir(new_cwd)
    m = 0
    for i in new_FListC:
        fileExtension = os.path.splitext(i)[1]
        os.rename(i,str(m)+fileExtension)
        m = m+1
    n=n+1
    os.chdir('..')
    os.chdir(new_cwd)
os.chdir('../..')
