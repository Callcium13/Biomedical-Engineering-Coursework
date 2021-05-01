def get_floatlist(question_string):
  while True:
    check = 0
    data = (input(question_string)).split(',')
    for i in data:
      #check without - or . to allow negatives and floats
      if not (i.lstrip('-').lstrip('.').isnumeric()) or not (i.lstrip('0.').isnumeric()):
        check = 1
    if check == 0:
      break
    print('Error: Float must only contain numeric characters')
  data = list(map(float,data))
  return data

#function to get derivation of user inputted function using forward difference formula and compare to true derivation
#returns in format [estimate,actual,percent difference]
def dydx(x,h):
  def function(fx):
    #enter function here with float in place of variable
    return fx ** 2

  results = []
  for i in range(0,len(x)):
    #calculates using central difference method and adds delta to data
    results.append(((function(x[i] + h)) - (function(x[i] - h))) / (2*h))

  return results


print('Derivative list = ', dydx( get_floatlist('CSV of floats = '),float(input('h = '))))
