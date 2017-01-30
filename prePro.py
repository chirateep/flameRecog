#!/usr/bin/env python
 
import numpy as np
import cv2
from matplotlib import pyplot as plt

def gabor_filter():
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
	accum = np.zeros_like(img)
	for kern in filters:
		fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
		np.maximum(accum, fimg, accum)
	return accum

def remove_noise(img):
	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	return dst
 
if __name__ == '__main__':
	
	for i in range(1320):
		img = cv2.imread('../Data/Pro/image'+ str(i) + '.jpg')
		img = remove_noise(img)
		
		filters = []	
		filters = gabor_filter()
		#print len(filters)

		#for i in range(len(filters)):
		print 'image' + str(i)
		fliter_6 = process(img, filters[6])
		cv2.imwrite("../Data/Full/6/image" + str(i) + ".jpg", fliter_6)
		fliter_7 = process(img, filters[7])
		cv2.imwrite("../Data/Full/7/image" + str(i) + ".jpg", fliter_7)
		fliter_10 = process(img, filters[10])
		cv2.imwrite("../Data/Full/10/image" + str(i) + ".jpg", fliter_10)
		fliter_11 = process(img, filters[11])
		cv2.imwrite("../Data/Full/11/image" + str(i) + ".jpg", fliter_11)
		filters_14 = process(img, filters[14])
		cv2.imwrite("../Data/Full/14/image" + str(i) + ".jpg", filters_14)
		filters_15 = process(img, filters[15])
		cv2.imwrite("../Data/Full/15/image" + str(i) + ".jpg", filters_15)

# 6 2 Color Perfect
# 7 Its ok 
# 10 2 Color Perfect
# 11 2 Color Perfect
# 14 2 Color Perfect
# 15 It ok