from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector



class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        # Make the window start in fullscreen mode
        self.root.attributes('-fullscreen', True)
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False,False)


        # ........Variables...........
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_batch=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phn=StringVar()
        self.var_radio=StringVar()
        # self.var_radio2=StringVar()





        # Load and Display bg img
        img_bg = Image.open("sample images/Background image.jpg")
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())  # Full screen



        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((500, 105), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=105)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered



        # title
        Lab_title=Label(self.root, text="Student Management System",font= ("Gabriola", 35, "bold"), bg= "#1C1C1C", fg= "#00FF00" )
        Lab_title.place(x=0, y=115, height=60, width=self.root.winfo_screenwidth())


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
                            activebackground="#1C1C1C",
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





        # # Fram
        # main_frame = Frame(self.root,bd=3)
        # main_frame.place(x=10,y=180,width=1260,height=540)


        # Left lable frame
        left_frame=LabelFrame(self.root,bd=3,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",20,"bold"),labelanchor=N)
        left_frame.place(x=20,y=190,width=600,height=520)

        img_leftF = Image.open("sample images/student_detail2.jpg")
        img_leftF = img_leftF.resize((580,130), Image.Resampling.LANCZOS)
        self.photo_leftF = ImageTk.PhotoImage(img_leftF)

        img_leftF_lbl = Label(left_frame, image=self.photo_leftF)
        img_leftF_lbl.place(x=7, y=0, width=580, height=130)


        # Current course lable frame
        curr_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Times New Roman",15,"bold"))
        curr_course_frame.place(x=7,y=135,width=580,height=95)

        # Department lable & combobox
        dep_lable=Label(curr_course_frame,text="Department:",font=("Times New Roman",15,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=5,sticky=W)

        self.dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_dep,font=("Times New Roman",12),width=14,state="readonly")
        self.dep_combo["values"]=("Setect Department","Computer Science","Management")
        self.dep_combo.current(0)
        # Bind the department combobox selection to a function
        self.dep_combo.bind("<<ComboboxSelected>>", self.update_course_options)
        self.dep_combo.grid(row=0,column=1,padx=2,pady=3,sticky=W)

        # Course lable & combobox
        course_lable=Label(curr_course_frame,text="Course:",font=("Times New Roman",15,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=5,sticky=W)

        self.course_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_course,font=("Times New Roman",12),width=14,state="readonly")
        self.course_combo["values"]=("Setect Course","","","")
        self.course_combo.current(0)
        self.course_combo.grid(row=0,column=3,padx=2,pady=3,sticky=W)

        # year lable & combobox
        year_lable=Label(curr_course_frame,text="Addmission Year:",font=("Times New Roman",15,"bold"),bg="white")
        year_lable.grid(row=1,column=0,sticky=W)

        year_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("Times New Roman",12),width=14,state="readonly")
        year_combo["values"]=("Setect Year","2020","2021","2022","2023","2024","2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=3,sticky=W)

        # Semester lable & combobox
        Semester_lable=Label(curr_course_frame,text="Semester:",font=("Times New Roman",15,"bold"),bg="white")
        Semester_lable.grid(row=1,column=2,padx=5,sticky=W)

        Semester_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_sem,font=("Times New Roman",12),width=14,state="readonly")
        Semester_combo["values"]=("Setect Semester","1","2","3","4","5","6")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=3,sticky=W)


        # Class Student Information lable frame
        Class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Times New Roman",15,"bold"))
        Class_student_frame.place(x=7,y=235,width=580,height=190)

        # StudentId lable & Entry
        StudentID_lable=Label(Class_student_frame,text="StudentID:",font=("Times New Roman",15,"bold"),bg="white")
        StudentID_lable.grid(row=0,column=0,pady=3,sticky=W)

        StudentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=15,font=("Times New Roman",12),style="")
        StudentID_entry.grid(row=0,column=1,padx=3,pady=3,sticky=W)

        # Student_Name lable & Entry
        StudentName_lable=Label(Class_student_frame,text="Student Name:",font=("Times New Roman",15,"bold"),bg="white")
        StudentName_lable.grid(row=0,column=2,pady=3,sticky=W)

        StudentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=15,font=("Times New Roman",12))
        StudentName_entry.grid(row=0,column=3,padx=3,pady=3,sticky=W)

        # class division lable & Entry
        batch_lable=Label(Class_student_frame,text="Batch:",font=("Times New Roman",15,"bold"),bg="white")
        batch_lable.grid(row=1,column=0,pady=3,sticky=W)

        batch_combo=ttk.Combobox(Class_student_frame,width=13,
                                    textvariable=self.var_batch,
                                    font=("Times New Roman",12),
                                    state="readonly")
        batch_combo["values"]=("Setect Batch","1","2")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=3,pady=3,sticky=W)

        # Roll No lable & Entry
        roll_lable=Label(Class_student_frame,text="Roll No:",font=("Times New Roman",15,"bold"),bg="white")
        roll_lable.grid(row=1,column=2,pady=3,sticky=W)

        roll_entry=ttk.Entry(Class_student_frame,width=15,textvariable=self.var_roll,font=("Times New Roman",12))
        roll_entry.grid(row=1,column=3,padx=3,pady=3,sticky=W)

        # Gender lable & comboo
        gen_lable=Label(Class_student_frame,text="Gender:",font=("Times New Roman",15,"bold"),bg="white")
        gen_lable.grid(row=2,column=0,pady=3,sticky=W)

        gen_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("Times New Roman",12),width=13,state="readonly",background='darkblue')
        gen_combo["values"]=("Setect Gender","Male","Female","Others")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=3,pady=3,sticky=W)

        # gen_entry=ttk.Entry(Class_student_frame,width=15,font=("Times New Roman",12))
        # gen_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # DOB lable & Entry
        dob_lable=Label(Class_student_frame,text="DOB:",font=("Times New Roman",15,"bold"),bg="white")
        dob_lable.grid(row=2,column=2,pady=3,sticky=W)

        dob_entry=DateEntry(Class_student_frame,width=13,textvariable=self.var_dob,font=("Times New Roman",12),state="readonly",date_pattern='dd-mm-yyyy')
        dob_entry.grid(row=2,column=3,padx=3,pady=3,sticky=W)

        # email lable & Entry
        email_lable=Label(Class_student_frame,text="Email:",font=("Times New Roman",15,"bold"),bg="white")
        email_lable.grid(row=3,column=0,pady=3,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,width=15,textvariable=self.var_email,font=("Times New Roman",12))
        email_entry.grid(row=3,column=1,padx=3,pady=3,sticky=W)

        # Phone No lable & Entry
        phone_lable=Label(Class_student_frame,text="Phone No:",font=("Times New Roman",15,"bold"),bg="white")
        phone_lable.grid(row=3,column=2,pady=3,sticky=W)

        phone_entry=ttk.Entry(Class_student_frame,width=15,textvariable=self.var_phn,font=("Times New Roman",12))
        phone_entry.grid(row=3,column=3,padx=3,pady=3,sticky=W)

        # Radio Buttons
        button_1=ttk.Radiobutton(Class_student_frame,text="Take Photo Sample",variable=self.var_radio,value="yes")
        button_1.grid(row=6,column=0)

        button_2=ttk.Radiobutton(Class_student_frame,text="Do Not Take Photo Sample",variable=self.var_radio,value="no",)
        button_2.grid(row=6,column=2,padx=10,pady=3,sticky=W)

        # Buttons
        style1 = ttk.Style()
        style1.configure("CustomL.TButton", font=("Arial", 10, "bold"), foreground="blue", )

        save_button=ttk.Button(left_frame,text="Save",command=self.add_data,width=19,style="CustomL.TButton")
        save_button.place(x=5,y=455)

        update_button=ttk.Button(left_frame,text="Update",width=19,style="CustomL.TButton")
        update_button.place(x=151,y=455)

        del_button=ttk.Button(left_frame,text="Delete",width=19,style="CustomL.TButton")
        del_button.place(x=299,y=455)

        rest_button=ttk.Button(left_frame,text="Rest",width=19,style="CustomL.TButton",
                                command=self.reset_data)
        rest_button.place(x=445,y=455)

        take_pic_button=ttk.Button(left_frame,text="Take Photo Sample",width=35,style="CustomL.TButton")
        take_pic_button.place(x=20,y=429)

        update_pic_button=ttk.Button(left_frame,text="Update Photo Sample",width=35,style="CustomL.TButton")
        update_pic_button.place(x=315,y=429)



        # Right lable frame
        right_frame=LabelFrame(self.root,bd=3,bg="white",relief=RIDGE,text="Student Details",font=("Times New Roman",20,"bold"),labelanchor=N)
        right_frame.place(x=650,y=190,width=600,height=520)

        img_rightF = Image.open("sample images/btnStudent.png")
        img_rightF = img_rightF.resize((580,110), Image.Resampling.LANCZOS)
        self.photo_rightF = ImageTk.PhotoImage(img_rightF)

        img_rightF_lbl = Label(right_frame, image=self.photo_rightF)
        img_rightF_lbl.place(x=7, y=0, width=580, height=110)


