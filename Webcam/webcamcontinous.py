import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frameT
    ret, frame = cap.read()


    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(10)
    cv2.imwrite('test.jpeg',frame)


# When everything done, release the capture


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
    face_locations = face_recognition.face_locations(image)

    i = 1
    os.system('mkdir images')
    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save('images/'+str(i)+'.jpg')
        i = i+1
        # pil_image.show() # To save the image

    ###################################

    import os
    import time
    import MySQLdb
    db= MySQLdb.connect(host="localhost", user="root",passwd="klo", db="haazriLogin")
    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    from PIL import Image
    import face_recognition
    count = 0
    cwd = os.getcwd()+'/copied_dataset'
    flag = '[False]'
    wd =os.getcwd()+'/images'
    List = os.listdir(wd)
    print(wd)
    print(List)
    files=len(List)
    print(files)

    for k in range(1,files+1,1):
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
                try:
                    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
                except:
                    pass

                known_faces = [
                    test_face_encoding
                ]
                results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
                print (results)
                if (str(results) == '[True]' or m == 1):
                    if(str(results) == '[True]'):
                        print("i=",i)
                        id=i
                        flag = '[True]'
                        cur = db.cursor()
                        cur.execute("""UPDATE student SET Status='true' WHERE id=%s""",(id))
                        db.commit()
                    break
                m+=1
            if(flag == '[True]'):
                os.system('rm -rf '+cwd+'/'+i)
                flag = '[False]'
                count+=1
                break
    print (count)
    os.system('rm -rf '+wd)
    print("--- %s seconds ---" % (time.time() - start_time))
cap.release()
cv2.destroyAllWindows()
