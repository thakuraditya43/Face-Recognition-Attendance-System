import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkfont
from PIL import Image,ImageTk
from time import strftime



class DeveloperDetail:
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

     # developers details button
    import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DeveloperDetail:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Details")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        title = tk.Label(self.root, text="DEVELOPERS", font=("Helvetica", 24, "bold"), bg="white", fg="green")
        title.pack(pady=20)

        # Scrollable Frame
        canvas = tk.Canvas(self.root, bg="white", bd=0, highlightthickness=0)
        frame = tk.Frame(canvas, bg="white")
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Team data from image
        team_members = [
            {"name": "Aditya Kumar", "email": "aditya_24a12res813@iitp.ac.in"},
            {"name": "Aditya Kumar", "email": "aditya_24a12res814@iitp.ac.in"},
            {"name": "Aditya Kumar", "email": "aditya_24a12res1174@iitp.ac.in"},
            {"name": "Akarsh Kumar", "email": "akarsh_24a12res827@iitp.ac.in"},
            {"name": "Akash Kumar", "email": "akash_24a12res829@iitp.ac.in"},
        ]

        # Display each developer
        for idx, dev in enumerate(team_members, start=1):
            dev_frame = tk.Frame(frame, bg="white", pady=10, padx=10, bd=1, relief="solid")
            dev_frame.pack(fill="x", padx=20, pady=5)

            name_lbl = tk.Label(dev_frame, text=f"{idx}. {dev['name']}", font=("Helvetica", 14, "bold"), bg="white", anchor="w")
            name_lbl.pack(fill="x")

            email_lbl = tk.Label(dev_frame, text=dev["email"], font=("Helvetica", 12), bg="white", fg="blue", anchor="w")
            email_lbl.pack(fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    obj = DeveloperDetail(root)
    root.mainloop()

        


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


