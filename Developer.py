from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from PIL import Image,ImageTk
from time import strftime


class Developer_detail:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        # Make the window start in fullscreen mode
        self.root.attributes('-fullscreen', True)
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False,False)



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
                            text="Developer Section",
                            font= ("Monotype Corsiva", 40, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
        Lab_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


        # Home Button
        img_Home = Image.open("sample images/home.jpg")
        img_Home = img_Home.resize((55,55), Image.Resampling.LANCZOS)
        self.photo_Home = ImageTk.PhotoImage(img_Home)

        btt_Home=Button(Lab_title,
                            image=self.photo_Home,
                            padx=5,pady=5,bd=0,
                            cursor="hand2",
                            command=self.home,
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_Home.place(x=0,y=0,width=55,height=55)


        # ========Time==========#
        time_lb=Label(Lab_title, 
                            
                            font= ("Monotype Corsiva", 15, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        time_lb.place(x=1190,y=0,height=55)

        def Time():
            string = strftime('%H:%M:%S\n%p')
            time_lb.config(text=string)
            time_lb.after(1000, Time)
        Time()





        # Developer detail button
        img_detail = Image.open("sample images/developer.png")
        img_detail = img_detail.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_detail = ImageTk.PhotoImage(img_detail)

        btt_detail=Button(self.root,
                            image=self.photo_detail,
                            text="Developer Details",
                            compound="top",
                            
                            relief=RAISED,cursor="hand2",
                            font= ("Gabriola", 20, "bold"),
                            bg= "#1C1C1C",
                            fg= "#00FF00",
                            command=self.Unavailable)
        btt_detail.place(x=100,y=200,width=200,height=245)



        # View Source Code button
        img_Code = Image.open("sample images/git.jpeg")
        img_Code = img_Code.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Code = ImageTk.PhotoImage(img_Code)

        btt_Code=Button(self.root,
                            image=self.photo_Code,
                            relief=RAISED,
                            cursor="hand2",
                            text="View Source Code",
                            compound="top",
                            font= ("Gabriola", 20, "bold"),
                            bg= "#1C1C1C", fg= "#00FF00",
                            command=self.Unavailable)
        btt_Code.place(x=400,y=200,width=200,height=245)



        # Theme button
        img_Theme = Image.open("sample images/theme.jpg")
        img_Theme = img_Theme.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Theme = ImageTk.PhotoImage(img_Theme)

        btt_Theme=Button(self.root,
                        image=self.photo_Theme,
                        relief=RAISED,
                        text="Theme",
                        compound="top",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",
                        command=self.Unavailable)
        btt_Theme.place(x=700,y=200,width=200,height=245)



        # What Users Say button
        img_track = Image.open("sample images/tracker.jpg")
        img_track = img_track.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_track = ImageTk.PhotoImage(img_track)

        btt_track=Button(self.root,
                        image=self.photo_track,
                        relief=RAISED,
                        compound="top",
                        text="What Users Say",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",
                        command=self.Not_ready)
        btt_track.place(x=1000,y=200,width=200,height=245)



        # Check for Updates button
        img_Updates = Image.open("sample images/update.jpg")
        img_Updates = img_Updates.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Updates = ImageTk.PhotoImage(img_Updates)

        btt_Updates=Button(self.root,
                        image=self.photo_Updates,
                        relief=RAISED,
                        compound="top",
                        text="Check for Updates",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",
                        command=self.Not_ready)
        btt_Updates.place(x=100,y=500,width=200,height=245)



        # Manage Modules button
        img_Modules = Image.open("sample images/module.jpg")
        img_Modules = img_Modules.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Modules = ImageTk.PhotoImage(img_Modules)

        btt_Modules=Button(self.root,
                        image=self.photo_Modules,
                        relief=RAISED,
                        text="Manage Modules",
                        compound="top",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",
                        command=self.Unavailable)
        btt_Modules.place(x=400,y=500,width=200,height=245)



        # Run Diagnostics button
        img_diagnostics = Image.open("sample images/diagnostics.jpg")
        img_diagnostics = img_diagnostics.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_diagnostics = ImageTk.PhotoImage(img_diagnostics)

        btt_diagnostics=Button(self.root,
                            image=self.photo_diagnostics,
                            text="Run Diagnostics",
                            font= ("Gabriola", 20, "bold"), 
                            bg= "#1C1C1C",
                            compound="top",
                            fg= "#00FF00",
                            relief=RAISED,
                            cursor="hand2",
                            command=self.Not_ready)
        btt_diagnostics.place(x=700,y=500,width=200,height=245)



        # Exit button
        img_Exit = Image.open("sample images/exit.jpg")
        img_Exit = img_Exit.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Exit = ImageTk.PhotoImage(img_Exit)

        btt_Exit=Button(self.root,
                        image=self.photo_Exit,
                        relief=RAISED,
                        cursor="hand2",
                        text="Exit",
                        font= ("Gabriola", 25, "bold"), 
                        bg= "#1C1C1C", 
                        fg= "#00FF00",
                        compound="top",
                        command=self.Confirm_Exit)
        btt_Exit.place(x=1000,y=500,width=200,height=245)






    def toggle_fullscreen(self):
        """Toggle between fullscreen and maximized mode"""
        if self.root.attributes('-fullscreen'):  # If currently fullscreen
            self.root.attributes('-fullscreen', False)  # Exit fullscreen
            self.root.state('zoomed')  # Maximize window to fit screen
        else:
            self.root.attributes('-fullscreen', True)  # Go back to fullscreen





    # -----------------------------------------------Button Functions-------------------------------------------#

    # Home button
    def home(self):
        from main import Face_Recognition_System
        self.clear_window()                          # Clear current UI
        self.app = Face_Recognition_System(self.root)       # Load Home UI in new window



    # Exit Button
    def Confirm_Exit(self):
        confirm_exit = tkinter.messagebox.askyesnocancel(
            "Face Recognition Attendance System",
            "Hope you had a smooth session!\nWould you like to exit now?")
        if confirm_exit:
            self.root.destroy()
        else:
            return



    # not available functions
    def Not_ready(self):
            messagebox.showerror("Error", "OOPS!!\nNot ready yet")
    
    def Unavailable(self):
        msg = tkinter.messagebox.askretrycancel(title= "404 Error !",message="Temporarily unavailable.\nPlease try again later.")
        if msg:
            self.Unavailable()
        else:
            return



    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()





if __name__ == "__main__":
    root = Tk()
    # root.config(bg="#1C1C1C")
    app = Developer_detail(root)
    root.mainloop()