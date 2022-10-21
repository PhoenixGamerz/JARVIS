import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# Text To Speech
def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait

# To Convert Voice Into Text
def takecommand():
	r = sr.Recognizer()
	with sr.Microphone as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source,timeout=1,phrase_time_limit=5)
	
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User Said : {query}")
	
	except Exception as e:
		speak("Say That Again Please...")
		return "none"
	return query

# To Wish
def wish():
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<=12:
		speak("Good Morning!")
	elif hour>12 and hour<18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")
	speak("Hello, My Name Is Jarvis, Please Tell Me How Can I Help You?")

# To Send Email
def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('ashmitdas1989@gmail.com', 'ashmit1989')
	server.sendmail('ashmitdas1989@gmail.com', to, content)
	server.close()

if __name__ == "__main__":
	wish()
	while True:
		
		query = takecommand().lower()
		
		# Logic Building For Tasks
		
		if "open notepad" in query:
			npath = "" # Here Enter Your Notepad Path
			os.startfile(npath)
		
		elif "open adobe reader" in query:
			apath = "" # Here Enter Your Adobe Reader Path
		
		elif "open command prompt" in query:
			os.system("start cmd")
		
		elif "open camera" in query:
			cap = cv2.VideoCapture(0)
			while True:
				ret, img = cap.read()
				cv2.imshow('webcam', img)
				k = cv2.waitKey(50)
				if k==27:
					break;
			cap.release()
			cv2.destroyAllWindows()
		
		elif "play music" in query:
			music_dir = "" # Here Enter Your Music Directory Path
			songs = os.listdir(music_dir)
			rd = random.choice(songs)
			os.startfile(os.path.join(music_dir, rd))
		
		elif "ip address" in query:
			ip = get('https://api.ipify.org').text
			speak(f"Your IP Address Is {ip}")
		
		elif "wikipedia" in query:
			speak("Searching Wikipedia...")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According To Wikipedia...")
			speak(results)
		
		elif "open youtube" in query:
			webbrowser.open("www.youtube.com")
		
		elif "open facebook" in query:
			webbrowser.open("www.facebook.com")
		
		elif "open stackoverflow" in query:
			webbrowser.open("www.stackoverflow.com")
		
		elif "open google" in query:
			speak("What Should I Search On Google?")
			cm = takecommand().lower()
			webbrowser.open(f"{cm}")
		
		elif "play song on youtube" in query:
			kit.playonyt("i am on my way")
		
		elif "send email to ashmit" in query:
			try:
				speak("What Should I Say?")
				content = takecommand().lower()
				to = "ashmitdas62@gmail.com"
				sendEmail(to,content)
				speak("Email Has Been Sent Successfully.")
			
			except Exception as e:
				print(e)
				speak("Sorry, I Am Not Able To Send This Email.")
		
		elif "no thanks" in query:
			speak("Thanks For Using Me, Have A Good Day.")
			sys.exit()
		
		speak("Do You Have Any Other Work?")