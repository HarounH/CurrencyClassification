'''
@author Haroun
This file has a few functions which help visualize the training and testing data.
Should help with understanding data.
'''
# The usual imports
import sys,os
import datetime as dt, random, pickle
import numpy as np
import pandas as pd
import pdb
import matplotlib.pyplot as plt

def showMatrix(mat):
	plt.imshow(mat)
	plt.show()
def flatArray2imageMatrix(pixels, dims):
	imgMatrix = np.zeros( dims , dtype=np.uint8 )
	# one possiblity: pixels.reshape(dims) ... doesn't work :(
	for r in range(0, dims[0]):
		for c in range(0, dims[1]):
			for d in range(0, dims[2]):
				imgMatrix[r][c][d] = pixels[r*dims[2]*dims[1] + c*dims[2] + d]
	return imgMatrix

if __name__ == '__main__':
	imgFile = '../data/RAW_PIXELS_train.csv' if len(sys.argv)<3 else sys.argv[2] # This is the file from which to get images.
	dimensions= (160,120,3) # 3 channels of 160x120 pixels
	buffering = 1 # We should be doing line buffering, really.
	lineItr = 0
	idx = int(sys.argv[1]) if len(sys.argv)>1 else 10
	print('USAGE: python ' + sys.argv[0] + ' <idx-to-display> <imgFilePath=../data/RAW_PIXELS_train.csv by default>')
	print('File format: metadata,label, 160*120*3 pixels per line ')
	with open(imgFile, 'rb', buffering) as f:
		line = None
		while lineItr < idx:
			line = f.readline() # Read a line, mate.
			lineItr += 1
		toks = line.split(',')
		metaData = toks[0]
		noteType = toks[1]
		pixelArr = toks[2:]
		for i in range(0, len(pixelArr)):
			pixelArr[i] = int(pixelArr[i])
		plt.imshow(flatArray2imageMatrix(pixelArr, dimensions))
		plt.show()