import cv2
import face_recognition
import mediapipe as mp
import numpy as np
import os
from datetime import datetime


cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()


def encode_faces(path_to_img):
    encoded_faces = []
    image = face_recognition.load_image_file(path_to_img)
    encode = face_recognition.face_encodings(image)[0]
    encoded_faces.append(encode)
    return encoded_faces


def compare_faces(known_encodings, new_encodings):
    match = face_recognition.compare_faces(known_encodings, new_encodings)
    return match


ef = []
faces_ = os.listdir('faces')
for face in faces_:
    ef.append(encode_faces(f"faces/{face}"))

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    # mat = compare_faces(ef, hena_encoding)
