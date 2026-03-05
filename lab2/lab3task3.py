while True:
    n = int(input("Please enter a number between 3 and 9: "))
    
    if 3 <= n <= 9:
        break
    print("Invalid input. Please enter a number between 3 and 9")

for i in range(1, 2*n):
    if i <= n:
        print("*" * i)
    else:
        print("*" * (2*n - i))