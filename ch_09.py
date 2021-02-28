# Complete the factorial function below.
def factorial(n):
   return n * factorial(n-1) if n > 1 else 1

n = int(input())
i = 1 #contador

result = factorial(n)

print(result)
#fptr.write(str(result) + '\n')

#fptr.close()