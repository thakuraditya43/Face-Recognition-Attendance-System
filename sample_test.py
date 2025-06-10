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
#         # call myself again after the GIF’s own delay (or 100 ms if unavailabel)
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























# import tkinter as tk
# from tktimepicker import AnalogPicker, AnalogThemes
# # note: you can also make use of mouse wheel or keyboard to scroll or enter the spin timepicker
# root = tk.Tk()

# time_picker = AnalogPicker(root)
# time_picker.pack(expand=True, fill="both")

# theme = AnalogThemes(time_picker)
# theme.setDracula()

# root.mainloop()






# import tkinter as tk
# from tkinter import ttk
# from tkinter import simpledialog

# class TimePickerDialog(simpledialog.Dialog):
#     def body(self, master):
#         self.title("Pick Your Time Slot")
#         ttk.Label(master, text="Hour:").grid(row=0, column=0, padx=5, pady=5)
#         ttk.Label(master, text="Minute:").grid(row=1, column=0, padx=5, pady=5)

#         self.hour_var = tk.StringVar(value="12")
#         self.minute_var = tk.StringVar(value="00")

#         self.hour_spinbox = ttk.Spinbox(master, from_=0, to=23, wrap=True, textvariable=self.hour_var, width=5, format="%02.0f")
#         self.minute_spinbox = ttk.Spinbox(master, from_=0, to=59, wrap=True, textvariable=self.minute_var, width=5, format="%02.0f")

#         self.hour_spinbox.grid(row=0, column=1, padx=5, pady=5)
#         self.minute_spinbox.grid(row=1, column=1, padx=5, pady=5)
#         return self.hour_spinbox  # initial focus

#     def apply(self):
#         self.result = f"{int(self.hour_var.get()):02d}:{int(self.minute_var.get()):02d}"

# def main():
#     root = tk.Tk()
#     root.title("Tkinter Time Picker Example")
#     root.geometry("300x150")

#     def open_time_picker():
#         dialog = TimePickerDialog(root)
#         if dialog.result:
#             result_label.config(text=f"Selected time: {dialog.result}")

#     pick_time_button = ttk.Button(root, text="Pick Time", command=open_time_picker)
#     pick_time_button.pack(pady=20)

#     result_label = ttk.Label(root, text="Selected time: None")
#     result_label.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()



'''-------------------------------------------------------------------------------'''
# import tkinter as tk  # Import Tkinter for GUI
# from tkinter import ttk  # Import themed widgets
# from tktimepicker import AnalogPicker, AnalogThemes  # Import time picker module

# class TimePickerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Time Picker")  # Set window title

#         # Header Label
#         self.label = tk.Label(root, text="Pick your time slot", font=("Arial", 16))
#         self.label.pack(pady=10)  # Add space around label
        
#         # Frame to group time entry components
#         self.time_frame = tk.Frame(root)
#         self.time_frame.pack(pady=10)  # Add spacing
        
#         # Variables to store hour and minute (default values)
#         self.hour_var = tk.StringVar(value="11")
#         self.minute_var = tk.StringVar(value="05")
        
#         # Hour Entry Field
#         self.hour_entry = tk.Entry(self.time_frame, textvariable=self.hour_var, width=2, font=("Arial", 24))
#         self.hour_entry.grid(row=0, column=0)  # Place in first column
        
#         # Colon separator between hour and minutes
#         self.colon_label = tk.Label(self.time_frame, text=":", font=("Arial", 24))
#         self.colon_label.grid(row=0, column=1)  # Center between entries
        
#         # Minute Entry Field
#         self.minute_entry = tk.Entry(self.time_frame, textvariable=self.minute_var, width=2, font=("Arial", 24))
#         self.minute_entry.grid(row=0, column=2)  # Place in third column

#         # Initialize Analog Picker
#         self.analog_picker = AnalogPicker(root)
#         # self.analog_picker.configure(theme=AnalogThemes.dark)  # Set dark theme
#         theme = AnalogThemes(self.analog_picker)
#         theme.setDracula()  # or theme.setClassic()

#         self.analog_picker.pack(pady=20)  # Add spacing below time entry

# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TimePickerApp(root)
#     root.mainloop()



'''===================================================================================='''


# import tkinter as tk
# from tkinter import ttk
# from tktimepicker import AnalogPicker, AnalogThemes

# class TimePickerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Time Picker")

#         tk.Label(root, text="Pick your time slot", font=("Arial", 16)).pack(pady=10)

#         self.time_frame = tk.Frame(root)
#         self.time_frame.pack(pady=10)

#         self.hour_var = tk.StringVar(value="11")
#         self.minute_var = tk.StringVar(value="05")
#         self.ampm_var = tk.StringVar(value="AM")

#         self.hour_entry = tk.Spinbox(self.time_frame, wrap=True,state="readonly", from_=1, to=12, textvariable=self.hour_var, width=2, font=("Arial", 24), format="%02.0f")
#         self.hour_entry.grid(row=0, column=0)

#         tk.Label(self.time_frame, text=":", font=("Arial", 24)).grid(row=0, column=1)

#         self.minute_entry = tk.Spinbox(self.time_frame, wrap=True,state="readonly", from_=0, to=59, textvariable=self.minute_var, width=2, font=("Arial", 24), format="%02.0f")
#         self.minute_entry.grid(row=0, column=2)

