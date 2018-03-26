import socket
import os

HOST = "192.168.1.201"
PORT = 2368

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('', PORT))

while True:
	data = soc.recv(1248)
	raw_data = data[:-6]
	for k in range(12):
		offset = k * 100
		#print('Block #: {}'.format(k))
		azimuth = raw_data[2+offset] | (raw_data[3+offset] << 8)
		azimuth = azimuth / 100
		#print(raw_data)
		#print('azimuth: {}\n'.format(azimuth/100))
		#for k in range(12):
		for i in range(2):
			count = 0
			for j in range(16):
				distance = raw_data[4+j*3+i*48+offset] | (raw_data[5+j*3+offset] << 8)
				distance = distance / 500
				reflectivity = data[6+j*3+offset]
				print('Channel: ', j, 'Angle: ', azimuth, 'Distance: ', distance)
				if azimuth >= 0.0 and azimuth <= 1.0 and distance < 1.0:
					count += 1
					#print(distance)
			if count > 7:
				os.system('say "close" &')
