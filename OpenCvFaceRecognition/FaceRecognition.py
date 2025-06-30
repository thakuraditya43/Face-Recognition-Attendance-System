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




    # ========face recognition ========================
        from pyexpat import features

        import mysql
        from tqdm import tk

        def face_recog(self):
            def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predicted = classifier.predict(gray_image[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host="localhost", username="root", password="Test@123",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Roll from student where id=" + str, (id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("select Roll from student where id=" + str, (id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("select Dep from student where id=" + str, (id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    if confidence > 77:
                        cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{d}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                                    3)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "unknown Face", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, y]

                return coord

            def recognize(img, clf, faceCascade):
                coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "face", clf)
                return img

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                image = recognize(img.clf, faceCascade)
                cv2.imshow("Welcome TO face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break
                    viedo_cap.release()
                    cv2.destroyAllWindows()

        if __name__ == "__main__":
            root = tk
            obj = face_recog(root)
            root.mainloop()

# Note: This module is not meant to be run standalone.
# To use the face recognition training, run the main application and click the "Face Detector" button.

