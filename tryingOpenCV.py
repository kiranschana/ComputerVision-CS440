import cv2
import numpy as np 

## FLAGS ##
demo = True
debug = True
## ##### ##

cap = cv2.VideoCapture(0)

# Game Variables
states = ['idle', 'start', 'shoot', 'results']
currentState = states[0]
p1Score = 0
cpScore = 0
shakeCount = 0
p1Choice = "Rock"
cpChoice = "Paper"
pResult = "Lose"

# Helper function for text
def doubleText(frame, xy, text):
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, text, (xy[0] - 2, xy[1] + 2), font, 1, (0,0,0), 2, cv2.LINE_AA)
	cv2.putText(frame, text, (xy[0], xy[1]), font, 1, (255,255,255), 2, cv2.LINE_AA)


# Loop on frames of video
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Game Logic
	if currentState == 'idle':
		# waiting for start gesture
		shakeCount = 0
		p1Choice = "Rock"
		cpChoice = "Paper"
		pResult = "Lose"

	# if currentState == 'start':
		

	# if currentState == 'shoot':
		

	# if currentState == 'results':
		

	# UI For Demo
	if debug:
		doubleText(frame, (30, 650), "Game state: " + currentState)

	doubleText(frame, (30,30), "Play Rock Paper Scissors!")
	doubleText(frame, (30,70), "Player Score: " + str(p1Score))
	doubleText(frame, (30,110),"AI Score: "+ str(cpScore))

	if currentState == 'idle':    # 0
		doubleText(frame, (475, 200), "Shake Fist to Begin!")
	if currentState == 'start':   # 1
		doubleText(frame, (600, 200), "Ready")
	if currentState == 'shoot' or currentState == 'results':   # 2 or 3
		doubleText(frame, (500, 400), "AI Choice: " + cpChoice)
	if currentState == 'results': # 3
		doubleText(frame, (550, 200), "You " + pResult + "!")
		doubleText(frame, (500, 440), "Player Choice: " + p1Choice)

	# Display the video
	if demo:
		cv2.imshow('frame', frame)
	else:
		cv2.imshow('gray', gray)

	# Close by pressing 'q'
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Closes program
cap.release()
cv2.destroyAllWindows()