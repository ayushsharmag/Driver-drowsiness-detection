import cv2 #cv2 is an opencv library for capturing video/image
# Numpy for array related functions
import numpy as np
#face_utils for basic operations of conversion
from imutils import face_utils
#pygame is used for importing and using the alarm sounds
from pygame import mixer
import time
# Dlib for deep learning based Modules and face landmark detection
import dlib
#tkinter for setting up 
from tkinter import *
import tkinter as tk
#for basic conversion operations 
from imutils import face_utils
#initialising the tkinter application
root = Tk()
root.title(" Driver Drowsiness Detection by Ayush")
# root.configure(background="lightgreen")
bg = PhotoImage(file = r"D:\Coding\project driver1\project driver\back2.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
#Initializing the camera and taking the instance


#Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\Coding\project driver1\project driver\shape_predictor_68_face_landmarks.dat")

#status marking for current state



#for finding the euclidean distance
def distance(ptA,ptB):
	dist = np.linalg.norm(ptA - ptB)
	return dist

#to basically finding the distance between up and down eye 
def check(a,b,c,d,e,f):
	up = distance(b,d) + distance(c,e)
	down = distance(a,f)
	ratio = up/(2.0*down)

	#Checking if it is blinked or not
	if(ratio>0.25):
		return 2  #for open(active eyes)
	elif(ratio>0.21 and ratio<=0.25):
		return 1  #for drowsy
	else:
		return 0  #for sleeping

def main():
	cap = cv2.VideoCapture(r'D:\Coding\project driver1\project driver\preview.mp4')
	sleep = 0
	drowsy = 0
	active = 0
	status=""
	color=(0,0,0)
	count=0
	while True:
		_, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		height,width=frame.shape[0:2]
		faces = detector(gray)
		face_frame = frame.copy()
		#detected face in faces array
		for face in faces:
			x1 = face.left()
			y1 = face.top()
			x2 = face.right()
			y2 = face.bottom()

			
			cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

			landmarks = predictor(gray, face)
			landmarks = face_utils.shape_to_np(landmarks)

			#The numbers are actually the landmarks which will show eye
			left_blink = check(landmarks[36],landmarks[37], 
				landmarks[38], landmarks[41], landmarks[40], landmarks[39])
			right_blink = check(landmarks[42],landmarks[43], 
				landmarks[44], landmarks[47], landmarks[46], landmarks[45])
			
			#Now judge what to do for the eye blinks
			if(left_blink==0 or right_blink==0):
				sleep+=1
				drowsy=0
				active=0
				if(sleep>6):
						count+=1
						status="SLEEPING !!!"
						color = (255,0,0)
						mixer.init()
						mixer.music.load(r"D:\Coding\project driver1\project driver\sound_files\alarm2.wav")
						cv2.imwrite("dataset/frame_yawn%d.jpg"% sleep, frame)
						mixer.music.play()
						while mixer.music.get_busy():  # wait for music to finish playing
							time.sleep(1)
			elif(left_blink==1 or right_blink==1):
				sleep=0
				active=0
				drowsy+=1
				if(drowsy>6):
						count+=1
						status="Drowsy !"
						color = (0,0,255)
						mixer.init()
						mixer.music.load(r"D:\Coding\project driver1\project driver\sound_files\alarm1.wav")
						mixer.music.play()
						while mixer.music.get_busy():  # wait for music to finish playing
							time.sleep(1)
			else:
				drowsy=0
				sleep=0
				active+=1
				if(active>6):
					status="Active :)"
					color = (0,255,0)
				
			cv2.putText(frame, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

			for n in range(0, 68):
				(x,y) = landmarks[n]
				cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

		cv2.imshow("Frame", frame)
		
		key = cv2.waitKey(1) & 0xFF 
	
	

		if key == ord('q'):
			if count >= 0:
				t3.delete("1.0", END)
				t3.insert(END, count)
			break

def camera():
	cap = cv2.VideoCapture(0)
	sleep = 0
	drowsy = 0
	active = 0
	status=""
	color=(0,0,0)
	count=0

	while True:
		_, frame = cap.read()
		height,width=frame.shape[0:2]
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
		cv2.rectangle(frame, (0,height-100),(200,height),(255,255,255),thickness=cv2.FILLED)
		faces = detector(gray)
		#detected face in faces array
		for face in faces:
			x1 = face.left()
			y1 = face.top()
			x2 = face.right()
			y2 = face.bottom()

			face_frame = frame.copy()		
			cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

			landmarks = predictor(gray, face)
			landmarks = face_utils.shape_to_np(landmarks)

			#The numbers are actually the landmarks which will show eye 
			#for left eye 37-42 which indexes 36-41
			left_blink = check(landmarks[36],landmarks[37], 
				landmarks[38], landmarks[41], landmarks[40], landmarks[39])
			#for right eye 43-48 which indexes 42-47
			
			right_blink = check(landmarks[42],landmarks[43], 
				landmarks[44], landmarks[47], landmarks[46], landmarks[45])
			
			#Now judge what to do for the eye blinks
			if(left_blink==0 or right_blink==0):
				sleep+=1
				drowsy=0
				active=0
				if(sleep>6):
						count+=1
						status="SLEEPING !!!"
						color = (255,0,0)
						mixer.init()
						mixer.music.load(r"D:\Coding\project driver1\project driver\sound_files\alarm2.wav")
						cv2.imwrite("dataset/frame_yawn%d.jpg"% sleep, frame)
						mixer.music.play()
						while mixer.music.get_busy():  # wait for music to finish playing
							time.sleep(1)
			elif(left_blink==1 or right_blink==1):
				sleep=0
				active=0
				drowsy+=1
				if(drowsy>6):
						status="Drowsy !"
						color = (0,0,255)
						mixer.init()
						mixer.music.load(r"D:\Coding\project driver1\project driver\sound_files\alarm1.wav")
						mixer.music.play()
						while mixer.music.get_busy():  # wait for music to finish playing
							time.sleep(1)
			else:
				drowsy=0
				sleep=0
				active+=1
				if(active>6):
					status="Active :)"
					color = (0,255,0)
			cv2.putText(frame, status, (10,450), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

			for n in range(0, 68):
				(x,y) = landmarks[n]
				cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

		cv2.imshow("Frame", frame)
		
		key = cv2.waitKey(1) & 0xFF 
	
	

		if key == ord('q'):
			if count >= 0:
				t4.delete("1.0", END)
				t4.insert(END, count)
			break


w2 = Label(root,justify=LEFT, text=" Driver Drowsiness Detection")
w2.config(font=("Times", 30),background="white")
w2.grid(row=1, column=0, columnspan=2, padx=100,pady=40)
w2 = Label(root,justify=LEFT, text=" BY AVI PRUTHI")
w2.config(font=("Times", 30),background="white")
w2.grid(row=2, column=0, columnspan=2, padx=100,pady=10)


lr = Button(root, text="Video",height=2, width=10, command=main)
lr.config(font=("Times", 17),background="lightgreen")
lr.grid(row=15, column=0,pady=10)
lr = Button(root, text="Camera",height=2, width=10, command=camera)
lr.config(font=("Times", 17),background="lightgreen")
lr.grid(row=16, column=0,pady=10)

NameLb = Label(root, text="Predict using:")
NameLb.config(font=("Times", 15),background="lightblue")
NameLb.grid(row=13, column=0, pady=20)

t3 = Text(root, height=2, width=15)
t3.config(font=("Times", 15))
t3.grid(row=15, column=1 ,padx=60)
t4 = Text(root, height=2, width=15)
t4.config(font=("Times", 15))
t4.grid(row=16, column=1 ,padx=60)

root.mainloop()

