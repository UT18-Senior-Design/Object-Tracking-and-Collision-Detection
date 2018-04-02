#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 22:01:51 2018

@author: evanreid
"""

"""imports"""
import numpy as np
import matplotlib.pyplot as plt


"""Initialize all of the matrices that we will use"""
delta_t = 1
F_ = np.array([[1, 0, delta_t, 0],[0, 1, 0, delta_t],[0, 0, 1, 0], [0, 0, 0, 1]])
R_laser = np.eye(4)*0.0225
H_laser = np.array([[1,0,0,0],[0,1,0,0]])
#P_ = np.array([[1,0,0,0],[0,1,0,0],[0,0,1000,0],[0,0,0,1000]])
Q_ = np.array([[0.25*R_laser[0,0]*delta_t**4, 0, 0.5*R_laser[0,0]*delta_t**3,0],
               [0,0.25*R_laser[1,1]*delta_t**4 ,0,0.5*R_laser[0,0]*delta_t**3],
               [0.5*R_laser[0,0]*delta_t**3,0,R_laser[0,0]*delta_t**2,0],
               [0, 0.5*R_laser[0,0]*delta_t**3, 0,R_laser[1,1]*delta_t**2 ]])

""" Start the code for the FIlter """
#x_ = np.array([0, 0, 1, 1])
#results = np.empty([1,2])


""" Kalman Filter Class """
class Kalman:
    def __init__(self, x, P, locarray):
        self.x_ = x
        self.P_ = P
        self.results = np.empty([1,2])
        self.locarray = locarray
    def update_locarray(self, locarray):
        self.locarray = locarray
    def calc(self):
        for n in range(1,len(self.locarray)):   
            #Predict 
            self.x_ = F_.dot(self.x_)
            self.P_ = F_.dot(self.P_).dot(F_.T) + Q_
            # Kalman Update
            self.z = np.array([self.locarray[n,0],self.locarray[n,1], self.locarray[n,0]-self.locarray[n-1,0], self.locarray[n,1]-self.locarray[n-1,1]])
            self.y = self.z-self.x_
            self.S = self.P_ + R_laser
            self.K = self.P_.dot(np.linalg.inv(self.S))
            self.x_ = self.x_ + self.K.dot(self.y)
            self.P_ = (np.eye(len(self.P_))-self.K).dot(self.P_)
            self.results = np.append(self.results, [self.x_[0:2]], axis = 0)    
        plt.plot(self.results[:,0], self.results[:,1])
        plt.title("Results")
        plt.xlabel('x (meters)')
        plt.ylabel('y (meters)')
        plt.legend(['Object 1', 'Object 2'])
        




"""MAIN"""

#sample constructor data
P_sample = np.array([[1,0,0,0],[0,1,0,0],[0,0,1000,0],[0,0,0,1000]])
x_sample = np.array([0, 0, 1, 1])

"""GET LOCARRAY INPUT"""
locarray1 = np.empty([1,3])
with open("obj_pose-laser-radar-synthetic-ukf-input1.txt","r") as f:
    for line in f:
        location = line.lower()
        location = location.replace("\n","")
        location = location.split("\t")
        for n in range(len(location)):
           location[n] = float(location[n])
        locarray1 = np.append(locarray1, [location], axis = 0)
plt.plot(locarray1[1:,0],locarray1[1:,1])
plt.xlabel('x (meters)')
plt.ylabel('y (meters)')
#plt.title("Input")
#plt.show()

locarray2 = np.empty([1,3])
with open("obj_pose-laser-radar-synthetic-ukf-input2.txt","r") as f:
    for line in f:
        location = line.lower()
        location = location.replace("\n","")
        location = location.split("\t")
        for n in range(len(location)):
           location[n] = float(location[n])
        locarray2 = np.append(locarray2, [location], axis = 0)
plt.plot(locarray2[1:,0],locarray2[1:,1])
plt.title("Input")
plt.legend(['Object 1', 'Object 2'])
plt.show()




sample_k = Kalman(x_sample, P_sample, locarray1)
#sample_k.update_locarray(locarray1)
sample_k.calc()

sample_k_2 = Kalman(x_sample, P_sample, locarray2)
#sample_k_2.update_locarray(locarray2)
sample_k_2.calc()