# --------------------------------------Search System--------------------------------------- #

        # Search lable frame
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Times New Roman",15,"bold"))
        search_frame.place(x=7,y=115,width=580,height=70)

        # search lable, combobox,entry & button
        search_lable=Label(search_frame,text="Search by:",font=("Times New Roman",15,"bold"),fg="red",bg="white")
        search_lable.grid(row=0,column=0,padx=4,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("Times New Roman",12),width=10,state="readonly")
        search_combo["values"]=("Setect","StudentID","Roll No","Others")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=4,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("Times New Roman",12))
        search_entry.grid(row=0,column=2,padx=4,pady=5,sticky=W)

        style2 = ttk.Style()
        style2.configure("CustomR.TButton", font=("Arial", 10, "bold"), foreground="red", )

        search_button=ttk.Button(search_frame,text="Save",width=14,style="CustomR.TButton")
        search_button.grid(row=0,column=3,padx=4,pady=5,sticky=W)

        Show_all_button=ttk.Button(search_frame,text="Show All",width=14,style="CustomR.TButton")
        Show_all_button.grid(row=0,column=4,padx=4,pady=5,sticky=W)

#                                       Search Table
        # Search table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=190,width=580,height=235)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,
                                            column=("dep","course","year","sem","id","name","batch","roll","gender",'dob',"email","phn no","photo"),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("batch",text="Batch")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phn no",text="Phone No")
        self.student_table.heading("photo",text="Photo Sample Status")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("batch",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phn no",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)



    # ==============================================================================================================#
    # ---------------------------------------Funtion Declaration-----------------------------------------------------------#

    def add_data(self):
        if (
        self.var_dep.get() == "Setect Department" or
        self.var_course.get() == "Setect Course" or
        self.var_year.get() == "Setect Year" or
        self.var_sem.get() == "Setect Semester" or
        self.var_std_id.get() == "" or
        self.var_std_name.get() == "" or
        self.var_batch.get() == "" or
        self.var_roll.get() == "" or
        self.var_gender.get() == "Setect Gender" or
        self.var_dob.get() == "" or
        self.var_email.get() == "" or
        self.var_phn.get() == "" or
        self.var_radio.get()==""
            ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_radio.get() == "no":  
            messagebox.showwarning("Action Required", "You have selected 'Do Not Take Photo Sample'.\nPlease select 'Take Photo Sample' to proceed.",parent=self.root)
        else:
            messagebox.showinfo("Wait!","Data is saving",parent=self.root)



            messagebox.showinfo("sucsses","saved",parent=self.root)
            # messagebox.showinfo("Selected Option", "You have selected 'Take Photo Sample' Option.\nPlease ")




    def update_course_options(self, event=None):
        """
        Updates the course combobox options based on the selected department.
        """
        selected_department = self.var_dep.get()
        if selected_department == "Computer Science":
            self.course_combo["values"] = ("Select Course",
                                            "B.Sc.(Hons.):CSDA",
                                            "B.Sc.(Hons.):AICS",
                                            "B.S.:CSDA",
                                            "B.S.:AICS",
                                            "M.S.:CSDA",
                                            "M.S.:AICS",
                                            "B.S.-M.S.:CSDA",
                                            "B.S.-M.S.:AICS",
                                            )
        elif selected_department == "Management":
            self.course_combo["values"] = ("Select Course", "BBA", "MBA", "BBA + MBA")
        else:
            self.course_combo["values"] = ("Select Course",) # Default for "Select Department" or unknown
        self.var_course.set("Select Course") # Reset the course selection to default





    def reset_data(self):
        
        self.var_dep.set( "Setect Department"),
        self.var_course.set( "Setect Course"),
        self.var_year.set( "Setect Year"),
        self.var_sem.set( "Setect Semester"),
        self.var_std_id.set( ""),
        self.var_std_name.set( ""),
        self.var_batch.set( ""),
        self.var_roll.set( ""),
        self.var_gender.set( "Setect Gender"),
        # self.var_dob.set(""),
        self.var_email.set( ""),
        self.var_phn.set( ""),
        self.var_radio.set(""),
        
        







    # Home button
    def home(self):
        from main import Face_Recognition_System
        self.clear_window()                          # Clear current UI
        self.app = Face_Recognition_System(self.root)       # Load Home UI in new window




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
    # root.config(bg="#f2f3f7")
    app = Student(root)
    root.mainloop()