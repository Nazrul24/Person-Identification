from msilib.schema import TextStyle
import tkinter as tk
from tkinter import Canvas, filedialog,Text
import os
from tracemalloc import stop
root = tk.Tk()

import numpy as np
import cv2
import face_recognition
from simple_facerec import SimpleFacerec





# Encode faces from a folder

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")


# Load Camera
def openCam():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        
        for face_loc, name in zip(face_locations, face_names):
            # print(face_loc)
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
        
        

def closeCam():
    print("Camera Close")


canvas = tk.Canvas(root,height=500,width=1200,bg = "#B2BEB5")
canvas.pack()

frame = tk.Frame(root,bg = '#FFFFFF')

frame.place(relwidth=0.9, relheight=0.8, relx=0.05,rely=0.1)

startRecog = tk.Button(root, text='Open Camera', padx=10,pady=5, fg='red',bg='#00CEFF',command=openCam)
startRecog.pack()

stopRecog = tk.Button(root, text='Close Camera', padx=10,pady=5, fg='green',bg='#00CEFF',command= closeCam)
stopRecog.pack()

root.mainloop()

#cap = cv2.VideoCapture(0)
cap.release()
cv2.destroyAllWindows()