import scipy.interpolate as *
import numpy as np



def linearregression(array1, array2)
  p1 = polyfit(array1,array2,1)
  plot(array1,array2,'o')
  plot(array1,polyval(p1,array1), 'r-')
