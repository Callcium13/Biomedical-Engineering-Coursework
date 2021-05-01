#requires turtle
#asks size of sequence
count = int(input('How many numbers in sequence?    '))
if False:  
  #asks angle of sequence
  ang = int(input('Angle of pattern?    '))
else:
  ang = 90
#generates fibonacci sequence
fib = [0,1]
i = 0
while (i < count):
  x = fib[i] + fib[i+1]
  fib.append(x)
  i = i + 1
print(fib)

#draws the fibonacci spiral
import turtle
import random
i = 0
t = turtle.Turtle()
while (True):
  i = i + 1
  j = 0
  while (j < count):
    j = j + 1
    rand = random.randint(1,360/ang)
    t.fd(fib[j + 1])
    t.rt(ang)
  t.rt(ang * rand)


 

  

  
