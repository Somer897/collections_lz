import numpy as np
import matplotlib.pyplot as plt             #импорты

x = np.linspace(0,10,100)                   #задаем область определения функции
y = x**3 + x**2 + 1                         #непосредственно сама функция
plt.plot(x, y)                              #создание графика
plt.show()                                  #его показ