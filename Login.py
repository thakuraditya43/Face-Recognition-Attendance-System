from tkinter import *
from tkinter import ttk
import PIL.GifImagePlugin
import itertools
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

from main import Face_Recognition_System



"""
========================================================================
                Face-Recognition Attendance | Login & Sign-up
========================================================================
Prerequisites
-------------
1. Python packages:
    pip install opencv-contrib-python customtkinter pillow mysql-connector-python

2. MySQL server running on your machine.

3. **Edit credentials**:
    In both SignUp.py and IITP_Login.py, update the `mysql.connector.connect`
    call so that `host`, `user`, and `password` match your own MySQL setup.
    Example:
        connect = mysql.connector.connect(
            host='localhost',
            user='YOUR_MYSQL_USER',
            password='YOUR_MYSQL_PASSWORD',
            database='face-recognition-attendance-system'
        )

Database Setup
--------------
CREATE DATABASE face_recognition_attendance_system;
USE face_recognition_attendance_system;

CREATE TABLE registration (
    F_name   VARCHAR(50)  NOT NULL,
    L_name   VARCHAR(50)  NOT NULL,
    ID       VARCHAR(50)  PRIMARY KEY,
    Password VARCHAR(255) NOT NULL,
    Contact  VARCHAR(15)  NOT NULL,
    Question VARCHAR(255) NOT NULL,
    Answer   VARCHAR(255) NOT NULL
);

┌──────────────────────────────────────────────────────────────────────┐
│ Column order in INSERT / SELECT statements in this code is:         │
│   F_name , L_name , ID , Password , Contact , Question , Answer     │
└──────────────────────────────────────────────────────────────────────┘

Running the App
---------------
python Login.py      # launches the login window
    ↳ “Create an account” opens SignUp.py flow to insert a user record.
    ↳ Successful login opens main Face Recognition System UI.

Notes
-----
* To reset a forgotten password, the user must answer their security question; 
the new password is saved back to the same `registration` table.

"""


class Log_in:
    def __init__(self, root):
        self.root = root
        # self.root.config(bg="#000208")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')
        self.root.minsize(770,410)
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        # self.root.resizable(False,False)

        
        # # Load and Display bg img
        # img_bg = Image.open("sample images/04bg.jpg")
        # img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        # self.photo_bg = ImageTk.PhotoImage(img_bg)

        img_bg = Image.open("sample images/04bg.jpg")
        # Use Image.LANCZOS instead of Image.Resampling.LANCZOS for compatibility
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())  # Full screen


        # title
        Lab_title=Label(self.root, 
                            text="Face Recognition for Secure Attendance Management",
                            font= ("Monotype Corsiva", 46,"bold"), 
                            bg= "#000000", 
                            fg= "#25C5FF" )
        Lab_title.place(x=0, y=25, height=75, width=self.root.winfo_screenwidth())



    
        # Frame
        main_frame = Frame(self.root,bd=0,height=410,width=770,bg="#000000")
        # main_frame.pack(anchor="center",expand=True,)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")



        # --- load the GIF as individual frames ---------------------------------

        gif_face = Image.open("sample images/face01.gif")

        frames  = []
        widths  = 385
        heights = 385


        try:
            while True:                      # extract every frame
                frame = gif_face.copy().resize((widths, heights), Image.Resampling.LANCZOS)
                frames.append(ImageTk.PhotoImage(frame))
                gif_face.seek(len(frames))        # go to next frame
        except EOFError:
            pass                             # ran out of frames

        self.frames_cycle = itertools.cycle(frames)  # endless iterator

        # --- label that will hold the background -------------------------------
        self.l_lbl = Label(main_frame,)
        self.l_lbl.place(x=2, y=12, width=380, height=385) 

        self.animation()            # kick-off animation


