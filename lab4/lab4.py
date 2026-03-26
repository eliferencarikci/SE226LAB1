n = int(input("Enter number of tasks:"))

tasks = {}  

#her task icin isim al-kac dependency var ögren 
for _ in range(n):
    task_name = input("Enter task name: ")
    dep_count = int(input(f"How many dependencies for {task_name}? "))

    
    dependencies = [] #dependency list olustur
    for i in range(dep_count):
        dep = input(f"Enter dependency {i+1}: ")
        dependencies.append(dep) #append()->listeye eleman ekler

    tasks[task_name] = dependencies #task->dependency lsitesi


#dictionary gezip key+value yazdır- items()->key value-verir
print("\nTask Structure:")
for task, deps in tasks.items():
    print(f"{task} -> {deps}")


#dependency listesi bos olanları bul
print("\nInitial Tasks (no dependencies):")
initial_tasks = [task for task in tasks if len(tasks[task]) == 0]

if initial_tasks:
    for t in initial_tasks:
        print(t)
else:
    print("none")




completed = set() # biten taskler
execution_order = [] # list
step = 1 

print("\nExecution Order:")

while len(completed) < len(tasks): # tüm taskler bitene kadar dön
    progress = False

    for task in tasks:
        
        if task not in completed:
            if all(dep in completed for dep in tasks[task]):
                print(f"Step {step}: {task}")
                execution_order.append(task)
                completed.add(task)
                step += 1
                progress = True

    
    if not progress:
        break


if len(completed) == len(tasks):
    print("ALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("No task can be started.")
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    
    for task in tasks:
        if task not in completed:
            print(task)