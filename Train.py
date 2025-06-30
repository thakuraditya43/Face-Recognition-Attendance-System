import os
import numpy as np
import cv2
from PIL import Image,ImageTk
from tkinter import messagebox




class TrainData:
    def __init__(self, root):
        self.root = root
        # print("Training data initialized with root window")


    def train_model(self):
        data_dir=("face_img")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')    # Gray scale image
            imageNP = np.array(img,"uint8")
            # id = int(os.path.split(image)[1].split(('.')[1]))

            filename = os.path.basename(image)
            student_id = filename.split('_')[0]

            try:
                id = int(student_id.replace("IITP", ""))  # Extract numeric part only
            except ValueError:
                print(f"Skipping malformed file: {filename}")
                continue


            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ========= train classifier =========== #
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed!!")



# Note: This module is not meant to be run standalone.
# To execute the training process, run the main application and click the "Train Face Data" button.
