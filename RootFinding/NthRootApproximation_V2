#recursive function to find all roots of an equation recursively
#by Callum Coffey
#04/11/2020

def equation(x):
  return (x**2 - 3)

def dydx(function,x,h):
  results = []
  for i in range(0,len(x)):
    #calculates using central difference method and adds delta to data
    results.append(((function(x[i] + h)) - (function(x[i] - h))) / (2*h))

  return results

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
#arg is equation, lower boundary , upper boundary ,the number of decimal places to measure to, max recursion depth(do not change!!), if recusion is first(not needed for outermost recursion), minimum distance between roots to search, maximum number of roots to check for

#if magnitude of bounds exceeds max recursion depth errors may occur
#may not output requested number of roots for trigonometric equations in positive direction
def root_find(function ,low = -10 ,high = 10 ,tolerance = 10 ,max_depth = 800 ,root_distance_min = 0.1):
  #creates list to contain all roots
  global roots
  roots = []

  #find and make list of inflection points
  peak_list = []
  #list starts at low
  peak_list.append(low)

  step = (high - low)/(1000000)
  x_list = []

  #makes list of x values to differentiate
  i = low
  while i <= high:
    i += step
    x_list.append(round(i,6))
  #differentiates x_list twice
  dydx_list = dydx(equation,x_list,step)

  #checks for when derivative = 0, meaning peaks
  for i in range(0,len(dydx_list)):
    if round(dydx_list[i],3) == 0:
      peak_list.append(x_list[i])

  #rounds values to tolerance
  for i in range(0,len(roots)):
    roots[i] = round(roots[i],2)

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
          if roots[i] == roots[j]:
            check = 1
            roots.pop(j)
          j += 1
        i += 1
      if check == 0:
        break
    return insert_sort(roots)
  return 'No roots within bounds'

print(root_find(equation))
