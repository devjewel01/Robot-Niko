import cv2
import numpy as np
import os
import dlib
from imutils import face_utils
from imutils.face_utils import FaceAligner


detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_aligner = FaceAligner(shape_predictor, desiredFaceWidth=400)

def fun(name,path,MAX_NUMBER_OF_IMAGES):
	video_capture = cv2.VideoCapture(0)


	# path = 'Images/test'
	print(path)
	directory = os.path.join(path, name)
	print(directory)
	if not os.path.exists(directory):
		os.makedirs(directory, exist_ok = 'True')

	number_of_images = 0
	count = 0

	while number_of_images < MAX_NUMBER_OF_IMAGES:
		ret, frame = video_capture.read()

		frame = cv2.flip(frame, 1)

		frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		#faces = face_cascade.detectMultiScale(frame, 1.3, 5)
		faces = detector(frame_gray)
		if len(faces) == 1:
			face = faces[0]
			(x, y, w, h) = face_utils.rect_to_bb(face)
			face_img = frame_gray[y-50:y + h+100, x-50:x + w+100]
			face_aligned = face_aligner.align(frame, frame_gray, face)

			if count == 5:
				num_img = str(number_of_images)
				cv2.imwrite(os.path.join(directory, str(name+num_img+'.jpg')), face_aligned)
				number_of_images += 1
				count = 0
			print(count)
			count+=1
			

		cv2.imshow('Video', frame)

		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break

	video_capture.release()
	cv2.destroyAllWindows()

fun("Ramim","Images/train",8)
fun("Ramim","Images/test",2)

