# -*- coding: utf-8 -*-
#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 2
# Efecto Doppler
#==========================================================

#**********************************************************
#	MODULOS
#**********************************************************
import numpy as np
import os
import matplotlib.pylab as plt
import AudioLib as ad

#Velocidad del sonido [m/s]
vs = 331.5

#Creando objeto de audio
sonido = ad.audio()

#Intervalo de tiempo
dt = 1/(44100.)
#Frecuencia de nota [Hz]
freq0 = 110.

#Tiempo maximo	[s]
tmax = 6.
#Arreglo de tiempo
tiempo = np.arange( 0, tmax, dt )
#Nota a reproducir
nota = ad.Amplitude*np.sin( 2*np.pi*freq0*tiempo )

#Cargando nota de audio
sonido.load( nota )
#Reproduciendo sonido
sonido.play()

#EFECTO DOPPLER ===========================================
#Creando objeto de audio asociado al observador
sonido_doppler = ad.audio()

#Distancia del observador a la carretera [m]
Lo = 1.0
#Velocidad del carro [m/s]
v_car = 6.0
#Distancia del carro inicialmente [m]
d_car = 18.0
#Tiempo de efecto doppler [s]
tmaxD = 6.0
#Arreglo de tiempo
tiempoD = np.arange( 0, tmaxD, dt )
#Numero de intervalos
Nt = int(len(tiempoD)/2.)

#Funcion de posicion del carro
def pos( t ):
    return -d_car + v_car*t
    
#Funcion de velocidad del carro dirigida a la fuente
def vel( t ):
    return v_car*1/np.sqrt( 1 + Lo**2/pos(t)**2 )
    
#Funcion de decaimiento de intensidad
def I( d ):
    return ad.Amplitude*np.exp(-abs(d)/20.)
    
#Transformacion de frecuencia Dopple
def freq( freq0, v, cond ):
    if cond == "Aleja":
	return freq0*vs/(vs - v)
    if cond == "Acerca":
	return freq0*vs/(vs + v)

#Calculo de efecto Doppler para la nota inicial
notaD = np.zeros( 2*Nt )
#Cuando la fuente se acerca
notaD[:Nt] = I( pos(tiempoD[:Nt]) )*\
np.sin( 2*np.pi*freq(freq0, vel( tiempoD[:Nt] ), 'Acerca')*tiempoD[:Nt] )
#Cuando la fuente se aleja
notaD[Nt:] = I( pos(tiempoD[Nt:]) )*\
np.sin( 2*np.pi*freq(freq0, vel( tiempoD[Nt:] ), 'Aleja')*tiempoD[Nt:] )

#Cargando nota de audio
sonido_doppler.load( notaD )
#Reproduciendo sonido
sonido_doppler.play()
#Graficando Sonido
sonido_doppler.plot()