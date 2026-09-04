
# Import computer vision library
import cv2

# OpenCV's face detecotr is called Haar Cascade classifier
# This loads the pre-trainiend detector in an XML file using the file path
# And stores it into the face_cascade
face_cascade = cv2.CascadeClassifier(
	cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Connect to webcam
cap = cv2.VideoCapture(0)

while True:

	# Was image retrieved successfully?
	# Save image
	ret, frame = cap.read()

	# Image not saved
	if not ret:
		break

	# Image saved -> 1. Convert to grayscale
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Image saved -> 2. Detect faces
	# Take the greyscale image and find areas that look like faces
	# The results are stored in faces
	faces = face_cascade.detectMultiScale(
		grey,

		# Controls how much the image is scalled between searches
		scaleFactor = 1.1,

		# confidence should be greater than 5 before saying it's a face
		# Lower number ->  more detection, but potentially more false positives
		# Higher number -> fewer less positives, but might miss some faces
		minNeighbors = 5,

		# Ignore looking for faces that are smaller than 30x30 (widthxheight) pixels
		minSize = (30, 30)
	)

	# Image saved -> 3. Draw green boxes
	# Store x,y w, h coordiantes and draw a bounding box around the coordinates with some buffer size
	for (x, y, w, h) in faces:
		cv2.rectangle(
			frame,				# Image
			(x, y),				# Top-left corner
			(x + w, y + h),			# Top-right corner
			(0, 255, 0),			# Color (green - [B, G, R])
			2				# Thickness
		)

	# Show the result
	cv2.imshow("Face Detection", frame)

	# Check for ESC
	if cv2.waitKey(1) == 27:
		break

# Clean amd close any/all OpenCV windows
cap.release()
cv2.destroyAllWindows()

	# Image saved -> 
