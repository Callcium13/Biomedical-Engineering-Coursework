def get_floatlist():
  check = 1
  while check == 1:
    data = (input('CSV of floats = ')).split(',')
    #check that input is list of integers and setup a check value
    for i in data:
      #check without - or . to allow negatives and floats
      if not i.lstrip('-').lstrip('.').lstrip('0.').isnumeric():
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

#function to get derivation of user inputted function using forward difference formula and compare to true derivation
#returns in format [estimate,actual,percent difference]
def dydx_list(x):
  results = []
  for i in range(1,len(x)):
    #calculates using central difference method and adds delta to data
    results.append(x[i] - x[i - 1])

  print('Average derivative = ',get_mean(results))
  return results


print('Derivative list = ',
  dydx_list
  (
    get_floatlist()
  )
)
