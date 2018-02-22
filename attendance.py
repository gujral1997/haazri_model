import os
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
from PIL import Image
import face_recognition
count = 0
cwd = os.getcwd()+'/copied_dataset'
flag = '[False]'
wd =os.getcwd()+'/images'
List = os.listdir(wd)
for k in range(1,24,1):
    unknown_image = face_recognition.load_image_file(wd+'/'+str(k)+'.jpg')
    FList = os.listdir(cwd)
    FListC = FList[0:]
    for i in FListC:
        new_cwd =cwd+'/'+i
        new_FList = os.listdir(new_cwd)
        new_FListC = new_FList[0:]
        m = 0
        for j in new_FListC:
            test_image=face_recognition.load_image_file(new_cwd+'/'+j)
            test_face_encoding = face_recognition.face_encodings(test_image)[0]
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

            known_faces = [
                test_face_encoding
            ]
            results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
            print (results)
            if (str(results) == '[True]' or m == 1):
                if(str(results) == '[True]'):
                    flag = '[True]'
                break
            m+=1
        if(flag == '[True]'):
            os.system('rm -rf '+cwd+'/'+i)
            flag = '[False]'
            count+=1
            break
print (count)
print("--- %s seconds ---" % (time.time() - start_time))
