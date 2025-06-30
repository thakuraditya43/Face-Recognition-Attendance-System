import cv2
import os
import numpy as np
import mysql.connector
# from tqdm import tk
# from pyexpat import features

    # ========face recognition ========================
class FaceDetector:
    def __init__(self, root):
        self.root = root
        print("Face detector initialized with root window")

    def detect_face(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
                id, predict = clf.predict(gray_image[y:y+h+10, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="P@ssword4SQL",
                                                database="face-recognition-attendance-system")
                my_cursor = conn.cursor()

                student_id = f"IITP{str(id).zfill(3)}"  # Converts 1 → IITP001, 12 → IITP012

                my_cursor.execute(f"SELECT Name FROM student WHERE S_ID = '{student_id}'")
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute(f"SELECT roll FROM student WHERE S_ID = '{student_id}'")
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute(f"SELECT department FROM student WHERE S_ID = '{student_id}'")
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                if confidence > 77:
                    cv2.rectangle(img, (x-10, y - 60), (x+w+20, y), (0, 255, 0), -1)  # Filled green box
                    cv2.putText(img, f"Name:{n}", (x+5, y - 35),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(0, 0, 0), thickness=1,lineType=cv2.LINE_AA)
                    cv2.putText(img, f"Roll:{r}", (x+5, y - 20),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(0, 0, 0), thickness=1,lineType=cv2.LINE_AA)
                    cv2.putText(img, f"Department:{d}", (x+5, y - 5),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(0, 0, 0), thickness=1,lineType=cv2.LINE_AA)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "unknown Face", (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)

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
            image = recognize(img,clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = tk
#     obj = FaceDetector(root)
#     root.mainloop()

# Note: This module is not meant to be run standalone.
# To use the face recognition training, run the main application and click the "Face Detector" button.

