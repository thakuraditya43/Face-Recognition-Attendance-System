from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkcalendar import DateEntry

from tkinter import messagebox



class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        # Make the window start in fullscreen mode
        self.root.attributes('-fullscreen', True)
        # Bind the Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False,False)


        # ........Variables...........
        self.std_id_var=StringVar()
        self.std_name_var=StringVar()
        self.dep_var=StringVar()
        self.course_var=StringVar()
        self.sem_var=StringVar()
        self.batch_var=StringVar()
        self.date_var=StringVar()
        self.time_var=StringVar()
        self.attendance_var=StringVar()


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
        img_logo = img_logo.resize((500, 105), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=105)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered



        # title
        Lab_title=Label(self.root, 
                            text="Attendance Management System",
                            font= ("Monotype Corsiva", 35, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
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
                            activebackground="#1C1C1C",
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




        # # Fram
        # main_frame = Frame(self.root,bd=3)
        # main_frame.place(x=10,y=180,width=1260,height=540)



        # Left lable frame
        left_frame=LabelFrame(self.root,bd=3,bg="white",relief=RIDGE,text="Student Attendance Details",font=("Times New Roman",20,"bold"),labelanchor=N)
        left_frame.place(x=20,y=200,width=600,height=520)

        img_leftF = Image.open("sample images/black.png")
        img_leftF = img_leftF.resize((580,130), Image.Resampling.LANCZOS)
        self.photo_leftF = ImageTk.PhotoImage(img_leftF)

        img_leftF_lbl = Label(left_frame, image=self.photo_leftF)
        img_leftF_lbl.place(x=10, y=0, width=580, height=130)




        # Class Student Information lable frame
        Class_student_frame=Frame(left_frame,bd=2,bg="white",
                                    relief=RIDGE,
                                    # text="Class Student Information",
                                    # font=("Times New Roman",15,"bold")
                                    )
        Class_student_frame.place(x=7,y=150,width=580,height=290)

        # StudentId lable & Entry
        StudentID_lable=Label(Class_student_frame,
                                text="StudentID:",
                                font=("Times New Roman",15,"bold"),bg="white")
        StudentID_lable.grid(row=0,column=0,pady=5,padx=3,sticky=W)

        StudentID_entry=ttk.Entry(Class_student_frame,
                                    textvariable=self.std_id_var,
                                    width=15,font=("Times New Roman",12),style="")
        StudentID_entry.grid(row=0,column=1,padx=3,pady=5,sticky=W)

        # Student_Name lable & Entry
        StudentName_lable=Label(Class_student_frame,
                                text="Student Name:",
                                font=("Times New Roman",15,"bold"),bg="white")
        StudentName_lable.grid(row=0,column=2,pady=5,padx=3,sticky=W)

        StudentName_entry=ttk.Entry(Class_student_frame,
                                    textvariable=self.std_name_var,
                                    width=15,font=("Times New Roman",12))
        StudentName_entry.grid(row=0,column=3,padx=3,pady=5,sticky=W)

        # Department lable & combobox
        dep_lable=Label(Class_student_frame,text="Department:",font=("Times New Roman",15,"bold"),bg="white")
        dep_lable.grid(row=1,column=0,padx=3,pady=5,sticky=W)

        self.dep_combo=ttk.Combobox(Class_student_frame,
                                textvariable=self.dep_var,
                                font=("Times New Roman",12),width=13,state="readonly")
        self.dep_combo["values"]=("Select Department","Computer Science","Management")
        self.dep_combo.current(0)
        # Bind the department combobox selection to a function
        self.dep_combo.bind("<<ComboboxSelected>>", self.update_course_options)
        self.dep_combo.grid(row=1,column=1,padx=3,pady=5,sticky=W)

        # Course lable & combobox
        course_lable=Label(Class_student_frame,text="Course:",font=("Times New Roman",15,"bold"),bg="white")
        course_lable.grid(row=1,column=2,padx=3,pady=5,sticky=W)

        self.course_combo=ttk.Combobox(Class_student_frame,
                                    textvariable=self.course_var,
                                    font=("Times New Roman",12),width=13,state="readonly")
        self.course_combo["values"]=("Select Course","","","")
        self.course_combo.current(0)
        self.course_combo.grid(row=1,column=3,padx=3,pady=5,sticky=W)


        # Semester lable & combobox
        Semester_lable=Label(Class_student_frame,text="Semester:",font=("Times New Roman",15,"bold"),bg="white")
        Semester_lable.grid(row=2,column=0,padx=3,pady=5,sticky=W)

        Semester_combo=ttk.Combobox(Class_student_frame,
                                    textvariable=self.sem_var,
                                    font=("Times New Roman",12),width=13,
                                    state="readonly")
        Semester_combo["values"]=("Select Semester","1","2","3","4","5","6")
        Semester_combo.current(0)
        Semester_combo.grid(row=2,column=1,padx=3,pady=5,sticky=W)


        batch_lable=Label(Class_student_frame,text="Batch:",
                                font=("Times New Roman",15,"bold"),bg="white")
        batch_lable.grid(row=2,column=2,pady=5,padx=3,sticky=W)

        batch_combo=ttk.Combobox(Class_student_frame,width=13,
                                    textvariable=self.batch_var,
                                    font=("Times New Roman",12),
                                    state="readonly")
        batch_combo["values"]=("Select Batch","1","2")
        batch_combo.current(0)
        batch_combo.grid(row=2,column=3,padx=3,pady=5,sticky=W)


        # Date & Time lable & Entry

        date_lable=Label(Class_student_frame,text="Date:",
                            font=("Times New Roman",15,"bold"),bg="white")
        date_lable.grid(row=3,column=0,padx=3,pady=5,sticky=W)

        date_entry=DateEntry(Class_student_frame,width=13,
                                textvariable=self.date_var,
                                font=("Times New Roman",12),state="readonly",date_pattern='dd-mm-yyyy')
        date_entry.grid(row=3,column=1,padx=3,pady=5,sticky=W)


        Time_lable=Label(Class_student_frame,
                                text="Time:",
                                font=("Times New Roman",15,"bold"),bg="white")
        Time_lable.grid(row=3,column=2,pady=5,padx=3,sticky=W)

        Time_entry=ttk.Entry(Class_student_frame,
                                    textvariable=self.time_var,
                                    width=15,font=("Times New Roman",12),style="")
        Time_entry.grid(row=3,column=3,padx=3,pady=5,sticky=W)


        # Attendance Status lable & comboo
        gen_lable=Label(Class_student_frame,text="Attendance Status:",
                        font=("Times New Roman",15,"bold"),bg="white")
        gen_lable.grid(row=4,column=0,pady=5,padx=3,sticky=W)

        gen_combo=ttk.Combobox(Class_student_frame,
                                textvariable=self.attendance_var,
                                font=("Times New Roman",12),width=13,state="readonly")
        gen_combo["values"]=("Select Status","","","Others")
        gen_combo.current(0)
        gen_combo.grid(row=4,column=1,padx=3,pady=5,sticky=W)



        # Buttons
        style1 = ttk.Style()
        style1.configure("CustomL.TButton", font=("Arial", 10, "bold"), foreground="blue", )

        import_button=ttk.Button(Class_student_frame,text="Import CSV",
                                # command=self.add_data,
                                width=18,style="CustomL.TButton")
        import_button.place(x=5,y=255)

        export_button=ttk.Button(Class_student_frame,text="Export CSV",width=18,style="CustomL.TButton")
        export_button.place(x=148,y=255)

        update_button=ttk.Button(Class_student_frame,text="Update",width=18,
                                    style="CustomL.TButton")
        update_button.place(x=292,y=255)

        rest_button=ttk.Button(Class_student_frame,text="Rest",width=18,style="CustomL.TButton",
                                command=self.reset_data)
        rest_button.place(x=435,y=255)





        # Right lable frame
        right_frame=LabelFrame(self.root,bd=3,bg="white",relief=RIDGE,text="Attendance Details",font=("Times New Roman",20,"bold"),labelanchor=N)
        right_frame.place(x=650,y=190,width=600,height=520)

        # img_rightF = Image.open("sample images/black.png")
        # img_rightF = img_rightF.resize((580,130), Image.Resampling.LANCZOS)
        # self.photo_rightF = ImageTk.PhotoImage(img_rightF)

        # img_rightF_lbl = Label(right_frame, image=self.photo_rightF)
        # img_rightF_lbl.place(x=10, y=0, width=580, height=130)

#                                       Search Table
        # Search table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=5,width=575,height=470)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendanceReport_Table=ttk.Treeview(table_frame,
                                            column=("id","name","dep","course","sem","batch",'date',"time","atten"),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.AttendanceReport_Table.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.AttendanceReport_Table.yview)


        self.AttendanceReport_Table.heading("id",text="Student ID")
        self.AttendanceReport_Table.heading("name",text="Name")
        self.AttendanceReport_Table.heading("dep",text="Department")
        self.AttendanceReport_Table.heading("course",text="Course")
        self.AttendanceReport_Table.heading("sem",text="Semester")
        self.AttendanceReport_Table.heading("batch",text="Batch")
        self.AttendanceReport_Table.heading("date",text="Date")
        self.AttendanceReport_Table.heading("time",text="Time")
        self.AttendanceReport_Table.heading("atten",text="Attendance")


        self.AttendanceReport_Table["show"]="headings"

        self.AttendanceReport_Table.column("id",width=100)
        self.AttendanceReport_Table.column("name",width=100)
        self.AttendanceReport_Table.column("dep",width=100)
        self.AttendanceReport_Table.column("course",width=100)
        self.AttendanceReport_Table.column("sem",width=100)
        self.AttendanceReport_Table.column("batch",width=100)
        self.AttendanceReport_Table.column("date",width=100)
        self.AttendanceReport_Table.column("time",width=100)
        self.AttendanceReport_Table.column("atten",width=100)

        self.AttendanceReport_Table.pack(fill=BOTH,expand=1)









    def reset_data(self):
        self.std_id_var.set("")
        self.std_name_var.set("")
        self.dep_var.set("Select Department")
        self.course_var.set("Select Course")
        self.sem_var.set("Select Semeter")
        self.batch_var.set("Select Batch")
        self.date_var.set("")
        self.time_var.set("")
        self.attendance_var.set("Select Status")







    def update_course_options(self, event=None):
        """
        Updates the course combobox options based on the selected department.
        """
        selected_department = self.dep_combo.get()
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
        self.course_combo.set("Select Course") # Reset the course selection to default




    def toggle_fullscreen(self):
        """Toggle between fullscreen and maximized mode"""
        if self.root.attributes('-fullscreen'):  # If currently fullscreen
            self.root.attributes('-fullscreen', False)  # Exit fullscreen
            self.root.state('zoomed')  # Maximize window to fit screen
        else:
            self.root.attributes('-fullscreen', True)  # Go back to fullscreen





            # Home button
    def home(self):
        from main import Face_Recognition_System
        self.clear_window()                          # Clear current UI
        self.app = Face_Recognition_System(self.root)       # Load Home UI in new window





    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()





if __name__ == "__main__":
    root = Tk()
    # root.config(bg="#f2f3f7")
    app = Attendance(root)
    root.mainloop()