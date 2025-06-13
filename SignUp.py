from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

from Login import Log_in


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




class Registration:
    def __init__(self, root):
        self.root = root
        # self.root.config(bg="#000208")                    # due to opens in same windows it is uneffective
        self.root.title("Face Recognition System")
        self.root.state('zoomed')
        
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False,False)



        #  background frame for black theme
        bg_frame = Frame(root, bg="#000208")
        bg_frame.place(x=0, y=0, relwidth=1, relheight=1)


        # Load and Display Logo
        img_logo = Image.open("sample images/registration.png")
        img_logo = img_logo.resize((770, 160), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=255, y=10, width=770, height=160)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered




# --------------text variable-------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_ID=StringVar()
        self.var_Q=StringVar()
        self.var_A=StringVar()
        self.var_P=StringVar()
        self.var_CP=StringVar()
        self.var_check=IntVar()


                # left label frame
        left_frame=LabelFrame(self.root,bd=3,bg="white",relief=RIDGE,
                                text="Welcome to IIT Patna’s Face Recognition Attendance System!",
                                font=("Times New Roman",16,"bold"),labelanchor=N,background="#000000",fg="#FFFFFF")
        left_frame.place(relx=0.25, rely=0.625,anchor="center",width=625,height=450)

        lb_0 = Label(left_frame,bd=0,bg="white",relief="flat",
                        text='Ready to experience the future of smart attendance?',justify="center",
                        font=("Times New Roman",16,),fg="#C90000",background="#000000")
        lb_0.place(x=5,y=10,width=614,height=20)

        lb_1 = Label(left_frame,bd=0,bg="#000000",relief="flat",justify="left",fg="#FFFFFF",
                        text='''
Sign up for our next-generation platform and say goodbye to manual registers and 
time-consuming processes.This system is built to make attendance faster, smarter, 
and more secure — with just a glance.

Please create your account by filling in the required details on the right. 
Once registered, you’ll be able to:
        - log in effortlessly,
        - mark attendance seamlessly, and
        - manage and view attendance records in real-time — all in one place.''',
                        font=("Times New Roman",14,),)
        lb_1.place(x=0,y=35,)


        lb_2 = Label(left_frame,bd=0,bg="white",relief="flat",
                        text="We're excited to have you on board as part of this innovative academic system.\n\nLet’s get started!.",
                        font=("Times New Roman",14,),fg="#069823",background="#000000")
        lb_2.place(x=0,y=300,)

        lb_3 = Label(left_frame,bd=0,bg="white",relief="flat",
                        text='Note: Please ensure all details are entered accurately.',
                        font=("Times New Roman",16,"bold"),fg="#FF0000",background="#000000")
        lb_3.place(x=0,y=375,)


                # Separator
        s = ttk.Separator(self.root, orient='vertical')
        s.place(relx=0.5, rely=0.625,anchor="center",height=480,)


        # Right label frame
        right_frame=LabelFrame(self.root,bd=3,bg="white",relief=RIDGE,
                                    text="Create An Account",font=("Times New Roman",20,"bold"),labelanchor=N)
        right_frame.place(relx=0.75, rely=0.625,anchor="center",width=620,height=450)

        # Label & Entry 
        Fname_lb=Label(right_frame,text="First Name:",font=("Times New Roman",15,"bold"),bg="white")
        Fname_lb.place(x=65,y=0)

        Fname_entry=ttk.Entry(right_frame,textvariable=self.var_fname,width=15,font=("Times New Roman",12))
        Fname_entry.place(x=65,y=25,width=200)

        Lname_lb=Label(right_frame,text="Last Name:",font=("Times New Roman",15,"bold"),bg="white")
        Lname_lb.place(x=365,y=0)

        Lname_entry=ttk.Entry(right_frame,width=15,font=("Times New Roman",12),textvariable=self.var_lname)
        Lname_entry.place(x=365,y=25,width=200)


        contact_lb=Label(right_frame,text="Contact:",font=("Times New Roman",15,"bold"),bg="white")
        contact_lb.place(x=65,y=75)

        contact_entry=ttk.Entry(right_frame,width=15,textvariable=self.var_contact,font=("Times New Roman",12))
        contact_entry.place(x=65,y=100,width=200)

        ID_lb=Label(right_frame,text="College ID:",font=("Times New Roman",15,"bold"),bg="white")
        ID_lb.place(x=365,y=75)

        ID_entry=ttk.Entry(right_frame,width=15,font=("Times New Roman",12),textvariable=self.var_ID)
        ID_entry.place(x=365,y=100,width=200)


        Q_lb=Label(right_frame,text="Select Security Question:",font=("Times New Roman",15,"bold"),bg="white")
        Q_lb.place(x=65,y=150)

        Q_combo=ttk.Combobox(right_frame,width=15,textvariable=self.var_Q,font=("Times New Roman",12),state="readonly")
        Q_combo["values"]=("Select a Question","What was the name of your first pet?","In what city were you born?","What was your childhood nickname?","What is your favorite Anime?","")
        Q_combo.current(0)
        Q_combo.place(x=65,y=175,width=200)

        A_lb=Label(right_frame,text="Security Question's Answer:",font=("Times New Roman",15,"bold"),bg="white")
        A_lb.place(x=365,y=150)

        A_entry=ttk.Entry(right_frame,width=15,font=("Times New Roman",12),textvariable=self.var_A)
        A_entry.place(x=365,y=175,width=200)


        P_lb=Label(right_frame,text="Password:",font=("Times New Roman",15,"bold"),bg="white")
        P_lb.place(x=65,y=225)

        P_entry=ttk.Entry(right_frame,width=15,font=("Times New Roman",12),textvariable=self.var_P)
        P_entry.place(x=65,y=250,width=200)

        CP_lb=Label(right_frame,text="Confirm Password:",font=("Times New Roman",15,"bold"),bg="white")
        CP_lb.place(x=365,y=225)

        CP_entry=ttk.Entry(right_frame,width=15,font=("Times New Roman",12),textvariable=self.var_CP)
        CP_entry.place(x=365,y=250,width=200)


        # Terms & Conditions
        check = Checkbutton(right_frame,text="I agree The Terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,font=("Times New Roman",12),bg="#FFFFFF")
        check.place(x=65,y=300)


        # Buttons
        R_btn = Button(right_frame,text="Create Account",
                        font=("Times New Roman",12,"bold"),
                        bg="#00FF04",fg="#000000",activebackground="#00FF04",
                        command=self.registration)
        R_btn.place(x=65,y=350)

        c_btn = Button(right_frame,text="Clear",
                        font=("Times New Roman",12,"bold"),
                        bg="#FF1C1C",fg="#E6E6E6",command=self.clear,activebackground="#FF1C1C")
        c_btn.place(x=310,y=350)

        L_btn = Button(right_frame,text="Log in Now",
                        font=("Times New Roman",12,"bold"),
                        bg="#0044FF",fg="#FFFFFF",command=self.Signin,activebackground="#0044FF")
        L_btn.place(x=475,y=350)



                # Already have an account? Log_in Here!
        log = Label(self.root,
                            
                            text="Already have an account?",
                            relief="solid",bd=0,
                            font= ("Arial", 11,),
                            bg= "#000000", fg= "#FFFFFF")
        log.place(relx=0.85, rely=0.27,anchor="center")

        log = Button(self.root,
                            cursor="hand2",
                            text="Log_in Here!",
                            relief="solid",bd=0,
                            font= ("Arial", 10,"bold"),
                            bg= "#000000", fg= "#1DCFE6",
                            activebackground="#000000",command=self.Signin,activeforeground="#FFFFFF")
        log.place(relx=0.951, rely=0.27,anchor="center")



# ---------------------- Functions ----------------------

    def registration(self):
        if (self.var_fname.get()=="" or
                self.var_lname.get()=="" or
                self.var_contact.get()=="" or
                self.var_ID.get()=="" or
                self.var_Q.get()=="Select a Question" or
                self.var_A.get()=="" or
                self.var_P.get()=="" or
                self.var_CP.get()==""
                ):
            messagebox.showerror("Error", "All fields are required")
        elif self.var_P.get()!=self.var_CP.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same.")
        elif self.var_check.get() == 0 :
            messagebox.showwarning("Action Required","Please accept Terms & Conditions to continue.")
        else:
            connect = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
            my_cursor=connect.cursor()
            query=("select * from registration where ID=%s")
            value=(self.var_ID.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exists")
            else:
                my_cursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s)",(
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_ID.get(),
                                    self.var_P.get(),
                                    self.var_contact.get(),
                                    self.var_Q.get(),
                                    self.var_A.get()
                ))
            connect.commit()
            connect.close()
            messagebox.showinfo("Success","You have registered successfully, you can Login now.")



    # clear button
    def clear(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_ID.set("")
        self.var_Q.set("Select a Question")
        self.var_A.set("")
        self.var_P.set("")
        self.var_CP.set("")
        self.var_check.set(0)



    # Login button
    def Signin(self):
        # self.clear_window()                 # Clear current UI
        self.app = Log_in(self.root)       # Load Student UI in new window



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
    
    app = Registration(root)
    root.mainloop()