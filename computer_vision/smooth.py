import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/audi.jpeg',0)
# img = cv2.medianBlur(img,5)

th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(th,-1,kernel)

plt.subplot(121),plt.imshow(th, 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst, 'gray'),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


