"""
@author: Jacopo Braccio s273999
"""
"""Perform K_NN algorithm over a test vector in order to check the 
accuracy of a classifier based only on the two features found (border and asymmetry)"""

#class 0 corresponds to low risk
#class 1 corresponds to medium risk
#class 2 corresponds to melanoma

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = pd.read_csv("classification.csv")
x = x.drop("Name", axis = 1)

train = x.to_numpy()

counter_low = 0
counter_med = 0
counter_mel = 0

for i in range (0, train.shape[0]):
    if train[i,2] == 0:
        counter_low = counter_low + 1 
    if train[i,2] == 1:
        counter_med = counter_med + 1
    if train [i,2] == 2:
        counter_mel = counter_mel + 1

low_ris = np.zeros((counter_low,3))
medium_ris = np.zeros((counter_med,3))
melanoma = np.zeros((counter_mel,3))

#Separate the three different classes in three different nparrays
j = 0
for i in range (0,train.shape[0]):
    if train[i,2] == 0:
        low_ris[j,:] = train[i,:]
j = 0
for i in range (0,train.shape[0]):
    if train[i,2] == 1:
        medium_ris[j,:] = train[i,:]
        j = j+1
j = 0
for i in range (0,train.shape[0]):     
    if train [i,2] == 2:
        melanoma[j,:] = train[i,:]
        j = j+1


#test vector ./images/low_risk_11.jpg,1.1637,0.86,0 
test = np.array((1.1637,0.86))

distance_vector = np.zeros((train.shape[0],2)) #(distance,class)
for i in range (0,train.shape[0]):
    distance = ((test[0] - train[i,0])**2 + (test[1] - train[i,1])**2)**(1/2)
    distance_vector[i,0] = distance
    distance_vector[i,1] = train[i,2]

distance_vector = distance_vector[distance_vector[:,0].argsort()]
k_nn = distance_vector[0:5,:]

#count the occurrencies of each class in the distance vector
counter_low = 0
counter_med = 0
counter_mel = 0
for i in range (0, k_nn.shape[0]):
    if k_nn[i,1] == 0:
        counter_low = counter_low + 1 
    if k_nn[i,1] == 1:
        counter_med = counter_med + 1
    if k_nn[i,1] == 2:
        counter_mel = counter_mel + 1
prob_low = round(counter_low/k_nn.shape[0],2)*100
prob_med = round(counter_med/k_nn.shape[0],2)*100
prob_mel = round(counter_mel/k_nn.shape[0],2)*100

print(f"The probability is: {prob_low}% of being low_risk, {prob_med}% of being medium_risk, {prob_mel}% of being melanoma")

plt.xlabel("Asymmetry")
plt.ylabel("Ratio")
plt.scatter(low_ris[:,0],low_ris[:,1])
plt.scatter(medium_ris[:,0],medium_ris[:,1])
plt.scatter(melanoma[:,0], melanoma[:,1])
plt.scatter(test[0],test[1])
plt.show()