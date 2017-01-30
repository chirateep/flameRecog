import cv2
print (cv2.__version__)
vidcap = cv2.VideoCapture('../Data/Video/input.mp4')
success, image = vidcap.read()
count = 0
success = True
while success:
	success, image = vidcap.read()
	print 'Read a new frame', success
	cv2.imwrite("../Data/Capture/frame%d.jpg" % count, image)
	count += 1