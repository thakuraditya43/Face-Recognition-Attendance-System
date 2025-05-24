from tkinter import *
# import tkinter
import tkinter.messagebox as tkm
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime


class Help_desk:
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
                            text="Help Desk",
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





        # User Manual button
        img_Manual = Image.open("sample images/manual2.jpg")
        img_Manual = img_Manual.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Manual = ImageTk.PhotoImage(img_Manual)

        btt_Manual=Button(self.root,
                            image=self.photo_Manual,
                            text="User Manual",
                            compound="top",
                            command=self.Unavailable,
                            relief=RAISED,cursor="hand2",
                            font= ("Gabriola", 20, "bold"),
                            bg= "#1C1C1C",
                            fg= "#00FF00")
        btt_Manual.place(x=100,y=200,width=200,height=245)



        # FAQs button
        img_FAQ = Image.open("sample images/FAQ.png")
        img_FAQ = img_FAQ.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_FAQ = ImageTk.PhotoImage(img_FAQ)

        btt_FAQ=Button(self.root,
                            image=self.photo_FAQ,
                            relief=RAISED,
                            cursor="hand2",
                            text="FAQs",
                            compound="top",
                            font= ("Gabriola", 20, "bold"),
                            bg= "#1C1C1C", fg= "#00FF00",command=self.Unavailable)
        btt_FAQ.place(x=400,y=200,width=200,height=245)



        # About button
        img_About = Image.open("sample images/about.png")
        img_About = img_About.resize((190,190), Image.Resampling.LANCZOS)
        self.photo_About = ImageTk.PhotoImage(img_About)

        btt_About=Button(self.root,
                        image=self.photo_About,
                        relief=RAISED,
                        text="About",
                        compound="top",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",
                        command=self.Unavailable)
        btt_About.place(x=700,y=200,width=200,height=245)



        # chatbot button
        img_chat = Image.open("sample images/chatbot.jpeg")
        img_chat = img_chat.resize((195,195), Image.Resampling.LANCZOS)
        self.photo_chat = ImageTk.PhotoImage(img_chat)

        btt_chat=Button(self.root,
                        image=self.photo_chat,
                        relief=RAISED,
                        compound="top",
                        text="ChatBot",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",
                        command=self.Not_ready)
        btt_chat.place(x=1000,y=200,width=200,height=245)



        # Send Feedback / Rating button
        img_Feedback = Image.open("sample images/feedback.jpg")
        img_Feedback = img_Feedback.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Feedback = ImageTk.PhotoImage(img_Feedback)

        btt_Feedback=Button(self.root,
                        image=self.photo_Feedback,
                        relief=RAISED,
                        compound="top",
                        text="Send Feedback",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",command=self.Not_ready)
        btt_Feedback.place(x=100,y=500,width=200,height=245)



        # Suggestion button
        img_suggest = Image.open("sample images/suggestion.jpg")
        img_suggest = img_suggest.resize((195,195), Image.Resampling.LANCZOS)
        self.photo_suggest = ImageTk.PhotoImage(img_suggest)

        btt_suggest=Button(self.root,
                        image=self.photo_suggest,
                        relief=RAISED,
                        text="Help us Improve",
                        compound="top",
                        font= ("Gabriola", 20, "bold"),
                        bg= "#1C1C1C",
                        fg= "#00FF00",
                        cursor="hand2",command=self.Not_ready)
        btt_suggest.place(x=400,y=500,width=200,height=245)



        # Contact Support button
        img_Contact = Image.open("sample images/contact.png")
        img_Contact = img_Contact.resize((200,200), Image.Resampling.LANCZOS)
        self.photo_Contact = ImageTk.PhotoImage(img_Contact)

        btt_Contact=Button(self.root,
                            image=self.photo_Contact,
                            text="Contact Support",
                            font= ("Gabriola", 20, "bold"), 
                            bg= "#1C1C1C",
                            compound="top",
                            fg= "#00FF00",
                            relief=RAISED,
                            cursor="hand2",
                            command=self.Unavailable)
        btt_Contact.place(x=700,y=500,width=200,height=245)



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



    # not available functions
    def Not_ready(self):
            tkm.showerror("Error", "OOPS!!\nNot ready yet")
    
    def Unavailable(self):
        msg = tkm.askretrycancel(title= "404 Error !",message="Temporarily unavailable.\nPlease try again later.")
        if msg:
            self.Unavailable()
        else:
            return




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
        confirm_exit = tkm.askyesnocancel(
            "Face Recognition Attendance System",
            "Hope you had a smooth session!\nWould you like to exit now?")
        if confirm_exit:
            self.root.destroy()
        else:
            return





    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = Tk()
    # root.config(bg="#1C1C1C")
    app = Help_desk(root)
    root.mainloop()