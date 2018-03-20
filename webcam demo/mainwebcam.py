import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frameT
    ret, frame = cap.read()


    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('test.jpeg',frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

cwd = os.getcwd()+'/copied_dataset/*'
wd = os.getcwd()
os.system('rm -rf '+cwd)
os.system('cp -r '+wd+'/dataset_original/* '+wd+'/copied_dataset/')

################
from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("test.jpeg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

# print("I found {} face(s) in this photograph.".format(len(face_locations)))
i = 1
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save('images/'+str(i)+'.jpg')
    i = i+1
    # pil_image.show() # To save the image

###################################

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
for k in range(1,2,1):
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
