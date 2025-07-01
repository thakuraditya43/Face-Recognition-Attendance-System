import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import filedialog
import os
import csv

mydata=[]   # List to store attendance data imported from or to be exported as CSV

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
        self.std_id_var=tk.StringVar()
        self.std_name_var=tk.StringVar()
        self.dep_var=tk.StringVar()
        self.course_var=tk.StringVar()
        self.sem_var=tk.StringVar()
        self.batch_var=tk.StringVar()
        self.date_var=tk.StringVar()
        self.time_var=tk.StringVar()
        self.attendance_var=tk.StringVar()


        # Load and display background images
        img_bg = Image.open(r"sample images\Background image.jpg")
        img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), 
                                    Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = tk.Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), 
                        height=self.root.winfo_screenheight())  # Full screen



        # Load and Display Logo
        img_logo = Image.open("sample images/IITP Name&Logo.png")
        img_logo = img_logo.resize((500, 105), Image.Resampling.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=105)  # Full width
        l_lbl.config(anchor="center")   # Make the logo centered



        # Create and configure the title and Home button
        Lbl_title=tk.Label(self.root, 
                            text="Attendance Management System",
                            font= ("Monotype Corsiva", 35, "bold") if "Monotype Corsiva" in tk.font.families() else ("Times New Roman", 35, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
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
                            activebackground="#1C1C1C",
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_Home.place(x=0,y=0,width=55,height=55)


        # ========Time==========#
        time_lb=tk.Label(Lbl_title, 
                            
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tk.font.families() else ("Times New Roman", 15, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        time_lb.place(x=1190,y=0,height=55)

        def Time():
            string = strftime('%H:%M:%S\n%p')
            time_lb.config(text=string)
            time_lb.after(1000, Time)
        Time()



        # Left frame for student attendance entry form
        left_frame=tk.LabelFrame(self.root,bd=3,bg="white",relief="ridge",text="Student Attendance Details",font=("Times New Roman",20,"bold"),labelanchor="n")
        left_frame.place(relx=0.25,rely=0.6,relwidth=0.469, relheight=0.65,anchor="center")

        img_leftF = Image.open("sample images/Attendance.jpg")
        img_leftF = img_leftF.resize((580,130), Image.Resampling.LANCZOS)
        self.photo_leftF = ImageTk.PhotoImage(img_leftF)

        img_leftF_lbl = tk.Label(left_frame, image=self.photo_leftF)
        img_leftF_lbl.place(relx=0.5, rely=0.15,anchor="center", width=580, height=130)



        # Class Student Information label frame
        Class_student_frame=tk.Frame(left_frame,bd=2,bg="white",
                                    relief="ridge",
                                    # text="Class Student Information",
                                    # font=("Times New Roman",15,"bold")
                                    )
        Class_student_frame.place(relx=0.5, rely=0.625,anchor="center",width=580,height=290)

        # StudentId label & Entry
        StudentID_label=tk.Label(Class_student_frame,
                                text="StudentID:",
                                font=("Times New Roman",15,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,pady=5,padx=3,sticky="W")

        StudentID_entry=ttk.Entry(Class_student_frame,
                                    textvariable=self.std_id_var,
                                    width=15,font=("Times New Roman",12),style="")
        StudentID_entry.grid(row=0,column=1,padx=3,pady=5,sticky="w")

        # Student_Name label & Entry
        StudentName_label=tk.Label(Class_student_frame,
                                text="Student Name:",
                                font=("Times New Roman",15,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,pady=5,padx=3,sticky="w")

        StudentName_entry=ttk.Entry(Class_student_frame,
                                    textvariable=self.std_name_var,
                                    width=15,font=("Times New Roman",12))
        StudentName_entry.grid(row=0,column=3,padx=3,pady=5,sticky="w")

        # Department label & combobox
        dep_label=tk.Label(Class_student_frame,text="Department:",font=("Times New Roman",15,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=3,pady=5,sticky="W")

        self.dep_combo=ttk.Combobox(Class_student_frame,
                                textvariable=self.dep_var,
                                font=("Times New Roman",12),width=13,state="readonly")
        self.dep_combo["values"]=("Select Department","Computer Science","Management")
        self.dep_combo.current(0)
        # Bind the department combobox selection to a function
        self.dep_combo.bind("<<ComboboxSelected>>", self.update_course_options)
        self.dep_combo.grid(row=1,column=1,padx=3,pady=5,sticky="W")

        # Course label & combobox
        course_label=tk.Label(Class_student_frame,text="Course:",font=("Times New Roman",15,"bold"),bg="white")
        course_label.grid(row=1,column=2,padx=3,pady=5,sticky="W")

        self.course_combo=ttk.Combobox(Class_student_frame,
                                    textvariable=self.course_var,
                                    font=("Times New Roman",12),width=13,state="readonly")
        self.course_combo["values"]=("Select Course",)
        self.course_combo.current(0)
        self.course_combo.grid(row=1,column=3,padx=3,pady=5,sticky="W")


        # Semester label & combobox
        Semester_label=tk.Label(Class_student_frame,text="Semester:",font=("Times New Roman",15,"bold"),bg="white")
        Semester_label.grid(row=2,column=0,padx=3,pady=5,sticky="W")

        Semester_combo=ttk.Combobox(Class_student_frame,
                                    textvariable=self.sem_var,
                                    font=("Times New Roman",12),width=13,
                                    state="readonly")
        Semester_combo["values"]=("Select Semester","1","2","3","4","5","6")
        Semester_combo.current(0)
        Semester_combo.grid(row=2,column=1,padx=3,pady=5,sticky="W")


        batch_label=tk.Label(Class_student_frame,text="Batch:",
                                font=("Times New Roman",15,"bold"),bg="white")
        batch_label.grid(row=2,column=2,pady=5,padx=3,sticky="w")

        batch_combo=ttk.Combobox(Class_student_frame,width=13,
                                    textvariable=self.batch_var,
                                    font=("Times New Roman",12),
                                    state="readonly")
        batch_combo["values"]=("Select Batch","1","2")
        batch_combo.current(0)
        batch_combo.grid(row=2,column=3,padx=3,pady=5,sticky="W")


        # Date & Time label & Entry

        date_label=tk.Label(Class_student_frame,text="Date:",
                            font=("Times New Roman",15,"bold"),bg="white")
        date_label.grid(row=3,column=0,padx=3,pady=5,sticky="W")

        date_entry=DateEntry(Class_student_frame,width=13,
                                textvariable=self.date_var,
                                font=("Times New Roman",12),state="readonly",date_pattern='dd-mm-yyyy')
        date_entry.grid(row=3,column=1,padx=3,pady=5,sticky="W")


        Time_label=tk.Label(Class_student_frame,
                                text="Time:",
                                font=("Times New Roman",15,"bold"),bg="white")
        Time_label.grid(row=3,column=2,pady=5,padx=3,sticky="W")

        Time_entry=ttk.Entry(Class_student_frame,
                                    textvariable=self.time_var,
                                    width=15,font=("Times New Roman",12),style="")
        Time_entry.grid(row=3,column=3,padx=3,pady=5,sticky="W")


        # Attendance Status label & comboo
        status_label=tk.Label(Class_student_frame,text="Attendance Status:",
                        font=("Times New Roman",15,"bold"),bg="white")
        status_label.grid(row=4,column=0,pady=5,padx=3,sticky="W")

        status_combo=ttk.Combobox(Class_student_frame,
                                textvariable=self.attendance_var,
                                font=("Times New Roman",12),width=13,state="readonly")
        status_combo["values"]=("Select Status", "Present", "Absent", "Late", "Excused")
        status_combo.current(0)
        status_combo.grid(row=4,column=1,padx=3,pady=5,sticky="W")



        # Buttons to import, export, update, and reset attendance data
        style1 = ttk.Style()
        style1.configure("CustomL.TButton", font=("Arial", 10, "bold"), foreground="blue", )

        import_button=ttk.Button(Class_student_frame,text="Import CSV",
                    command=self.importCSV,width=18,style="CustomL.TButton")
        import_button.place(x=5,y=255)

        export_button=ttk.Button(Class_student_frame,text="Export CSV",width=18,
                                command=self.exportCSV,style="CustomL.TButton")
        export_button.place(x=148,y=255)

        update_button=ttk.Button(Class_student_frame,text="Update",width=18,
                                    style="CustomL.TButton",command=self.update_data)
        update_button.place(x=292,y=255)

        reset_button=ttk.Button(Class_student_frame,text="Reset",width=18,style="CustomL.TButton",
                                command=self.reset_data)
        reset_button.place(x=435,y=255)



        # Right frame for displaying the attendance report in a table
        right_frame=tk.LabelFrame(self.root,bd=3,bg="white",relief="ridge",text="Attendance Details",font=("Times New Roman",20,"bold"),labelanchor='n')
        right_frame.place(relx=0.75,rely=0.6,relwidth=0.469, relheight=0.65,anchor='center')


#                                       Search Table
        # Search table frame
        table_frame=tk.Frame(right_frame,bd=2,bg="white",relief="ridge")
        table_frame.place(x=10,y=5,width=575,height=470)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")


        self.AttendanceReport_Table=ttk.Treeview(table_frame,
                                            column=("id","name","dep","course","sem","batch",'date',"time","atten"),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side="bottom",fill="x")
        scroll_x.config(command=self.AttendanceReport_Table.xview)
        scroll_y.pack(side="right",fill="y")
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
        self.AttendanceReport_Table.column("dep",width=150)
        self.AttendanceReport_Table.column("course",width=150)
        self.AttendanceReport_Table.column("sem",width=75)
        self.AttendanceReport_Table.column("batch",width=75)
        self.AttendanceReport_Table.column("date",width=100)
        self.AttendanceReport_Table.column("time",width=100)
        self.AttendanceReport_Table.column("atten",width=100)

        self.AttendanceReport_Table.pack(fill="both",expand=1)

        # Bind event to fill form when a row is selected
        self.AttendanceReport_Table.bind("<ButtonRelease>",self.get_cursor)



    # ==================================Fetch Data===================
    
    # Display provided rows of attendance data in the table
    def fetchData(self,rows):
        self.AttendanceReport_Table.delete(*self.AttendanceReport_Table.get_children())
        for i in rows:
            self.AttendanceReport_Table.insert("",tk.END,values=i)


    # Open a file dialog to import attendance data from a CSV file
    def importCSV(self):
        global mydata
        mydata.clear() 
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if not fln:
            return
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 


    # Export current attendance data to a CSV file
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export.", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",
                filetypes=[("CSV File", ".csv"), ("All Files", ".*")],defaultextension=".csv",
                parent=self.root)
            if not fln:
                return  # User cancelled save dialog
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)  # Changed from exp_write.append(i)
            messagebox.showinfo("Export Successful", "Attendance data has been exported successfully.", parent=self.root)
        except Exception as es:
            messagebox.showerror("Export Failed", f"Failed to export data.\nReason: {str(es)}", parent=self.root)


# Fills entry fields with selected row data from the table
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport_Table.focus()
        content=self.AttendanceReport_Table.item(cursor_row)
        rows=content['values']
        self.std_id_var.set(rows[0])
        self.std_name_var.set(rows[1])
        self.dep_var.set(rows[2])
        self.course_var.set(rows[3])
        self.sem_var.set(rows[4])
        self.batch_var.set(rows[5])
        self.date_var.set(rows[6])
        self.time_var.set(rows[7])
        self.attendance_var.set(rows[8])


    def update_data(self):
        updated = False
        for index, row in enumerate(mydata):
            if row[0] == self.std_id_var.get():
                mydata[index] = [
                    self.std_id_var.get(), self.std_name_var.get(), self.dep_var.get(),
                    self.course_var.get(), self.sem_var.get(), self.batch_var.get(),
                    self.date_var.get(), self.time_var.get(), self.attendance_var.get()
                ]
                updated = True
                break
        if updated:
            self.fetchData(mydata)
            messagebox.showinfo("Update Successful", "Attendance record has been updated successfully.", parent=self.root)
        else:
            messagebox.showerror("Update Failed", "No matching Student ID found in the data.", parent=self.root)


    # Clear all entry fields in the attendance form
    def reset_data(self):
        self.std_id_var.set("")
        self.std_name_var.set("")
        self.dep_var.set("Select Department")
        self.course_var.set("Select Course")
        self.sem_var.set("Select Semester")
        self.batch_var.set("Select Batch")
        self.date_var.set("")
        self.time_var.set("")
        self.attendance_var.set("Select Status")


    # Update course dropdown based on selected department
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
    root = tk.Tk()
    # root.config(bg="#f2f3f7")
    app = Attendance(root)
    root.mainloop()