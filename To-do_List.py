tasks =[]
# -----DEFINING FUNCTIONS-----
#(i)
def add_task():
	task = input("Enter task: ")
	deadline = input("Enter deadline (DD-MM-YYYY): ")
	if task == "":
		print("Task cannot be empty!")
	else:
		task_dict = {}
		task_dict.update({"task":task})
		task_dict.update({"status":"Pending"})
		task_dict.update({"deadline":deadline})
		tasks.append(task_dict)
		print("Task Saved Successfully✅")

#(ii)
def view_task():
	if len(tasks)==0:
		print("No tasks available")
	else:
			count = 1
			for i in tasks:
				print(f"{count}.  {i['task']}")
				print("Status :", i["status"])
				print("Deadline:",i["deadline"])
				count+=1
		
#(iii)
def mark_task():
	comp_task = int(input("Enter Task no. that is completed : "))
	if comp_task>len(tasks) or comp_task<=0:
		print("Invalid Task Number")
	else:
		tasks[(comp_task)-1].update({"status":"Completed"})
		print("Task Updated successfully✅")

#(iv)
def del_task():
	deltask = int(input("Enter Task Number to Delete: "))
	if deltask > len(tasks) or deltask<=0:
		print("Invalid Task Number")
	else:
		del tasks[(deltask)-1]
		print("Task Deleted Successfully✅")

#(v)
def save_task():
	my_file = open("tasks.txt","w")
	for i in tasks:
		task_text= i["task"] + "|" + i["status"] + "|" + i["deadline"]
		my_file.write(task_text + "\n")
	my_file.close()

#(vi)
def load_task():
	loadtask = open("tasks.txt","r")
	for line in loadtask:
		x = line.strip()
		parts = x.split("|")
		task_dict2 = {"task":parts[0],"status":parts[1],"deadline":parts[2]}
		tasks.append(task_dict2)
	loadtask.close()


#--------MAIN MENU--------
try:
	load_task()
except:
	pass
while True:
	print ("="*50)
	print("TO-DO LIST".center(50))
	print("="*50, "\n\n\n")
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Mark Task Complete")
	print("4. Delete Task")
	print("5. Exit")
	try:
		choice = int(input("Enter choice (1-5) : "))
	except:
		print("Please Type Valid Number only")
		continue
# Add Task 
	if choice == 1:
		add_task()
		
#View Tasks
	elif choice == 2:
		view_task()

#Mark Task Complete	
	elif choice == 3:
				mark_task()
				
#Delete Tasks			
	elif choice == 4:
				del_task()
								
#Exit programme			
	elif choice == 5:
		save_task()
		break		
		
#Wrong choice 
	else :
		print("Wrong choice, Only type valid number")