#code to adaptably integrate an equation between user defined max and min
#by Callum Coffey
#02/11/2020

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
def adapt_integrate(xmin,xmax,tolerance = 0.00001):
  #function to input equation used by integration function
  def equation(x):
    return x**2

  #initialize at minimum
  i, area, h = xmin ,0 , tolerance

  #iterates through strips of width h
  while i <= xmax:
    y = equation(i)

    #adapting h to suit parts of the equation where there is a large difference between f(i) and f(i + h)
    while tolerance <= h <= 1:
      if y == 0:
        break
      
      error = (y - equation(i + h)) / y
      if error < -tolerance:
        h = h / 2
      if error > tolerance:
        h = h * 2
      if -tolerance < error < tolerance:
        break

    #adds current strip area to total area
    area = area + y * h
    #iterate by h
    i += h
  return float(area)

#main
print(
  adapt_integrate(
    get_float('Xmin = '), get_float('Xmax = ')
  )
)
