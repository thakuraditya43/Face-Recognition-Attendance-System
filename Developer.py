import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
from time import strftime
import webbrowser
import PIL
import mysql.connector
import tkcalendar
import cv2


class DeveloperDetail:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False, False)


        # Load and Display background image
        img_bg = Image.open(r"sample images\Background image.jpg")
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = tk.Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        bg_lbl.lower()


        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((500, 115), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)
        l_lbl.config(anchor="center")



        # Title
        lbl_title = tk.Label(self.root,
                            text="Developer Section",
                            font=("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"),
                            bg="#1C1C1C",
                            fg="#00FF00")
        lbl_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


        # Home Button
        img_Home = Image.open("sample images/home.jpg")
        img_Home = img_Home.resize((55, 55), Image.Resampling.LANCZOS)
        self.photo_Home = ImageTk.PhotoImage(img_Home)

        btt_Home = tk.Button(lbl_title,
                                image=self.photo_Home,
                                padx=5, pady=5, bd=0,
                                cursor="hand2",
                                command=self.home,
                                activebackground="#1C1C1C",
                                bg="#1C1C1C",
                                fg="#00FF00")
        btt_Home.place(relx=0.001, height=55)


        # Time Label
        time_lb = tk.Label(lbl_title,
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
        btn_developer = self.create_button("sample images/developer.png","Developer Details", 
                                            self.show_team_info, 0.15, 0.45)
        
        btn_code = self.create_button("sample images/git.jpeg", "View Source Code", 
                                        self.open_code, 0.385, 0.45)
        
        btn_Theme = self.create_button("sample images/theme.jpg", "Theme",
                                        self.not_ready, 0.62, 0.45)
        
        btn_Users_Say = self.create_button("sample images/tracker.jpg", "User Feedback",
                                            self.not_ready, 0.855, 0.45)
        
        btn_update = self.create_button("sample images/update.jpg", "Check for Updates", 
                                        self.check_for_updates, 0.15, 0.8)
        
        btn_modules = self.create_button("sample images/module.jpg","Module Details",
                                        self.show_module_info, 0.385, 0.8)
        
        btn_diagnostics = self.create_button("sample images/diagnostics.jpg", "Run Diagnostics",
                                                self.not_ready, 0.62, 0.8)
        
        btn_exit = self.create_button("sample images/exit.jpg", "Exit", 
                                        self.confirm_exit, 0.855, 0.8)

    # ---------------- Button Actions ---------------- #

    # Home button
    def home(self):
        from main import Face_Recognition_System
        self.clear_window()
        self.app = Face_Recognition_System(self.root)


    # Exit button
    def confirm_exit(self):
        confirm_exit = messagebox.askyesnocancel(
            "Face Recognition Attendance System",
            "Your session seems to be going well.\nAre you sure you want to exit the Face Recognition Attendance System?")
        if confirm_exit:
            self.root.destroy()


    # under development functions
    def not_ready(self):
        messagebox.showinfo("Info", "This feature is under development.")


    # Open GitHub repository
    def open_code(self):
        webbrowser.open("https://github.com/Akarsh-Coding/Face-Recognition-Attendance-System.git")


    # Display team members with their roles
    def show_team_info(self):
        top = tk.Toplevel(self.root)
        top.title("Team Members")
        top.geometry("550x700")
        top.configure(bg="#1c1c1c")
        top.resizable(False, False)

        tk.Label(top, text="Development Team", font=("Times New Roman", 22, "bold"), bg="#1c1c1c", fg="#00ff00").pack(pady=8)

            # Frame to hold Text and Scrollbar
        text_frame = tk.Frame(top, bg="#1c1c1c")
        text_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Text widget with vertical scrollbar
        text_widget = tk.Text(text_frame, wrap="word", font=("Calibri", 14),
                                bg="#1c1c1c", fg="#ffffff", insertbackground="white", borderwidth=0)
        text_widget.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")

        text_widget.configure(yscrollcommand=scrollbar.set)

        team_details = [
            {
                "name": "Akarsh Kumar",
                "email": "akarsh_24a12res827@iitp.ac.in",
                "work": (
                    "    - Designed and implemented the entire graphical user interface (GUI) using Tkinter, ensuring user-friendly interaction and intuitive navigation.\n"
                    "    - Developed the face data training module using OpenCV to process captured images for recognition.\n"
                    "    - Write code to record attendance during face recognition, storing data in a CSV file while preventing duplicate entries for the same student on the same day.\n"
                    "    - Integrated all project modules (face recognition, database, attendance management, help sections, etc.) into a seamless and fully functional application.\n"
                    "    - Maintains the GitHub repository by managing commits, handling code versioning, and documenting the overall project structure."
                )
            },
            {
                "name": "Aditya Kumar",
                "email": "aditya_24a12res1174@iitp.ac.in",
                "work": (
                    "    - Led the backend development of the project by setting up and integrating MySQL for reliable attendance data storage and retrieval.\n"
                    "    - Managed the face data encoding and linking with database records, ensuring accuracy in student recognition and logging.\n"
                    "    - Develop a Python script to handle importing, exporting, and updating records in a CSV file.\n"
                    "    - Provided valuable insights and technical suggestions for module implementation and application flow.\n"
                    "    - Actively participated in team coordination, contributing to effective planning, feature integration, and module-level testing."
                )
            },
            {
                "name": "Aditya Kumar",
                "email": "aditya_24a12res813@iitp.ac.in",
                "work": (
                    "    - Created multiple additional utility windows like FAQs, About Us, Contact Information, and Team Info, enhancing the overall project completeness.\n"
                    "    - Developed face capturing and image saving logic using OpenCV for recognition processing.\n"
                    "    - Suggested improvements for UI/UX and provided extensive feedback during testing and debugging phases.\n"
                    "    - Collaborated with the team to refine the interface layout and improve user experience across different modules."
                )
            },
            {
                "name": "Aditya Kumar",
                "email": "aditya_24a12res814@iitp.ac.in",
                "work": (
                    "    - Implemented face recognition with OpenCV: drew bounding boxes, displayed student details on match, and labeled unknown if unmatched."
                )
            },
            {
                "name": "Akash Kumar",
                "email": "akash_24a12res829@iitp.ac.in",
                "work":(
                    "    - Nothing"
                )
            }
        ]
            

        # Define font tags for name/email and work
        text_widget.tag_configure("name_tag", font=("Calibri", 16, "bold"), foreground="#00ff00",justify="center")
        text_widget.tag_configure("work_tag", font=("Calibri", 14), foreground="#ffffff",justify="left")

        # Insert team info with different fonts
        for idx, member in enumerate(team_details, start=1):
            text_widget.insert("end", f"{idx}. {member['name']} — {member['email']}\n", "name_tag")
            text_widget.insert("end", f"{member['work']}\n\n", "work_tag")

        # Disable editing
        text_widget.config(state="disabled")

        ttk.Button(top, text="Close", command=top.destroy).pack(pady=8)


    # Update checking function
    def check_for_updates(self):
        top = tk.Toplevel(self.root)
        top.title("Checking for Updates")
        top.geometry("400x150")
        top.configure(bg="#1c1c1c")
        top.resizable(False, False)

        label = tk.Label(top, text="Checking for updates...", font=("Arial", 14), bg="#1c1c1c",fg="#ffffff")
        label.pack(pady=20)

        progress = ttk.Progressbar(top, mode='indeterminate', length=300)
        progress.pack(pady=10)
        progress.start(10)

        def finish_check():
            progress.stop()
            top.destroy()
            messagebox.showinfo("Updates", "No updates available at the moment.")

        top.after(10000, finish_check)


    # Show list of used modules with version and purpose
    def show_module_info(self):
        top = tk.Toplevel(self.root)
        top.title("Module Information")
        top.geometry("700x300")
        top.configure(bg="#1c1c1c")
        top.resizable(False, False)

        modules = [
            {"name": "tkinter", "purpose": "GUI development", "version": tk.TkVersion},
            {"name": "Pillow", "purpose": "Image processing", "version": PIL.__version__},
            {"name": "mysql.connector", "purpose": "MySQL database connection", "version": mysql.connector.__version__},
            {"name": "time", "purpose": "Time-based functions", "version": "built-in"},
            {"name": "tkcalendar", "purpose": "Date selection widget", "version": tkcalendar.__version__},
            {"name": "OpenCV (cv2)", "purpose": "Computer vision", "version": cv2.__version__},
        ]

        tk.Label(top, text="Project Dependencies", font=("Helvetica", 16, "bold"), bg="#1c1c1c",fg="#00ff00").pack(pady=10,padx=10)
        detail_frame = tk.Frame(top, bg="#1c1c1c")
        detail_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

        headers = ["Module", "Purpose", "Version"]
        for col, header in enumerate(headers):
            tk.Label(detail_frame, text=header, font=("Helvetica", 12, "bold"), bg="lightgray", borderwidth=1, relief="solid", width=20).grid(row=1, column=col, padx=1, pady=1)

        for i, module in enumerate(modules, start=2):
            tk.Label(detail_frame, text=module["name"],bg="#1c1c1c", fg="white", borderwidth=1, relief="solid", width=20).grid(row=i, column=0, padx=1, pady=1)
            tk.Label(detail_frame, text=module["purpose"],bg="#1c1c1c", fg="white", borderwidth=1, relief="solid", width=30).grid(row=i, column=1, padx=1, pady=1)
            tk.Label(detail_frame, text=module["version"],bg="#1c1c1c", fg="white", borderwidth=1, relief="solid", width=20).grid(row=i, column=2, padx=1, pady=1)


    # Button creator function 
    def create_button(self, image_path, text, command, relx, rely):
        img = Image.open(image_path).resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        btn = tk.Button(self.root, image=photo, text=text, compound="top",
                        font=("Gabriola", 20, "bold"), bg="#1C1C1C", fg="#00FF00",
                        cursor="hand2", relief=tk.RAISED, command=command)
        btn.image = photo
        btn.place(relx=relx, rely=rely, anchor="center", width=200, height=245)


    # Enable toggling between fullscreen and windowed mode
    def toggle_fullscreen(self):
        if self.root.attributes('-fullscreen'):
            self.root.attributes('-fullscreen', False)
            self.root.state('zoomed')
        else:
            self.root.attributes('-fullscreen', True)


    # Clear all widgets from current window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = DeveloperDetail(root)
    root.mainloop()
