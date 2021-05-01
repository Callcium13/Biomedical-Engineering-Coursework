#function to find all roots of an equation recursively
#by Callum Coffey
#04/11/2020



import matplotlib.pyplot as plt
import time

def get_float(question_string):
  while True:
    data = input(question_string)
    #check without - or . to allow negatives and floats
    if data.replace('-','').replace('.',''):
      return float(data)
      break 
    print('\nError: Float must only contain numeric characters\n')

def equation(x):
  return x*2**(-x**2)

def plot(function,lower,upper):
  x_list, y_list = [],[]
  i = lower
  while i <= upper:
    x_list.append(i)
    y_list.append(equation(i))
    i += 0.1

  ax = plt.gca()

  ax.grid(True)
  ax.spines['left'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['bottom'].set_position('zero')
  ax.spines['top'].set_color('none')

  plt.plot(x_list,y_list,linewidth = 2)
  plt.title('Plot of f(x)')
  plt.show(block = False)

def dydx(function,x,h):
  results = []
  for i in range(0,len(x)):
    #calculates using central difference method and adds delta to data
    results.append(((function(x[i] + h)) - (function(x[i] - h))) / (2*h))

  return results

def extrema(equation, low, high):
  peak_list = []

  #list starts at low
  peak_list.append(low)

  #calculates step size to achieve 1 million steps
  step = (high - low)/(1000000)
  x_list = []

  #makes list of x values to differentiate
  i = low
  while i <= high:
    i += step
    x_list.append(i)
  #differentiates x_list twice
  dydx_list = dydx(equation,x_list,step)

  #checks for when derivative = 0, meaning peaks
  for i in range(0,len(dydx_list)):
    if round(dydx_list[i],3) == 0:
      peak_list.append(x_list[i])

  #rounds values to tolerance
  for i in range(0,len(peak_list)):
    peak_list[i] = round(peak_list[i],2)

  #remove duplicate roots
  while True:
    check = 0
    i = 0
    while i < len(peak_list):
      j = i + 1
      while j < len(peak_list):
        if round(peak_list[i],3) == round(peak_list[j],3):
          check = 1
          peak_list.pop(j)
        j += 1
      i += 1
    if check == 0:
      break  
  
  #ends list at high
  peak_list.append(high)

  for i in peak_list:
    plt.plot(i,0,'bo')
  plt.show(block = False)

  return peak_list

#equation to insertion sort a list of floats from lowest to highest
def insert_sort(unsorted):
  length = len(unsorted)

  i = 1
  #iterate through all integers
  while i < length:
    #remove next letter and store in x if it is lower than the previous
    if unsorted[i] < unsorted[i - 1]:
      x = unsorted[i]
      unsorted.pop(i)
      j = 0
      #iterate through sorted integers
      while j < i:
        #insert stored number into right placement
        if x < unsorted[j]:
          unsorted.insert(j, x)
          break
        j = j + 1
    i = i + 1
  return unsorted

#function to find roots of an equation
#arg is equation, lower boundary , upper boundary ,the number of decimal places to measure to, max recursion depth(do not change!!), minimum distance between roots to search
#if magnitude of bounds exceeds max recursion depth errors may occur
def root_find(function , extrema, low = -10 , high = 10 , tolerance = 10 , max_depth = 800 ,root_distance_min = 0.1, table = False):
  #creates list to contain all roots
  global roots
  roots = []
  
  #function that finds roots within bounds
  def root_find_inner(function ,low ,high ,tolerance , max_depth, root_distance_min):
    if not 'depth' in globals():
      global depth
      depth = 0
    depth += 1
    if depth < max_depth:
      #get average of high and low
      mid = (high + low)/2

      #creates a list of the y values in format (low,mid,high)
      y_list = [function(low),function(mid),function(high)]

      #round f(mid) so that near zero becomes zero
      y_list[1] = round(y_list[1],tolerance)

      #checks if this part of slope is positive or negative
      if y_list[0] < y_list[2]:
        positive = True
      else:
        positive = False

      if table:
        #store as string values for formating
        string_low, string_high, string_mid, string_mid_y = str(round(low,10)), str(round(high,10)), str(round(mid,10)), str(round(y_list[2],10))
        print(str(depth).center(3),string_low.center(13),string_high.center(13),string_mid.center(13) ,string_mid_y.center(13))


      if y_list[1] == 0:
        roots.append(mid)

      #evaluates f(mid) to determine which direction to go in based on slope and distance from zero
      #too low
      elif (y_list[1] < 0 and positive) or (y_list[1] > 0 and not positive):
        root_find_inner(function,mid,high,tolerance, max_depth, root_distance_min)

      #too high
      elif (y_list[1] > 0 and positive) or (y_list[1] < 0 and not positive):
        root_find_inner(function,low,mid,tolerance,max_depth, root_distance_min)

  #performs the root find using sets of inflection points as bounds
  for i in range(0, len(peak_list) - 1):
    global depth
    depth = 0

    #print a table header if arg is true
    if table:
      print('\nBisection Method table from',round(peak_list[i]),'to',round(peak_list[i+1]))
      print('Step'.center(3),'Lower Bound'.center(13),'Upper'.center(13),'Mid'.center(13),'Y-value Mid'.center(13))

    root_find_inner(equation, peak_list[i], peak_list[i + 1],tolerance , max_depth, root_distance_min)

  #round and removes duplicates for roots list before returning
  if roots:
    #rounds values to tolerance
    for i in range(0,len(roots)):
      roots[i] = round(roots[i],tolerance)
      #removes negative sign from zero caused by approaching from negative side and removes near roots caused by limits near zero
      t2 = 1 * 10 ** -(tolerance/2)
      if -t2 < roots[i] < t2:
        roots[i] = 0

    #remove duplicate roots
    while True:
      check = 0
      i = 0
      while i < len(roots):
        j = i + 1
        while j < len(roots):
          if round(roots[i]) == round(roots[j]):
            check = 1
            roots.pop(j)
          j += 1
        i += 1
      if check == 0:
        break
    return insert_sort(roots)
  return 'No roots within bounds'

def newton_method(function , peak_list, low = -10 , high = 10 , tolerance = 10 , max_depth = 800 ,root_distance_min = 0.1, table = False):
  #creates list to contain all roots
  roots = []

  #performs the root find using sets of inflection points as bounds with the estimate being the center
  for i in range(0, len(peak_list) - 1):
    depth = 0

    #print a table header if arg is true
    if table:
      print('\nNewton Method from',round(peak_list[i]),'to',round(peak_list[i+1]))
      print('Step'.center(3),'Mid'.center(13),'Y-value Mid'.center(13))

    #get average of high and low for the estimated root
    mid = (peak_list[i] + peak_list[i + 1]) /2

    #run the newton method until either the root is found or too many attempts
    #only operates within sets of ranges
    depth = 0
    while (depth < max_depth):
      depth += 1
      #creates a list of the y values in format (low,mid,high)
      f_mid = function(mid)

      #round f(mid) so that near zero becomes zero
      f_mid = round(f_mid,tolerance)

      if table:  
        #store as string values for formating
        string_mid, string_mid_y =  str(round(mid,10)), str(round(f_mid,10))
        print(str(depth).center(3),string_mid.center(13) ,string_mid_y.center(13))

      #break if root is found
      if f_mid == 0:
        roots.append(mid)
        break

      #finds derivative at mid using central difference method
      h = 0.0000000001
      dydx_mid = (equation(mid + h) - equation(mid - h)) / (2*h)

      #prevents divide by zero errors
      if dydx_mid == 0:
        dydx_mid = 0.00000000000000000001

      #calculate next estimate
      mid = mid - (f_mid / dydx_mid)

  #round and removes duplicates for roots list before returning
  if roots:
    #rounds values to tolerance
    for i in range(0,len(roots)):
      roots[i] = round(roots[i],tolerance)
      #removes negative sign from zero caused by approaching from negative side and removes near roots caused by limits near zero
      t2 = 1 * 10 ** -(tolerance/2)
      if -t2 < roots[i] < t2:
        roots[i] = 0

    #remove duplicate roots
    while True:
      check = 0
      i = 0
      while i < len(roots):
        j = i + 1
        while j < len(roots):
          if round(roots[i]) == round(roots[j]):
            check = 1
            roots.pop(j)
          j += 1
        i += 1
      if check == 0:
        break
    return insert_sort(roots)
  return 'No roots within bounds'


print('\nBounds for graph of equation:')
plot(equation,get_float('Lower Bounds = '),get_float('Upper Bounds = '))

print('\nBounds for roots of equation:')
lower = get_float('Lower Bounds = ')
upper = get_float('Upper Bounds = ')

peak_list = extrema(equation, lower, upper)

if True:
  tic1 = time.process_time()
  bisection_method_results = root_find(equation, peak_list, lower, upper)
  tic2 = time.process_time()
  print('\nBisection method run time: ',tic2 - tic1)
  print('Roots = ',bisection_method_results)

  for i in bisection_method_results:
    plt.plot(i,0,'ro')
  plt.show(block = False)

if True:
  tic1 = time.process_time()
  newton_method_results = newton_method(equation, peak_list, lower, upper)
  tic2 = time.process_time()
  print('\nNewton method run time: ',tic2 - tic1)
  print('Roots = ',newton_method_results)

  for i in newton_method_results:
    plt.plot(i,0,'ro')
  plt.show(block = False)
