# -*- coding: utf-8 -*-
"""Manahil_Shaikh_Color_Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EIZqmth9zz9dstblHSdVFhkiRFRid0WM
"""

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os

from google.colab.patches import cv2_imshow

"""Read the Image and convert to RGB using OpenCV functionalities"""

Image = cv2.imread('/content/colorpic.jpg')
Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
cv2_imshow(Image)

"""Image Pre-preocessing"""

Resized_image = cv2.resize(Image, (600, 400), interpolation = cv2.INTER_AREA)
cv2_imshow(Resized_image)
modified_image = Resized_image.reshape(-1, 3)
print(modified_image.shape)

"""Loading Kmeans model"""

KM = KMeans()

labels = KM.fit_predict(modified_image)

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

KMeans_counts = Counter(labels)

def Plotting(cent , counts):
  center_colors = cent.cluster_centers_
  ordered_colors = [center_colors[i] for i in counts.keys()]
  rgb_colors = [ordered_colors[i] for i in counts.keys()]
  hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]

  plt.figure(figsize = (8, 6))
  plt.pie(counts.values(), labels = hex_colors , colors = hex_colors)

Plotting(KM,KMeans_counts)

"""#References
https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71
"""