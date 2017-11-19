#author: Wesam Saleh
#Version: 1.0

import cv2, time #uses open-cv2 to read images
from difflib import SequenceMatcher

img= cv2.imread("Capture.png") #reads in a photo



first_frame = None

video = cv2.VideoCapture(0) 

a=1
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #uses a haarcascade file to detect faces in a photo to increase accuracy


faces=face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)


	



while True:
	check, frame = video.read() #uses webcam to capture images (strong webcam recommended)

	faces1=face_cascade.detectMultiScale(frame,
	scaleFactor=1.1,
	minNeighbors=5)

	cv2.imshow("Color Frame", frame)

	if first_frame is None:
		first_frame = frame
	else:
		pass
	
	match = SequenceMatcher(None, str(faces1), str(faces)).ratio() #uses difflib's sequence matcher to compare the intensites of the photo captured through the webcam and the photo that has been fed through the program earlier
	if(match > .5): #if the accuracy is above .5, then the file can be accessed
		print("Access Granted")
		print("Hello Wesam")
		print(match)
		break
		#NOTE: THERE IS NO ACTUAL FILE, THIS IS JUST AN EXAMPLE OF HOW THIS PROGRAM MAY BE USED
	else:
		print("Your not Wesam!!!!") # otherwise the file may not be accessed 
		print("Your file is still locked. Goodbye!")
		print(match)
		break

		
video.release() #exits the webcam when first frame has been captured
cv2.destroyAllWindows() #destroys all windows


