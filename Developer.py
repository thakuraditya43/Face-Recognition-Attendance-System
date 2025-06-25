import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkfont
from PIL import Image,ImageTk
from time import strftime



class DeveloperDetail:
    def _init_(self, root):
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
        Lab_title=tk.Label(self.root, 
                            text="Developer Section",
                            font= ("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
        Lab_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


        # Home Button
        img_Home = Image.open("sample images/home.jpg")
        img_Home = img_Home.resize((55,55), Image.Resampling.LANCZOS)
        self.photo_Home = ImageTk.PhotoImage(img_Home)

        btt_Home=tk.Button(Lab_title,
                            image=self.photo_Home,
                            padx=5,pady=5,bd=0,
                            cursor="hand2",
                            command=self.home,
                            activebackground="#1C1C1C",
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_Home.place(relx=0.001,height=55,)


        # ========Time==========#
        time_lb=tk.Label(Lab_title, 
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        time_lb.place(relx=0.926,height=55)

        def Time():
            string = strftime('%H:%M:%S\n%p')
            time_lb.config(text=string)
            time_lb.after(1000, Time)
        Time()



    # # -----------------------------------------------Creating Buttons-------------------------------------------#

        # Developer details button
        btn_details = self.create_button("sample images/developer.png", 
                                        "Developer Details",
                                        self.unavailabel, 0.15, 0.45)
        


        # View Source Code button
        btn_source_code = self.create_button("sample images/git.jpeg", 
                                        "View Source Code",
                                    self.unavailabel, 0.385, 0.45)
        


        # Theme button
        btn_theme = self.create_button("sample images/theme.jpg", 
                                    "Theme",
                                    self.not_ready, 0.62, 0.45)
        


        # What Users Say button
        btn_feedback = self.create_button("sample images/tracker.jpg", 
                                        "What Users Say" ,
                                        self.not_ready, 0.855, 0.45)
        


        # Check for Updates button
        btn_Updates = self.create_button("sample images/update.jpg", 
                                        "Check for Updates",
                                        self.unavailabel, 0.15, 0.8)
        


        # Manage Modules button
        btn_Modules = self.create_button("sample images/module.jpg", 
                                        "Manage Modules",
                                        self.unavailabel, 0.385 , 0.8)
        


        # Run Diagnostics button
        btn_run_diagnostics = self.create_button("sample images/diagnostics.jpg", 
                                        "Run Diagnostics",
                                        self.not_ready, 0.62 , 0.8)
        


        # Exit button
        btn_Exit = self.create_button("sample images/exit.jpg", 
                                        "Exit",
                                        self.confirm_Exit, 0.855 , 0.8)





    # -----------------------------------------------Button Functions-------------------------------------------#

    # Home button
    def home(self):
        from main import Face_Recognition_System
        self.clear_window()                          # Clear current UI
        self.app = Face_Recognition_System(self.root)       # Load Home UI in new window



    # Exit Button
    def confirm_Exit(self):
        confirm_exit = messagebox.askyesnocancel(
            "Face Recognition Attendance System",
            "Your session seems to be going well.\nAre you sure you want to exit the Face Recognition System?")
        if confirm_exit:
            self.root.destroy()
        else:
            return


    '''----------------------------'''
    # not availabel functions
    def not_ready(self):
        messagebox.showinfo("Info", "This feature is under development.")

    
    def unavailabel(self):
        msg = messagebox.askretrycancel(title="404 Error!", message="Temporarily unavailabel.\nPlease try again later.")
        if msg:
            self.unavailabel()
        else:
            return

    def show_team_info(self):
        top = tk.Toplevel(self.root)
        top.title("Team Members")
        top.geometry("500x300")
        top.configure(bg="white")

        tk.Label(top, text="Team Members", font=("Times New Roman", 20, "bold"), bg="white", fg="black").pack(pady=10)

        members = [
            {"name": "Aditya Kumar", "email": "aditya_24a12res813@iitp.ac.in"},
            {"name": "Aditya Kumar", "email": "aditya_24a12res814@iitp.ac.in"},
            {"name": "Aditya Kumar", "email": "aditya_24a12res1174@iitp.ac.in"},
            {"name": "Akarsh Kumar", "email": "akarsh_24a12res827@iitp.ac.in"},
            {"name": "Akash Kumar",  "email": "akash_24a12res829@iitp.ac.in"},
        ]

        for idx, member in enumerate(members, start=1):
            tk.Label(top,
                     text=f"{idx}. {member['name']} — {member['email']}",
                     font=("Calibri", 12),
                     bg="white", anchor="w").pack(anchor="w", padx=20, pady=2)



def check_for_updates(self):
    top = tk.Toplevel(self.root)
    top.title("Checking for Updates")
    top.geometry("400x150")
    top.configure(bg="white")
    top.resizable(False, False)

    label = tk.Label(top, text="Checking for updates...", font=("Arial", 14), bg="white")
    label.pack(pady=20)

    progress = ttk.Progressbar(top, mode='indeterminate', length=300)
    progress.pack(pady=10)
    progress.start(10)  # Adjust speed if needed

    def finish_check():
        progress.stop()
        top.destroy()
        messagebox.showinfo("Updates", "No updates available at the moment.")

    # Close after 30 seconds
    top.after(30000, finish_check)


def show_module_info(self):
    import tkinter as tk
    import PIL
    import mysql.connector
    import time
    import tkcalendar
    import cv2

    # Module info as list of dicts
    modules = [
        {"name": "tkinter", "purpose": "GUI development", "version": tk.TkVersion},
        {"name": "Pillow", "purpose": "Image processing", "version": PIL.__version__},
        {"name": "mysql.connector", "purpose": "MySQL database connection", "version": mysql.connector.__version__},
        {"name": "time", "purpose": "Time-based functions", "version": "built-in"},
        {"name": "tkcalendar", "purpose": "Date selection calendar widget", "version": tkcalendar.__version__},
        {"name": "OpenCV (cv2)", "purpose": "Computer vision and image processing", "version": cv2.__version__}
    ]

    # Create top-level window
    top = tk.Toplevel(self.root)
    top.title("Module Information")
    top.geometry("600x350")
    top.configure(bg="white")
    top.resizable(False, False)

    # Heading
    tk.Label(top, text="Modules Used in the Project", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

    # Create table headers
    headers = ["Module", "Purpose", "Version"]
    for col, header in enumerate(headers):
        tk.Label(top, text=header, font=("Helvetica", 12, "bold"), bg="lightgray", borderwidth=1, relief="solid", width=20).grid(row=1, column=col, padx=1, pady=1)

    # Fill in module data
    for i, module in enumerate(modules, start=2):
        tk.Label(top, text=module["name"], bg="white", borderwidth=1, relief="solid", width=20).grid(row=i, column=0, padx=1, pady=1)
        tk.Label(top, text=module["purpose"], bg="white", borderwidth=1, relief="solid", width=30).grid(row=i, column=1, padx=1, pady=1)
        tk.Label(top, text=module["version"], bg="white", borderwidth=1, relief="solid", width=20).grid(row=i, column=2, padx=1, pady=1)

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
    app = DeveloperDetail(root)
    root.mainloop()