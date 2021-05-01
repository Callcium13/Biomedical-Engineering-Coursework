#ask whether to have an endpoint
inf = int(input('Infinite? (1 or 0)   '))
num = 0
if (inf == 0):  
  #ask for range
  num = int(input('Range = ? (eg. 50, 1000, 25000)    '))

#check all numbers within range
i = 1
prime = [2]
while ((i < num) or (inf == 1)):
  i = i + 2
  #compare against all numbers in range
  check = 1
  j = 1
  while (j < i) and (check != 0):
    j = j + 1
    check = i%j
    if (j == i):
      prime.append(j)
      if (inf == 1):
        print(i)

print('The prime numbers between 1 and',num,'are;')
print(prime)
