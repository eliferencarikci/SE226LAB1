x=int(input("Please enter a positive integer greater than 1:"))

count=0
print(x,end="")

while x!=1 :
    if x%2==0 :
        x =x//2
    else:
        x = x*3+1

    print(" -> ",x,end="")  
    count += 1

print("\nTotal Steps:",count)



