import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime


datetimepath = "faces"
images = []
class_name = []
my_list = os.listdir(path)

for cl in my_list:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    class_name.append(os.path.splitext(cl)[0])


def encode_faces(image):
    encoded_faces = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encoded_faces.append(encode)
    return encoded_faces


# encode_list = encode_faces(images)
print("Encoding Complete")


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


cap = cv2.VideoCapture(0)


# while True:
#     success, img = cap.read()
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#     faces_cur_frame = face_recognition.face_locations(img)
#     encode_cur_frame = face_recognition.face_encodings(img, faces_cur_frame)
#
#     for encode_face, face_loc in zip(encode_cur_frame, faces_cur_frame):
#         matches = face_recognition.compare_faces(encode_list, encode_face)
#         face_dis = face_recognition.face_distance(encode_list, encode_face)
#         match_index = np.array(face_dis)
#
#         # if matches[match_index]:
#         #     name = class_name[match_index].upper()
#         #     print(name)
#         #     y1, y2, x1, x2
#
#     cv2.imshow('cap', img)
#     cv2.waitKey(1)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(small_frame)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(, face_encodings)
            name = "unknown"

        # face_names = []
        # for face_encoding in face_encodings:
        #     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        #     name = "unknown"

            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = matches[first_match_index]
            #     print(first_match_index)

            # /
    process_this_Frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


