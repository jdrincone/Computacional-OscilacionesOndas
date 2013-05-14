#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 3: Parte 1
# Solucion numerica de 4 pendulos simples acoplados
#==========================================================
from __future__ import division
import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as integ

#Ecuaciones de movimiento
def dF(Y, t):
    #Valor anterior de theta pendulo 1
    theta1 = Y[0]
    #Valor anterior de omega pendulo 1
    omega1 = Y[1]
    #Valor anterior de la tension pendulo 1
    tension1 = Y[2]
    
    #Valor anterior de theta pendulo 2
    theta2 = Y[3]
    #Valor anterior de omega pendulo 2
    omega2 = Y[4]
    #Valor anterior de la tension pendulo 2
    tension2 = Y[5]
    
    #Valor anterior de theta pendulo 3
    theta3 = Y[6]
    #Valor anterior de omega pendulo 3
    omega3 = Y[7]
    #Valor anterior de la tension pendulo 3
    tension3 = Y[8]
    
    #Valor anterior de theta pendulo 4
    theta4 = Y[9]
    #Valor anterior de omega pendulo 4
    omega4 = Y[10]
    #Valor anterior de la tension pendulo 4
    tension4 = Y[11]
    
    #Derivada de theta pendulo 1
    Dtheta1 = omega1
    #Derivada de omega pendulo 1
    Domega1 = -(g/l1)*np.sin( theta1 ) + \
    f*(g/l1)*( theta2 )*np.cos( theta1 )
    #Derivada de la tension pendulo 1
    Dtension1 = 3*omega1*(-m*g*np.sin( theta1 ) + \
    f*m*g*( theta2 )*np.cos( theta1 )) + \
    f*m*g*( omega2 )*np.sin( theta1 )
    
    #Derivada de theta pendulo 2
    Dtheta2 = omega2
    #Derivada de omega pendulo 2
    Domega2 = -(g/l2)*np.sin( theta2 ) + \
    f*(g/l2)*( theta1 + theta3 )*np.cos( theta2 )
    #Derivada de la tension pendulo 2
    Dtension2 = 3*omega2*(-m*g*np.sin( theta2 ) + \
    f*m*g*( theta1 + theta3 )*np.cos( theta2 )) + \
    f*m*g*( omega1 + omega3 )*np.sin( theta2 )
    
    #Derivada de theta pendulo 3
    Dtheta3 = omega3
    #Derivada de omega pendulo 3
    Domega3 = -(g/l3)*np.sin( theta3 ) + \
    f*(g/l3)*( theta2 + theta4 )*np.cos( theta3 )
    #Derivada de la tension pendulo 3
    Dtension3 = 3*omega3*(-m*g*np.sin( theta3 ) + \
    f*m*g*( theta2 + theta4 )*np.cos( theta3 )) + \
    f*m*g*( omega2 + omega4 )*np.sin( theta3 )
    
    #Derivada de theta pendulo 4
    Dtheta4 = omega4
    #Derivada de omega pendulo 4
    Domega4 = -(g/l4)*np.sin( theta4 ) + \
    f*(g/l4)*( theta3 )*np.cos( theta4 )
    #Derivada de la tension pendulo 4
    Dtension4 = -3*omega4*(-m*g*np.sin( theta4 ) + \
    f*m*g*( theta3 )*np.cos( theta4 )) + \
    f*m*g*( omega3 )*np.sin( theta4 )
    
    return (Dtheta1, Domega1, Dtension1, \
    Dtheta2, Domega2, Dtension2, \
    Dtheta3, Domega3, Dtension3, \
    Dtheta4, Domega4, Dtension4)
    
#Gravedad
g = 9.8
#Masa de todos los pendulos
m = 1.
#Longitud pendulo 1
l1 = 1.0
#Longitud pendulo 2
l2 = 2.0
#Longitud pendulo 3
l3 = 3.0
#Longitud pendulo 4
l4 = 2.0
#Factor de acoplamiento 
f = 0.10
#Tiempos
tiempo = np.arange( 0, 200, 0.1 )
    

#SOLUCION NUMERICA
#Condicion inicial pendulo 1
#Angulo inicial
theta1_t0 = 0.0
#Velocidad angular inicial
omega1_t0 = 0.0
#Tension inicial
tension1_t0 = m*l1*omega1_t0**2 + m*g*np.cos( theta1_t0 )

#Condicion inicial pendulo 2
#Angulo inicial
theta2_t0 = 0.0
#Velocidad angular inicial
omega2_t0 = 0.0
#Tension inicial
tension2_t0 = m*l2*omega2_t0**2 + m*g*np.cos( theta2_t0 )

#Condicion inicial pendulo 3
#Angulo inicial
theta3_t0 = 0.0
#Velocidad angular inicial
omega3_t0 = 0.0
#Tension inicial
tension3_t0 = m*l3*omega3_t0**2 + m*g*np.cos( theta3_t0 )

#Condicion inicial pendulo 4
#Angulo inicial
theta4_t0 = np.pi/4
#Velocidad angular inicial
omega4_t0 = 0.0
#Tension inicial
tension4_t0 = m*l3*omega3_t0**2 + m*g*np.cos( theta3_t0 )

#Condiciones iniciales de todos los pendulos
cond_ini = ( theta1_t0, omega1_t0, tension1_t0, \
theta2_t0, omega2_t0, tension2_t0,\
theta3_t0, omega3_t0, tension3_t0,
theta4_t0, omega4_t0, tension4_t0)
#Solucion numerica de todos los pendulos
theta1_t, omega1_t, tension1_t, \
theta2_t, omega2_t, tension2_t, \
theta3_t, omega3_t, tension3_t, \
theta4_t, omega4_t, tension4_t = \
np.transpose( integ.odeint( dF, cond_ini, tiempo ) )

#Guardado de resultados en archivo externo
datos = np.transpose((tiempo, theta1_t, theta2_t, \
theta3_t, theta4_t))
np.savetxt( 'amplitudes.txt', datos )

#Grafica de las soluciones
plt.plot( tiempo, theta1_t, label = 'pendulo 1', \
color='red', linewidth = 2 )
plt.plot( tiempo, theta2_t, label = 'pendulo 2', \
color='blue', linewidth = 2 )
plt.plot( tiempo, theta3_t, label = 'pendulo 3', \
color='green', linewidth = 2 )
plt.plot( tiempo, theta4_t, label = 'pendulo 4', \
color='black', linewidth = 2 )

#Formato de grafica
plt.title('Soluciones de pendulos acoplados')
plt.xlabel('tiempo')
plt.ylabel('Angulo oscilacion [rad]')
plt.grid()
plt.legend()
plt.show()