'''
################# 4. sum of n for n terms. sum of x squared for x terms.
n = int(input("Enter number n:"))
for i in range(n):
  n += i
print("n =", n)

total = 0
x = int(input("Enter number x:"))
for i in range(n):
  total += x**i
  print("x =", x)
'''
#palindrome: 5225, 9, 121. How do you check if it's a palindrome?

################# 3d. take input of number and display the reverse of the number
num = 374
remainder = 0
reverse = 0
while num > 0:
  digit = num % 10
  reverse = (reverse*10) + digit
  num//=10
  print("digit:", digit, "\n")

print("Reverse is", reverse)


'''
################# 3c. add the sum of the cubed digits. For example 1**3 + 3**3 + 5**3 = 153
num = 153
sum = 0
while num > 0:
  digit = num % 10
  sum += digit**3
  num//=10
  print("sum:", sum)
  print("digit:", digit, "\n")
print("sum of digits of 153 is", sum)

################# 3. Find sum of even digits, sum of odd digits of 4127
num = 4127
s_odd = 0
s_even = 0
n_odd = 0
n_even = 0
while num > 0:
  digit = num % 10
  if digit % 2 == 0:
    n_even += 1
    s_even += digit
  else:
    n_odd +=1
    s_odd +=digit
  num//=10
print("sum of odd:", s_odd, "\nsum of even:", s_even)


################# 3. Sum of digits in a number
num_str = input("Enter a number")
sum = 0
while num > 0:
  digit = num%10
  sum += digit
  num//=10
print("Sum of digits=", sum)


################# Write programs to display 1 + 2 + 3 + 4 and 1 + 3 + 5 + 7
n = 0
for i in range(5):
  n += i
print(n)

n = 0
for i in range(1, 8, 2):
  n += i
print(n)
print(1 + 3 + 5 + 7)


print("KPH \t MPH")
for KPH in range (60, 130, 10):
  MPH = KPH * .6214
  print(KPH, "\t",format(MPH, '.1f'))


################# 
print("Number Square \n---------")
for i in range(1, 10):
  square = i**2
  print(square)


#################  For Loop - in lists  ###########
for x in [3, 4, 7]:
  print(x)

for x in ["Amy", "Sandy", "Alex"]:
  print(x)

a = 12
b = 6.67
for x in [a, b]:
  print(x)


#################  While Loop  ###########
choice = 1
while choice == 1:
  num = int(input("enter a number:"))
  print("Square=", num*num)
  choice = int(input("Want to find the square of another number(1 for true / 0 for false):"))

#################  Factorial - While Loop  ###########
n = int(input("What's your number?"))
factorial = 1
i = 1 #put first value before loop
while (i <= n):
  factorial *= i
  i = i + 1
print(factorial)

#################  Factorial  #################
n = int(input("What's your number?"))
total = 1
for i in range(1, n+1):
  factorial *= i
  # factorial = factorial * i
print(factorial)


#################  Notes  #################
Count - controlled = for loop
Condition - controlled = While loop
  While loops executes when it's true, and stops when it becomes false
'''