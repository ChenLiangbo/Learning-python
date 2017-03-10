# -*- coding: utf-8 -*-
from sympy import *
import numpy as np

x = np.linspace(1,10,1000)
print("x = ",x.shape)
y = np.sin(x)
z = np.cos(x)

from matplotlib import pyplot as plt
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x)$")
plt.grid(True)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()