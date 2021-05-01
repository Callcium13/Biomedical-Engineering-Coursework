
#function to bubble sort
def bubble_sort(unsorted):
    length = len(unsorted)
    #iterate through all integers until check is 0
    #acts as a "do while"
    while (True):
        check = 0
        for i in range(length - 1):
            if (unsorted[i] > unsorted[i + 1]):
                #make any swaps and note
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                check = check + 1
        if (check == 0):
            break
    return unsorted

#function to selection sort
def select_sort(unsorted):
  length = len(unsorted)
  i = 0
  #iterate through all integers
  while i < length:
      low = i
      j = i
      #iterate through all unsorted integers
      while j < length - 1:
          j = j + 1
          #note lowest unsorted number
          if unsorted[low] > unsorted[j]:
              low = j
      #place lowest in end of sorted section
      unsorted[i], unsorted[low] = unsorted[low], unsorted[i]
      i = i + 1
  return unsorted

#function to insertion sort
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

#function to merge sort
def merge_sort(unsorted):
  length = len(unsorted)
  if length > 1:
    #split array into left and right
    mid = length // 2
    #deal with odd lengths
    left = unsorted[:mid]
    right = unsorted[mid:]
       
    #sort half of list if it contains more than one integer
    left = merge_sort(left)    
    right = merge_sort(right)

    unsorted = []
    #checks that left and right lists both cntain at least one entry
    while left and right:
    #checks for lower first value of left and right lists
      if left[0] > right[0]:
        #pops and appends that value to list unsorted
        unsorted.append(right.pop(0))
      else:
        unsorted.append(left.pop(0))
    for i in left:
      unsorted.append(i)
    for i in right:
      unsorted.append(i)
  return unsorted

#function to do a combination of a merge and insert sort where any element larger than 
def custom_sort(unsorted):
  length = len(unsorted)
  if length > 40:
    #split array into left and right
    mid = length // 2
    #deal with odd lengths
    left = unsorted[:mid]
    right = unsorted[mid:]
       
    #sort half of list if it contains more than one integer
    left = custom_sort(left)    
    right = custom_sort(right)

    sort = []
    while left and right:
      if left[0] > right[0]:
        sort.append(right.pop(0))
      else:
        sort.append(left.pop(0))
    for i in left:
      sort.append(i)
    for i in right:
      sort.append(i)
  else:
    sort = insert_sort(unsorted)
  return sort

#function to sort list of integer through; bubble, selection, insertion and merge
#in order to get the fastest sorting method for similar data
#requires functions for all sorts
#sort start: stops sorting algorithms that are slower with large lists, choose 0 - 4
def best_sort(list, repeats = 100, print_sorted = 0, print_times = 0, print_best = 1, print_length = 1, sort_start = 0):
  import time
  #takes user input of string and converts to list of integers
  #input and convert to lists

  if print_length == 1:
    print('Length: ',len(unsorted),'\n')

  data = []

  if sort_start < 1:
    #bubble sort
    times = []
    i = 0
    while i < repeats:
      tic1 = time.perf_counter()
      bubble_sort(unsorted)
      tic2 = time.perf_counter()
      times.append(tic2 - tic1)
      i = i + 1
    data.append([sum(times) / len(times),'Bubble Sort'])

  if sort_start < 2:
    #selection sort
    times = []
    i = 0
    while i < repeats:
      tic1 = time.perf_counter()
      select_sort(unsorted)
      tic2 = time.perf_counter()
      times.append(tic2 - tic1)
      i = i + 1
    data.append([sum(times) / len(times),'Selection Sort'])

  if sort_start < 3:
    #insertion sort
    times = []
    i = 0
    while i < repeats:
      tic1 = time.perf_counter()
      insert_sort(unsorted)
      tic2 = time.perf_counter()
      times.append(tic2 - tic1)
      i = i + 1
    data.append([sum(times) / len(times),'Insert Sort'])

  if sort_start < 4:
    #merge sort
    times = []
    i = 0
    while i < repeats:
      tic1 = time.perf_counter()
      merge_sort(unsorted)
      tic2 = time.perf_counter()
      times.append(tic2 - tic1)
      i = i + 1
    data.append([sum(times) / len(times),'Merge Sort'])

  #custom sort
  times = []
  i = 0
  while i < repeats:
    tic1 = time.perf_counter()
    custom_sort(unsorted)
    tic2 = time.perf_counter()
    times.append(tic2 - tic1)
    i = i + 1
  data.append([sum(times) / len(times),'Custom Sort'])

  if print_times == 1:  
    i = 0
    while i < 5 - sort_start:
      print(data[i][1],'{:2e}'.format(data[i][0]),'\n')
      i = i + 1
  insert_sort(data)
  if print_best == 1:
    print('Fastest was: ', data[0][1],'\n')

#Normal data entry
if False:
  unsorted = (input('Integers to sort? \n')).split(',')
  check = 0
  for i in unsorted:
    if not i.lstrip('-').isnumeric():
      print('Error: List must only contain numeric characters')
      check = 1
  if check == 0:
    unsorted = list(map(float,unsorted))
    best_sort(unsorted)

#Infinite mode for stress testing
if True:
  import random
  unsorted = []
  for i in range(0,1000):
    num = random.randint(0, 10)
    if True:
      num = num + random.random()
    unsorted.append(num)
  best_sort(unsorted,10,0,1,1,1,2)

#Testing and optimization
if False:
  import time
  import random
  unsorted = []
  for i in range(0,10000):
    num = random.randint(0, 10)
    if False:
      num = num + random.random()
    unsorted.append(num)

  times = []
  i = 0
  while i<10:
    tic1 = time.perf_counter()
    sort = custom_sort(unsorted)
    tic2 = time.perf_counter()
    times.append(tic2 - tic1)
    i = i + 1
  avg = sum(times) / len(times)
  print('Time = ','{:2e}'.format(avg),'\n')
  print('sorted = ', sort)
