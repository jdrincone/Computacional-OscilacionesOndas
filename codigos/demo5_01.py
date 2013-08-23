#!/usr/bin/env python
#==========================================================
# DEMOSTRACION 1:
# Simulacion de interferencia en una caja cuadrada
#==========================================================

import AudioLib as ad
import Tkinter
import matplotlib.pylab as plt
import numpy as np
import scipy.interpolate as interp

from matplotlib.backends.backend_tkagg \
import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

#Funcion de amplitud de una fuente
def Z_amplitud(x, y, x0, y0, t, f, lamb):
    #Posicion de la fuente
    r0 = np.array([x0, y0])
    #Posicion donde se evalua el campo
    r = np.array([x, y])
    rr0 = np.linalg.norm(r-r0)
    return ad.Amplitude*1/(rr0+1.0)*\
    np.sin( 2*np.pi*(t*f - rr0/lamb ) )

#==========================================================
# Clase App para la generacion de entorno grafico
#==========================================================
class App:
  def __init__(self, master):
    #Creando contenedor
    self.frame = Tkinter.Frame(master)
    #******************************************************
    #	Propiedades Fuente
    #******************************************************
    #Etiqueta de Propiedades de la Fuente
    self.label = Tkinter.Label(self.frame,\
    text='PROPIEDADES\n DE LA FUENTE')
    self.label.pack(side='top')
    
    #Tamano caja
    self.label = Tkinter.Label(self.frame,\
    text='Longitud Caja [m]')
    self.label.pack(side='top') 
    self.Lbox = Tkinter.DoubleVar()
    self.L_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.Lbox, width = 6 )
    self.L_textbox.pack(side='top')

    #Coordenada x
    self.label = Tkinter.Label(self.frame, text='X')
    self.label.pack(side='top') 
    self.xsource = Tkinter.DoubleVar()
    self.xs_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.xsource, width = 6 )
    self.xs_textbox.pack(side='top')
    
    #Coordenada y
    self.label = Tkinter.Label(self.frame, text='Y')
    self.label.pack(side='top') 
    self.ysource = Tkinter.DoubleVar()
    self.ys_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.ysource, width = 6 )
    self.ys_textbox.pack(side='top')
        
    #Velocidad onda
    self.label = Tkinter.Label(self.frame,\
    text='Velocidad Onda [m/s]')
    self.label.pack(side='top') 
    self.vel = Tkinter.DoubleVar()
    self.vel_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.vel, width = 6 )
    self.vel_textbox.pack(side='top')

    #Frecuencia de onda
    self.label = Tkinter.Label(self.frame,\
    text='Frecuencia [Hz]')
    self.label.pack(side='top') 
    self.freq = Tkinter.DoubleVar()
    self.f_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.freq, width = 6 )
    self.f_textbox.pack(side='top')
    
    #Seleccion de condiciones de frontera
    self.label = Tkinter.Label(self.frame,\
    text='Frontera reflectiva\n[0 -- no\t1 -- si]')
    self.label.pack(side='top')  
    self.frontera = Tkinter.IntVar()
    self.front_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.frontera, width = 6 )
    self.front_textbox.pack(side='top')
    
    #Boton Calcular fuente
    self.sour_buttom = Tkinter.Button( self.frame,\
    text="Calcular Fuente", command=self.plot_source,\
    width =12)
    self.sour_buttom.pack(side = 'top')
        
        
    #******************************************************
    #	Propiedades Observador
    #******************************************************
    #Etiqueta de Propiedades del obsevador
    self.label = Tkinter.Label(self.frame,\
    text='PROPIEDADES\n DEL OBSERVADOR')
    self.label.pack(side='top')
    
    #Coordenada x
    self.label = Tkinter.Label(self.frame, text='X')
    self.label.pack(side='top') 
    self.xobs = Tkinter.DoubleVar()
    self.xo_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.xobs, width = 6 )
    self.xo_textbox.pack(side='top')
    
    #Coordenada y
    self.label = Tkinter.Label(self.frame, text='Y')
    self.label.pack(side='top') 
    self.yobs = Tkinter.DoubleVar()
    self.yo_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.yobs, width = 6 )
    self.yo_textbox.pack(side='top')
    
    #Tiempo senal
    self.label = Tkinter.Label(self.frame,\
    text='Tiempo observador')
    self.label.pack(side='top') 
    self.tmax = Tkinter.DoubleVar()
    self.tm_textbox = Tkinter.Entry( self.frame,\
    textvariable = self.tmax, width = 6 )
    self.tm_textbox.pack(side='top')
    
    #Boton Calcular Audio
    self.obs_buttom = Tkinter.Button( self.frame,\
    text="Calcular Audio", command=self.plot_obs,\
    width =12)
    self.obs_buttom.pack(side = 'top')

    fig = Figure(figsize=(6,6))
    self.ax = fig.add_subplot(111)
    self.ax.set_title("Interferencia",\
    fontsize=15)
    self.canvas = FigureCanvasTkAgg(fig,master=master)
    self.ax.grid()
    self.canvas.show()
    self.canvas.get_tk_widget().pack(side='right',\
    fill='none', expand=0)
    self.frame.pack()

  #******************************************************
  #	General Properties Methods
  #******************************************************
  #Grafiacion del campo
  def plot_source(self):
    #Tamano caja
    L = self.Lbox.get()
    #Resolucion de la caja
    NS = 200
    #Grid
    XM = np.linspace( 0, L, NS )
    YM = np.linspace( 0, L, NS )
    #Posicion de la fuente
    X0 = self.xsource.get()
    Y0 = self.ysource.get()
    #Frecuencia
    f = self.freq.get()
    #Velocidad de onda
    vel = self.vel.get()
    #Longitud de onda
    lamb = vel/f
    #Condicional de fronteras reflectivas
    reflex = self.frontera.get()
    
    #Calculo de Amplitud del campo
    Z = np.zeros( (NS,NS) )
    for i in xrange( 0, NS ):
      for j in xrange( 0, NS ):
	x = XM[i]
	y = YM[j]
	Z[-j,i] = \
	Z_amplitud(x, y, X0, Y0, 0.0, f, lamb )
	if reflex == 1:
	  Z[-j,i] -= \
	  Z_amplitud(x, y, 0.0, -Y0, 0.0, f, lamb ) +\
	  Z_amplitud(x, y, 0.0, 2*L-Y0, 0.0, f, lamb ) +\
	  Z_amplitud(x, y, -X0, 0.0, 0.0, f, lamb ) +\
	  Z_amplitud(x, y, 2*L-X0, 0.0, 0.0, f, lamb )

    self.ax.clear()
    self.ax.grid()
    self.ax.set_title('Amplitud Onda Sonora')
    self.ax.set_xlabel('X [m]')
    self.ax.set_ylabel('Y [m]')
    self.ax.imshow( Z, extent = (0,L,0,L) )
    self.canvas.draw()
    
    
  #Grafiacion del sonido medido por el observador
  def plot_obs(self):
    #Tamano caja
    L = self.Lbox.get()
    #Posicion de la fuente
    X0 = self.xsource.get()
    Y0 = self.ysource.get()
    #Posicion del observador
    XOb = self.xobs.get()
    YOb = self.yobs.get()
    #Frecuencia
    f = self.freq.get()
    #Velocidad de onda
    vel = self.vel.get()
    #Longitud de onda
    lamb = vel/f
    #Condicional de fronteras reflectivas
    reflex = self.frontera.get()
    
    #Intervalo de tiempo
    dt = 1/(44100.)
    #Tiempo maximo
    tmax = self.tmax.get()
    #Arreglo de tiempo
    self.tiempo = np.arange( 0, tmax, dt )
    #Calculo de campo en el punto del observador
    self.Z = \
    Z_amplitud(XOb, YOb, X0, Y0, self.tiempo, f, lamb )
    if reflex == 1:
      self.Z -= \
      Z_amplitud(XOb, YOb, 0.0, -Y0, self.tiempo, f, lamb )+\
      Z_amplitud(XOb, YOb, 0.0, 2*L-Y0, self.tiempo, f, lamb )+\
      Z_amplitud(XOb, YOb, -X0, 0.0, self.tiempo, f, lamb )+\
      Z_amplitud(XOb, YOb, 2*L-X0, 0.0, self.tiempo, f, lamb )
      self.Z *= 1/(5.)
    #Grafica
    self.ax.clear()
    self.ax.grid()
    self.ax.set_title('Amplitud Onda Sonora por Observador')
    self.ax.set_xlabel('tiempo [s]')
    self.ax.set_ylabel('Amplitud [$A_0$]')
    self.ax.plot( self.tiempo, self.Z/(1.0*ad.Amplitude) )
    self.ax.set_ylim( (-1, 1) )
    self.ax.set_xlim( (0, tmax) )
    self.canvas.draw()
    #Creando objeto de audio
    sonido = ad.audio()
    #Cargando nota de audio
    sonido.load( self.Z )
    #Reproduciendo sonido
    sonido.play()
        
root = Tkinter.Tk()
root.wm_title("Interferencia Sonora")
app = App(root)
root.mainloop()