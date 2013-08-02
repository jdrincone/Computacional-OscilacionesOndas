# -*- coding: utf-8 -*-
#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 1
# Coeficientes de Fresnel
# por: Rodolfo Restrepo
#==========================================================

#**********************************************************
#	MODULOS
#**********************************************************
from visual.graph import*

def eval(x):
    return x

#Entrada por pantalla del ángulo de incidencia.
#Calculado respecto a la horizontal. Luego el ángulo que nos
#interesa es pi/2-thetai.
thetai=pi/180*eval(input("Entre grados para ángulo incidente(0-90):"))
#Entrada por pantalla del coeficiente de refracción.
n=eval(input("Entre un coeficiente de refracción (n>=1):"))

thetat=arcsin(sin(thetai)/n) #Angulo transmitido.
k=50 #Magnitud del rayo incidente.
w=0.5 #Frecuencia angular (escalada).
Eoi=50 #Amplitud del campo electrico.
Boi=Eoi #Amplitud del campo magnetico.

#Coeficiente de reflexion en el plano perpendicular.
Rsigma=(cos(thetai)-n*cos(thetat))/(n*cos(thetai)+cos(thetat))
#Coeficiente de reflexion en el plano paralelo.
Rpi=(n*cos(thetat)-cos(thetai))/(cos(thetai)+n*cos(thetat))
#Ampitud del campo electrico/magnetico reflejado.
Eor=Rsigma*Eoi
Bor=Rpi*Boi
#Coeficiente de transmision en el plano perpendicular.
Tsigma=2*n*cos(thetai)/(cos(thetat)+n*cos(thetai))
#Coeficiente de transmision en el plano perpendicular.
Tpi=2*n*cos(thetai)/(cos(thetai)+n*cos(thetat))
#Amplitud del campo electrico/magnetico transmitido.
Eot=Tsigma*Eoi
Bot=Tpi*Boi

escena=display(width=600,height=600,range=300)
rayoinc=arrow(color=color.white)   #Rayo incidente.
rayorefle=arrow(color=color.white) #Rayo reflejado.
rayotrans=arrow(color=color.white) #Rayo transmitido.
Bi=arrow(color=color.blue) #Campo magnetico incidente.
Ei=arrow(color=color.red)  #Campo electrico incidente.
Br=arrow(color=color.blue) #Campo magnetico reflejado.
Er=arrow(color=color.red)  #Campo electrico reflejado.
Bt=arrow(color=color.blue) #Campo magnetico transmitido.
Et=arrow(color=color.red)  #Campo electrico transmitido.
trail=curve(color=color.red)
trail2=curve(color=color.blue)
trail3=curve(color=color.red)
trail4=curve(color=color.blue)

ejey=curve(pos=[(0,-250,0),(0,250,0)],color=color.white)
ejex=curve(pos=[(-250,0,0),(250,0,0)],color=color.white)
#La interfaz representa un cambio de medio.
interfaz=box(pos=(0,0,0),color=color.blue,length=500,
             width=250,height=1,opacity=0.3)
#El plano de incidencia es el plano generado por la normal
#y el rayo incidente.
planoN=box(pos=(0,0,0),color=color.white,length=500,width=1,
           height=500,opacity=0.4)

#Direción de incidencia.
rayoi=curve(pos=[(0,0,0),(300*sin(thetai),300*cos(thetai),0)],
            color=color.yellow)
#Dirección del rayo reflejado.
rayor=curve(pos=[(0,0,0),(-300*sin(thetai),300*cos(thetai),0)],
            color=color.yellow)
#Dirección del rayo transmitido.
rayot=curve(pos=[(0,0,0),(-300*sin(thetat),-300*cos(thetat),0)],
            color=color.yellow)

yini=300*cos(thetai)
xini=300*sin(thetai)

#Este for es para el rayo incidente. 
for t in arange(0,300,0.1):
    rate(100)
    y=yini-t*cos(thetai) #Posición vertical.
    x=xini-t*sin(thetai) #Posición horizontal.
    rayoinc.pos=vector(x,y) 
    rayoinc.axis=vector(-k*sin(thetai),-k*cos(thetai),0)
    Bi.pos=(x,y)
    Bi.axis=(-Boi*sin((pi/2)-thetai)*cos(w*t*0.2),
             Boi*cos((pi/2)-thetai)*cos(w*t*0.2),0)
    Ei.pos=vector(x,y)
    Ei.axis=(0,0,Eoi*cos(w*t*0.2))
    trail.append(pos=Ei.pos+Ei.axis)  
    trail2.append(pos=Bi.pos+Bi.axis)

#Este for es para los rayos reflejado y transmitido.
for t in arange(0,300,0.1):
    rate(100)
    yr=t*cos(thetai)
    xr=-t*sin(thetai)
    rayorefle.pos=vector(xr,yr)
    rayorefle.axis=(-k*sin(thetai),k*cos(thetai),0)
    Br.pos=vector(xr,yr)
    Br.axis=(Bor*sin((pi/2)-thetai)*cos(w*t*0.2),
             Bor*cos((pi/2)-thetai)*cos(w*t*0.2),0)
    Er.pos=vector(xr,yr)
    Er.axis=(0,0,Eor*cos(w*t*0.2))
    trail.append(pos=Er.pos+Er.axis)
    trail2.append(pos=Br.pos+Br.axis)
    
    yt=-t*cos(thetat)
    xt=-t*sin(thetat)
    rayotrans.pos=vector(xt,yt)
    rayotrans.axis=(-k*sin(thetat),-k*cos(thetat),0)
    Bt.pos=vector(xt,yt)
    Bt.axis=(Bot*-sin((pi/2)-thetat)*cos(w*t*0.2),
             Bot*cos((pi/2)-thetat)*cos(w*t*0.2),0)
    Et.pos=vector(xt,yt)
    Et.axis=(0,0,Eot*cos(w*t*0.2))
    trail3.append(pos=Et.pos+Et.axis)
    trail4.append(pos=Bt.pos+Bt.axis)