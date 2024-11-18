import tkinter as tk
from tkinter import messagebox
import json
from face_tracker import recognize_face
from gps_verifier import verify_location

class SmartAttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Attendance System")
        self.attendance_records = self.load_attendance_records()

        # Tkinter Interface
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.start_button = tk.Button(root, text="Start Face Tracker", command=self.start_face_tracker)
        self.start_button.pack()

        self.attendance_label = tk.Label(root, text="Attendance Records:")
        self.attendance_label.pack()
        self.attendance_text = tk.Text(root)
        self.attendance_text.pack()

        self.update_attendance_text()

    def load_attendance_records(self):
        try:
            with open('attendance.json', 'r') as file:
                return json.load(file)["attendance_records"]
        except FileNotFoundError:
            return []

    def save_attendance_records(self):
        with open('attendance.json', 'w') as file:
            json.dump({"attendance_records": self.attendance_records}, file)

    def start_face_tracker(self):
        name = self.name_entry.get()
        if name:
            recognize_face()
            if verify_location():
                self.attendance_records.append({
                    "name": name,
                    "date": "2023-04-01",  # Replace with actual date
                    "time": "10:00",  # Replace with actual time
                    "location": "Department XYZ"  # Replace with actual location
                })
                self.save_attendance_records()
                self.update_attendance_text()
                messagebox.showinfo("Success", "Attendance marked successfully!")
            else:
                messagebox.showerror("Error", "Invalid location!")
        else:
            messagebox.showerror("Error", "Please enter your name!")

    def update_attendance_text(self):
        self.attendance_text.delete(1.0, tk.END)
        for record in self.attendance_records:
            self.attendance_text.insert(tk.END, f"Name: {record['name']}, Date: {record['date']}, Time: {record['time']}, Location: {record['location']}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartAttendanceSystem(root)
    root.mainloop()
