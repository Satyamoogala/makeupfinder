import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Press "q" to Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('captured_image.jpg', frame)
            break
    cap.release()
    cv2.destryAllWindows()

capture_image() 

import face_recognition
from sklearn.cluster import KMeans
import cv2

def get_skin_tone(image_path):
    image = face_recognition.load_image_file(image_path)
    face_location = face_recognition.face_locations(image)
    top,right,bottom,left = face_location[0]

    face_image = image[top:bottom, left:right]
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BG2BGR)
    face_image = face_image.reshape((face_image.shape[0]*face_image.shape[1],3))

    kmeans = KMeans(n_clusters=5)
    kmeans.fit(face_image)
    colors = kmeans.cluster_centers_
    return colors

colors = get_skin_tone('captured_iage.jpg')
print(colors)