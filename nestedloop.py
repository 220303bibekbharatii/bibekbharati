# 1. WAP to print the multiplication table of 5
# num =5 
# start= 1
# end=10
# for i in range(start, end + 1):
#     result=num*i
#     print(f"{num}*{i}={result}")
# 2. WAP to print the multiplication from 1 to 10 upto 10 multiples
# Define the maximum number of multiples you want to print
# max_multiples = 10
# for num in range(1, 11):
#      print(f"Multiplication table for {num}:")
#      for multiple in range(1, max_multiples + 1):
#          result = num * multiple
#          print(f"{num} x {multiple} = {result}")
#      print()


# 3. WAP to print the factorial of given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter a number: "))
print(factorial(number))



