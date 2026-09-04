

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

#
test_image = face_recognition.load_image_file(
	"faces/11/2.jpg"
)

#
test_encoding = face_recognition.face_encodings(
	test_image
)[0]

#
result = face_recognition.compare_faces(
	[known_encoding], test_encoding
)

#
print(result)
