# -*- coding: utf-8 -*-
#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 1
# Soluciones de membrana circular que vibra
#==========================================================

#**********************************************************
#	MODULOS
#**********************************************************
import numpy as np
import scipy.special as sp
import os
import matplotlib.pylab as plt


class Circular_Membrane():
    '''=============================================================
	MEMBRANA CIRCULAR
    
	 Clase con funciones para visualizar modos de vibración 
	 normales de una membrana circular

	ARGUMENTOS:
	  *Radio de la membrana				R
	  *Velocidad de propagacion en el medio		c
    ============================================================='''

    def __init__(self, R = 1, c = 1 ):
	self.R = 1
	self.c = 1


    
    def f(self,r,theta,t,m,n):
	'''=============================================================
	   (m,n) Modo normal:
	    
	    Calcula el modo normal (m,n) de oscilación de la mebrana 
	    circular, donde n es el numero cuantico radial y m el 
	    numero angular.

	    ARGUMENTOS:
	      *Variable r					r
	      *Variable theta					theta
	      *Variable t					t
	      *Numero cuantico angular				m
	      *Numero cuantico radial				n
	============================================================='''
	lambda_mn = sp.jn_zeros(m,n)[-1]	
	return sp.jn( m, lambda_mn*r/self.R )*\
	       np.cos( lambda_mn*self.c*t/self.R )*\
	       np.cos( m* theta )



    def static_view(self,m=0,n=1,NS=100):
	'''=============================================================
	   Grafica Estatica (m,n) Modo normal:
	    
	    Realiza un grafico de densidad del modo de oscilación (m,n)
	    de la membrana circular en el tiempo t=0

	    ARGUMENTOS:
	      *Numero cuantico angular				m
	      *Numero cuantico radial				n
	      *Resolucion del grid (100 por defecto)		NS
	============================================================='''
	#Grid
	XM = np.linspace( -1*self.R, 1*self.R, NS )
	YM = np.linspace( 1*self.R, -1*self.R, NS )
	#---------------------------------------------------------------
	Z = np.zeros( (NS,NS) )
	for i in xrange( 0, NS ):
	    for j in xrange( 0, NS ):
		xd = XM[i]
		yd = YM[j]
		rd = ( xd**2 + yd**2 )**0.5
		thd = np.arctan( yd/xd )
		if xd<0:
		    thd = np.pi + thd
		if rd<self.R:
		    Z[j,i] = self.f( rd, thd, 0, m, n )
	#---------------------------------------------------------------
	Z[0,0] = -1; Z[1,0] = 1
	plt.xlabel( 'X (-R,R)' )
	plt.ylabel( 'Y (-R,R)' )
	plt.title( 'Circular Membrane: (%d,%d) mode'%(m,n) )
	plt.imshow( Z )
	plt.show()



    def dynamic_view(self,m=0,n=1,NS=100,Tmax=10,Nstep=10,v_name='video'):
	'''=============================================================
	   Grafica Dinamica (m,n) Modo normal:
	    
	    Realiza un video del modo de oscilación (m,n)  de la membrana
	    circular como un mapa de calor desde t=0 hasta t=Tmax,
	    con NStep frames.

	    ARGUMENTOS:
	      *Numero cuantico angular				m
	      *Numero cuantico radial				n
	      *Resolucion del grid (100 por defecto)		NS
	      *Tiempo Maximo					Tmax
	      *Numero de Frames					NStep
	      *Nombre del archivo de video			v_name
	============================================================='''
	#Grid
	XM = np.linspace( -1*self.R, 1*self.R, NS )
	YM = np.linspace( 1*self.R, -1*self.R, NS )
	files = []
	k = 0
	for t in np.linspace( 0, Tmax, Nstep ):
	    #-----------------------------------------------------------
	    Z = np.zeros( (NS,NS) )
	    for i in xrange( 0, NS ):
		for j in xrange( 0, NS ):
		    xd = XM[i]
		    yd = YM[j]
		    rd = ( xd**2 + yd**2 )**0.5
		    thd = np.arctan( yd/xd )
		    if xd<0:
			thd = np.pi + thd
		    if rd<self.R:
			Z[j,i] = self.f( rd, thd, t, m, n )
	    #-----------------------------------------------------------
	    Z[0,0] = -1; Z[1,0] = 1
	    plt.xlabel( 'X (-R,R)' )
	    plt.ylabel( 'Y (-R,R)' )
	    plt.title( 'Circular Membrane: (%d,%d) mode. t=%f'%(m,n,t) )
	    plt.imshow( Z )
	    print t
	    fname='_tmp-%03d.png'%k
	    k+=1
	    plt.savefig(fname)
	    files.append(fname)
	    plt.close()

	print 'Making movie animation.mpg - this make take a while'
	os.system("ffmpeg -f image2 -i _tmp-%03d.png  %s.mpg"%(v_name))
	os.system('rm -rf *.png')