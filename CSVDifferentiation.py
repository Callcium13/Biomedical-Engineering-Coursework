import csv

with open('dailycalories.csv', newline='') as f:
    data = list(csv.reader(f))
data.pop(0)

for i in data:
  i[1] = int(i[1])
#function to get derivation of user inputted function using forward difference formula and compare to true derivation
#returns in format [estimate,actual,percent difference]
def dydx_list(x):
  results = []
  for i in range(2,len(x)):
    #calculates using central difference method and adds delta to data
    results.append(x[i][1] - x[i - 1][1])

  return results


print('Derivative list = ',
  dydx_list
  (
    data
  )
)
