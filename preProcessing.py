import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

def create_dir(dir):
	""""Create directory if Do not have that directory.
		Args:
			dir: The Directory that want to create
	"""
	if not os.path.exists(dir):
		os.makedirs(dir)

def captureVideo(read_dir, write_dir):
	"""Capture video to frame per second.
		Args:
			read_dir: The Directory that video locate
			write_dir: The Directory that want to store image after cut from Video
	"""
	vidcap = cv2.VideoCapture(read_dir)
	success, image = vidcap.read()
	frame_count = 0
	success = True

	while success:

		success, image = vidcap.read()
		if not success:
			print 'Finish Capture Video'
			return frame_count

		cv2.imwrite(write_dir + 'frame%d' % frame_count + '.jpg' , image)
		frame_count += 1

def cropImage(read_dir, write_dir, frame_count):
	"""Crop image.
		Args:
			read_dir: The Directory that dataset image locate
			write_dir: The Directory that want to store image after crop image
			frame_count: A Number of frame in Dataset
	"""
	for i in np.arange(0, frame_count, 1):
		
		image = cv2.imread(read_dir + str(i) + '.jpg')
		cropped = image[0:720, 200: 900]
		cv2.imwrite(write_dir + 'image' + str(i) + '.jpg', cropped)

	print 'Finish Crop Image'

def gabor_filter():
	"""Gabor filter for Preprocessing.
		Retures: 
			The Gabor filter that create from many parameter
	"""
	filters = []
	ksize = 25
	for theta in np.arange(0, np.pi, np.pi/4):
		for lamda in np.arange(0, np.pi, np.pi/4): 
			kern = cv2.getGaborKernel(ksize = (ksize, ksize), sigma = 1.0, theta = theta, 
				lambd = lamda, gamma = 1.0, psi = 0, ktype=cv2.CV_32F)
			kern /= 1.5*kern.sum()
			filters.append(kern)
	return filters

def process(img, filters):
	"""Run filter on image.
		Args:
			img: A image that want to use filter
			filter: A kind of filter of image processing
	"""
	accum = np.zeros_like(img)
	for kern in filters:
		fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
		np.maximum(accum, fimg, accum)
	return accum

def remove_noise(img):
	"""Remove noise from image by Mean
		Args:
			img: A image that wanna remove noise
	"""
	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	return dst

def select_Filter(image, write_preprocessing_dir, filters, frame_count, number_filter):
	"""Select parameter on filter and write to directory
		Args:
			image: A raw image from Dataset
			write_preprocessing_dir: The dirertory to save image after pass filter
			filter: A filter of image processing
			frame_count: A frame of image in Dataset
			number_filter: A Integer that can choose parameter
	"""
	fliter_dir = write_preprocessing_dir + 'filter_' + str(number_filter) + '/'
	create_dir(fliter_dir)
	image_preprocessing = process(image, filters[number_filter])
	cv2.imwrite(fliter_dir + str (number_filter) + '_' + str(i) + ".jpg", image_preprocessing)

if __name__ == '__main__':	
	
	read_video_dir = '../Data/Video/'

	for filename in os.listdir(read_video_dir):

		write_capture_dir = '../Data/Capture/' + filename + '/'
		create_dir(write_capture_dir)

		frame_count = captureVideo(read_video_dir + filename , write_capture_dir)
	
		read_capture_dir = write_capture_dir + 'frame'
		write_cropped_dir = '../Data/Cropped/' + filename + '/'

		create_dir(write_cropped_dir)
		cropImage(read_capture_dir, write_cropped_dir, frame_count)

		write_preprocessing_dir =  '../Data/Preprocessing/' + filename + '/'

		for i in range(frame_count):
			image = cv2.imread(write_cropped_dir + 'image'+ str(i) + '.jpg')
			image = remove_noise(image)
			
			filters = []	
			filters = gabor_filter()

			select_Filter(image, write_preprocessing_dir, filters, frame_count, 6)
			# select_Filter(image, write_preprocessing_dir, filters, frame_count, 7) .. image not clear
			select_Filter(image, write_preprocessing_dir, filters, frame_count, 10)
			select_Filter(image, write_preprocessing_dir, filters, frame_count, 11)
			select_Filter(image, write_preprocessing_dir, filters, frame_count, 14)
			# select_Filter(image, write_preprocessing_dir, filters, frame_count, 15) .. image not clear
			print 'image' + str(i)