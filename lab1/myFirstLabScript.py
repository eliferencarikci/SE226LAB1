

#TASK1
name=input("What is your name?")
print(name)
print("Hello " + name)

id=input("What is your Student ID?")
print(id)
print("Your student ID is " +id)


#TASK2
total_seconds=int(input("Enter a total number of seconds:"))

hours=total_seconds //3600
remaining=total_seconds%3600

minutes=remaining //60
seconds=remaining%60

print(total_seconds,"second is",hours," hours,",minutes,"minutes, and",seconds,"seconds.")
 
