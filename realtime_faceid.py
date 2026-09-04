
#
import cv2

#
import face_recognition

#
known_image = face_recognition.load_image_file(
	"faces/11/1.jpg"
)

#
known_encoding = face_recognition.face_encodings(
	known_image
)[0]

# Open webcam
cap = cv2.VideoCapture(0)

process_this_frame = True


while True:
	ret, frame = cap.read()

	if not ret:
		print("Failed to capture frame")
		break

	# Shrink image to 1/4 size
	if process_this_frame:
		small_frame = cv2.resize(
			frame,
			(0,0),
			fx = 0.25,
			fy = 0.25
		)



	# Convert BGR -> RGB
	rgb_frame = cv2.cvtColor(
		frame,
		cv2.COLOR_BGR2RGB
	)

	# Find faces
	face_locations = face_recognition.face_locations(
		rgb_frame
	)

	# Generate encodings
	face_encodings = face_recognition.face_encodings(
		rgb_frame,
		face_locations
	)

	# Check each face found
	for (top, right, bottom, left),  live_encoding in zip(face_locations, face_encodings):


		matches = face_recognition.compare_faces(
			[known_encoding],
			live_encoding
		)

		distance = face_recognition.face_distance(
			[known_encoding],
			live_encoding
		)[0]

		# Green for access granted
		if matches[0]:
			color = (0, 255, 0)
			label = f"ACCESS GRANTED"
			print(f"ACCESS GRANTED | Distance: {distance:.4f}")

		# Red for access denied
		else:
			color = (0, 0, 255)
			label = f"ACCESS DENIED"
			print(f"ACCESS DENIED | Distance: {distance:.4f}")


		padding = 40

		# Draw face box
		cv2.rectangle(
			frame,
			(left - padding, top - padding),			# point 1 = upper-left corner
			(right + padding, bottom + padding),			# point 2 = lower-right corner 
			color,
			2
		)


		# Draw label background
		cv2.rectangle(
			frame,
			(left - padding, bottom - padding),
			(right + padding, bottom + padding),
			color,
			cv2.FILLED
		)

		# Draw Text
		cv2.putText(
			frame,
			label,
			(left + 6, bottom - 8),
			cv2.FONT_HERSHEY_SIMPLEX,
			0.6,
			(255, 255, 255),
			1
		)


		cv2.putText(
			frame,
			f"Dist: {distance:.4f}",
			(left + 6, bottom + 8),
			cv2.FONT_HERSHEY_SIMPLEX,
			0.5,
			(255, 255, 255),
		)

	# Only process every other frame
	process_this_frame = not process_this_frame

	cv2.imshow("FaceID",frame)

	if cv2.waitKey(1) == 27:
		break


cap. release()
cv2.destroyAllWindows()


