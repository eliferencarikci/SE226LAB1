while True:
    n = int(input("Please enter an integer between 10 and 100: "))
    if 10 <= n <= 100:
        break
    print("Invalid input. Please enter a number between 10 and 100")

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n+1):

    if i % 7 == 0:
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1

    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1

    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1

    else:
        print(i)
