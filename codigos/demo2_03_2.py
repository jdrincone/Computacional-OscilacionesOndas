#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 3: Parte 2
# Animacion grafica de 4 pendulos acoplados
#==========================================================
import numpy as np
import enthought.tvtk.tools.visual as visual

#Cargando datos de los pendulos
tiempo, theta1_t, theta2_t, theta3_t, theta4_t = \
np.transpose( np.loadtxt('amplitudes.txt') )

#Gravedad
g = 9.8
#Longitud pendulo 1
l1 = 1.0
#Longitud pendulo 2
l2 = 2.0
#Longitud pendulo 3
l3 = 3.0
#Longitud pendulo 4
l4 = 2.0
#Radio de cada esfera
radio = 0.2

#Creando pendulo 1
pendulo1 = visual.sphere( radius=radio, \
color=(0.0, 0.0, 1.0) )
pendulo1.pos = [ 1, -l1, 0 ]
pendulo1.t = 0
pendulo1.dt = 1
cuerda1 = visual.curve( points=[(1,0,0), (1,-l1,0)], \
radius=0.02 )

#Creando pendulo 2
pendulo2 = visual.sphere( radius=radio, \
color=(0.0, 0.0, 1.0) )
pendulo2.pos = [ 2, -l2, 0 ]
pendulo2.t = 0
pendulo2.dt = 1
cuerda2 = visual.curve( points=[(2,0,0), (2,-l2,0)], \
radius=0.02 )

#Creando pendulo 3
pendulo3 = visual.sphere( radius=radio, \
color=(0.0, 0.0, 1.0) )
pendulo3.pos = [ 3, -l3, 0 ]
pendulo3.t = 0
pendulo3.dt = 1
cuerda3 = visual.curve( points=[(3,0,0), (3,-l3,0)], \
radius=0.02 )

#Creando pendulo 4
pendulo4 = visual.sphere( radius=radio, \
color=(1.0, 0.0, 0.0) )
pendulo4.pos = [4, -l4*np.cos(theta4_t[0]), \
l4*np.sin(theta4_t[0])]
pendulo4.t = 0
pendulo4.dt = 1
cuerda4 = visual.curve( points=[(4,0,0), \
(4, -l4*np.cos(theta4_t[0]), l4*np.sin(theta4_t[0]))], \
radius=0.02 )

#Creando caja contenedora y cuerda de suspension
muro1 = visual.box( pos=(0., -1., 0.), size=(0.3, 5, 1), \
color=(0.6, 0.3, 0.0) )
muro2 = visual.box( pos=(5., -1., 0.), size=(0.3, 5, 1), \
color=(0.6, 0.3, 0.0) )
visual.curve( points=[(0,0,0), (5,0,0)], radius=0.02 )

#ITERACION DEL SISTEMA
def anim(): 
    #Evolucion del pendulo 1
    pendulo1.t = pendulo1.t + pendulo1.dt
    i = pendulo1.t
    pendulo1.pos = visual.vector( 1, \
    -l1*np.cos(theta1_t[i]), l1*np.sin(theta1_t[i]) )
    delta_thetha1 = theta1_t[i-1] - theta1_t[i]
    cuerda1.rotate( 180*delta_thetha1/np.pi, [1.,0.,0] )
    
    #Evolucion del pendulo 2
    pendulo2.t = pendulo2.t + pendulo2.dt
    i = pendulo2.t
    pendulo2.pos = visual.vector( 2, \
    -l2*np.cos(theta2_t[i]), l2*np.sin(theta2_t[i]) )
    delta_thetha2 = theta2_t[i-1] - theta2_t[i]
    cuerda2.rotate( 180*delta_thetha2/np.pi, [1.,0.,0] )
    
    #Evolucion del pendulo 3
    pendulo3.t = pendulo3.t + pendulo3.dt
    i = pendulo3.t
    pendulo3.pos = visual.vector( 3, \
    -l3*np.cos(theta3_t[i]), l3*np.sin(theta3_t[i]) )
    delta_thetha3 = theta3_t[i-1] - theta3_t[i]
    cuerda3.rotate( 180*delta_thetha3/np.pi, [1.,0.,0] )
    
    #Evolucion del pendulo 4
    pendulo4.t = pendulo4.t + pendulo4.dt
    i = pendulo4.t
    pendulo4.pos = visual.vector( 4, \
    -l4*np.cos(theta4_t[i]), l4*np.sin(theta4_t[i]) )
    delta_thetha4 = theta4_t[i-1] - theta4_t[i]
    cuerda4.rotate( 180*delta_thetha4/np.pi, [1.,0.,0] )
    
a = visual.iterate(10, anim)
visual.show()