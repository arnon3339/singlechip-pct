from PIL import Image
import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
import numpy as np
import cv2

plt.figure()
# filename = get_testdata_files("../image/imgs/cp600.dcm")
ds = pydicom.dcmread("/home/g0/Projects/pct/image/imgs/cp600.dcm")
image = plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
image._A
fig = plt.gcf()
fig.canvas.draw()
img_arr = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
# img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
img_arr = cv2.cvtColor(img_arr, cv2.COLOR_RGB2BGR)
plt.close()

img = Image.fromarray(img_arr)
img.show()