#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 2
# Comparacion de solucion completa y aproximada para el 
# pendulo simple
#==========================================================
import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integ

#Solucion aproximada
def Theta(t):
    theta = theta0*np.sin( omega0*t + delta )
    return theta

#Ecuaciones de movimiento
def dF(Y, t):
    #Valor anterior de theta
    theta = Y[0]
    #Valor anterior de omega
    omega = Y[1]
    #Valor anterior de la tension
    tension = Y[2]
    #Derivada de theta
    Dtheta = omega
    #Derivada de omega
    Domega = -g*np.sin( theta )/l
    #Derivada de la tension
    Dtension = -3*omega**m*g*np.sin( theta )
    return (Dtheta, Domega, Dtension)
    
#Gravedad
g = 9.8
#Longitud
l = 1
#Masa
m = 1
#Frecuencia
omega0 = np.sqrt( g/l )
#Tiempos
tiempo = np.arange( 0, 10, 0.01 )
    
#SOLUCION APROXIMADA
#Amplitud
theta0 = 0.17
#Fase
delta = np.pi/2.
#Grafica
plt.plot( tiempo, Theta(tiempo), label='solucion aproximada' )

#SOLUCION NUMERICA
#Angulo inicial
theta_t0 = 0.17
#Velocidad angular inicial
omega_t0 = 0.0
#Tension inicial
tension_t0 = m*l*omega_t0**2 + m*g*np.cos( theta_t0 )
#Condiciones iniciales
cond_ini = ( theta_t0, omega_t0, tension_t0 )
#Solucion numerica
theta_t, omega_t, tension_t = np.transpose( 
integ.odeint( dF, cond_ini, tiempo ) )
#Grafica
plt.plot( tiempo, theta_t, label='solucion numerica' )

plt.legend()
plt.show()