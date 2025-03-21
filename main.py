#Project: This is an exoplanet detection simulator
#Autor: Josue Silva
#Date: 16/03/2025

import random
import math
import numpy as np 
from matplotlib import pyplot as plt

exoplanetProbability = random.randint(0, 10)
transitPoint = 1
transitFinal = False

#10% Exoplanet
if(exoplanetProbability<=1):
    transitTime = random.uniform(0, 10)
    def glow(time):
        global transitPoint
        global transitFinal
        if(time >= transitTime and time <= transitTime+3):
            if(transitPoint >= 0.985 and transitFinal == False):
                transitPoint-=0.001
                glowSimulation = random.uniform(-0.005, 0.005) + transitPoint
            else:
                transitFinal = True
                transitPoint = transitPoint+0.001
                glowSimulation = random.uniform(-0.005, 0.005) + transitPoint
        else:
            glowSimulation = random.uniform(-0.005, 0.005) + 1
        return glowSimulation

    time = np.linspace(0, 10, 100)  # Tiempo de 0 a 10 con 100 puntos
    Glowgraph = [glow(t) for t in time]
    
else: #90% No exoplanet
    def glow(time):
        glowSimulation = random.uniform(-0.01, 0.01) + 1  # Fluctuación pequeña aleatoria
        return glowSimulation

    # Generar datos para la si mulación
    time = np.linspace(0, 10, 100)  # Tiempo de 0 a 10 con 100 puntos
    Glowgraph = [glow(t) for t in time]


plt.axis([0,10,0.97,1.012])
plt.xlabel("Time")
plt.ylabel("Glow Intensity")
plt.title("Exoplanet detection simulator")
plt.plot(time,Glowgraph)
plt.grid(True)
plt.savefig("grf.jpg")


