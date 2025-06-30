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
        btn_manual = self.create_button("sample images/manual2.jpg", "User Manual", self.unavailable, 0.15, 0.45)
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

    def unavailable(self):
        msg = messagebox.askretrycancel("404 Error!", "Temporarily unavailable.\nPlease try again later.")
        if msg:
            self.unavailable()


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


    def show_faq_window(self):
        faq_win = tk.Toplevel(self.root)
        faq_win.title("Frequently Asked Questions")
        faq_win.geometry("510x500")
        faq_win.configure(bg="#1c1c1c")
        faq_win.resizable(False, False)

        # Scrollable Frame
        canvas = tk.Canvas(faq_win, bg="white", borderwidth=0)
        frame = tk.Frame(canvas, bg="#1c1c1c")
        scrollbar = ttk.Scrollbar(faq_win, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def on_frame_config(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        frame.bind("<Configure>", on_frame_config)

        # FAQ content
        faqs = [
            ("1. What is this system?", "An automated system to mark attendance using facial recognition."),
            ("2. How does it work?", "Detects, encodes, and compares face features with stored data."),
            ("3. What libraries are used?", "OpenCV, face_recognition, Tkinter, PIL, etc."),
            ("4. How accurate is it?", "Typically 90%–98% under good conditions."),
            ("5. Is it secure?", "Fairly secure but can be improved with liveness detection."),
            ("6. Can it recognize multiple faces?", "Yes, in a single frame."),
            ("7. Where is attendance stored?", "CSV, Excel, or database like SQLite."),
            ("8. Can new users be added?", "Yes, by adding their images and encoding their faces."),
            ("9. Limitations?", "Sensitive to lighting, face angles, and image quality."),
            ("10. Can it be extended?", "Yes, with cloud, SMS, mobile apps, etc."),
        ]

        # Add FAQs to the frame
        for q, a in faqs:
            tk.Label(frame, text=q, font=("Helvetica", 12, "bold"),bg="#1c1c1c", fg="white", anchor="w", justify="left").pack(fill="x", padx=20, pady=(10, 0))
            tk.Label(frame, text="   " + a, font=("Helvetica", 12),bg="#1c1c1c", fg="white", anchor="w", justify="left", wraplength=650).pack(fill="x", padx=20)


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
