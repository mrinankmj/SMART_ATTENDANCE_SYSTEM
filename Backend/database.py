import pyrebase
from firebase_config import config

class Database:
    def __init__(self):
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.firestore()

    def insert_attendance(self, name, date, time, location):
        self.db.collection('attendance').add({
            'name': name,
            'date': date,
            'time': time,
            'location': location
        })

    def get_attendance(self):
        attendance = self.db.collection('attendance').stream()
        for doc in attendance:
            print(f"{doc.id} => {doc.to_dict()}")

# Usage
db = Database()
db.insert_attendance("John Doe", "2023-04-01", "10:00", "Department XYZ")
db.get_attendance()
