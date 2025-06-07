# import itertools
# from tkinter import *
# import PIL
# from PIL import Image, ImageTk
# import PIL.GifImagePlugin

# class Log_in:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Face Recognition System")
#         self.root.state("zoomed")

#         # --- load the GIF as individual frames ---------------------------------
#         gif = Image.open("sample images/01bg.gif")

#         frames  = []
#         widths  = self.root.winfo_screenwidth()
#         heights = self.root.winfo_screenheight()

#         try:
#             while True:                      # extract every frame
#                 frame = gif.copy().resize((widths, heights), Image.Resampling.LANCZOS)
#                 frames.append(ImageTk.PhotoImage(frame))
#                 gif.seek(len(frames))        # go to next frame
#         except EOFError:
#             pass                             # ran out of frames

#         self.frames_cycle = itertools.cycle(frames)  # endless iterator

#         # --- label that will hold the background -------------------------------
#         self.bg_lbl = Label(self.root, bd=0)
#         self.bg_lbl.place(x=0, y=0, width=widths, height=heights)

#         self.animate_background()            # kick-off animation

#     # ---------------------------------------------------------------------------
#     def animate_background(self):
#         self.bg_lbl.configure(image=next(self.frames_cycle))
#         # call myself again after the GIF’s own delay (or 100 ms if unavailable)
#         delay = getattr(Image.open, "info", {}).get("duration", 100)
#         self.root.after(delay, self.animate_background)

# # -------------------------------------------------------------------------------
# if __name__ == "__main__":
#     root = Tk()
#     app = Log_in(root)
#     root.mainloop()





# from tkinter import *

# class Log_in:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Face Recognition System")
#         self.root.state("zoomed")

#         # Load animated GIF using Tkinter's PhotoImage
#         self.bg_gif = PhotoImage(file="sample images/high-tech-computer-futuristic-binary-code-4k-data-92gn7sxocfuxjd2d.gif")

#         # Create label with GIF
#         self.bg_lbl = Label(self.root, image=self.bg_gif)
#         self.bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

#     def toggle_fullscreen(self):
#         if self.root.attributes('-fullscreen'):
#             self.root.attributes('-fullscreen', False)
#             self.root.state('zoomed')
#         else:
#             self.root.attributes('-fullscreen', True)

# if __name__ == "__main__":
#     root = Tk()
#     app = Log_in(root)
#     root.mainloop()



# import customtkinter as ctk

# # ctk.set_appearance_mode("light")
# # ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.geometry("800x600")
# app.configure(bg="white")


# frame = ctk.CTkFrame(master=app, width=400, height=250, corner_radius=20, fg_color="lightblue")
# frame.place(relx=0.5, rely=0.5, anchor="center")
# frame.pack_propagate(False)  

# # Add a test label
# label = ctk.CTkLabel(master=frame, text="Test Frame", font=("Arial", 20))
# label.pack(pady=20)

# app.mainloop()





# import customtkinter as ctk

# # ctk.set_appearance_mode("light")
# # ctk.set_default_color_theme("blue")

# root = ctk.CTk()
# root.geometry("300x150")

# entry = ctk.CTkEntry(root, corner_radius=15, width=200, height=40, placeholder_text="Rounded Entry")
# entry.place(x=100,y=500)

# root.mainloop()
