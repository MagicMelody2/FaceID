
# Import OpenCV
import cv2

# Use camera number 0 to store frame in cap
cap = cv2.VideoCapture(0)


while True:

	# ret -> Did it work?
	# frame -> The actual image
	# Storing is simmiliar to (True, image)
	ret, frame = cap.read()

	# If ret = false, then the image failed
	if not ret:
		print("Failed to capture frame")
		break

	# If ret = true, display the frame in the window "Webcam"
	cv2.imshow("Webcam", frame)

	# Wait one second to exit window if user presses ESC key
	if cv2.waitKey(1) == 27: 
		break


# Shutdown and clean camera connection
cap.release()

# Close the OpenCV window that the program created (Webcam)
cv2.destoryAllWindows()
