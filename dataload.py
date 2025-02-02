from tkinter import *
from PIL import Image, ImageTk
import cv2
import face_recognition
import os
import glob
import pygame
from gtts import gTTS
import threading

cap = cv2.VideoCapture(0)
pygame.mixer.init()

names = []
images = []

def text_to_speech(text):
    try:
        output_file = r'output.mp3'  # Specify absolute path here
        tts = gTTS(text=text, lang='en')
        tts.save(output_file)
        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until the speech is finished
            continue
        pygame.mixer.quit()
    except PermissionError:
        print(" ")

def snapshot():
    thread = threading.Thread(target=capture_images)
    thread.start()

def capture_images():
    name = name_var.get().strip()
    normalized_name = name.lower()

    print(f"Capturing the images for {name}") 
    text_to_speech("Please wait while we are capturing your data")

    if normalized_name in [n.lower() for n in names]:
        print(f"The name '{name}' already exists. Please enter a unique name.")
        text_to_speech("The name already exists. Please enter a unique name.")
        return

    known_encodings = []
    known_names = []

    # Load existing images and encodings
    for image_path in glob.glob(r'C:\Users\JAGRUTI\Desktop\face_recognition\images\*\*.jpg'):
        known_image = face_recognition.load_image_file(image_path)
        known_encoding = face_recognition.face_encodings(known_image)
        if known_encoding:
            known_encodings.append(known_encoding[0])
            known_names.append(os.path.basename(os.path.dirname(image_path)))

    # Capture a single frame to check for existing faces
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        return

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(cv2image)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        if True in matches:
            print(f"The face already exists. Please enter a unique person.")
            text_to_speech("The face already exists. Please enter a unique person.")
            return

    # If no matches, create the folder and capture images
    folder_path = r'C:\Users\JAGRUTI\Desktop\face_recognition\images\{}'.format(name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    count = 1
    while count <= 50:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)

        face_locations = face_recognition.face_locations(cv2image)
        face_encodings = face_recognition.face_encodings(cv2image, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            top, right, bottom, left = face_location
            face_img = img.crop((left, top, right, bottom))
            filename = os.path.join(folder_path, f"{name}_{count}.jpg")
            face_img.save(filename)
            known_encodings.append(face_encoding)
            known_names.append(name)
            count += 1

        # Show feedback in GUI label
        label.configure(text=f"Captured {count-1} images for {name}")
    updatedata()
    print(f"Images of {name} have been successfully captured.")
    text_to_speech(f"Thank you for the patience, {name} data has been successfully saved.")
    text_to_speech("You can close the window now")

def updatedata():
    names.clear()
    images.clear()

    path = r'C:\Users\JAGRUTI\Desktop\face_recognition\images\*'
    for folder in glob.glob(path):
        folder_name = os.path.basename(folder)
        if os.path.isdir(folder):
            names.append(folder_name)

    print(names)

def show_frames():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    label.after(10, show_frames)

def quitapp():
    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()
    win.destroy()

win = Tk()
win.title("Face Recognition Data Collection")
name_var = StringVar()
label = Label(win)
label.grid()

name_entry = Entry(win, textvariable=name_var, font=('calibre', 10, 'normal'))
name_entry.grid(row=1, column=0)

snap_btn = Button(win, text='Snapshot', command=snapshot)
snap_btn.grid(row=3, column=0)

quit_btn = Button(win, text='Quit', command=quitapp)
quit_btn.grid(row=4, column=0)

show_frames()
win.mainloop()