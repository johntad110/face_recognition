import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime


cap = cv2.VideoCapture(0)

# john = face_recognition.load_image_file("faces/john.jpg")
# john_encoding = face_recognition.face_encodings(john)[0]
#
# yidu = face_recognition.load_image_file("faces/yid.jpg")
# yidu_encoding = face_recognition.face_encodings(yidu)[0]
#
# dibo = face_recognition.load_image_file("faces/dibo.JPG")
# dibo_encode = face_recognition.face_encodings(dibo)[0]

known_face_encodings = []
known_face_names = []
path = 'faces'
images = []
my_list = os.listdir(path)

for cl in my_list:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    known_face_names.append(os.path.splitext(cl)[0])
print("Here are the names:", known_face_names, "I have this much images:", len(images))
print("This are the images", len(images))

known_face_encodings_t = []

for img in images:
    cv2.imshow("win_name", img)
    print("Img shown")
    encode_t = face_recognition.face_encodings(img)[0]
    print("Encoding successful")
    known_face_encodings_t.append(encode_t)
    face_loc = face_recognition.face_locations(img)[0]
    cv2.rectangle(img, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 0, 255))
    # cv2.imshow("I got the face", img)
    # cv2.waitKey(1)

print("lets see if this is true:", len(known_face_encodings_t))
# matches = face_recognition.compare_faces(known_face_encodings, john_encoding)
# face_distances = face_recognition.face_distance(known_face_encodings_t, john_encoding)
# best_match_index = np.argmin(face_distances)
# if matches[best_match_index]:
#     name = known_face_names[best_match_index]


def encode_faces(image):
    encoded_faces = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encoded_faces.append(encode)
    return encoded_faces, print('encoding list finished')


# encoding_known_faces = encode_faces(images)
# known_face_encodings.append(encoding_known_faces)
# print("I encode this much face:", len(encoding_known_faces))


def mark_attendance(names):
    with open('attendace.csv', 'r+') as f:
        mtdatalist = f.readlines()
        name_list = []
        for line in mtdatalist:
            entry = line.split(',')
            name_list.append(entry[0])
        if names not in name_list:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{names},{dtstring}')


# 'full_name_list' in this case is known_face_names
def absent_students(full_name_list):
    with open('attendace.csv', 'r') as f:
        a_line = f.readlines()
    for a_name in a_line:
        if a_name not in full_name_list:
            with open('absent.csv', 'r+') as ab:
                ab.writelines(f'\n{a_name}')
        else:
            pass


# for the vid
face_locations = []
face_encodings = []
face_names = []
process_this_Frame = True


while True:
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_Frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(small_frame)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings_t, face_encoding)
            name = "Unknown"
            print("I think this one matches", matches)

            if True in matches:
                index_true = matches.index(True)
                t_n_f_img = os.listdir(path)[index_true]
                name = os.path.splitext(t_n_f_img)[0]
                print(index_true)
                print(name)

            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = matches[first_match_index]
            #     print("Here is first match index", first_match_index)

            # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # best_match_index = np.argmin(face_distances)
            # if matches[best_match_index]:
            #     name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_Frame = not process_this_Frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        mark_attendance(name)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

