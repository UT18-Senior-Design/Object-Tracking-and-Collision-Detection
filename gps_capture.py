import socket
import os
import pandas as pd

HOST = "192.168.1.201"
PORT = 8308

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('', PORT))


data = soc.recv(554)
data_string = data[206:270].decode('utf-8')
data_list = data_string.split(",")

df = pd.DataFrame(data_list)

latitude = df.iloc[3][0]+df.iloc[4][0]
longitude = df.iloc[5][0]+df.iloc[6][0]
speed = df.iloc[7][0]
time = df.iloc[1]

print (latitude)
print (longitude)
print (speed)

'''
print (data[206:270])
latitude = data[222:233]
print (latitude)
longitude = data[234:246]
print (longitude)
velocity = data[210:270]
print (velocity)
'''


                
                