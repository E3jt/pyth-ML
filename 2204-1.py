import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


tim = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37, 38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93, 94, 95, 96, 99, 100, 101]
tem =[1.08, 1.05, 1.01, 0.98, 0.96, 0.95, 0.94, 0.91, 0.89, 0.91, 0.9, 0.88, 0.9, 0.91, 0.92, 0.91, 0.89, 0.83, 0.78, 0.74, 0.69, 0.65, 0.6, 0.52, 0.44, 0.39, 0.3, 0.24, 0.2, 0.16, 0.11, 0.08, 0.07, 0.07, 0.07, 0.08, 0.07, 0.09, 0.09, 0.09, 0.08, 0.08, 0.07, 0.07, 0.07, 0.04, 0.01, -0.01, -0.03, -0.07, -0.13, -0.2, -0.28, -0.34, -0.37, -0.39, -0.42, -0.42, -0.42, -0.42, -0.42, -0.41, -0.44, -0.44, -0.45, -0.51, -0.6, -0.64, -0.62, -0.66, -0.7, -0.72, -0.7, -0.69, -0.68, -0.67, -0.67, -0.67, -0.69, -0.69, -0.74, -0.79, -0.82, -0.85, -0.86, -0.86, -0.85, -0.82, -0.76, -0.67, -0.57, -0.48, -0.4, -0.32, -0.29, -0.23, -0.17, 0.09, 0.64]

model = numpy.poly1d (numpy.polyfit(tim, tem, 20))

line = numpy.linspace (1, 101, 100)

plt.scatter (tim, tem)
plt.plot(line, model (line))
plt.show()

print (r2_score (tem, model(tim)))

temp = model(102)

print(temp)
