import cv2
import os
import numpy as np

# Face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to dataset
DATASET_PATH = 'Image_Dataset'

# Step 1: Load images and train model
def prepare_training_data(path):
    faces = []
    labels = []
    label_map = {}
    current_id = 0

    for person_name in os.listdir(path):
        person_path = os.path.join(path, person_name)
        if not os.path.isdir(person_path):
            continue

        label_map[current_id] = person_name

        for image_file in os.listdir(person_path):
            img_path = os.path.join(person_path, image_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue

            faces_rects = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces_rects:
                face_roi = img[y:y+h, x:x+w]
                faces.append(face_roi)
                labels.append(current_id)

        current_id += 1

    return faces, labels, label_map

print("[INFO] Training model...")
faces, labels, label_map = prepare_training_data(DATASET_PATH)
recognizer.train(faces, np.array(labels))  # 🔥 <--- TRAINING CODE LINE
print("[INFO] Training complete.")

# Step 2: Real-time recognition
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rects = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_rects:
        face_roi = gray[y:y+h, x:x+w]
        label_id, confidence = recognizer.predict(face_roi)

        if confidence < 80:
            name = label_map[label_id]
            text = f"{name} ({round(confidence, 1)}%)"
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
