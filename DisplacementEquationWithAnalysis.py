#Multiple functions to determine range of values for the variables not supplied by user and perform light analysis on the data
#by Callum Coffey
#Equation of mechanical displacement
def displace(list, recursive = 0, a = 0, u = 0):
  #check for enough data supplied
  if sum(['s' in list or 'd' in list or 'displacement' in list or 'distance'in list,'v' in list or 'u' in list or 'velocity' in list or 'initial velocity'in list,'a' in list or 'acceleration' in list]) < 2:
    print('Error : Requires two of (s,v,a)\n')
    return
  if  ( not ('v' in list or 'u' in list or 'velocity' in list or 'initial velocity'in list) or not ('a' in list or 'acceleration' in list)) and not ('t' in list or 'time' in list):
    print('Error : Requires known time if velocity or acceleration is unknown\n')
    return

  #checks that function is being run first time
  if recursive == 0:
    if 't' in list or 'time' in list:
      #get time
      t = int(input('Time in seconds?\n'))

    if 'a' in list or 'acceleration' in list:
      #get acceleration
      a = int(input('Acceleration in meters per second squared?\n'))

    if 'v' in list or 'u' in list or 'velocity' in list or 'initial velocity'in list:
      #get initial velocity
      u = int(input('Initial velocity in meters per second?\n'))

    if 's' in list or 'd' in list or 'displacement' in list or 'distance'in list:
      #get displacement
      s = int(input('Displacement?\n'))
  
  #calculates based on missing variables
  #calculates s from known variables
  if not ('s' in list or 'd' in list or 'displacement' in list or 'distance'in list):
    #create a time list with user inputted step size and maximum  
    t = []
    step = float(input('Time step size?\n'))
    end = float(input('Time maximum?\n'))
    i = 0
    #acts as do while statement with (round(i,1)) < end as a finishing condition
    while True:
      t.append(round(i,1))
      i = i + step
      if (round(i,1)) > end:
        break

    #calculates unknown variables
    #matches time with velocity and displacement in nested list
    #data[time,velocity,displacement]
    data = []
    for i in range(len(t)):
      data.append([])
      #putting time values in data
      data[i].append(t[i])

      #v = u + at
      #solving for v and putting in nested data array
      v = data[i][0]
      v = u + a*v
      data[i].append(float(v))

      #s =  vt + 0.5*at^2
      #solving for s and putting in nested data array
      s = data[i][0]
      s = s * u
      s = s + (a * data[i][0] * data[i][0]) / 2
      data[i].append(s)

    print('\nInitial velocity = ',u,'\nAcceleration = ',a,'\nFinal displacement = ',s,'\nFinal velocity = ',v,'\n')
    print(data, '\n')
    return a,u,data

  #calculates v from known variables and applies data to displace()
  if not ('v' in list or 'u' in list or 'velocity' in list or 'initial velocity'in list):
    #calculates unknown variables
    #s =  ut + 0.5*at^2
    #u = (s - 0.5 * a * t **2) / t
    #solving for s and putting in nested data array
    u = s - (0.5 * a * t ** 2) / t
    return displace(['a','v'],1,a,u)
    
  #calculates a from known variables
  if not ('a' in list or 'acceleration' in list):
    #calculates unknown variables
    #s =  ut + 0.5*at^2
    #a = (2 * (s - u * t)) / (t ** 2)
    #solving for s and putting in nested data array
    a = (2 * (s - u * t)) / (t ** 2)
    return displace(['a','v'],1,a,u)
  
#function to analyze results of the function displace
def analysis(list):
    a = list[0]
    u = list[1]
    data = list[2]

    #acceleration analysis
    if a > 0:
      print('Object is undergoing acceleration')
    elif a < 0:
      print('Object is undergoing decceleration')
    else:
      print('Object is moving at a constant speed')

    #velocity analysis
    if u == 0:
      print('Object starts with no initial velocity')
    else:
      print('Object begins in motion')
    for i in range(len(data)):
      if data[i][1] == 0:
        print('Velocity is zero at: ','Time = ',data[i][0],'Displacement = ',data[i][2])
    
    #displacement analysis
    for i in range(len(data)):
      if data[i][2] == 0:
        print('Displacement is zero at: ','Time = ',data[i][0],'Velocity = ',data[i][1])

analysis(displace((input('Variables known in s = ut + 1/2at^2?\n')).split(',')))
