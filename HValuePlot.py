import matplotlib.pyplot as plt
import math

def get_floatlist():
  check = 1
  while check == 1:
    data = (input('CSV of floats = ')).split(',')
    #check that input is list of integers and setup a check value
    for i in data:
      #check without - or . to allow negatives and floats
      if not i.lstrip('-').lstrip('.').isnumeric():
        print('Error: List must only contain numeric characters')
        break
      check = 0 

  data = list(map(float,data))
  return data

def get_mean(list):
  mean = 0
  for i in list:
    mean = mean + i
  mean = mean / len(list)
  return mean

#enter function here with float in place of variable
def function(float):
  halfpi = math.pi/2
  return math.sin((halfpi)*(float))

#enter derivation of function here
def dydfunctionx(float):
  halfpi = math.pi/2
  return math.cos((halfpi)*(float)) * halfpi

def plot_dydx():
  #function to get derivation of user inputted function using forward difference formula and compare to true derivation
  #returns in format [estimate,actual,percent difference]
  def dydx(x,h):
    results = []
    for i in range(0,len(x)):
      results.append([])

      #calculates and adds delta to data
      results[i].append(((function(x[i] + h)) - (function(x[i]))) / h)

      #appends results with actual delta from true derivation
      results[i].append(dydfunctionx(x[i]))

      if not results[i][1] == 0:
        #calculate percent difference
        results[i].append(100 * (results[i][0] - results[i][1]) / (results[i][1]))
      else:
        results[i].append(0)
    return results  

  #gets average of list of percent differences when supplied with dydx results
  def per_diff(list):
    for i in range(0,len(list)):
      per_diff = []
      per_diff.append(list[i][2])
    return get_mean(per_diff)

  h_results = []
  x = []
  for i in range(-100 , 100):
    x.append(i)

  #runs while the ith iterable of h is less than 10, acts as magnitude scales
  #makes list called h_results of the absoloute values of the percent differences for differentiation of the user supplied function
  h_list = []
  i = 0
  while True:
    h_list.append(1 * 10 ** i)
    h_results.append(abs(per_diff(dydx(x,h_list[i]))))
    i -= 1
    if not i > -10:
      break
  
  print(h_list,h_results)
  #plot the results
  plt.plot(h_list, h_results)
  plt.xlabel("h")
  plt.ylabel("Percent difference")
  plt.title('Percent difference over values of h')
  plt.show()

plot_dydx()
