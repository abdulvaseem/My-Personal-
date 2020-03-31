# !pip install face_recognition - command to install module
import face_recognition
""" if you are using google colab 
from google.colab import files
files.upload()"""
import numpy as np
import glob
import cv2
from IPython.display import display, Image
k=glob.glob(r"/content/vaseem/.jpg") # give the address of the file(DB) in which all the images are present
picture_of_me=face_recognition.load_image_file(r'/content/quiery.jpg')  # quiery image address
my_face_encoding=face_recognition.face_encodings(picture_of_me)[0]

for i in range(0,len(k)):
    k[i]="%r"%k[i]
    unknown_picture = face_recognition.load_image_file(eval(k[i]))
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results=face_recognition.compare_faces(np.array([my_face_encoding]),np.array(unknown_face_encoding))
    if results[0]==True:
         print('pictures matched')
    else:
         print('picture not matched')

print("pictures are matched .")
display(Image(filename='/content/Quiery.jpg'))

