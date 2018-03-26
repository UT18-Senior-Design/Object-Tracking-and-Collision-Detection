# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 12:09:53 2018

@author: James Park
"""

import numpy as np
import math


x1 = 100
x2 = 200

y1 = 250
y2 = 400

R = np.matrix([[.9488748023394,-.2911564866294,-.1219200958782],[.1049112802644,-.07339345198426,.991769428502],[-.2977083014607,-.9538560171742,-.03909559747501]])
T = np.matrix([[-1.059938136855],[1.622779443469],[.2771311359013]])

C_tl = np.matrix([[x1],[y2],[1]])
C_tr = np.matrix([[x2],[y2],[1]])
C_bl = np.matrix([[x1],[y1],[1]])
C_br = np.matrix([[x2],[y1],[1]])

l_tl = np.add(np.matmul(R,C_tl),T)
l_tr = np.add(np.matmul(R,C_tr),T)
l_bl = np.add(np.matmul(R,C_bl),T)
l_br = np.add(np.matmul(R,C_br),T)

x = np.mean([l_tl[0],l_tr[0],l_bl[0],l_br[0]])
y = np.mean([l_tl[1],l_tr[1],l_bl[1],l_br[1]])
distance = math.sqrt((x*x)+(y*y))

print (x)
print (y)
print (distance)