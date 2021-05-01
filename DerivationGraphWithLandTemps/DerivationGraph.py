#function to get first and second derivation of historical land temperatures using data 
#sourced from https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data
#by Callum Coffey
#29/10/2020
from matplotlib import pyplot as plt
import csv

def get_mean(list):
  mean = 0
  for i in list:
    mean = mean + i
  mean = mean / len(list)
  return mean
  
#Open the file
data = open("GlobalLandTemperatures_GlobalTemperatures.csv")
#Read the file as csv
data = csv.reader(data, delimiter=",")
#Store csv file as list
data = list(data)

results = []
x = []

#puts dates into results
#puts temps into results and list x
for i in range (len(data)):
  results.append([data[i][0]])
  results[i].append(data[i][1])
  #if there is a datapoint
  if (data[i][1]).strip(''):
    x.append(float(data[i][1]))
  #if a datapoint is blank, fill in with previous datapoint
  else:
    x.append(x[i-1])   


# the change in the objects temperature over time
dx = []

for i in range(1,len(x)):
  # use differentiation formula to calc delta temp
  results[i].append(x[i] - x[i - 1])
  dx.append(results[i][2])

# the change in the change in the objects temperature, useful to figure out overall trends such as atypically fast transitions
ddx = []

for i in range(1,len(dx)):
  # use differentiation formula to calc delta temp
  results[i].append(dx[i] - dx[i - 1])
  ddx.append(results[i][3])

t1 = []

#make list of times eg(1,2,3...1000)
for i in range(1,len(results)+1):
  t1.append(i)

#make lists that are times except last element and last two elements respectively
t2 = t1[0:-1]
t3 = t1[0:-2]

#print out the results
print('First derivitave of temperature is',dx,'\nSecond derivative of temperature is = ',ddx)
print(results)

print('Blue is Temperature, Orange is first derivative, Green is second derivative')

#plot the results
plt.plot(t1,x)
plt.plot(t2,dx)
plt.plot(t3,ddx)
plt.xlabel("Time(Months Since 1st day of January 1750)")
plt.ylabel("Land Temperatures(Celsius)")
plt.title('Global Temperature Trends')
plt.show()