#         self.ampm_spin = tk.Spinbox(self.time_frame, values=("AM", "PM"), textvariable=self.ampm_var, width=4, font=("Arial", 18), wrap=True,state="readonly")
#         self.ampm_spin.grid(row=0, column=3, padx=10)

#         self.analog_picker = AnalogPicker(root)
#         theme = AnalogThemes(self.analog_picker)
#         theme.setDracula()
#         self.analog_picker.pack(pady=20)

#         self.previous_time = None
#         self.poll_analog_time()

#         tk.Button(root, text="Print Time", command=self.get_time).pack(pady=10)

#     def poll_analog_time(self):
#         try:
#             analog_time = self.analog_picker.time()
#             if isinstance(analog_time, tuple) and len(analog_time) == 3:
#                 hour, minute, ampm = analog_time
#                 if self.previous_time != (hour, minute, ampm):
#                     self.previous_time = (hour, minute, ampm)
#                     self.hour_var.set(f"{hour:02}")
#                     self.minute_var.set(f"{minute:02}")
#                     self.ampm_var.set(ampm)
#                     self.minute_entry.focus_set()
#         except Exception as e:
#             print("Polling error:", e)

#         self.root.after(500, self.poll_analog_time)

#     def get_time(self):
#         manual_time = f"{self.hour_var.get()}:{self.minute_var.get()} {self.ampm_var.get()}"
#         print("Manual Time Entry:", manual_time)

#         try:
#             hour, minute, ampm = self.analog_picker.time()
#             analog_time = f"{hour:02}:{minute:02} {ampm}"
#             print("Analog Picker Time:", analog_time)
#         except Exception as e:
#             print("Error retrieving analog time:", e)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TimePickerApp(root)
#     root.mainloop()

"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
import tkinter as tk
import math

class AnalogPicker(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=200, height=200, **kwargs)
        self.hour = 12
        self.minute = 0
        self.ampm = "AM"
        self.draw_clock()

    def set_time(self, hour, minute, ampm):
        """Update internal state and redraw clock based on manual input."""
        try:
            self.hour = int(hour) % 12 if int(hour) != 12 else 12
            self.minute = int(minute) % 60
            self.ampm = ampm.upper() if ampm.upper() in ["AM", "PM"] else "AM"
            self.draw_clock()
        except ValueError:
            pass  # Ignore invalid input

    def draw_clock(self):
        """Draw the analog clock with current time settings."""
        self.delete("all")
        center_x, center_y = 100, 100
        radius = 90

        # Clock face
        self.create_oval(center_x - radius, center_y - radius,
                         center_x + radius, center_y + radius,
                         outline="black", width=2)

        # Hour ticks
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = center_x + (radius - 10) * math.sin(angle)
            y1 = center_y - (radius - 10) * math.cos(angle)
            x2 = center_x + radius * math.sin(angle)
            y2 = center_y - radius * math.cos(angle)
            self.create_line(x1, y1, x2, y2, width=2)

        # Calculate angles
        hour_angle = (self.hour % 12 + self.minute / 60) * 30
        minute_angle = self.minute * 6

        # Hour hand
        hx = center_x + 40 * math.sin(math.radians(hour_angle))
        hy = center_y - 40 * math.cos(math.radians(hour_angle))
        self.create_line(center_x, center_y, hx, hy, width=4, fill="black")

        # Minute hand
        mx = center_x + 60 * math.sin(math.radians(minute_angle))
        my = center_y - 60 * math.cos(math.radians(minute_angle))
        self.create_line(center_x, center_y, mx, my, width=2, fill="blue")

        # AM/PM display
        self.create_text(center_x, center_y + 70, text=f"{self.ampm}", font=("Helvetica", 12, "bold"))

class TimeSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manual to Analog Time Sync")

        # Variables
        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.ampm_var = tk.StringVar(value="AM")

        # Manual time input
        tk.Label(root, text="Hour (1-12):").pack()
        self.hour_entry = tk.Entry(root, textvariable=self.hour_var, width=5)
        self.hour_entry.pack()

        tk.Label(root, text="Minute (0-59):").pack()
        self.minute_entry = tk.Entry(root, textvariable=self.minute_var, width=5)
        self.minute_entry.pack()

        tk.Label(root, text="AM/PM:").pack()
        self.ampm_entry = tk.Entry(root, textvariable=self.ampm_var, width=5)
        self.ampm_entry.pack()

        # Analog clock
        self.analog_picker = AnalogPicker(root)
        self.analog_picker.pack(pady=10)

        # Sync manual -> analog
        self.hour_var.trace_add("write", lambda *args: self.update_analog_from_manual())
        self.minute_var.trace_add("write", lambda *args: self.update_analog_from_manual())
        self.ampm_var.trace_add("write", lambda *args: self.update_analog_from_manual())

    def update_analog_from_manual(self):
        hour = self.hour_var.get()
        minute = self.minute_var.get()
        ampm = self.ampm_var.get().upper()

        if hour.isdigit() and minute.isdigit() and ampm in ["AM", "PM"]:
            self.analog_picker.set_time(hour, minute, ampm)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeSelectorApp(root)
    root.mainloop()
