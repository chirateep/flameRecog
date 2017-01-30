import cv2
import numpy as np

for i in np.arange(0, 1320, 1):
	image = cv2.imread('../Data/Capture/frame'+ str(i) + '.jpg')
	# print image.shape
	cropped = image[0:720, 200: 900]
	# cv2.imshow("crop", cropped)
	# cv2.waitKey(0)
	cv2.imwrite("../Data/Pro/image" + str(i) + ".jpg", cropped)