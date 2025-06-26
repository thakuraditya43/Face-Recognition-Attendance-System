# Face Recognition for Secure Attendance Management

This is an ongoing group project developed by a team of five students. 
The system is designed to automate attendance tracking using traditional face recognition techniques via OpenCV. 
It captures, trains, and recognizes faces in real time and securely records attendance using a MySQL database. 
Attendance data can also be exported to CSV files for reporting. 

---

## 👥 Team

- Akarsh Kumar  
- Aditya kumar 814 
- Aditya kumar 1174 
- [Member 4 Name]  
- [Member 5 Name]

---

## 🔧 Features

- Real-time face detection and recognition using OpenCV
- Face registration through webcam
- Attendance logging with date and time
- GUI-based interface built with Tkinter
- Backend powered by MySQL database
- Option to export attendance data to CSV format

---

## 🛠 Technologies Used

- Python 3
- OpenCV (LBPH Face Recognizer)
- Tkinter (GUI)
- MySQL (Database)
- MySQL Connector for Python
- NumPy and Pandas

---

## 🖥️ How It Works

1. **Register Faces** – Captures multiple images of each individual using the webcam.
2. **Train the Model** – Uses LBPH (Local Binary Patterns Histograms) for face recognition.
3. **Recognize & Mark Attendance** – Matches face with trained data and logs attendance into a MySQL database with timestamp.
4. **Export Data** – Attendance records can be exported to CSV files for reports.

---

## 📁 Folder Structure

