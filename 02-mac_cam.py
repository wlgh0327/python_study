import cv2
import numpy as np
import matplotlib.pyplot as plt


def nothing_to_do(x) :
	pass

if __name__ == '__main__' :
	cap = cv2.VideoCapture(0)
	
	cv2.namedWindow('frame')
	cv2.createTrackbar('K', 'frame', 1, 21, nothing_to_do)

	while(True) :
		ret, frame = cap.read()
		
		k = cv2.getTrackbarPos('K', 'frame')
		if k == 0:
			k = 1
## Do blur
		kernel = np.ones((k, k), np.float32) / (k*k)
		frame = cv2.filter2D(frame, -1, kernel)

# Image flipping
		frame = cv2.flip(frame, 1)
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q') :
			break

	cap.release()
	cv2.destroyAllWindows()
