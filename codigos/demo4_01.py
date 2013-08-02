# -*- coding: utf-8 -*-
#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 1
# Interferencia de Ondas
#==========================================================

#**********************************************************
#	MODULOS
#**********************************************************
import numpy as np
import os
import matplotlib.pylab as plt

#Funcion de amplitud de una fuente
def Z_amplitud(x, y, x0, y0, A0, t):
    #Posicion de la fuente
    r0 = np.array([x0, y0])
    #Posicion donde se evalua el campo
    r = np.array([x, y])
    return A0*np.sin( 2*np.pi*(t/f - np.linalg.norm(r-r0)/lamb ) )

#PARAMETROS
#frecuencia		[Hz]
f = 10.
#Longitud de onda	[m]
lamb = 1.0
#Tamano de la caja	[m]
L = 10.0
#Resolucion grid caja
NS = 100

#Posicion X fuente 1	[m]
x01 = 1.0	
#Posicion Y fuente 1	[m]
y01 = 2.0
#Amplitud fuente 1	[m]
A01 = 0.1
#Posicion X fuente 2	[m]
x02 = 5.0	
#Posicion Y fuente 2	[m]
y02 = 5.0
#Amplitud fuente 2	[m]
A02 = 0.1

#Tiempo final		[s]
Tmax = 20.0
#Numero de intervalos
Nstep = 41

#GRID Y EVOLUCION
XM = np.linspace( 0, L, NS )
YM = np.linspace( 0, L, NS )

k = 0
for t in np.linspace( 0, Tmax, Nstep ):
    #-----------------------------------------------------------
    Z = np.zeros( (NS,NS) )
    for i in xrange( 0, NS ):
	for j in xrange( 0, NS ):
	    x = XM[i]
	    y = YM[j]
	    Z[-j,i] = Z_amplitud(x, y, x01, y01, A01, t) + \
	    Z_amplitud(x, y, x02, y02, A02, t)
    #-----------------------------------------------------------
    plt.xlabel( 'X (0,L)' )
    plt.ylabel( 'Y (0,L)' )
    plt.title( 'Interfencia: t=%f'%(t) )
    plt.imshow( Z, extent = (0,L,0,L), vmax = A01 + A02 )
    print t
    fname='_tmp-%03d.png'%k
    k+=1
    plt.savefig(fname)
    plt.close()

print 'Making movie animation.mpg - this make take a while'
os.system("ffmpeg -f image2 -i _tmp-%03d.png  video.mpg")
os.system('rm -rf *.png')