import cv2
import numpy as np
import face_recognition

imgdibo = face_recognition.load_image_file('faces/dibo.JPG')
imgdibo = cv2.cvtColor(imgdibo, cv2.COLOR_BGR2RGB)
imgmercy = face_recognition.load_image_file('faces/mercy.JPG')
imgmercy = cv2.cvtColor(imgmercy, cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(imgdibo)[0]
encode_dibo = face_recognition.face_encodings(imgdibo)[0]
cv2.rectangle(imgdibo, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)

face_loc_mercy = face_recognition.face_locations(imgmercy)[0]
encode_mercy = face_recognition.face_encodings(imgmercy)[0]
cv2.rectangle(imgmercy, (face_loc_mercy[3], face_loc_mercy[0]), (face_loc_mercy[1], face_loc_mercy[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encode_dibo], encode_mercy)
face_dis = face_recognition.face_distance([encode_dibo], encode_mercy)
print(results, face_dis)
cv2.putText(imgdibo, f'{results} {round(face_dis[0], 2)}', (30, 30), cv2.FONT_ITALIC, 0.5, (255, 0, 255))

cv2.imshow('dibo', imgdibo)
cv2.imshow('mercy', imgmercy)
cv2.waitKey(0)
