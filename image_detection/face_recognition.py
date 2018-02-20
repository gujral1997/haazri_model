import face_recognition

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("images/1.jpg")
# biden_image = face_recognition.load_image_file("/home/johnny/haazri_model/image_detection/images/1.jpg")
# obama_image = face_recognition.load_image_file("obama.jpg")
# unknown_image = face_recognition.load_image_file("dataset/"+str(i)+".jpg")
i =0
while True:
    unknown_image = face_recognition.load_image_file("dataset/"+str(i)+".jpg")

    # Get the face encodings for each face in each image file
    # Since there could be more than one face in each image, it returns a list of encodings.
    # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    known_faces = [
        biden_face_encoding
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    print (results)
    i = i + 1
    if(results == "[False]"):
        break

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
# results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# print("Is the unknown face a picture of Biden? {}".format(results[0]))
# print("Is the unknown face a picture of Obama? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
