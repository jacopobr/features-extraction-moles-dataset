"""
@author: Jacopo Braccio, matricola 273999
"""
import copy
import functions as fc
import numpy as np
import matplotlib.image as mpimg
import moles_list as ml
import crop_image as crop
import asymmetry_functions as asy

"""Load the image and show it."""
title = input("Insert the name of the picture you want to examinate (without '.jpg' extension): ")
filein = f"./images/{title}.jpg"
im_or = mpimg.imread(filein)
fc.showimage('Original image:', im_or)

"""Quantize the image"""
if (filein in ml.cluster_3):
    number_clusters = 3
    [quantized_im, palette] = fc.quantize(im_or,number_clusters)
if (filein in ml.cluster_5):
    number_clusters = 5
    [quantized_im, palette] = fc.quantize(im_or,number_clusters)
fc.showimage('Quantized image:', quantized_im)

"""Finding the darkest cluster which should correspond to the mole"""
palette = np.sort(palette, axis = 0) #collection of centroids
darkest = fc.darkest_cluster(palette, number_clusters)

"""Printing the mole as a black and white image"""
isol = fc.isolate_cluster(quantized_im,darkest)
fc.showimage("Binary image: ", isol)

"""Centering the mole"""
center_of_image_x = round(isol.shape[0]/2)
center_of_image_y = round(isol.shape[1]/2)
(top_up, top_down, top_left, top_right) = crop.crop_image(isol, center_of_image_x, center_of_image_y)
mole = isol[top_up - 5 : top_down + 5, top_left - 5: top_right + 5, :] #printing the cropped image with some margins of tollerance
fc.showimage("Mole before smoothing: ",mole)

"""Removing noise by smoothing"""
zero_one_m = fc.zero_one_matrix(mole)
(filtered_mole, area) = fc.smoothing(zero_one_m, mole)
fc.showimage("Mole after smoothing:", filtered_mole)
area = round(area,2)
ideal_perimeter = round(2 * 3.14 * (area/3.14)**(1/2),3)
fil_mol = copy.deepcopy(filtered_mole)

"""Drawing borders"""
[borders, perimeter] = fc.borders(fil_mol)
fc.showimage('Border of the mole: ', borders)
ratio = round(perimeter/ideal_perimeter,4)
print(f"{filein} -> area = {area} px^2, ideal perimeter {ideal_perimeter} px, measuerd perimeter: {perimeter} px, ratio: {ratio}")

"""asymmetry"""
(top_up, top_down, top_left, top_right) = crop.crop_image(filtered_mole, round(filtered_mole.shape[0]/2), round(filtered_mole.shape[1]/2))
filtered_mole = filtered_mole[top_up:top_down,top_left+1:top_right,:]
(x,y) = asy.center_mole(filtered_mole,top_up, top_down, top_left, top_right)
asy.ratio(filtered_mole,x,y)
