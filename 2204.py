import numpy
import matplotlib.pyplot as plt
from scipy import stats

pay = [320.50,334.90,345.50,359.00,375.90,390.90,404.00,419.20,431.20,443.60,457.60,479.10,488.50,498.50,498.30,506.10,517.40,518.30,527.10,538.60,550.00,568.30,585.20,585.70,609.80,640.00]#tygodniowa w GB
yr = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,2022]   #lata



slope , intercept, r, p, str_err = stats.linregress(yr,pay)

def func1(y):
  return slope * y + intercept
  

nextyear = func1(2023) 
model = list(map(func1, yr))


print(nextyear)
print(r)

plt.scatter(yr, pay)
plt.plot(yr, model)
plt.show()
