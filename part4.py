'''
***PART 4***

Write a program that repeatedly prompts the user to enter numbers until the user enters 0. The program calculate the product of all of the entered numbers and prints the product.

Example of what should appear when this part runs:

Enter a number or enter 0 to stop: 2
Enter a number or enter 0 to stop: 3
Enter a number or enter 0 to stop: 10
Enter a number or enter 0 to stop: 0
Product: 60

'''

i = int
x = 1

while i != 0:
  i = int(input("enter a number or enter 0 to stop: "))
  if (i != 0):
    x = x * i
print ("Product: ", x)
#done