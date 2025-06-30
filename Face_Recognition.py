import cv2
import os
import numpy as np
import mysql.connector
import csv
from datetime import datetime

    # ========== Face Recognition and Attendance Module ==========
class FaceDetector:
    def __init__(self, root):
        self.root = root
        print("Face detector initialized with root window")

    def detect_face(self):
        attendance_list = []    # List to track already marked attendance in current session


        # Function to mark attendance and store it in a CSV file
        def mark_attendance(student_data):
            filename = "Attendance.csv"
            file_exists = os.path.isfile(filename)
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")
            row = student_data + [date, time, "Present"]

            # Avoid duplicate entries
            if student_data[0] not in [att[0] for att in attendance_list]:
                attendance_list.append(student_data)

                with open(filename, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    if not file_exists:
                        writer.writerow(["S_ID", "Name", "Roll", "Department", "Course", "Semester", "Batch", "Date", "Time", "Status"])
                    writer.writerow(row)


        # Function to draw face boundary and fetch student details from DB
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            # coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
                id, predict = clf.predict(gray_image[y:y+h+10, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Connect to MySQL database
                conn = mysql.connector.connect(host="localhost", username="root", password="P@ssword4SQL",
                                                database="face-recognition-attendance-system")
                my_cursor = conn.cursor()

                student_id = f"IITP{str(id).zfill(3)}"  # Converts 1 → IITP001, 12 → IITP012

                my_cursor.execute(f"SELECT Name, roll, department, course, semester, batch FROM student WHERE S_ID = '{student_id}'")
                data = my_cursor.fetchone()
                conn.close()

                if data and confidence > 77:
                    # Unpack data and display on screen
                    name, roll, department, course, semester, batch = data
                    cv2.rectangle(img, (x-10, y - 60), (x+w+20, y), (0, 255, 0), -1)  # Filled green box
                    cv2.putText(img, f"Name:{name}", (x+5, y - 35),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(0, 0, 0), thickness=1,lineType=cv2.LINE_AA)
                    cv2.putText(img, f"Roll:{roll}", (x+5, y - 20),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(0, 0, 0), thickness=1,lineType=cv2.LINE_AA)
                    cv2.putText(img, f"Department:{department}", (x+5, y - 5),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(0, 0, 0), thickness=1,lineType=cv2.LINE_AA)
                    # Prepare student data and mark attendance
                    student_data = [student_id, name, roll, department, course, semester, batch]
                    mark_attendance(student_data)

                else:
                    # If confidence is low, treat as unknown
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "unknown Face", (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

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
            cv2.imshow("Face Recognition Attendance", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


# Note: This module is not meant to be run standalone.
# To use the face recognition training, run the main application and click the "Face Detector" button.

