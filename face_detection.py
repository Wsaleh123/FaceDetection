import cv2, time
from difflib import SequenceMatcher

img= cv2.imread("Capture.png")



first_frame = None

video = cv2.VideoCapture(0)

a=1
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


faces=face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)


	



while True:
	check, frame = video.read()

	faces1=face_cascade.detectMultiScale(frame,
	scaleFactor=1.1,
	minNeighbors=5)

	cv2.imshow("Color Frame", frame)

	if first_frame is None:
		first_frame = frame
	else:
		pass
	
	match = SequenceMatcher(None, str(faces1), str(faces)).ratio()
	if(match > .5):
		print("Access Granted")
		print("Hello Wesam")
		print(match)
		break
		
	else:
		print("Your not Wesam!!!!")
		print("Your file is still locked. Goodbye!")
		print(match)
		break

		
video.release()
cv2.destroyAllWindows()