# -------------------------------------------------------------------------------



        # Separator
        s = ttk.Separator(main_frame, orient='vertical')
        s.place(x=385,y=15,height=380,)



        # Load and Display Logo
        img_logo = Image.open("sample images/login.jpg")
        img_logo = img_logo.resize((310, 120), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = Label(main_frame, image=self.photo_logo, bg="#FFFFFF")
        l_lbl.place(x=422, y=10, width=310, height=110)  
        l_lbl.config(anchor="center")   # Make the logo centered


        # Username
        user_frame=LabelFrame(main_frame,bd=2,relief="groove",bg="#000000",fg="#FFFFFF",text="Username or Email ID",font=("Times New Roman",15,),)
        user_frame.place(x=430,y=135,width=290,height=55)

        self.user_entry = Entry(user_frame, 
                                    bg="#FFFFFF",fg="#7B7B7B",
                                    bd=0,
                                    font=("Arial", 18,),
                                    relief="solid")
        self.user_entry.place(x=1,y=0,width=285)

        # password
        pwd_frame=LabelFrame(main_frame,bd=2,relief="groove",bg="#000000",fg="#FFFFFF",text="Password",font=("Times New Roman",15,),)
        pwd_frame.place(x=430,y=205,width=290, height=55)

        self.pwd_entry = Entry(pwd_frame, 
                                    bg="#FFFEFE",
                                    bd=0,show="*",
                                    font=("Arial", 18,),
                                    fg="#7B7B7B",
                                    relief="solid")
        self.pwd_entry.place(x=1,y=0,width=285)


        # Log in Buttons
        log_button = Button(main_frame, 
                                    
                                    text="Log in",
                                    bg="#004AB1",activebackground="#004AB1",activeforeground="#FFFFFF",
                                    bd=1,
                                    font=("Arial", 20,),
                                    fg="#FFFAFA",
                                    cursor="hand2",
                                    relief="solid",
                                    command=self.login)
        log_button.place(x=430,y=275,width=290, height=45,)

        # Lost password⁇
        l_pwd = Button(main_frame,
                            cursor="hand2",
                            text="Lost password?",
                            relief="solid",bd=0,
                            font= ("Arial", 12,),
                            bg= "#000000", fg= "#2B6EFF",
                            activebackground="#000000",
                            activeforeground="#FFFFFF",
                            command=self.forget_pwd)
        l_pwd.place(x=520,y=330)


        # Not registered? Create an account
        r_label = Label(main_frame,
                            
                            text="Not registered ?",
                            relief="solid",bd=0,
                            font= ("Arial", 13,),
                            bg= "#000000", fg= "#FFFFFF")
        r_label.place(x=447,y=363)

        Create = Button(main_frame,
                            cursor="hand2",
                            text="Create an account",
                            activebackground="#000000",
                            activeforeground="#FFFFFF",
                            relief="solid",bd=0,
                            font= ("Arial", 13,),
                            bg= "#000000", fg= "#2B6EFF",
                            command=self.register)
        Create.place(x=567,y=360)





#  ======================= Button Function ========================== #

    # Create an account button
    def register(self):
        from SignUp import Registration
        # self.clear_window()                 # Clear current UI
        self.app = Registration(self.root)       # Load Student UI in new window

    # Main file
    def home(self):
        self.clear_window()                 # Clear current UI
        self.app = Face_Recognition_System(self.root)       # Load Student UI in new window




    def login(self):
        if (self.user_entry.get() == "" or self.pwd_entry.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        # elif ( or self.pwd_entry.get() == ""):
        #     pass
        else:
            connect = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
            my_cursor=connect.cursor()
            my_cursor.execute("select * from registration where ID=%s and Password=%s",(
                self.user_entry.get(),self.pwd_entry.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Invalid","Invalid Username and Password")
                self.user_entry.delete(0,END),
                self.pwd_entry.delete(0,END)
            else:
                self.home()
            connect.close()


    # Lost password⁇
    def forget_pwd(self):
        if self.user_entry.get() == "":
            messagebox.showerror("Error","Please enter Username to reset password")
        else:
            connect = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
            my_cursor=connect.cursor()
            query = ("select F_name, Question, Answer from registration where ID=%s")
            Value=(self.user_entry.get(),)
            my_cursor.execute(query,Value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter a valid username")
            else:
                name = row[0]
                Question=row[1]
                Ans = row[2]
                connect.close()
                # self.root.attributes('-disabled', True)   # disable the main window while the Toplevel is open  # it has to turned off when window close
                self.forget_pwd_win(name,Question,Ans)
            
        
    '''============================================================================'''
    # forget password window
    def forget_pwd_win(self,name,Q,ans):

        self.win = Toplevel(self.root)
        win = self.win
        # win = Toplevel(self.root)
        win.title("Reset Password")
        win.config(bg="#FFFFFF")
        win.geometry(f"770x385+249+184")
        win.resizable(False,False)

        self.win.grab_set()


            # -------------- Message ------------------- #
        lb_1 = Label(win,bd=0,bg="white",relief="flat",
                        text=f'Welcome back, {name}!',
                        font=("Times New Roman",20,"bold"),fg="#FF0000",justify="center")
        lb_1.place(x=5,y=5,width=375)

        lb_2 = Label(win,bd=0,bg="white",
                        text="Forgot your password?",
                        font=("Times New Roman",20,),fg="#000000",justify="center")
        lb_2.place(x=5,y=50,width=375,)

        lb_3 = Label(win,bd=0,bg="white",
                        text="•      No worries —we’re here to help you get\n back into your account." \
                        "\n•    To reset your password, please answer the\n security question correctly to confirm\n your identity." \
                        "\n•      Once verified, you’ll be able to set a new\n password and regain access to\n your account." \
                        "\n•       Make sure your new password is strong,\n easy for you to remember, and hard for\n others to guess.",
                        font=("Times New Roman",16,),fg="#000000",justify="center")
        lb_3.place(x=5,y=100,width=375)

                # Separator
        s = ttk.Separator(win, orient='vertical')
        s.place(x=385,y=25,height=335,)

        # ----------------- Reset your password --------------------------- #
        lb_1 = Label(win,bd=0,bg="white",relief="flat",
                        text=" Reset Your Password ",
                        font=("Times New Roman",20,"bold"),fg="#FF0000",justify="center")
        lb_1.place(x=390,y=5,width=375)


        Q_lb_1=Label(win,text="Your Security Question:",font=("Times New Roman",16,"bold"),bg="white",justify="center")
        Q_lb_1.place(x=390,y=60,width=375)

        Q_lb_2=Label(win,text=Q,font=("Times New Roman",16,),bg="white")
        Q_lb_2.place(x=400,y=88)

        A_lb=Label(win,text="Security Question's Answer:",font=("Times New Roman",16,"bold"),bg="white",justify="center")
        A_lb.place(x=390,y=125,width=375)

        self.A_entry=ttk.Entry(win,width=15,font=("Times New Roman",14),)
        self.A_entry.place(x=400,y=155,width=300)


        P_lb=Label(win,text="New Password:",font=("Times New Roman",15,"bold"),bg="white")
        P_lb.place(x=395,y=215)

        self.P_entry=ttk.Entry(win,width=15,font=("Times New Roman",13),)
        self.P_entry.place(x=395,y=240,width=175)

        CP_lb=Label(win,text="Confirm Password:",font=("Times New Roman",15,"bold"),bg="white")
        CP_lb.place(x=585,y=215)

        self.CP_entry=ttk.Entry(win,width=15,font=("Times New Roman",13),)
        self.CP_entry.place(x=585,y=240,width=175)

                # ------------------- Buttons -------------------- #
        R_btn = Button(win,text="Set New Password",
                        font=("Times New Roman",12,"bold"),
                        bg="#00FF04",fg="#000000",activebackground="#00FF04",
                        command=lambda:self.reset_pwd(ans))
        R_btn.place(x=400,y=300)

        clear_btn = Button(win,text="Clear",
                        font=("Times New Roman",12,"bold"),
                        bg="#FF1C1C",fg="#E6E6E6",command=self.clear,activebackground="#FF1C1C")
        clear_btn.place(x=595,y=300)

        close_btn = Button(win,text="Close",
                        font=("Times New Roman",12,"bold"),
                        bg="#0044FF",fg="#FFFFFF",command=self.Close_forget_pwd_win,activebackground="#0044FF")
        close_btn.place(x=705,y=300)






                # ------------------- Buttons Functions -------------------- #
    def reset_pwd(self,ans):
        if (self.A_entry.get()=="" or
                self.P_entry.get()=="" or
                self.CP_entry.get()==""):
            messagebox.showerror("Error", "All fields are required",parent=self.win)
        elif(self.P_entry.get() != self.CP_entry.get()):
            messagebox.showerror("Error", "Password and Confirm Password mustbe same.",parent=self.win)
        elif(self.A_entry.get() != ans):
            messagebox.showerror("404 Error","Security Question's Answer entered is wrong",parent=self.win)
        else:
            pass
            connect = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
            my_cursor=connect.cursor()
            query=("update registration set Password=%s where ID=%s")
            value=(self.P_entry.get(),self.user_entry.get(),)
            my_cursor.execute(query,value)
            connect.commit()
            connect.close()
            self.Close_forget_pwd_win()
            messagebox.showinfo("Success","New password set successfully.\nNow you can log in with the new password")


    # close button
    def Close_forget_pwd_win(self):
        self.win.destroy()




        # clear button
    def clear(self):
        self.A_entry.delete(0, END)
        self.P_entry.delete(0, END)
        self.CP_entry.delete(0, END)



    # ---------------------------------------------------------------------------
    # def animation(self):
    #     self.l_lbl.configure(image=next(self.frames_cycle))
    #     # call myself again after the GIF’s own delay (or 100 ms if unavailabel)
    #     delay = getattr(Image.open, "info", {}).get("duration", 100)
    #     self.root.after(delay, self.animation)


    def animation(self):
        try:
            self.l_lbl.configure(image=next(self.frames_cycle))
            self.root.after(100, self.animation)
        except (TclError, AttributeError):
            # Widget has been destroyed or does not exist, safely ignore
            pass



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
    root = Tk()
    
    app = Log_in(root)
    root.mainloop()