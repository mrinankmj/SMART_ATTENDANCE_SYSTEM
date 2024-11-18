from backend.face_tracker import main as face_tracker_main
from backend.gps_verifier import verify_location
from backend.database import Database

def main():
    # Initialize Database
    db = Database()

    # Start Face Tracker
    face_tracker_main()

    # Verify Location (if GPS is enabled)
    is_location_valid = verify_location()
    if is_location_valid:
        print("Location is within the allowed area.")
    else:
        print("Location is not within the allowed area.")

    # Example: Get Attendance Records
    print("Attendance Records:")
    db.get_attendance()

if __name__ == "__main__":
    main()
