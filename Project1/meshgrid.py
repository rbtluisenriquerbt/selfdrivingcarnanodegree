# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
##nx, ny = (3,2)
##x = np.linspace(0,1,nx)
##y = np.linspace(0,1,ny)

##xv, yv = np.meshgrid(x,y, sparse = True)

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

xx, yy = np.meshgrid(x, y, sparse=True)

z = np.sin(xx**2 + y**2) / (xx*2 + y**2)
