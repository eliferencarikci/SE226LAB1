def factorial(x):
    if x==0 or x==1: return 1
    else: return x*factorial(x-1)
 #base case
term=lambda x,n:(x**n)/ factorial(n)

def exp_x(x,n):
     total=0
     for i in range(n+1):
      total += term(x,i)
     return total

x=float(input("enter value for x:"))
n=int(input("enter number of terms(n):"))

print("Result:",exp_x(x,n)) 
