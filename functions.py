"""
@author: Jacopo Braccio, matricola 273999
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster


"""Function for showing images"""
def showimage(title, im):
    plt.figure()
    plt.imshow(im)
    plt.title(title)
    plt.show()
"""---"""

"""Function for quantizing image through KMeans method"""
def quantize(img, n_colors):
    [width , height, depth] = img.shape
    img_2D = np.reshape(img, (width * height, depth)) #make the image 2 dimensional
    model = cluster.KMeans(n_clusters = n_colors, random_state = 0)
    labels = model.fit_predict(img_2D)
    palette = model.cluster_centers_.astype('uint8')
    quantized_img = np.reshape(palette[labels], (width, height, palette.shape[1]))
    return (quantized_img, palette)
"""---"""

"""Function for finding the darkest cluster:
'palette' has inside all the colours representing the clusters, it has been sorted in order that the darkest one is on top.
modificato rispetto l'inizio visto che 5 cluster li riclusterizzo in 3"""

def darkest_cluster(palette, n_clusters):
    if (n_clusters == 3):
        darkest = np.zeros((1,3))
        darkest[0,:] = palette[0,:]
    if (n_clusters >= 5):
        darkest = np.zeros((2,3))
        darkest[0,:] = palette[0,:]
        darkest[1,:] = palette[1,:]
    return (darkest)
"""---"""


"""Function used to isolate the darkest cluster which is representing the mole. This function will make white all the pixels not
belonging to te darkest cluster, and black the others"""
def isolate_cluster(quant_im, darkest_colour):
    counter = 0
    for i in range (0,quant_im.shape[0]):
        for j in range (0,quant_im.shape[1]):
            if (quant_im[i,j,:] != darkest_colour).all():
                quant_im[i,j,:] = [255,255,255]
            else: 
                quant_im[i,j,:] = [0,0,0]
                counter = counter +1
    return (quant_im)
"""---"""

"""Creating a 2D matrix of zeros and 1 representing the black and white image which is still 3D"""
def zero_one_matrix (mole):
    zero_one_m = np.zeros((mole.shape[0],mole.shape[1]))
    for i in range (0, mole.shape[0]):
        for j in range(0,mole.shape[1]):
            if (mole[i,j,:] == [255,255,255]).all():
                zero_one_m[i,j] = 0 #white
            else:
                zero_one_m[i,j] = 1 #black
    return zero_one_m

"""By averaging small portion of the image, small groups of single pixels and single pixel can be eliminated,
or white portion inside the moles are filled."""
def smoothing(zero_one_m,mole):
    area = 0 
    for i in range(2, mole.shape[0]-2): #per evitare collisione con i bordi
        for j in range(2, mole.shape[1]-2):#per evitare collisione con i bordi
            average = submatrix = zero_one_m[i-2:i+3, j-2:j+3].sum()/25 
            if (average < 0.4):
                mole[i,j,:] = [255,255,255]
            if (average  > 0.4):
                mole[i,j,:] = [0,0,0]
                area = area +1
    return (mole,area)
"""---"""

"""Drawing borders of the mole: check when the colour changes from left to right or from top to bottom"""
def borders(mole):
    perimeter = 0
    for i in range (0,mole.shape[0]-1):
        for j in range (0, mole.shape[1]-1):
            if ((mole[i,j,:] != mole[i,j+1,:]).all() or (mole[i,j,:] != mole[i+1,j,:]).all()):
                mole[i,j,:] = [0,0,255]
                perimeter += 1
            else:
                mole[i,j,:] = [255,255,255]
    return (mole, perimeter)
"""---"""

