import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector
import cv2


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
        self.var_dep=tk.StringVar()
        self.var_course=tk.StringVar()
        self.var_year=tk.StringVar()
        self.var_sem=tk.StringVar()
        self.var_std_id=tk.StringVar()
        self.var_std_name=tk.StringVar()
        self.var_batch=tk.StringVar()
        self.var_roll=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_dob=tk.StringVar()
        self.var_email=tk.StringVar()
        self.var_phn=tk.StringVar()
        self.var_radio=tk.StringVar()





        # Load and Display bg img
        img_bg = Image.open("sample images/Background image.jpg")
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = tk.Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())  # Full screen



        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((500, 105), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=105)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered



        # title
        Lbl_title=tk.Label(self.root, text="Student Management System",font= ("Gabriola", 35, "bold") if "Gabriola" in tk.font.families() else ("Times New Roman", 35, "bold"),
                            bg= "#1C1C1C", fg= "#00FF00" )
        Lbl_title.place(x=0, y=115, height=60, width=self.root.winfo_screenwidth())


        # Home Button
        img_Home = Image.open("sample images/home.jpg")
        img_Home = img_Home.resize((55,55), Image.Resampling.LANCZOS)
        self.photo_Home = ImageTk.PhotoImage(img_Home)

        btt_Home=tk.Button(Lbl_title,
                            image=self.photo_Home,
                            padx=5,pady=5,bd=0,
                            cursor="hand2",
                            command=self.home,
                            bg= "#1C1C1C",
                            activebackground="#1C1C1C",
                            fg= "#00FF00")
        btt_Home.place(relx=0.001,height=55,)


        # ========Time==========#
        time_lb=tk.Label(Lbl_title, 
                            
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tk.font.families() else ("Times New Roman", 15, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        time_lb.place(relx=0.926,height=55)

        def Time():
            string = strftime('%H:%M:%S\n%p')
            time_lb.config(text=string)
            time_lb.after(1000, Time)
        Time()




        # Left label frame
        left_frame=tk.LabelFrame(self.root,bd=3,bg="white",relief="ridge",text="Student Details",font=("Times New Roman",20,"bold"),labelanchor="n")
        left_frame.place(relx=0.25,rely=0.6,relwidth=0.469, relheight=0.7,anchor="center")

        img_leftF = Image.open("sample images/student_detail2.jpg")
        img_leftF = img_leftF.resize((580,130), Image.Resampling.LANCZOS)
        self.photo_leftF = ImageTk.PhotoImage(img_leftF)

        img_leftF_lbl = tk.Label(left_frame, image=self.photo_leftF)
        img_leftF_lbl.place(relx=0.5, rely=0.13,anchor="center", width=580, height=130)


        # Current course label frame
        curr_course_frame=tk.LabelFrame(left_frame,bd=2,bg="white",relief="ridge",text="Current Course Information",font=("Times New Roman",15,"bold"))
        curr_course_frame.place(relx=0.5, rely=0.35,anchor="center",width=580,height=95)

        # Department label & combobox
        dep_label=tk.Label(curr_course_frame,text="Department:",font=("Times New Roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,sticky="w")

        self.dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_dep,font=("Times New Roman",12),width=14,state="readonly")
        self.dep_combo["values"]=("Select Department","Computer Science","Management")
        self.dep_combo.current(0)
        # Bind the department combobox selection to a function
        self.dep_combo.bind("<<ComboboxSelected>>", self.update_course_options)
        self.dep_combo.grid(row=0,column=1,padx=2,pady=3,sticky="w")

        # Course label & combobox
        course_label=tk.Label(curr_course_frame,text="Course:",font=("Times New Roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky="w")

        self.course_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_course,font=("Times New Roman",12),width=14,state="readonly")
        self.course_combo["values"]=("Select Course","","","")
        self.course_combo.current(0)
        self.course_combo.grid(row=0,column=3,padx=2,pady=3,sticky="w")

        # year label & combobox
        year_label=tk.Label(curr_course_frame,text="Admission Year:",font=("Times New Roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,sticky="w")

        year_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("Times New Roman",12),width=14,state="readonly")
        year_combo["values"]=("Select Year","2020","2021","2022","2023","2024","2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=3,sticky="w")

        # Semester label & combobox
        Semester_label=tk.Label(curr_course_frame,text="Semester:",font=("Times New Roman",15,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=5,sticky="w")

        Semester_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_sem,font=("Times New Roman",12),width=14,state="readonly")
        Semester_combo["values"]=("Select Semester","1","2","3","4","5","6")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=3,sticky="w")


        # Class Student Information label frame
        Class_student_frame=tk.LabelFrame(left_frame,bd=2,bg="white",relief="ridge",text="Class Student Information",font=("Times New Roman",15,"bold"))
        Class_student_frame.place(relx=0.5, rely=0.625,anchor="center",width=580,height=190)

        # StudentId label & Entry
        StudentID_label=tk.Label(Class_student_frame,text="StudentID:",font=("Times New Roman",15,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,pady=3,sticky="w")

        StudentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=15,font=("Times New Roman",12),style="")
        StudentID_entry.grid(row=0,column=1,padx=3,pady=3,sticky="w")

        # Student_Name label & Entry
        StudentName_label=tk.Label(Class_student_frame,text="Student Name:",font=("Times New Roman",15,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,pady=3,sticky="w")

        StudentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=15,font=("Times New Roman",12))
        StudentName_entry.grid(row=0,column=3,padx=3,pady=3,sticky="w")

        # class division label & Entry
        batch_label=tk.Label(Class_student_frame,text="Batch:",font=("Times New Roman",15,"bold"),bg="white")
        batch_label.grid(row=1,column=0,pady=3,sticky="w")

        # class division label & Entry
        batch_combo=ttk.Combobox(Class_student_frame,width=13,
                                    textvariable=self.var_batch,
                                    font=("Times New Roman",12),
                                    state="readonly")
        batch_combo["values"]=("Select Batch","1","2")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=3,pady=3,sticky="w")

        # Roll No label & Entry
        roll_label=tk.Label(Class_student_frame,text="Roll No:",font=("Times New Roman",15,"bold"),bg="white")
        roll_label.grid(row=1,column=2,pady=3,sticky="w")

        roll_entry=ttk.Entry(Class_student_frame,width=15,textvariable=self.var_roll,font=("Times New Roman",12))
        roll_entry.grid(row=1,column=3,padx=3,pady=3,sticky="w")

        # Gender label & comboo
        gen_label=tk.Label(Class_student_frame,text="Gender:",font=("Times New Roman",15,"bold"),bg="white")
        gen_label.grid(row=2,column=0,pady=3,sticky="w")

        gen_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("Times New Roman",12),width=13,state="readonly",)
        gen_combo["values"]=("Select Gender","Male","Female","Others")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=3,pady=3,sticky="w")

        # gen_entry=ttk.Entry(Class_student_frame,width=15,font=("Times New Roman",12))
        # gen_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # DOB label & Entry
        dob_label=tk.Label(Class_student_frame,text="DOB:",font=("Times New Roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,pady=3,sticky="w")

        dob_entry=DateEntry(Class_student_frame,width=13,textvariable=self.var_dob,font=("Times New Roman",12),state="readonly",date_pattern='dd-mm-yyyy')
        dob_entry.grid(row=2,column=3,padx=3,pady=3,sticky="w")

        # email label & Entry
        email_label=tk.Label(Class_student_frame,text="Email:",font=("Times New Roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,pady=3,sticky="W")

        email_entry=ttk.Entry(Class_student_frame,width=15,textvariable=self.var_email,font=("Times New Roman",12))
        email_entry.grid(row=3,column=1,padx=3,pady=3,sticky="W")

        # Phone No label & Entry
        phone_label=tk.Label(Class_student_frame,text="Phone No:",font=("Times New Roman",15,"bold"),bg="white")
        phone_label.grid(row=3,column=2,pady=3,sticky="W")

        phone_entry=ttk.Entry(Class_student_frame,width=15,textvariable=self.var_phn,font=("Times New Roman",12))
        phone_entry.grid(row=3,column=3,padx=3,pady=3,sticky="W")

        # Radio Buttons
        button_1=ttk.Radiobutton(Class_student_frame,text="Take Photo Sample",variable=self.var_radio,value="yes")
        button_1.grid(row=6,column=0)

        button_2=ttk.Radiobutton(Class_student_frame,text="Do Not Take Photo Sample",variable=self.var_radio,value="no",)
        button_2.grid(row=6,column=2,padx=10,pady=3,sticky="W")

        # Buttons
        style1 = ttk.Style()
        style1.configure("CustomL.TButton", font=("Arial", 10, "bold"), foreground="blue", )

        save_button=ttk.Button(left_frame,text="Save",command=self.add_data,width=19,style="CustomL.TButton")
        save_button.place(relx=0.005, rely=0.89)

        update_button=ttk.Button(left_frame,text="Update",width=19,style="CustomL.TButton",command=self.update_data)
        update_button.place(relx=0.254, rely=0.89)

        del_button=ttk.Button(left_frame,text="Delete",width=19,style="CustomL.TButton",command=self.delete_data)
        del_button.place(relx=0.501, rely=0.89)

        reset_button=ttk.Button(left_frame,text="Reset",width=19,style="CustomL.TButton",
                                command=self.reset_data)
        reset_button.place(relx=0.751, rely=0.89)

        take_pic_button=ttk.Button(left_frame,command=self.generate_dataset,text="Take Photo Sample",width=35,style="CustomL.TButton")
        take_pic_button.place(relx=0.25, rely=0.85,anchor="center")

        update_pic_button=ttk.Button(left_frame,text="Update Photo Sample",width=35,style="CustomL.TButton")
        update_pic_button.place(relx=0.75, rely=0.85,anchor="center")



        # Right label frame
        right_frame=tk.LabelFrame(self.root,bd=3,bg="white",relief="ridge",text="Student Details",font=("Times New Roman",20,"bold"),labelanchor="n")
        right_frame.place(relx=0.75,rely=0.6,relwidth=0.469, relheight=0.7,anchor='center')

        img_rightF = Image.open("sample images/btnStudent.png")
        img_rightF = img_rightF.resize((580,130), Image.Resampling.LANCZOS)
        self.photo_rightF = ImageTk.PhotoImage(img_rightF)

        img_rightF_lbl = tk.Label(right_frame, image=self.photo_rightF)
        img_rightF_lbl.place(relx=0.5, rely=0.13,anchor="center", width=580, height=130)


# --------------------------------------Search System--------------------------------------- #

        # Search label frame
        search_frame=tk.LabelFrame(right_frame,bd=2,bg="white",relief="ridge",text="Search System",font=("Times New Roman",15,"bold"))
        search_frame.place(relx=0.5, rely=0.33,anchor="center",width=580,height=70)

        # search label, combobox,entry & button
        search_label=tk.Label(search_frame,text="Search by:",font=("Times New Roman",15,"bold"),fg="red",bg="white")
        search_label.grid(row=0,column=0,padx=4,pady=5,sticky="W")

        search_combo=ttk.Combobox(search_frame,font=("Times New Roman",12),width=10,state="readonly")
        search_combo["values"]=("Select","StudentID","Roll No","Others")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=4,pady=5,sticky="W")

        search_entry=ttk.Entry(search_frame,width=15,font=("Times New Roman",12))
        search_entry.grid(row=0,column=2,padx=4,pady=5,sticky="W")

        style2 = ttk.Style()
        style2.configure("CustomR.TButton", font=("Arial", 10, "bold"), foreground="red", )

        search_button=ttk.Button(search_frame,text="Save",width=14,style="CustomR.TButton")
        search_button.grid(row=0,column=3,padx=4,pady=5,sticky="W")

        Show_all_button=ttk.Button(search_frame,text="Show All",width=14,style="CustomR.TButton")
        Show_all_button.grid(row=0,column=4,padx=4,pady=5,sticky="W")

#                                       Search Table
        # Search table frame
        table_frame=tk.Frame(right_frame,bd=2,bg="white",relief="ridge")
        table_frame.place(relx=0.5, rely=0.65,anchor="center",width=580,height=235)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")

        self.student_table=ttk.Treeview(table_frame,
                                            column=("dep","course","year","sem","id","name","batch","roll","gender",'dob',"email","phn no","photo"),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side="bottom",fill="x")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.pack(side="right",fill="y")
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

        self.student_table.column("dep",width=120)
        self.student_table.column("course",width=120)
        self.student_table.column("year",width=60)
        self.student_table.column("sem",width=80)
        self.student_table.column("id",width=90)
        self.student_table.column("name",width=130)
        self.student_table.column("batch",width=75)
        self.student_table.column("roll",width=90)
        self.student_table.column("gender",width=80)
        self.student_table.column("dob",width=80)
        self.student_table.column("email",width=150)
        self.student_table.column("phn no",width=100)
        self.student_table.column("photo",width=120)

        self.student_table.pack(fill="both",expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    # ==============================================================================================================#
    # ---------------------------------------Funtion Declaration-----------------------------------------------------------#

    def add_data(self):
        if (
        self.var_dep.get() == "Select Department" or
        self.var_course.get() == "Select Course" or
        self.var_year.get() == "Select Year" or
        self.var_sem.get() == "Select Semester" or
        self.var_std_id.get() == "" or
        self.var_std_name.get() == "" or
        self.var_batch.get() == "" or
        self.var_roll.get() == "" or
        self.var_gender.get() == "Select Gender" or
        self.var_dob.get() == "" or
        self.var_email.get() == "" or
        self.var_phn.get() == "" 
        or self.var_radio.get()==""
            ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        # elif self.var_radio.get() == "no":  
        #     messagebox.showwarning("Action Required", "You have selected 'Do Not Take Photo Sample'.\nPlease select 'Take Photo Sample' to proceed.",parent=self.root)
        else:
            # messagebox.showinfo("Wait!","Data is saving",parent=self.root)
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                                         
                
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_batch.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phn.get(),
                self.var_radio.get()
                    ))                                                                         
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)                                                                                        
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # ========================= Fetch Data ========================== #

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",tk.END,values=i)
            conn.commit()
        conn.close()         


    # ------------get cursor-------
    def get_cursor(self, event=None):
        cursor_focus = self.student_table.focus()
        if not cursor_focus:
            return  # nothing selected

        content = self.student_table.item(cursor_focus)
        data = content.get("values", [])

        if len(data) != 13:  # you expect 13 fields in each row
            return

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_batch.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phn.set(data[11])
        self.var_radio.set(data[12])


    #=================== Generate data set or Take photo samples ====================# 
    def generate_dataset(self): 
        if (
        self.var_dep.get() == "Select Department" or
        self.var_course.get() == "Select Course" or
        self.var_year.get() == "Select Year" or
        self.var_sem.get() == "Select Semester" or
        self.var_std_id.get() == "" or
        self.var_std_name.get() == "" or
        self.var_batch.get() == "" or
        self.var_roll.get() == "" or
        self.var_gender.get() == "Select Gender" or
        self.var_dob.get() == "" or
        self.var_email.get() == "" or
        self.var_phn.get() == "" 
        or self.var_radio.get()==""
            ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_radio.get() == "no":  
            messagebox.showwarning("Action Required", "You have selected 'Do Not Take Photo Sample'.\nPlease select 'Take Photo Sample' to proceed.",parent=self.root)
        else:
            # messagebox.showinfo("Wait!","Data is saving",parent=self.root)
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s," \
                    "Name=%s,batch=%s,roll=%s,gen=%s,dob=%s,email=%s,phn=%s,photo=%s where S_ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_batch.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phn.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()
                    ))                                                                        
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()  

                #-------------------Load predefined data on face frontals from opencv------------------#  
                    
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                video_cap = cv2.VideoCapture(0)  # 0 for the default camera
                img_id = 0
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3,minNeighbors= 5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                        return img[y:y+h, x:x+w]
                    return None


                # def run_camera():
                while True:

                    ret, my_frame = video_cap.read()
                    cropped = face_cropped (my_frame)
                    if cropped is  not None:
                        img_id += 1
                        face=cv2.resize(my_frame, (450, 450))  # Resize frame to 450x450 pixels
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert color from BGR to grayscale
                        file_name_path ="face_img/user." + str(id) + "." + str(img_id) +".jpg"
                        cv2.imwrite(file_name_path, face)  # Save the cropped face image
                        cv2.putText(face,str(img_id),(50,50) ,cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)  # Display the cropped face

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Press 'q' to exit or after capturing 100 images
                        break
                video_cap.release()  # Release the camera
                cv2.destroyAllWindows()  # Close all OpenCV windows
                messagebox.showinfo("Success","Data has been saved successfully",parent=self.root)

                # threading.Thread(target=run_camera, daemon=True).start()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)            

# ========== Button Function ================= #

    def reset_data(self):
        self.var_dep.set( "Select Department"),
        self.var_course.set( "Select Course"),
        self.var_year.set( "Select Year"),
        self.var_sem.set( "Select Semester"),
        self.var_std_id.set( ""),
        self.var_std_name.set( ""),
        self.var_batch.set("Select Batch"),
        self.var_roll.set( ""),
        self.var_gender.set( "Select Gender"),
        # self.var_dob.set(""),
        self.var_email.set( ""),
        self.var_phn.set( ""),
        self.var_radio.set(""),


    def update_data(self):
        if (
        self.var_dep.get() == "Select Department" or
        self.var_course.get() == "Select Course" or
        self.var_year.get() == "Select Year" or
        self.var_sem.get() == "Select Semester" or
        self.var_std_id.get() == "" or
        self.var_std_name.get() == "" or
        self.var_batch.get() == "" or
        self.var_roll.get() == "" or
        self.var_gender.get() == "Select Gender" or
        self.var_dob.get() == "" or
        self.var_email.get() == "" or
        self.var_phn.get() == "" 
        or self.var_radio.get()==""
            ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update this student details")
                if update>0:
                    conn = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s," \
                    "Name=%s,batch=%s,roll=%s,gen=%s,dob=%s,email=%s,phn=%s,photo=%s where S_ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_batch.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phn.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student Details Updated Successflly.")
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error",f"cannot update due to:\n{str(es)}")


    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete data.", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete data","Do you want to delete this student details")
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', user='root', password= 'P@ssword4SQL',database='face-recognition-attendance-system')
                    my_cursor=conn.cursor()
                    sql="delete from student where S_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student Details Deleted Successflly.")
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error",f"cannot delete due to:\n{str(es)}")



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
    root = tk.Tk()
    # root.config(bg="#f2f3f7")
    app = Student(root)
    root.mainloop()