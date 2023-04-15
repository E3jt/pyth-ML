import numpy
import matplotlib.pyplot as plt


def hit1():
    x = numpy.random.normal(10.0, 1.0, 10000)


    plt.hist(x, 100)
    plt.show()

    
def hit2():
    x = numpy.random.uniform(0.0, 16.0, 160)

    plt.hist(x, 16)
    plt.show()
    

#hit1()
#hit2()
