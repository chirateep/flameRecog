import cv2
import os

def captureVideo(read_dir, write_dir):
	
	vidcap = cv2.VideoCapture(read_dir)
	success, image = vidcap.read()
	count = 0
	success = True
	while success:
		success, image = vidcap.read()
		print 'Read a new frame', success
		cv2.imwrite(write_dir + "%d" % count + ".jpg" , image)
		count += 1

if __name__ == '__main__':	
	
	read_video_dir = '../Data/Video/input.mp4'
	write_vidro_dir = '../Data/Capture/frame'

	for filename in os.listdir(read_video_dir):
		new_dir = '../Data/' 
		if not os.path.exists(newpath):
		    os.makedirs(newpath)