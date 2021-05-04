"""
@author: Jacopo Braccio, matricola 273999
"""

"""Find the interval in which the mole is contained
In orderd to make this method work, some images have been manually centered.
Starting from the center of the images, the algorithm moves in the main four direction
(top, bottom, left, right) in order to find the farest pixel, those will be representing
mole's limits."""

def crop_image(img, x_center, y_center):
    
    top_down = y_center
    top_up = y_center
    top_left = x_center
    top_right = x_center
    
    """Find the temporany values of the outer poitns"""
    if (img[x_center, y_center, :] == [0,0,0]).all(): 
        #lowest pixel of the mole from the center
        while True:
            top_right += 1
            if (img[x_center, top_right, :] != [0,0,0,]).all(): #x più a destra
                break        
        while True:
            top_left = top_left - 1
            if (img[x_center, top_left, :] != [0,0,0,]).all(): #x più a sinistra
                break      
        while True:
            top_up = top_up - 1
            if (img[top_up, y_center, :] != [0,0,0,]).all(): #y più in alto
                break   
        while True:
            top_down += 1
            if (img[top_down, y_center, :] != [0,0,0,]).all(): #y più in basso
                break     
"""Update each value of the outer points by scanning through columns and rows"""
    #Top_RIGHT Update
    for x in range (top_right, img.shape[0]):
        counter = 0
        for y in range (top_up, top_down):
            if (img[y,x,:] == [0,0,0]).all():
                counter += 1
        if (counter == 0):
            top_right = x
            break
    #TOP_DOWN Update
    for x in range (top_down, img.shape[0]):
        counter = 0
        for y in range (top_left, top_right):
            if (img[x,y,:] == [0,0,0]).all():
                counter += 1
        if (counter == 0):
            top_down = x
            brea
    #TOP_UP Update
    for x in range (top_up, 0, -1): #inverse loop
        counter = 0
        for y in range (top_left, top_right):
            if (img[x,y,:] == [0,0,0]).all():
                counter += 1
        if (counter == 0):
            top_up = x
            break       
    #TOP_left Update
    for x in range (top_left, 0, -1): #inverse loop
        counter = 0
        for y in range (top_up, top_down):
            if (img[y,x,:] == [0,0,0]).all():
                counter += 1
        if (counter == 0):
            top_left = x
            break

    return (top_up, top_down, top_left, top_right)

    
    