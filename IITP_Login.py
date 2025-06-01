from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import customtkinter as ctk
from customtkinter import CTkImage
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
python IITP_Login.py      # launches the login window
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
        self.root.config(bg="#000208")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')
        self.root.minsize(770,383)
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


    
        # # Frame
        # main_frame = Frame(self.root,bd=3,height=385,width=770)
        # # main_frame.pack(anchor="center",expand=True,)
        # main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # # ctk frame
        main_frame = ctk.CTkFrame(self.root, width=770, height=410, corner_radius=10, fg_color="#FFFFFF")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        main_frame.pack_propagate(False)  


        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((310, 100), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = Label(main_frame, image=self.photo_logo, bg="#FFFEFE")
        l_lbl.place(x=37, y=25, width=310, height=100)  
        l_lbl.config(anchor="center")   # Make the logo centered


        # Username
        self.user_entry = ctk.CTkEntry(main_frame, 
                                    corner_radius=10,
                                    width=290,
                                    height=45, 
                                    placeholder_text="Username or email",
                                    bg_color="#FFFEFE",fg_color="#FFFEFE",
                                    border_width=1,
                                    font=("Arial", 18,),
                                    text_color="#7B7B7B")
        self.user_entry.place(x=45,y=145)

        # password
        self.pwd_entry = ctk.CTkEntry(main_frame, 
                                    corner_radius=10, 
                                    width=290, height=45, 
                                    placeholder_text="Password",
                                    fg_color="#FFFEFE",
                                    border_width=1,show="*",
                                    font=("Arial", 18,),
                                    text_color="#7B7B7B")
        self.pwd_entry.place(x=45,y=210)


        # Log in Buttons
        log_button = ctk.CTkButton(main_frame, 
                                    corner_radius=10, 
                                    width=290, height=45, 
                                    text="Log in",
                                    fg_color="#004AB1",hover_color="#0054CA",
                                    border_width=1,
                                    font=("Arial", 20,),
                                    text_color="#FFFAFA",
                                    cursor="hand2",
                                    command=self.login)
        log_button.place(x=45,y=275)

        # Lost password⁇
        l_pwd = Button(main_frame,
                            cursor="hand2",
                            text="Lost password?",
                            relief="solid",bd=0,
                            font= ("Arial", 12,),
                            bg= "#FFFFFF", fg= "#0011FF",
                            command=self.forget_pwd)
        l_pwd.place(x=140,y=330)



        # Separator
        s = ttk.Separator(main_frame, orient='vertical')
        s.place(x=385,y=15,height=380,)



        # Sign in with
        Sign_Lable = Label(main_frame,
                            
                            text="Sign in with",
                            bd=0,
                            font= ("Arial", 16,),
                            bg= "#FFFFFF", fg= "#242424")
        Sign_Lable.place(x=525,y=125)


        # Microsoft
        img_MS = Image.open("sample images/MS_logo.png")
        # img_MS = img_MS.resize((35,35), Image.Resampling.LANCZOS)
        # self.photo_MS = ImageTk.PhotoImage(img_MS)
        self.photo_MS = CTkImage(light_image=img_MS, dark_image=img_MS, size=(35,35))

        btt_MS=ctk.CTkButton(main_frame,
                            image=self.photo_MS,
                            width=165,height=40,
                            border_width=2,
                            corner_radius=10,
                            cursor="hand2",
                            command=self.home,
                            text="Microsoft",
                            compound="left",
                            font= ("Arial", 20,),
                            fg_color= "#FFFFFF",
                            text_color= "#232323",
                            bg_color="#FFFFFF",
                            hover_color="#D4D4D4")
        btt_MS.place(x=502,y=170)



        # Not registered? Create an account
        r_label = Label(main_frame,
                            
                            text="Not registered ?",
                            relief="solid",bd=0,
                            font= ("Arial", 13,),
                            bg= "#FFFFFF", fg= "#2D2D2D")
        r_label.place(x=450,y=277)

        Create = Button(main_frame,
                            cursor="hand2",
                            text="Create an account",
                            relief="solid",bd=0,
                            font= ("Arial", 13,),
                            bg= "#FFFFFF", fg= "#0011FF",
                            command=self.register)
        Create.place(x=570,y=273)


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
            else:
                self.home()


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


        Q_lb_1=Label(win,text="Your Security Quetion:",font=("Times New Roman",16,"bold"),bg="white",justify="center")
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




        win.mainloop()


                # ------------------- Buttons Functions -------------------- #
    def reset_pwd(self,ans):
        if (self.A_entry.get()=="" or
                self.P_entry.get()=="" or
                self.CP_entry.get()==""):
            messagebox.showerror("Error", "All fields are required",parent=self.win)
        elif(self.P_entry.get() != self.CP_entry.get()):
            messagebox.showerror("Error", "Password and Confirm Password mustbe same.",parent=self.win)
        elif(self.A_entry.get() != ans):
            messagebox.showerror("404 Error","Security Question's Answer entered is worng",parent=self.win)
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
            messagebox.showinfo("Sucsses","New Password set sucssesfuly.\nNow you can login with new password")


    # close button
    def Close_forget_pwd_win(self):
        self.win.destroy()




        # clear button
    def clear(self):
        self.A_entry.delete(0, END)
        self.P_entry.delete(0, END)
        self.CP_entry.delete(0, END)





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