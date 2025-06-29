# import tkinter as tk
# from tkinter import ttk,messagebox
# import tkinter.font as tkfont
# from PIL import Image,ImageTk
# from time import strftime



# class HelpDesk:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Face Recognition System")
#         # Make the window start in fullscreen mode
#         self.root.attributes('-fullscreen', True)
#         # Bind the Escape key to exit fullscreen
#         self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
#         self.root.resizable(False,False)



#         # Load and Display background image
#         img_bg = Image.open(r"sample images\Background image.jpg")
#         img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), 
#                                     Image.Resampling.LANCZOS)
#         self.photo_bg = ImageTk.PhotoImage(img_bg)

#         bg_lbl = tk.Label(self.root, image=self.photo_bg)
#         bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), 
#                         height=self.root.winfo_screenheight())
#         bg_lbl.lower()



#         # Load and Display Logo
#         img_logo = Image.open("sample images/IITP Name&Logo.png")
#         img_logo = img_logo.resize((500, 115), Image.Resampling.LANCZOS)
#         self.photo_logo = ImageTk.PhotoImage(img_logo)

#         l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
#         l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)  # Full width
#         l_lbl.config(anchor="center")   # Make the logo centered



#             # title
#         lab_title=tk.Label(self.root, 
#                             text="Help Desk", 
#                             font= ("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"), 
#                             bg= "#1C1C1C", 
#                             fg= "#00FF00" )
#         lab_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


#         # Home Button
#         img_Home = Image.open("sample images/home.jpg")
#         img_Home = img_Home.resize((55,55), Image.Resampling.LANCZOS)
#         self.photo_Home = ImageTk.PhotoImage(img_Home)

#         btt_Home=tk.Button(lab_title,
#                             image=self.photo_Home,
#                             padx=5,pady=5,bd=0,
#                             cursor="hand2",
#                             command=self.home,
#                             activebackground="#1C1C1C",
#                             bg= "#1C1C1C",
#                             fg= "#00FF00")
#         btt_Home.place(relx=0.001,height=55,)


#         # ========Time==========#
#         time_lb=tk.Label(lab_title,
#                             font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
#                             bg= "#1C1C1C", 
#                             fg= "#00FF00" )

#         time_lb.place(relx=0.926,height=55)

#         def Time():
#             string = strftime('%H:%M:%S\n%p')
#             time_lb.config(text=string)
#             time_lb.after(1000, Time)
#         Time()



#     # # -----------------------------------------------Creating Buttons-------------------------------------------#

#         # User Manual details button
#         btn_manual = self.create_button("sample images/manual2.jpg", 
#                                         "User Manual",
#                                         self.unavailabel, 0.15, 0.45)
        


#         # FAQs button
#         btn_FAQ = self.create_button("sample images/FAQ.png", 
#                                         "FAQs",
#                                     self.unavailabel, 0.385, 0.45)
        


#         # About button
#         btn_About = self.create_button("sample images/about.png", 
#                                     "About",
#                                     self.unavailabel, 0.62, 0.45)
        


#         # chatbot button
#         btn_chatbot = self.create_button("sample images/chatbot.jpeg", 
#                                         "ChatBot" ,
#                                         self.not_ready, 0.855, 0.45)
        


#         # Send Feedback / Rating button
#         btn_Feedback = self.create_button("sample images/feedback.jpg", 
#                                         "Send Feedback",
#                                         self.not_ready, 0.15, 0.8)
        


#         # Suggestion button
#         btn_suggest = self.create_button("sample images/suggestion.jpg", 
#                                         "Help us Improve",
#                                         self.not_ready, 0.385 , 0.8)
        


#         # Contact button
#         btn_Contact = self.create_button("sample images/contact.png", 
#                                         "Contact Support",
#                                         self.unavailabel, 0.62 , 0.8)
        


#         # Exit button
#         btn_Exit = self.create_button("sample images/exit.jpg", 
#                                         "Exit",
#                                         self.confirm_exit, 0.855 , 0.8)





#     # -----------------------------------------------Button Functions-------------------------------------------#

#     # not availabel functions
#     def not_ready(self):
#         messagebox.showinfo("Info", "This feature is under development.")
    
#     def unavailabel(self):
#         msg = messagebox.askretrycancel(title= "404 Error!",message="Temporarily unavailabel.\nPlease try again later.")
#         if msg:
#             self.unavailabel()
#         else:
#             return

#     '''-------------------------------------------------------------'''

#     # Home button
#     def home(self):
#         from main import Face_Recognition_System
#         self.clear_window()                          # Clear current UI
#         self.app = Face_Recognition_System(self.root)       # Load Home UI in new window


#     # Exit Button
#     def confirm_exit(self):
#         confirm_exit = messagebox.askyesnocancel(
#             "Face Recognition Attendance System",
#             "Your session seems to be going well.\nAre you sure you want to exit the Face Recognition System?")
#         if confirm_exit:
#             self.root.destroy()
#         else:
#             return



# # ------------- button creation function -------------- #
#     def create_button(self, image_path, text, command, relx, rely):
#         img = Image.open(image_path).resize((200, 200), Image.Resampling.LANCZOS)
#         photo = ImageTk.PhotoImage(img)
#         btn = tk.Button(self.root, image=photo, text=text, compound="top",
#                         font=("Gabriola", 20, "bold"), bg="#1C1C1C", fg="#00FF00",
#                         cursor="hand2", relief=tk.RAISED, command=command)
#         btn.image = photo  # Store a reference
#         # btn.place(x=x, y=y, width=200, height=245)
#         btn.place(relx=relx, rely=rely, anchor="center", width=200, height=245)






#     def toggle_fullscreen(self):
#         """Toggle between fullscreen and maximized mode"""
#         if self.root.attributes('-fullscreen'):  # If currently fullscreen
#             self.root.attributes('-fullscreen', False)  # Exit fullscreen
#             self.root.state('zoomed')  # Maximize window to fit screen
#         else:
#             self.root.attributes('-fullscreen', True)  # Go back to fullscreen



#     def clear_window(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()



# if __name__ == "__main__":
#     root = tk.Tk()
#     # root.config(bg="#1C1C1C")
#     app = HelpDesk(root)
#     root.mainloop()


# Ensure output directory exists
import os
import cv2

if not os.path.exists("face_img"):
    os.makedirs("face_img")

cap = cv2.VideoCapture(0)
img_id = 0

while True:
    ret, my_frame = cap.read()
    if not ret:
        break

    cropped = face_cropped(my_frame)
    if cropped is not None:
        img_id += 1
        face = cv2.resize(cropped, (450, 450))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        file_name_path = f"face_img/user.{id}.{img_id}.jpg"
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(img_id), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Cropped Face", face)  # Show cropped face only

    if cv2.waitKey(1) == 13 or img_id == 100:  # Stop when Enter is pressed or 100 images captured
        break

cap.release()
cv2.destroyAllWindows()
