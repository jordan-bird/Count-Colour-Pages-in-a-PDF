import sys

import pdf2image
import numpy as np

def count_pages(filename):
	print("Converting PDF to images...")
	images = pdf2image.convert_from_path(filename)
	print("Done.")
	total_pages = len(images)
	print("Total number of pages: " + str(total_pages))

	print("Counting B/W and colour pages...")
	sw=0
	colour=0
	for count, image in enumerate(images):
		print("Analysing page " + str(count) + "/" + str(total_pages), end="\r")
		img = np.array(image.convert('HSV'))
		hsv_sum = img.sum(0).sum(0)
		if hsv_sum[0] == 0 and hsv_sum[1] == 0:
			sw += 1
		else:
			colour += 1
	print("Analysing page " + str(total_pages) + "/" + str(total_pages))

	print("\nB/W: " + str(sw))
	print("Colour: " + str(colour))
	
if __name__ == "__main__":
	filename = str(sys.argv[1])
	if not filename.endswith(".pdf"):
		filename += ".pdf"
	print("Counting Colour/BW pages in: " + filename)
	count_pages(filename)