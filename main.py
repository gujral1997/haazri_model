# cp -r /home/johnny/data/work/haazri_model/dataset_original/* /home/johnny/data/work/haazri_model/copied_dataset/
import os
cwd = os.getcwd()+'/copied_dataset/*'
wd = os.getcwd()
os.system('rm -rf '+cwd)
os.system('cp -r '+wd+'/dataset_original/* '+wd+'/copied_dataset/')
os.system('python3 attendance.py')
