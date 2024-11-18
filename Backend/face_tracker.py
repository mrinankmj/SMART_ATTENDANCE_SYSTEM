import cv2
import tkinter as tk
from tkinter import filedialog
from backend.database import Database

def recognize_face():
    # Simplified face recognition logic; integrate with your model
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Face detection/recognition logic here
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    root = tk.Tk()
    button = tk.Button(root, text="Start Face Tracker", command=recognize_face)
    button.pack()
    root.mainloop()

    # After successful recognition, insert into database
    db = Database()
    db.insert_attendance("John Doe", "2023-04-01", "10:00", "Department XYZ")

if __name__ == "__main__":
    main()
