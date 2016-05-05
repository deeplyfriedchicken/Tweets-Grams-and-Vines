#CMiC Image Compressor Starter file
#first some imports
import sys
import scipy
import scipy.ndimage
import numpy as np
import PIL
import pywt
import argparse
import operator
import json
import struct
from heapq import merge

#wrapper for showing np.array() as an image
def show(image):
	scipy.misc.toimage(image).show()

def huff(lst, acc, code): # uses a binary tree to assign codes to keys
	if type(lst) is str:
		code.append((lst, acc))
	else:
		left = huff(lst[0], acc + "0", code)
		right = huff(lst[1], acc + "1", code)

#open the image and take the 2D DWT
#After that, it's up to you!
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input_image")
	parser.add_argument("output_file")
	parser.add_argument("--wavelet", help="wavelet name to use. Default=haar", default="haar")
	parser.add_argument("--quantize", help="quantization level to use. Default=4", type=int, default=4)
	args = parser.parse_args()

	input_file_name = args.input_image
	try:
		im = scipy.ndimage.imread(input_file_name, flatten=True, mode="L")
		print "Attempting to open %s..." % input_file_name
	except:
		print "Unable to open input image. Qutting."
		quit()
	# show(im)
	#get height and width
	(height, width) = im.shape
	wavelet = args.wavelet
	q = args.quantize
	w = open(args.output_file, 'wb')

	header = {'version': "CMiCv1", 'height': height, 'width': width, 'wavelet': wavelet, 'q': q}

	if height % 2 == 1:
		height += 1
		header['height_bool'] = True
		row_n = [[0] * header['width']]
		header['height_new'] = height
		print len(row_n)
		im = np.append(im, row_n, 0)
	else:
		header['height_bool'] = False
	if width % 2 == 1:
		width += 1
		header['width_bool'] = True
		header['width_new'] = width
		column_n = [[0]] * height # okay since height would change first
		im = np.hstack((im, column_n))
	else:
		header['width_bool'] = False

	print im
	print len(im)
	show(im)


	LL, (LH, HL, HH) = pywt.dwt2(im, wavelet, mode='periodization')

	'''the following block of code will let you look at the decomposed image. Uncomment it if you'd like
	'''

	dwt = np.zeros((height, width))
	dwt[0:height/2, 0:width/2] = LL
	dwt[height/2:,0:width/2] = HL
	dwt[0:height/2, width/2:] = LH
	dwt[height/2:,width/2:] = HH
	show(dwt)

	flat_LL = LL.flatten()
	flat_LL = np.insert(flat_LL, 0, 0)
	flat_LL = np.diff(flat_LL)
	flat_LL  = [np.asscalar(np.round(np.int16(x))) for  x in flat_LL]

	array_LH = np.array(LH)
	array_LH = [np.asscalar(np.round(np.int16(x)))/q for x in array_LH.flatten()]

	array_HL = np.array(HL)
	array_HL = [np.asscalar(np.round(np.int16(x)))/q for x in array_HL.flatten()]

	array_HH = np.array(HH)
	array_HH = [np.asscalar(np.round(np.int16(x)))/q for x in array_HH.flatten()]

	huff_arr = list(flat_LL) + list(array_LH) + list(array_HL) + list(array_HH)

	# huff_arr = map(str, huff_arr)
	print len(huff_arr)
	print huff_arr[0]
	print type(huff_arr[0])

	#stats
	dict1 = {}
	for val in huff_arr:
		if str(val) in dict1:
			dict1[str(val)] += 1
		else:
			dict1[str(val)] = 1
	lst = dict1.items()
	lst = sorted(lst, key=lambda y:y[1])
	while len(lst) > 1:
		z = lst[0]
		y = lst[1]
		v = z[1] + y[1]
		k = [z[0], y[0]]
		lst.append([k,v])
		lst = sorted(lst[2:], key=lambda y:y[1]) # sorts a balanced tree
	tree = lst[0][0]
	code = []
	huff(tree, "", code)
	huffman = dict(code)

	w.write(json.dumps(header))
	w.write("\n")
	w.write(json.dumps(huffman))
	w.write("\n")

	binary_string = ""
	for x in range(len(huff_arr)):
		binary_string += huffman[str(huff_arr[x])]
	if len(binary_string) % 8 != 0:
		remainder = len(binary_string) % 8
		for i in range(0, 8-remainder):
			binary_string = binary_string + "0"
	loops = list(binary_string)
	tot = float(len(binary_string))
	integer = str(''.join(loops[0:8]))
	print "Compressing..."
	while integer != "":
		progress = round(100 - 100*(float(len(loops))/tot), 2) # Progress bar
		sys.stdout.write("\r"+ str(progress) + "% completed" )
		sys.stdout.flush()
		new = int(integer,2)
		w.write(struct.pack("B",new))
		loops = loops[8:]
		integer = str(''.join(loops[0:8]))

if __name__ == '__main__':
	main()
