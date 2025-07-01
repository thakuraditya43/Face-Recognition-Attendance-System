import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkfont
from PIL import Image,ImageTk
from time import strftime
import os 

from Student import Student
from Face_Recognition import FaceDetector
from Attendance import Attendance
from Train import TrainData
from Developer import DeveloperDetail
from Help import HelpDesk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        # Make the window start in fullscreen mode
        self.root.attributes('-fullscreen', True)
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False,False)



        # Load and Display background image
        img_bg = Image.open(r"sample images\Background image.jpg")
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), 
                                    Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = tk.Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), 
                        height=self.root.winfo_screenheight())  
        bg_lbl.lower()



        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((500, 115), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered



        # title
        lbl_title=tk.Label(self.root, 
                            text="Face Recognition for Secure Attendance Management",
                            font= ("Monotype Corsiva", 38, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 38, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
        lbl_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


        # ========Time==========#
        time_lbl=tk.Label(lbl_title, 
                            
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        time_lbl.place(relx=0.925,height=55)

        def Time():
            string = strftime('%I:%M:%S\n%p')
            time_lbl.config(text=string)
            time_lbl.after(1000, Time)
        Time()


        # ========Date==========#
        date_lbl=tk.Label(lbl_title, 
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
                            
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        date_lbl.place(relx=0.005,height=55,)

        def date():
            string = strftime('%A\n%d-%m-%Y')
            date_lbl.config(text=string)
            # date_lb.after(1000, Time)
            date_lbl.after(60000, date)  # update every minute
        date()



    # -----------------------------------------------Creating Buttons-------------------------------------------#

        # Student details button
        btn_student = self.create_button("sample images/student.webp", 
                                        "Student Details",
                                        self.student_details, 0.15, 0.45)



        # Detect Face button
        btn_DetFace = self.create_button("sample images/FaceID-MainArt.jpg", 
                                        "Face Attendance",
                                        self.detect_face, 0.385, 0.45)
        


        # Attendance button
        btn_Atten = self.create_button("sample images/attendance.png", 
                                    "Attendance Manager",
                                    self.atten_win, 0.62, 0.45)
        


        # Help button
        btn_help = self.create_button("sample images/help.jpg", 
                                        "Help Desk",
                                        self.help_d, 0.855, 0.45)
        


        # Train Data button
        btn_train = self.create_button("sample images/train.jpg", 
                                        "Train Face Data",
                                        self.train_data, 0.15, 0.8)
        


        # Photos button
        btn_Photo = self.create_button("sample images/image.jpg", 
                                        "Photo Gallery",
                                        self.open_gallery, 0.385 , 0.8)
        


        # Developer button
        btn_Developer = self.create_button("sample images/developer.png", 
                                        "Developer Section",
                                        self.developer, 0.62 , 0.8)
        


        # Exit button
        btn_Exit = self.create_button("sample images/exit.jpg", 
                                        "Exit",
                                        self.confirm_exit, 0.855 , 0.8)





    # -----------------------------------------------Button Functions-------------------------------------------#
    
    # Student details button
    def student_details(self):
        self.clear_window()                 # Clear current UI
        self.app = Student(self.root)       # Load Student UI in new window


    # Attendance details button
    def atten_win(self):
        self.clear_window()                 # Clear current UI
        self.app = Attendance(self.root)       # Load Student UI in new window


    # Developer button
    def developer(self):
        self.clear_window()                          # Clear current UI
        self.app = DeveloperDetail(self.root)       # Load Developer UI in new window


    # Help button
    def help_d(self):
        self.clear_window()                          # Clear current UI
        self.app = HelpDesk(self.root)       # Load Help UI in new window


    def detect_face(self):
        self.app = FaceDetector(self.root)
        self.app.detect_face()  # Run the face_recognition method directly


    def train_data(self):
        self.app = TrainData(self.root)
        self.app.train_model()  # Run the training method directly


    def open_gallery(self):
        os.startfile("face_img")


    # Exit Button
    def confirm_exit(self):
        confirm_exit = messagebox.askyesnocancel(
            "Face Recognition Attendance System",
            "Your session seems to be going well.\nAre you sure you want to exit the Face Recognition System?")
        if confirm_exit:
            self.root.destroy()
        else:
            return



# ------------- button creation function -------------- #
    def create_button(self, image_path, text, command, relx, rely):
        img = Image.open(image_path).resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        btn = tk.Button(self.root, image=photo, text=text, compound="top",
                        font=("Gabriola", 20, "bold"), bg="#1C1C1C", fg="#00FF00",
                        cursor="hand2", relief=tk.RAISED, command=command)
        btn.image = photo  # Store a reference
        # btn.place(x=x, y=y, width=200, height=245)
        btn.place(relx=relx, rely=rely, anchor="center", width=200, height=245)





    def toggle_fullscreen(self):
        """Toggle between fullscreen and maximized mode"""
        if self.root.attributes('-fullscreen'):  # If currently fullscreen
            self.root.attributes('-fullscreen', False)  # Exit fullscreen
            self.root.state('zoomed')  # Maximize window to fit screen
        else:
            self.root.attributes('-fullscreen', True)  # Go back to fullscreen



    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    # root.config(bg="#1C1C1C")
    app = Face_Recognition_System(root)
    root.mainloop()


