import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
#from matplotlib import pyplot as plt

from copy import deepcopy
prima = io.imread("primazon1.png")

red_channel = deepcopy(prima)
green_channel = deepcopy(prima)
blue_channel = deepcopy(prima)

red_channel[:,:,1]=0
red_channel[:,:,2]=0

green_channel[:,:,0]=0
green_channel[:,:,2]=0

blue_channel[:,:,0]=0
blue_channel[:,:,1]=0

fig, ax = plt.subplots(ncols=2, nrows = 2)

ax[0,0].imshow(prima)
ax[0,0].set_title("Original")

ax[0,1].imshow(red_channel)
ax[0,1].set_title("Filter Merah")

ax[1,0].imshow(green_channel)
ax[1,0].set_title("Filter Hijau")

ax[1,1].imshow(blue_channel)
ax[1,1].set_title("Filter Biru")

plt.show()