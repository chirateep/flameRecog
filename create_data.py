from PIL import Image
import numpy as np
import csv
from collections import defaultdict
import os
import cv2
import shutil

def read_label_fromcsv(label_csv_dir):
	"""Read label from CSV file.
	  Args:
	    label_csv_dir: The directory that has label CSV file.
	  Returns:
	    label of file in dict().
	"""
	with open(label_csv_dir, 'rb') as csvfile:

		reader = csv.DictReader(csvfile)
		label = dict()
		
		for row in reader:
			label[row['Image'] + '.jpg'] = row['Label']

	return label

def create_dir_for_training(label, create_data_dir):
	"""Create directory divied by labels.
	  Args:
	    label: label load in dict() format.
	    create_data_dir: directory to Image in Dict() format
	"""
	training_dir = '../Data/Training/'
	for image in label:
		dstdir = os.path.join(training_dir, label[image])
		create_dir(dstdir)
		shutil.copy(create_data_dir[image], dstdir)


def create_dir(dir):
	"""Create directory if Do not have that directory.
		Args:
			dir: Directory that want to create
	"""
	if not os.path.exists(dir):
		os.makedirs(dir)


if __name__ == '__main__':

	label = dict()
	label_csv_dir = '/home/zanninna/SeniorProject/Data/Training/Flame Recog Label - Filter_6.csv'
	label = read_label_fromcsv(label_csv_dir)

	create_data_dir = dict()
	preprocessing_dir = '../Data/Preprocessing/'

	for filename in os.listdir(preprocessing_dir):
		video_preprocessing_dir = os.path.join(preprocessing_dir, filename)
		for filename_video in os.listdir(video_preprocessing_dir):
			image_preprocessing_dir = os.path.join(video_preprocessing_dir, filename_video)
			for filename_image in os.listdir(image_preprocessing_dir):
				create_data_dir[filename_image[len(filename_video[7:])+1:]] = os.path.join(image_preprocessing_dir, filename_image)
			
			create_dir_for_training(label, create_data_dir)			