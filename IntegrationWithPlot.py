#code to intgreate an equation between ser defined max and min, plotting integral area, the y value of the line and h.
#by Callum Coffey
#02/11/2020

import matplotlib.pyplot as plt
import math

#function to prompt the user for a float, checking for non-numerical values
def get_float(question_string):
  while True:
    data = input(question_string)
    #check without - or . to allow negatives and floats
    if data.lstrip('-').lstrip('.').lstrip('0.').isnumeric():
      return float(data)
      break
    print('Error: Float must only contain numeric characters')

#function to integrate an equation based on initial value,final vaue, and stepsize, returning area as a float
def integrate_plot(xmin,xmax,h = 0.01):
  #function to input equation used by integration function
  def equation(x):
    return x * math.sin(x)

  #initialize at minimum
  i, area = xmin, 0
  y_list, i_list = [], []

  #iterates through strips of width h
  while i <= xmax:
    y = equation(i)
    y_list.append(y)
    #adds current strip area to total area
    area = area + y * h
    #iterate by h
    i_list.append(i)
    i = i + h

  print(area)
  plt.plot(i_list,y_list,color = 'r',linewidth = 2)
  plt.bar(i_list,y_list,width=(h),align='edge',edgecolor='b')
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title('Integration')
  plt.show()
  

integrate_plot(get_float('Xmin = '), get_float('Xmax = '))
