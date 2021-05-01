#Function to perform data analysis on composite beams
#data = [[shape,youngs modulus, [x,y], area , centroid, second moment]]
#results= [bending moment, y min, y max, y, stress min, stress max, stress]
#by Callum Coffey
#21/10/2020
def comp_beam():
  data = []
  #How many shapes
  while True:
    num_shapes = (input('Number of discrete shapes? \n'))
    #check that input is numeric
    if not num_shapes.isnumeric():
      print('Error: Enter a number')
    else:
      num_shapes = int(num_shapes)
      break

  #Get shape type of each shape
  for i in range(0,num_shapes):
    data.append([])
    while True:
      print('\nShape', i+1 ,'is')
      data[i].append(input('1.)rectangle, 2.)circle, 3.)annulus\n'))
      
      #check that input is integer
      if not data[i][0].isnumeric():
        print('\nError: Enter an integer between 1 and 3')
        data[i].pop(0)
      else:
        data[i][0] = int(data[i][0])
        #check that input is valid shape  
        if not (1 <= data[i][0] <= 3):
          print('\nError: Enter a valid shape')
          data[i].pop(0)
        else:
          break
    

  #Get Youngs modulus of each shape
  for i in range(0,num_shapes):
    while True:
      print('\nYoungs Modulus of shape', i+1 ,'is')
      data[i].append(input('\n'))
      
      #check that input is integer
      if not data[i][1].isnumeric():
        print('Error: Enter an integer')
      else:
        data[i][1] = int(data[i][1])
        break

  #Get dimensions of each shape
  for i in range(0,num_shapes):
    if data[i][0] == 1:
      while True:
        print('\nDimensions of shape', i+1 ,'is (x,y)')
        data[i].append(input('\n').split(','))
        
        #check that input is integer
        if not data[i][2][0].isnumeric() or not data[i][2][1].isnumeric():
          print('Error: Enter an integer for both dimensions')
        else:
          data[i][2][0], data[i][2][1] = int(data[i][2][0]), int(data[i][2][1])
          break
      
    if data[i][0] == 2:
        print('\nRadius of shape', i+1, ' ?')
        data[i].append(input('\n').split(','))
        
        #check that input is integer
        if not data[i][2][0].isnumeric() or not data[i][2][1].isnumeric():
          print('Error: Enter an integer for both dimensions')
        else:
          data[i][2][0], data[i][2][1] = int(data[i][2][0]), int(data[i][2][1])
          break

    if data[i][0] == 3:
        print('\nInner diameter, Outer diameter of shape', i+1 ,'is (i,o)')
        data[i].append(input('\n').split(','))
        
        #check that input is integer
        if not data[i][2][0].isnumeric() or not data[i][2][1].isnumeric():
          print('Error: Enter an integer for both dimensions')
        else:
          data[i][2][0], data[i][2][1] = int(data[i][2][0]), int(data[i][2][1])
          break

  #Convert to lowest young modulus material
  #get lowest young modulus
  for i in range(0,num_shapes):
    E_min = data[0][1]
    if E_min < data[i][1]:
      E_min = data[i][1]
  
  #multiply every y value by the shapes modulus/minimum modulus
  for i in range(0,num_shapes):
    data[i][2][1] = data[i][2][1] * data[i][1] / E_min  

  #get area of each shape
  for i in range(0,num_shapes):
    if data[i][0] == 1:
      #x * y
      data[i].append(data[i][2][0] * data[i][2][1])

    if data[i][0] == 2:
      #pi * r^2
      data[i].append(1.5707963268 * (data[i][2][0] / 2) ** 2)

    if data[i][0] == 3:
      #pi * r^2 - r^2
      data[i].append(3.1415926536 * ((data[i][2][0] / 2)**2 - (data[i][2][1] / 2)**2))

  #Get centroid of each shape
  if data[0][0] == 1:
    #x * y
    data[0].append(data[0][2][1] / 2)

  if data[0][0] == 2:
    #pi * r^2
    data[0].append((data[0][2][0] / 2))

  if data[0][0] == 3:
    #pi * r^2 - r^2
    data[0].append(data[i][2][1] / 2)

  length = 0
  for i in range(1,num_shapes):
    length = length + data[i - 1][2][1]
    if data[i][0] == 1:
      #x * y
      data[i].append(data[i][2][1] / 2 + length)

    if data[i][0] == 2:
      #pi * r^2
      data[i].append(data[i][2][0] / 2 + length)

    if data[i][0] == 3:
      #pi * r^2 - r^2
      data[i].append(data[i][2][1] / 2 + length)

  #Calculated overall centroid


  #Calculate second moment


  #Calculate stress at different points


  #Undo conversion


comp_beam()
