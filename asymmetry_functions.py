"""
@author: Jacopo Braccio, matricola 273999
"""
import functions as fc
import cv2

"""center of the mole corresponds to the center of the image since the borders are given by the outer points
of the mole"""
def center_mole (mole, top_up, top_down, top_left, top_right):
	a=int(round(mole.shape[0]/2))
	b=int(round(mole.shape[1]/2))
	return (a,b)

def ratio(image,x,y):


	partial_area = 0
	partial_area_2 = 0
	for i in range(0,image.shape[0]):
		for j in range(0,y): #y represents the row of the mean point 
			if (image[i,j,:] == [255,255,255]).all():
				partial_area = partial_area + 1 #partial white area of the left half of the mole
		for j in range(y,image.shape[1]):
			if (image[i,j,:] == [255,255,255]).all():
				partial_area_2 = partial_area_2 + 1 #partial white area of the right half of the mole

	for i in range(0,image.shape[0]):
		image[i,y,:] = [255,0,0] #draw red line along the straight vertical dividing the images into two parts

	image = cv2.circle(image,(y,x),2,[0,255,0],-1)
	fc.showimage("Division of the mole into 2 parts", image)


	percentage_left = ((partial_area)/(y*image.shape[0]))*100
	percentage_right = ((partial_area_2)/(y*image.shape[0]))*100

	if (partial_area > partial_area_2):
		ratio = partial_area_2/partial_area
	if (partial_area < partial_area_2):
		ratio = partial_area/partial_area_2
	if (partial_area == partial_area_2):
		ratio = 1

	print("The asymmetry parameter is equal to: ", round(ratio,4))
	return round(ratio,4)

