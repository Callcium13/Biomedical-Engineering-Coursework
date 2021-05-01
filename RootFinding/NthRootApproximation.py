#Program to find the square, cube and nth root of a user supplied number and value for n
#checks that num is not negative
num = -1
while (num < 1):
  #ask the number to get the root of
  num = (int(input("Number?: ")))

res_p = -1
while res_p <= 1:
    #ask the how many decimal places accuracy
    res_p = (int(input("Decimal Places? (eg. 1, 2, 5): ")))

#convert decimal places to step size
res = 1 / (10**res_p)

nth = -1
while nth < 0:
    #ask the number to get the root of
    nth = (int(input("nth root n=?: ")))

#calculate square root X
i = 0
x = 0
while (x <= num):
    i = i + res
    x = 1
    for j in range(2):
        x = x * i

#Find closest fit to terminal count
if ((i)**2 == num):
    square_X = i
elif ((i + 1)**2 - num) < (num - (i + 1)**2):
    square_X = i + res
elif ((i + 1)**2 - num) > (num - (i + 1)**2):
    square_X = i - res
else:
    square_X = 'ERROR'

#calculate cubed root X
i = 0
x = 0
while (x <= num):
    i = i + res
    x = 1
    for j in range(3):
        x = x * i

if ((i)**3 == num):
    cube_X = i
elif ((i + 1)**3 - num) <= (num - (i + 1)**3):
    cube_X = i + res
elif ((i + 1)**3 - num) > (num - (i + 1)**3):
    cube_X = i - res
else:
    cube_X = 'ERROR'

#calculate nth root
i = 0
x = 0
while (x <= num):
    i = i + res
    x = 1
    for j in range(nth):
        x = x * i

if ((i)**nth == num):
    nth_X = i
elif ((i + 1)**nth - num) <= (num - (i + 1)**nth):
    nth_X = i + res
elif ((i + 1)**nth - num) > (num - (i + 1)**nth):
    nth_X = i - res
else:
    nth_X = 'ERROR'

#round off to place count
square_X = round(square_X, res_p)
cube_X = round(cube_X, res_p)
nth_X = round(nth_X, res_p)

print('Square root approximation=', square_X)
print('Cube root approximation=', cube_X)
print(nth,'th root approximation=', nth_X)
