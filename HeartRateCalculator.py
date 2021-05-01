#code to collect heart rate data and perform basic analysis on it
#NOT A MEDICAL DIAGNOSTIC TOOL, FOR EDUCATIONAL PURPOSES ONLY
#by Callum Coffey
#01/11/2020

#function to prompt the user for a float, checking for non-numerical values
def get_float(question_string):
  while True:
    data = input(question_string)
    #check without - or . to allow negatives and floats
    if data.lstrip('-').lstrip('.').lstrip('0.').isnumeric():
      return float(data)
      break
    print('Error: Float must only contain numeric characters')

def heartrate_derivation():
  #Ask the user for their name and age
  name,age = (input('Name = '), get_float('Age = '))

  #Calculate the users target heart rate for optimal exercise
  optimal_rate = 220 - age

  #Seperate users name and test results
  #data_a has name, age and optimal rate but no results
  data_a = [name,age,optimal_rate]
  #data_b will include test results but no name
  data_b = [age, optimal_rate]

  #Inform the user and prompt them to exercise to reach this heart rate
  print('\nYour optimal heart rate is', int(optimal_rate),'\nPlease excercise to reach this rate')

  #Prompt the user to enter their HR intermediately after cessation of exercise and every minute after until 5 mins
  heart_rate = [get_float('\nRate immediately after excercise = ')]

  #due to only the first few minutes being of interest, scalability is not required here making a fixed string list optimal
  times = ['one minute', 'two minutes', 'three minutes', 'four minutes', 'five minutes']
  i = 0
  for i in times:
    print('Heart rate after', i, '?')
    heart_rate.append(get_float('Heart rate = '))
  data_b.append(heart_rate)

  #Calculate the gradient of HR recovery for the data entered
  dydx_heart_rate = []
  for i in range(len(heart_rate) - 1):
    dydx_heart_rate.append(heart_rate[i] - heart_rate[i + 1])
  data_b.append(dydx_heart_rate)

  #Analysis section
  if dydx_heart_rate[0] <= 12:
    print('\nThis recovery rate is not indicative of good fitness and health\n')
  else:
    print('\nThis recovery rate indicates good fitness and health\n')
  return data_a, data_b

#main
print('Heart Rate Data = ',heartrate_derivation()[1])
