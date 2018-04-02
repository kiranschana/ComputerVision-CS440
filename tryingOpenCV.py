import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, 'Play Rock Paper Scissors!', (30,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
	cv2.putText(frame, 'Player Score: 0', (30,70), font, 1, (255,255,255), 2, cv2.LINE_AA)
	cv2.putText(frame, 'AI Score: 0', (30,110), font, 1, (255,255,255), 2, cv2.LINE_AA)

	# Display the video
	cv2.imshow('frame', frame)
	#cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()