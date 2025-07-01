import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
from time import strftime

class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False, False)

        # Background
        try:
            img_bg = Image.open("sample images/Background image.jpg")
            img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
            self.photo_bg = ImageTk.PhotoImage(img_bg)
            bg_lbl = tk.Label(self.root, image=self.photo_bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.root.config(bg="#f0f0f0")

        # Logo
        try:
            img_logo = Image.open("sample images/IITP Name&Logo.png")
            img_logo = img_logo.resize((500, 115), Image.Resampling.LANCZOS)
            self.photo_logo = ImageTk.PhotoImage(img_logo)
            l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
            l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)
        except:
            pass

        # Title
        lab_title = tk.Label(self.root, 
            text="Help Desk", 
            font=("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"), 
            bg="#1C1C1C", fg="#00FF00")
        lab_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


        # Home Button
        img_Home = Image.open("sample images/home.jpg")
        img_Home = img_Home.resize((55,55), Image.Resampling.LANCZOS)
        self.photo_Home = ImageTk.PhotoImage(img_Home)

        btt_Home=tk.Button(lab_title,
                            image=self.photo_Home,
                            padx=5,pady=5,bd=0,
                            cursor="hand2",
                            command=self.home,
                            bg= "#1C1C1C",
                            activebackground="#1C1C1C",
                            fg= "#00FF00")
        btt_Home.place(relx=0.001,height=55,)

        # Time Clock
        time_lb = tk.Label(lab_title,
            font=("Times New Roman", 15, "bold"), bg="#1C1C1C", fg="#00FF00")
        time_lb.place(relx=0.926, height=55)

        def Time():
            string = strftime('%H:%M:%S\n%p')
            time_lb.config(text=string)
            time_lb.after(1000, Time)
        Time()

        # HelpDesk Feature Buttons
        btn_manual = self.create_button("sample images/manual2.jpg", "User Manual", self.show_user_manual, 0.15, 0.45)
        btn_FAQs = self.create_button("sample images/FAQ.png", "FAQs", self.show_faq_window, 0.385, 0.45)
        btn_about = self.create_button("sample images/about.png", "About", self.show_about_us, 0.62, 0.45)
        btn_chatbot = self.create_button("sample images/chatbot.jpeg", "ChatBot", self.not_ready, 0.855, 0.45)
        btn_rating = self.create_button("sample images/feedback.jpg", "Send Feedback", self.not_ready, 0.15, 0.8)
        btn_suggestion = self.create_button("sample images/suggestion.jpg", "Help us Improve", self.not_ready, 0.385, 0.8)
        btn_contact = self.create_button("sample images/contact.png", "Contact Support", self.openHelp, 0.62, 0.8)
        btn_exit = self.create_button("sample images/exit.jpg", "Exit", self.confirm_exit, 0.855, 0.8)



    # -----------------------------------------------Button Functions-------------------------------------------#

