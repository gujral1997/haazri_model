import face_recognition
import os

# Load the jpg files into numpy arrays
test_image = face_recognition.load_image_file("images/1.jpg")

i =0
while True:
    unknown_image = face_recognition.load_image_file("dataset/"+str(i)+".jpg")


    test_face_encoding = face_recognition.face_encodings(test_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    known_faces = [
        test_face_encoding
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    print (results)
    i = i + 1
    if (str(results) == '[True]'):
        break
