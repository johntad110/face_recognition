import face_recognition
import cv2


hen = face_recognition.load_image_file("faces/dibo.JPG")
encode = face_recognition.face_encodings(hen)
face_loc = face_recognition.face_locations(hen)[0]
cv2.rectangle(hen, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 0, 255))
face_names = ['dibo']

cv2.rectangle(hen, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
cv2.putText(hen, "dibo", (face_loc[3], face_loc[0]), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)

henm = face_recognition.load_image_file("faces/mercy.JPG")
encodem = face_recognition.face_encodings(henm)
face_locm = face_recognition.face_locations(henm)[0]
cv2.rectangle(henm, (face_locm[3], face_locm[0]), (face_locm[1], face_locm[2]), (0, 0, 255))
face_namesm = ['mercy']

cv2.rectangle(henm, (face_locm[3], face_locm[0]), (face_locm[1], face_locm[2]), (255, 0, 255), 2)
cv2.putText(henm, "mercy", (face_locm[3], face_locm[0]), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)

cv2.imshow("win2", henm)
cv2.imshow("win", hen)
cv2.waitKey(0)
