from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

from Student import Student


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        # Make the window start in fullscreen mode
        self.root.attributes('-fullscreen', True)
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())



        # Load and Display bg img
        img_bg = Image.open(r"sample images\Background image.jpg")
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), 
                                    Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), 
                        height=self.root.winfo_screenheight())  # Full screen



        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((500, 115), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered



        # title
        Lab_title=Label(self.root, 
                            text="Face Recognition for Secure Attendance Management",
                            font= ("Monotype Corsiva", 40, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
        Lab_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())





        # Student details button
        img_Student = Image.open("sample images/student.webp")
        img_Student = img_Student.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Student = ImageTk.PhotoImage(img_Student)

        btt_student=Button(self.root,image=self.photo_Student,
                                command=self.student_details,relief=RAISED,cursor="hand2")
        btt_student.place(x=100,y=200,width=200,height=200)

        btt_student_1=Button(self.root,
                                text="Student Details",
                                command=self.student_details,
                                cursor="hand2",
                                relief=RAISED,
                                font= ("Gabriola", 25, "bold"),
                                bg= "#1C1C1C",
                                fg= "#00FF00")
        btt_student_1.place(x=100,y=400,width=200,height=40)



        # Detect Face button
        img_DetFace = Image.open("sample images/FaceID-MainArt.jpg")
        img_DetFace = img_DetFace.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_DetFace = ImageTk.PhotoImage(img_DetFace)

        btt_DetFace=Button(self.root,image=self.photo_DetFace,relief=RAISED,cursor="hand2")
        btt_DetFace.place(x=400,y=200,width=200,height=200)

        btt_DetFace=Button(self.root,
                            text="Face Detector",
                            cursor="hand2",
                            relief=RAISED,
                            font= ("Gabriola", 25, "bold"),
                            bg= "#1C1C1C", fg= "#00FF00")
        btt_DetFace.place(x=400,y=400,width=200,height=40)



        # Attendance button
        img_Atten = Image.open("sample images/attendance.png")
        img_Atten = img_Atten.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Atten = ImageTk.PhotoImage(img_Atten)

        btt_Atten=Button(self.root,image=self.photo_Atten,relief=RAISED,cursor="hand2")
        btt_Atten.place(x=700,y=200,width=200,height=200)

        btt_Atten=Button(self.root,
                            text="Attendence",
                            cursor="hand2",
                            relief=RAISED,
                            font= ("Gabriola", 25, "bold"),
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_Atten.place(x=700,y=400,width=200,height=40)



        # Help Chat button
        img_chat = Image.open("sample images/chatbot.jpeg")
        img_chat = img_chat.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_chat = ImageTk.PhotoImage(img_chat)

        btt_chat=Button(self.root,image=self.photo_chat,relief=RAISED,cursor="hand2")
        btt_chat.place(x=1000,y=200,width=200,height=200)

        btt_chat=Button(self.root,
                            text="Help Desk",
                            cursor="hand2",
                            relief=RAISED,
                            font= ("Gabriola", 25, "bold"),
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_chat.place(x=1000,y=400,width=200,height=40)



        # Train Data button
        img_train = Image.open("sample images/train.jpg")
        img_train = img_train.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_train = ImageTk.PhotoImage(img_train)

        btt_train=Button(self.root,image=self.photo_train,relief=RAISED,cursor="hand2")
        btt_train.place(x=100,y=500,width=200,height=200)

        btt_train=Button(self.root,
                            text="Train Data",
                            cursor="hand2",
                            relief=RAISED,
                            font= ("Gabriola", 25, "bold"),
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_train.place(x=100,y=700,width=200,height=40)



        # Photos button
        img_Photo = Image.open("sample images/image.jpg")
        img_Photo = img_Photo.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Photo = ImageTk.PhotoImage(img_Photo)

        btt_Photo=Button(self.root,image=self.photo_Photo,relief=RAISED,cursor="hand2")
        btt_Photo.place(x=400,y=500,width=200,height=200)

        btt_Photo=Button(self.root,
                            text="Photo",
                            cursor="hand2",
                            relief=RAISED,
                            font= ("Gabriola", 25, "bold"),
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_Photo.place(x=400,y=700,width=200,height=40)



        # Developer button
        img_Developer = Image.open("sample images/developer.png")
        img_Developer = img_Developer.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Developer = ImageTk.PhotoImage(img_Developer)

        btt_Developer=Button(self.root,image=self.photo_Developer,relief=RAISED,cursor="hand2")
        btt_Developer.place(x=700,y=500,width=200,height=200)

        btt_Developer=Button(self.root,
                                text="Developer",
                                cursor="hand2",
                                relief=RAISED,
                                font= ("Gabriola", 25, "bold"), 
                                bg= "#1C1C1C", 
                                fg= "#00FF00")
        btt_Developer.place(x=700,y=700,width=200,height=40)



        # Exit button
        img_Exit = Image.open("sample images/exit.jpg")
        img_Exit = img_Exit.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Exit = ImageTk.PhotoImage(img_Exit)

        btt_Exit=Button(self.root,image=self.photo_Exit,relief=RAISED,cursor="hand2")
        btt_Exit.place(x=1000,y=500,width=200,height=200)

        btt_Exit=Button(self.root,
                            text="Exit",
                            cursor="hand2",
                            relief=RAISED,
                            font= ("Gabriola", 25, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00")
        btt_Exit.place(x=1000,y=700,width=200,height=40)





    def toggle_fullscreen(self):
        """Toggle between fullscreen and maximized mode"""
        if self.root.attributes('-fullscreen'):  # If currently fullscreen
            self.root.attributes('-fullscreen', False)  # Exit fullscreen
            self.root.state('zoomed')  # Maximize window to fit screen
        else:
            self.root.attributes('-fullscreen', True)  # Go back to fullscreen





    # -----------------------------------------------Button Functions-------------------------------------------#
    
    # Student details button
    def student_details(self):
        self.clear_window()                 # Clear current UI
        self.app = Student(self.root)       # Load Student UI in the same window









    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()




if __name__ == "__main__":
    root = Tk()
    # root.config(bg="#1C1C1C")
    app = Face_Recognition_System(root)
    root.mainloop()
