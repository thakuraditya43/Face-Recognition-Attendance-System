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
        self.create_icon_button("sample images/home.jpg", lab_title, self.home, 0.001)

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
        self.create_button("sample images/manual2.jpg", "User Manual", self.unavailable, 0.15, 0.45)
        self.create_button("sample images/FAQ.png", "FAQs", self.show_faqs, 0.385, 0.45)
        self.create_button("sample images/about.png", "About", self.open_about_us, 0.62, 0.45)
        self.create_button("sample images/chatbot.jpeg", "ChatBot", self.not_ready, 0.855, 0.45)
        self.create_button("sample images/feedback.jpg", "Send Feedback", self.not_ready, 0.15, 0.8)
        self.create_button("sample images/suggestion.jpg", "Help us Improve", self.not_ready, 0.385, 0.8)
        self.create_button("sample images/contact.png", "Contact Support", self.openHelp, 0.62, 0.8)
        self.create_button("sample images/exit.jpg", "Exit", self.confirm_exit, 0.855, 0.8)

    def create_icon_button(self, path, parent, command, relx):
        try:
            img = Image.open(path).resize((55, 55), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            btt = tk.Button(parent, image=photo, bd=0, cursor="hand2", command=command,
                            activebackground="#1C1C1C", bg="#1C1C1C")
            btt.image = photo
            btt.place(relx=relx, height=55)
        except:
            pass

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

    def unavailable(self):
        msg = messagebox.askretrycancel("404 Error!", "Temporarily unavailable.\nPlease try again later.")
        if msg:
            self.unavailable()

    def home(self):
        from main import Face_Recognition_System
        self.clear_window()
        self.app = Face_Recognition_System(self.root)

    def confirm_exit(self):
        confirm = messagebox.askyesnocancel("Exit", "Are you sure you want to exit the system?")
        if confirm:
            self.root.destroy()

    def toggle_fullscreen(self):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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
        ttk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=10)

    def show_faqs(self):
        faq_text = (
            "Face Recognition Attendance System - FAQs\n"
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

    def open_about_us(self):
        about_win = tk.Toplevel(self.root)
        AboutUs(about_win)

class AboutUs:
    def __init__(self, root):
        self.root = root
        self.root.title("About Us - Face Attendance Recognition System")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        title = tk.Label(self.root, text="About Us", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        try:
            img = Image.open("logo.png").resize((100, 100), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo_img, bg="#f0f0f0").pack()
        except:
            pass

        info = (
            "Face Attendance Recognition System\n"
            "Version: 1.0\n\n"
            "This system uses facial recognition technology to automate and\n"
            "secure the attendance process for institutions and organizations.\n\n"
            "Key Features:\n"
            "- Real-time face detection and recognition\n"
            "- Automatic attendance marking\n"
            "- Data storage and retrieval\n"
            "- Developer and HelpDesk integration\n\n"
            "Developed by: Aditya Kumar & Team\n"
            "Project Type: School Project\n"
            "Technology: Python, OpenCV, Tkinter, PIL\n\n"
            "For any support, go to the Help section.\n"
            "© 2025 Face Attendance System. All rights reserved."
        )

        tk.Label(self.root, text=info, font=("Helvetica", 12), justify="left", bg="#f0f0f0", fg="#222").pack(padx=30, pady=10, anchor="w")

        ttk.Button(self.root, text="Close", command=self.root.destroy).pack(pady=10)

# Test run
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpDesk(root)
    root.mainloop()
