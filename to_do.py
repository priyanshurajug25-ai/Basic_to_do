v = []

def view():
    for i in range(len(v)):
        print(f'{i+1}. {v[i]}')

def add(task):
    if task in v:
        print('Already Exist')
    else:
        v.append(task)
        print("Task is been added")

def delete(task):
    if len(v)==0:
        print('Must add task to remove')
    elif task in v:
        v.remove(task)
        print("Task is been removed")
    else:
        print("Task doesn't exist")

while True:
    print('''
    1. Print Today Task
    2. Add Task
    3. Delete Task
    4. Exit
    ''')
    n = int(input("Enter : "))
    if(n==1):
        view()
    elif(n==2):
        task = input('Enter your task : ')
        add(task)
    elif(n==3):
        task = input('Enter your task : ')
        delete(task)
    elif(n==4):
        break
    else:
        print("Wrong number is been given")