# ------------- button creation function -------------- #
    def create_button(self, image_path, text, command, relx, rely):
        try:
            img = Image.open(image_path).resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            btn = tk.Button(self.root, image=photo, text=text, compound="top",
                            font=("Gabriola", 20, "bold"), bg="#1C1C1C", fg="#00FF00",
                            cursor="hand2", command=command)
            btn.image = photo
            btn.place(relx=relx, rely=rely, anchor="center", width=200, height=245)
        except:
            pass

    def not_ready(self):
        messagebox.showinfo("Info", "This feature is under development.")


    def home(self):
        from main import Face_Recognition_System
        self.clear_window()
        self.app = Face_Recognition_System(self.root)


    def openHelp(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help & Support")
        help_window.geometry("350x200")
        help_window.config(bg="#1c1c1c")
        help_window.grab_set()

        tk.Label(help_window, text="📞 Contact Support", font=("Arial", 14, "bold"),bg="#1c1c1c", fg="#00ff00").pack(pady=10)
        tk.Label(help_window, text="Email: support@faceattend.com", font=("Arial", 12),bg="#1c1c1c" ,fg="#ffffff").pack(pady=5)
        tk.Label(help_window, text="Phone: +91-98xxxxxx10", font=("Arial", 12),bg="#1c1c1c", fg="#ffffff").pack(pady=5)
        ttk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=10)


    def show_user_manual(self):
        manual_win = tk.Toplevel(self.root)
        manual_win.title("User Manual")
        manual_win.geometry("510x500")
        manual_win.configure(bg="#1c1c1c")
        manual_win.resizable(False, False)

        # Frame for Text + Scrollbar
        text_frame = tk.Frame(manual_win, bg="#1c1c1c")
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Text widget
        text_widget = tk.Text(text_frame, wrap="word", font=("Helvetica", 12),
                            bg="#1c1c1c", fg="white", insertbackground="white", borderwidth=0)
        text_widget.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.configure(yscrollcommand=scrollbar.set)

        # Tag styles
        text_widget.tag_configure("step", font=("Helvetica", 12, "bold"), foreground="#00ff00", spacing1=10)
        text_widget.tag_configure("desc", font=("Helvetica", 12), foreground="white", lmargin1=20, lmargin2=20)

        # Manual content
        manual = [
            ("Step 1: Create the MySQL Database",
            "Open your MySQL client and create a database named 'face-recognition-attendance-system'. "
            "Create a table named 'student' with columns: department, course, year, semester, S_ID, Name, batch, roll, gen, dob, email, phn, photo."),

            ("Step 2: Add Student Details",
            "Use the 'Student Details' section in the application to input and save new student records."),

            ("Step 3: Capture Photo Samples",
            "In the application, go to the photo capture section and take face samples using the webcam. "
            "Images will be saved automatically in the 'face_img' directory."),

            ("Step 4: Train Face Data",
            "Once all samples are collected, go to the 'Train Face Data' button and start training. "
            "This generates the 'classifier.xml' model used for recognition."),

            ("Step 5: Open Face Recognition for Attendance",
            "Start the face recognition module. When a trained face is detected, it is recognized and attendance is marked automatically."),

            ("Step 6: Manage Attendance Records",
            "Attendance is saved in 'Attendance.csv'. Use the Attendance Manager window to view, edit, or export records."),
        ]

        # Insert steps into text widget
        for step, desc in manual:
            text_widget.insert("end", step + "\n", "step")
            text_widget.insert("end", desc + "\n\n", "desc")

        text_widget.config(state="disabled")  # Make read-only



    def show_faq_window(self):
        faq_win = tk.Toplevel(self.root)
        faq_win.title("Frequently Asked Questions")
        faq_win.geometry("510x500")
        faq_win.configure(bg="#1c1c1c")
        faq_win.resizable(False, False)

        # Frame for Text + Scrollbar
        text_frame = tk.Frame(faq_win, bg="#1c1c1c")
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Text widget
        text_widget = tk.Text(text_frame, wrap="word", font=("Helvetica", 12),
                            bg="#1c1c1c", fg="white", insertbackground="white", borderwidth=0)
        text_widget.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.configure(yscrollcommand=scrollbar.set)

        # Tag styles
        text_widget.tag_configure("question", font=("Helvetica", 12, "bold"), foreground="#00ff00", spacing1=10)
        text_widget.tag_configure("answer", font=("Helvetica", 12), foreground="white", lmargin1=20, lmargin2=20)

        # FAQ content
        faqs = [
                ("1. What is this system?", 
                "A smart attendance system that uses facial recognition to automatically identify and mark students' presence."),

                ("2. How does face recognition work in this system?", 
                "The system detects faces from a live camera feed, encodes facial features, and matches them against stored data to recognize individuals."),

                ("3. What technologies or libraries are used?", 
                "This system is built using OpenCV, Tkinter (for GUI), MySQL (for data storage), and PIL for image handling."),

                ("4. How is face data trained and used?", 
                "Captured face images are trained using the LBPH (Local Binary Patterns Histogram) algorithm to generate a model used for recognition."),

                ("5. Is the system accurate?", 
                "Yes, it performs with 80%–90% accuracy under good lighting and clear face visibility."),

                ("6. Can it handle multiple faces at once?", 
                "Yes, the system can detect and process multiple faces in a single camera frame."),

                ("7. Where is the attendance data stored?", 
                "Attendance is recorded in a CSV file and can also be stored in a MySQL database for better management and analysis."),

                ("8. Can new students be added to the system?", 
                "Yes, new users can be added by capturing their face images and training the recognition model."),

                ("9. What are some limitations of the system?", 
                "It may struggle with poor lighting, occluded faces, extreme angles, or low-resolution cameras."),

                ("10. Can the system be improved or extended?", 
                "Yes, it can be extended with features like liveness detection, cloud sync, mobile apps, and SMS/email notifications."),
            ]


        # Insert questions and answers with formatting
        for q, a in faqs:
            text_widget.insert("end", q + "\n", "question")
            text_widget.insert("end", a + "\n\n", "answer")

        text_widget.config(state="disabled")  # Make read-only


    def show_about_us(self):
        # Create a top-level window
        about_win = tk.Toplevel(self.root)
        about_win.title("About Us - Face Attendance Recognition System")
        about_win.geometry("800x600")
        about_win.configure(bg="#1c1c1c")
        about_win.resizable(False, False)

        # Title label
        title = tk.Label(about_win, text="About Us", font=("Helvetica", 24, "bold"), bg="#1c1c1c", fg="#00ff00")
        title.pack(pady=20)

        # Main content frame
        content_frame = tk.Frame(about_win, bg="#1c1c1c")
        content_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Left: Image
        try:
            img = Image.open("sample images/about.jpg").resize((250, 400), Image.Resampling.LANCZOS)
            logo_img = ImageTk.PhotoImage(img)
            img_label = tk.Label(content_frame, image=logo_img, bg="#f0f0f0")
            img_label.image = logo_img  # keep reference
            img_label.pack(side="left", padx=10, pady=10)
        except:
            tk.Label(content_frame, text="[Image not found]", bg="#1c1c1c", fg="gray", font=("Helvetica", 12, "italic")).pack(side="left", padx=20)

        # Right: Text info
        info_text = (
            "Face Attendance Recognition System\n"
            "Version: 1.0\n\n"
            "This system uses facial recognition technology to automate and\n"
            "secure the attendance process for institutions and organizations.\n\n"
            "Key Features:\n"
            "- Real-time face detection and recognition\n"
            "- Automatic attendance marking\n"
            "- Data storage and retrieval\n"
            "- Developer and HelpDesk integration\n\n"
            "Developed by: Group-22\n"
            "Project Type: Capstone Project\n"
            "Technology: Python, OpenCV, Tkinter, PIL\n\n"
            "For any support, go to the Help section.\n"
            "© 2025 Face Attendance System. All rights reserved.")

        tk.Label(content_frame, text=info_text, font=("Helvetica", 12), justify="left", bg="#1c1c1c", fg="#ffffff", anchor="nw").pack(side="left", fill="both", expand=True,padx=10)

        # Close button
        ttk.Button(about_win, text="Close", command=about_win.destroy).pack(pady=15)





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




    def confirm_exit(self):
        confirm = messagebox.askyesnocancel("Exit", "Are you sure you want to exit the system?")
        if confirm:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = HelpDesk(root)
    root.mainloop()
