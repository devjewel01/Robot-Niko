import cv2
import os
import sys
import dlib
from imutils import face_utils
from imutils.face_utils import FaceAligner


ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..', '..'))
FACES_PATH = os.path.join(ROOT_PATH, 'data', 'faces')

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(os.path.join(ROOT_PATH, 'assets', 'models', 'shape_predictor_68_face_landmarks.dat'))
face_aligner = FaceAligner(shape_predictor, desiredFaceWidth=400)

def capture_faces(name, path, max_images):
	video_capture = cv2.VideoCapture(0)


	directory = os.path.join(path, name)
	print(directory)
	if not os.path.exists(directory):
		os.makedirs(directory, exist_ok=True)

	number_of_images = 0
	count = 0

	while number_of_images < max_images:
		ret, frame = video_capture.read()

		frame = cv2.flip(frame, 1)

		frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = detector(frame_gray)
		if len(faces) == 1:
			face = faces[0]
			(x, y, w, h) = face_utils.rect_to_bb(face)
			face_aligned = face_aligner.align(frame, frame_gray, face)

			if count == 5:
				num_img = str(number_of_images)
				cv2.imwrite(os.path.join(directory, str(name+num_img+'.jpg')), face_aligned)
				number_of_images += 1
				count = 0
			count+=1
			

		cv2.imshow('Video', frame)

		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break

	video_capture.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.exit('usage: capture_faces.py "<person name>"')
	person = sys.argv[1]
	capture_faces(person, os.path.join(FACES_PATH, 'train'), 8)
	capture_faces(person, os.path.join(FACES_PATH, 'test'), 2)
