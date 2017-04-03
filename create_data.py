from PIL import Image
import numpy as np
import csv
from collections import defaultdict
import os
import cv2


def transpose_image(label, dir_image_for_transpose, filename_video):

	rgb = np.empty(shape = (0,0))
	for image_dir in dir_image_for_transpose:
		image = Image.open(dir_image_for_transpose[image_dir])
		image = (np.array(image))

		r = image[:,:,0].flatten()
		g = image[:,:,1].flatten()
		b = image[:,:,2].flatten()
		image_label = label[image_dir]
		
		image_np = np.array(list(image_label) + list(r) + list(g) + list(b),np.uint8)
		rgb = np.append(rgb, image_np)
	rgb.tofile('../Data/Training/train_' + str(filename_video))

def read_rabel_fromcsv(label_csv_dir):

	with open(label_csv_dir, 'rb') as csvfile:

		reader = csv.DictReader(csvfile)
		label = dict()
		
		for row in reader:
			label[row['Image'] + '.jpg'] = row['Label']

	return label

if __name__ == '__main__':

	label = dict()
	label_csv_dir = '../Data/Training/Flame_Label.csv'
	label = read_rabel_fromcsv(label_csv_dir)

	preprocessing_dir = '../Data/Preprocessing/'
	dir_image_for_transpose = dict()

	for filename in os.listdir(preprocessing_dir):
		video_preprocessing_dir = preprocessing_dir + str(filename) + '/'
		for filename_video in os.listdir(video_preprocessing_dir):
			image_preprocessing_dir = video_preprocessing_dir + str(filename_video) + '/'
			for filename_image in os.listdir(image_preprocessing_dir):
				dir_image_for_transpose[filename_image] = image_preprocessing_dir + str(filename_image)
			transpose_image(label, dir_image_for_transpose, filename_video)