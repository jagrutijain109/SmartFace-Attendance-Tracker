from tkinter import *
from PIL import Image, ImageTk,ImageDraw
import cv2
import face_recognition
import glob
import os
import pygame
from gtts import gTTS


cap= cv2.VideoCapture(0)
images=[]
names=[]

pygame.mixer.init()

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
    # name = name_var.get()
    # if name in names:
    #     print(f"The name '{name}' already exists. Please enter a unique name.")
    #     return
    name = name_var.get().strip()
    normalized_name = name.lower()  # Normalize the name to lower case for comparison
    normalized_names = [n.lower() for n in names]  # Normalize the existing names

    if normalized_name in normalized_names:
        print(f"The name '{name}' already exists. Please enter a unique name.")
        text_to_speech("The name already exists. Please enter a unique name.")
        return
    
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    face_locations = face_recognition.face_locations(cv2image)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        im1 = img.crop((left, top, right, bottom))
        name=name_var.get()
        im1.save(r'C:\Users\JAGRUTI\Desktop\face_recognition\images\''+name+'.jpg')
    print(f"The '{name}' is successfully added in the data.")
    text_to_speech("Details are successfully added in the data.")
    updatedata()

def updatedata():
    path = r'C:\Users\JAGRUTI\Desktop\face_recognition\images\'*.*'
    for file in glob.glob(path):
        image = cv2.imread(file)
        a=os.path.basename(file)
        b=os.path.splitext(a)[0]
        names.append(b)
        images.append(image)
    print(names)

def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(10, show_frames)
           
     
def quitapp():
    win.destroy()          
       
# Create an instance of TKinter Window or frame
win = Tk()
name_var=StringVar()

# Set the size of the window
#win.geometry("700x350")

# Create a Label to capture the Video frames
label =Label(win)
label.grid()




name_entry = Entry(win,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=1,column=0)

# update_btn=Button(win,text = 'Update',command=updatedata)
# update_btn.grid(row=2,column=0)

snap_btn=Button(win,text = 'Snapshot',command=snapshot)
snap_btn.grid(row=3,column=0)



quit_btn=Button(win,text = 'Quit',command=quitapp)
quit_btn.grid(row=4,column=0)


# Define function to show frame


show_frames()

win.mainloop()
cap.release()
