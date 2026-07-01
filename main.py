from datetime import datetime, date
today = date.today()
tasks =[]
# -----DEFINING FUNCTIONS-----
#(i)
def add_task():
	task = input("Enter task: ")
	if task == "":
		print("Task cannot be empty!")
		return
		
	while True:
		deadline = input("Enter deadline (DD-MM-YYYY)\n[Press Enter to skip]:")
		if deadline == "":
			break
		else:
			try:
				datetime.strptime(deadline, "%d-%m-%Y")
				break
			except:
				print("Invalid date format! Please use DD-MM-YYYY or press Enter to skip.")
	task_dict = {
	"task" : task,
	"status" : "Pending",
	"deadline" : deadline
	}
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
				if i["deadline"] == "":
					print("Deadline : Not Set")
				else:
					print("Deadline:",i["deadline"])
					deadline = datetime.strptime(i["deadline"],"%d-%m-%Y").date()
					days_left = (deadline - today).days
					if i["status"] == "Completed":
						pass
					else:
						if days_left > 0:
							print("Days Remaining:",days_left)
						elif days_left ==0:
							print("Due Today ⚠️")
						else:
							print(f"Overdue by {abs(days_left)} days ⚠️")
				
				count+=1
		
#(iii)
def mark_task():
	comp_task = int(input("Enter Task no. that is completed : "))
	if comp_task>len(tasks) or comp_task<=0:
		print("Invalid Task Number")
	else:
		tasks[(comp_task)-1]["status"] = "Completed"
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
	
#(vii)
def search_task():
	search = input("Enter Keyword to Search:").lower()
	count = 0
	print("Search Result:")
	found = False
	for i in tasks:
		if search in i["task"].lower():
			count+=1
			print(f"{count}. {i['task']}")
			print("Status :", i["status"])
			found = True
			if i["deadline"] == "":
				print("Deadline : Not Set")
			else:
				print("Deadline:",i["deadline"])
				deadline = datetime.strptime(i["deadline"],"%d-%m-%Y").date()
				days_left = (deadline - today).days
				if i["status"] == "Completed":
					pass
				else:
						if days_left > 0:
							print("Days Remaining:",days_left)
						elif days_left ==0:
							print("Due Today ⚠️")
						else:
							print(f"Overdue by {abs(days_left)} days ⚠️")
	if not found:
			print("No matching tasks found.")
		


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
	print("5. Search Task")
	print("6. Exit")
	try:
		choice = int(input("Enter choice (1-6) : "))
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
				
#Delete Task			
	elif choice == 4:
		del_task()
				
#Search Tasks										
	elif choice == 5:
		search_task()
									
#Exit programme			
	elif choice == 6:
		save_task()
		print("\n" * 30)
		break		
		
#Wrong choice 
	else :
		print("Wrong choice, Only type valid number")