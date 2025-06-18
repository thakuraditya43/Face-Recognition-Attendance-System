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
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)
        l_lbl.config(anchor="center")

        # title
        lab_title = tk.Label(self.root, 
                            text="Help Desk", 
                            font=("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"), 
                            bg="#1C1C1C", 
                            fg="#00FF00")
        lab_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())

        # Home Button
        img_Home = Image.open("sample images/home.jpg")
        img_Home = img_Home.resize((55, 55), Image.Resampling.LANCZOS)
        self.photo_Home = ImageTk.PhotoImage(img_Home)

        btt_Home = tk.Button(lab_title,
                            image=self.photo_Home,
                            padx=5, pady=5, bd=0,
                            cursor="hand2",
                            command=self.home,
                            activebackground="#1C1C1C",
                            bg="#1C1C1C",
                            fg="#00FF00")
        btt_Home.place(relx=0.001, height=55)

        # Time
        time_lb = tk.Label(lab_title,
                            font=("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
                            bg="#1C1C1C", 
                            fg="#00FF00")
        time_lb.place(relx=0.926, height=55)

        def Time():
            string = strftime('%H:%M:%S\n%p')
            time_lb.config(text=string)
            time_lb.after(1000, Time)
        Time()

        # Buttons
        self.create_button("sample images/manual2.jpg", "User Manual", self.unavailabel, 0.15, 0.45)
        self.create_button("sample images/FAQ.png", "FAQs", self.unavailabel, 0.385, 0.45)
        self.create_button("sample images/about.png", "About", self.unavailabel, 0.62, 0.45)
        self.create_button("sample images/chatbot.jpeg", "ChatBot", self.not_ready, 0.855, 0.45)
        self.create_button("sample images/feedback.jpg", "Send Feedback", self.not_ready, 0.15, 0.8)
        self.create_button("sample images/suggestion.jpg", "Help us Improve", self.not_ready, 0.385, 0.8)
        self.create_button("sample images/contact.png", "Contact Support", self.openHelp, 0.62, 0.8)
        self.create_button("sample images/exit.jpg", "Exit", self.confirm_exit, 0.855, 0.8)

    # Not available functions
    def not_ready(self):
        messagebox.showinfo("Info", "This feature is under development.")

    def unavailable(self):
        msg = messagebox.askretrycancel(title="404 Error!", message="Temporarily unavailabel.\nPlease try again later.")
        if msg:
            self.unavailabel()
        else:
            return

    # Home button
    def home(self):
        from main import Face_Recognition_System
        self.clear_window()
        self.app = Face_Recognition_System(self.root)

    # Exit Button
    def confirm_exit(self):
        confirm_exit = messagebox.askyesnocancel(
            "Face Recognition Attendance System",
            "Your session seems to be going well.\nAre you sure you want to exit the Face Recognition System?")
        if confirm_exit:
            self.root.destroy()
        else:
            return

    # Create buttons
    def create_button(self, image_path, text, command, relx, rely):
        img = Image.open(image_path).resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        btn = tk.Button(self.root, image=photo, text=text, compound="top",
                        font=("Gabriola", 20, "bold"), bg="#1C1C1C", fg="#00FF00",
                        cursor="hand2", relief=tk.RAISED, command=command)
        btn.image = photo
        btn.place(relx=relx, rely=rely, anchor="center", width=200, height=245)

    # Fullscreen toggle
    def toggle_fullscreen(self):
        if self.root.attributes('-fullscreen'):
            self.root.attributes('-fullscreen', False)
            self.root.state('zoomed')
        else:
            self.root.attributes('-fullscreen', True)

    # Clear all widgets
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Help popup function added here
    def openHelp(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help & Support")
        help_window.geometry("350x200")
        help_window.config(bg="#ffffff")
        help_window.grab_set()

        tk.Label(help_window, text="📞 Contact Support", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
        tk.Label(help_window, text="Email: support@faceattend.com", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        tk.Label(help_window, text="Phone: +91-9876543210", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        tk.Label(help_window, text="Developer: Aditya Kumar", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        tk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=10)


    # FAQs function
    def show_faqs(self):
        faq_text = (
            "\nFace Recognition Attendance System - FAQs\n"
            "-------------------------------------------\n"
            "1. What is this system?\n   - An automated system to mark attendance using facial recognition.\n\n"
            "2. How does it work?\n   - Detects, encodes, and compares face features with stored data.\n\n"
            "3. What libraries are used?\n   - OpenCV, face_recognition, Tkinter, PIL, etc.\n\n"
            "4. How accurate is it?\n   - Typically 90%–98% under good conditions.\n\n"
            "5. Is it secure?\n   - Fairly secure but can be improved with liveness detection.\n\n"
            "6. Can it recognize multiple faces?\n   - Yes, in a single frame.\n\n"
            "7. Where is attendance stored?\n   - CSV, Excel, or database like SQLite.\n\n"
            "8. Can new users be added?\n   - Yes, by adding their images and encoding their faces.\n\n"
            "9. Limitations?\n   - Sensitive to lighting, face angles, and image quality.\n\n"
            "10. Can it be extended?\n   - Yes, with cloud, SMS, mobile apps, etc."
        )
        messagebox.showinfo("FAQs", faq_text)



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class AboutUs:
    def __init__(self, root):
        self.root = root
        self.root.title("About Us - Face Attendance Recognition System")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        # Header
        title = tk.Label(self.root, text="About Us", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        # Logo or Image (optional, use your logo if available)
        try:
            img = Image.open("logo.png")  # Replace with your image path
            img = img.resize((100, 100), Image.ANTIALIAS)
            self.logo_img = ImageTk.PhotoImage(img)
            logo_label = tk.Label(self.root, image=self.logo_img, bg="#f0f0f0")
            logo_label.pack()
        except:
            pass  # Skip if image not available

        # System Info
        info = """
Face Attendance Recognition System
Version: 1.0

This system uses facial recognition technology to automate and 
secure the attendance process for institutions and organizations.

Key Features:
- Real-time face detection and recognition
- Automatic attendance marking
- Data storage and retrieval
- Developer and HelpDesk integration

Developed by: Aditya Kumar & Team
Project Type: School Project
Technology: Python, OpenCV, Tkinter, PIL

For any support, go to the Help section.

© 2025 Face Attendance System. All rights reserved.
        """
        info_label = tk.Label(self.root, text=info, font=("Helvetica", 12), justify="left", bg="#f0f0f0", fg="#222")
        info_label.pack(padx=30, pady=10, anchor="w")

        # Close Button
        close_btn = ttk.Button(self.root, text="Close", command=self.root.destroy)
        close_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AboutUs(root)
    root.mainloop()

