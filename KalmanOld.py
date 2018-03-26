#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 22:01:51 2018

@author: evanreid
"""

import numpy as np
import matplotlib.pyplot as plt


locarray = np.empty([1,3])

with open("obj_pose-laser-radar-synthetic-ukf-input.txt","r") as f:
    for line in f:
        location = line.lower()
        location = location.replace("\n","")
        location = location.split("\t")
        for n in range(len(location)):
           location[n] = float(location[n])
        locarray = np.append(locarray, [location], axis = 0)
plt.plot(locarray[1:,0],locarray[1:,1])
plt.title("Input")
plt.show()

"""Initialize all of the matrices that we will use """
delta_t = 1

F_ = np.array([[1, 0, delta_t, 0],[0, 1, 0, delta_t],[0, 0, 1, 0], [0, 0, 0, 1]])

R_laser = np.eye(4)*0.0225


H_laser = np.array([[1,0,0,0],[0,1,0,0]])

P_ = np.array([[1,0,0,0],[0,1,0,0],[0,0,1000,0],[0,0,0,1000]])

Q_ = np.array([[0.25*R_laser[0,0]*delta_t**4, 0, 0.5*R_laser[0,0]*delta_t**3,0],
               [0,0.25*R_laser[1,1]*delta_t**4 ,0,0.5*R_laser[0,0]*delta_t**3],
               [0.5*R_laser[0,0]*delta_t**3,0,R_laser[0,0]*delta_t**2,0],
               [0, 0.5*R_laser[0,0]*delta_t**3, 0,R_laser[1,1]*delta_t**2 ]])

noise_ax = 9
noise_ay = 9

""" Start the code for the FIlter """
x_ = np.array([0, 0, 1, 1])
results = np.empty([1,2])
with open("results.txt", "w+") as f:
    for n in range(1,len(locarray)):
        
        #Predict 
        x_ = F_.dot(x_)
        P_ = F_.dot(P_).dot(F_.T) + Q_
        # Kalman Update
        z = np.array([locarray[n,0],locarray[n,1], locarray[n,0]-locarray[n-1,0], locarray[n,1]-locarray[n-1,1]])
        y = z-x_
        S = P_ + R_laser
        K = P_.dot(np.linalg.inv(S))
        x_ = x_ + K.dot(y)
        P_ = (np.eye(len(P_))-K).dot(P_)
        for n in range(2):
            f.write(str(x_[n])+"\t")
        f.write("\n")
        results = np.append(results, [x_[0:2]], axis = 0)
plt.plot(results[:,0], results[:,1])
plt.title("Results")
        





