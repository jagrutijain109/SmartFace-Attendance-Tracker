Visionary Attendance Logger 

This project is a comprehensive Face Recognition Attendance System that efficiently manages attendance records for both known and unknown individuals. Key features include real-time face recognition, attendance marking, and detailed time logging. Here’s an overview of the system’s capabilities:

Real-Time Face Recognition:

The system captures live video feed from a webcam and detects faces in real-time using face recognition technology.
It identifies known individuals by comparing the detected faces with a pre-existing database of known face encodings.
Attendance Marking:

For recognized individuals, the system automatically marks their attendance and logs the time of arrival.
The system saves the attendance records in an Excel file, including the username, current date, current time, and whether the person is "On Time" or "Late".
Handling Unknown Individuals:

When an unknown individual is detected, the system captures and saves multiple snapshots (25 images) of the person’s face.
These images are stored in a designated directory with a unique identifier (e.g., "unknown_person_1").
If the same unknown individual arrives again, the system recognizes the person from the stored snapshots and updates their attendance record accordingly.
Database Management:

The system maintains a database of known and unknown individuals by storing their face encodings and images.
It continuously updates the database with new entries, ensuring that repeated visits by the same unknown individuals are accurately tracked and recognized.
Attendance and Time Logging:

The system records the exact time of arrival for each individual and determines if they are "On Time" or "Late" based on a predefined threshold (e.g., arriving after a set time is considered late).
Attendance records are saved in an Excel file, which includes detailed logs of each entry.
User Feedback:

The system provides real-time feedback through a GUI, displaying messages such as "You are late" or "You are on time" based on the arrival time of the individual.
It also updates the user interface to show the number of captured images for each person.

How It Works:
Initialization:

The webcam is initialized, and the system starts capturing video frames.
A Tkinter GUI is launched to display the video feed and provide real-time feedback.
Face Detection and Recognition:

Each frame is processed to detect faces using the face_recognition library.
Detected faces are compared against the database of known faces to determine if they are recognized.
Image Saving and Encoding:

For known faces, attendance is marked directly.
For unknown faces, the system captures and saves 25 images, creating a new entry in the database.
Attendance Logging:

Attendance records, including the username, date, time, and status (On Time or Late), are logged in an Excel file.
Continuous Monitoring:

The system continuously monitors the video feed, updating the database and attendance records in real-time.
This project demonstrates the practical application of face recognition technology in an attendance management system, offering a robust solution for both known and unknown individuals.

