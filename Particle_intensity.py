#import np as np
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Read txt file as matrix
# Relative path needs ./(folder)/(file name)
input = []
input.append(np.loadtxt("./raw data/150C.txt", dtype='f'))

bwr = cm.get_cmap('bwr', 256)  # get colormap
viridis = cm.get_cmap('viridis', 256)

def CalculateParticleintensity (img, str) :
	average = img.mean()

	# Crop the image to ROI
	img_2 = img[356:1754, 370:1768]

	particle_area = np.where(img_2 < average, img_2, 0)

	# Show colormap of particle area which has lower intensity than average intensity of TEM image
	plt.imshow(particle_area, cmap=viridis)
	plt.colorbar(label='color')
	plt.title(str)
	plt.show()

	below_avr = np.where(img_2 < average)
	print("Average intensity at", str, " is ", img_2[below_avr].mean())


CalculateParticleintensity(input[0], "150C")
