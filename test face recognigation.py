import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

my_image = face_recognition.load_image_file("C:/Users/risha/Pictures/Camera Roll/WIN_20191108_10_28_10_Pro.jpg")
'#print(my_face)'
#the model tales 128 features as parameter to recognise our image or detect a face
#encodings varies between -1 to 1 for a face
my_face_encoding = face_recognition.face_encodings(my_image)[0]
'#print(my_face_encoding)'

# create arrays of known face encodings and their names

known_face_encodings = [my_face_encoding]
known_face_names = ["rishabh"]

#Initialising some variables

face_locations = []
face_encodings = []
face_names = []

while True:
    #Grab a single frame of video
    ret,frame = video_capture.read()
    frame = cv2.flip(frame,1)

    #Resize frame of video to 1/4  size for faster face recognition processing

    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

    #Convert the image from BGR color (which open cv uses) to rgb color (which face recognition uses)

    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #Find all  the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

    face_names = []

    for face_encoding_var in face_encodings:
        #See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding_var)
        name = "Unknown"

        #IF a match is found in known facce encodings , just use the first one
        if True in matches:
            first_match_index  = matches.index(True)
            name = known_face_names[first_match_index]
        face_names.append(name)
        print(name)
##        k = cv2.waitKey(1)
##        cv2.imshow("Image",frame)
    #Display the results
    #Image processing and by zip we r creating a zip folder for gatehering face location and name
    for(top,left,bottom,right), name in zip(face_locations,face_names):
        top*= 4
        left*= 4
        bottom*= 4
        right*= 4

        #Draw a box around the face
        print("Top : ",top,"Right : ",left,"Bottom : ",bottom,"Left : ",left)
        cv2.rectangle(frame, (left,top), (right,bottom), (0,0,255), 2)

        #Draw a label with a name below the face
        cv2.rectangle(frame, (left,bottom - 35), (right,bottom), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (right+6, bottom-6), font, 1.0, (255,255,255), 1)

    #Display the resulting image
    cv2.imshow('Video', frame)

    #Hit 'q' on keyboARD to quit!
    k = cv2.waitKey(1)
    if k  == ord('q'):
            break
#Rerlease handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

    

