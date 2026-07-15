from datetime import datetime, date
today = date.today()
tasks =[]
'''
=============================
TASK MANAGEMENT FUNCTIONS
=============================
'''

# Add a new task
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
	priority_ = input("Select Priority or press Enter to skip.\n1) High\n2) Medium\n3) Low\nYour Response(1-3): ")
	if priority_ == "1":
	   priority = "High"
	elif priority_ == "2":
	   priority = "Medium"
	elif priority_ == "3":
	   priority = "Low"
	else :
	    priority = "Not set"
	task_dict = {
	"task" : task,
	"status" : "Pending",
	"deadline" : deadline,
	"priority" : priority
	}
	tasks.append(task_dict)
	print("Task Saved Successfully✅")

#View all tasks
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
                print("Priority:",i["priority"])
                count+=1
		
#Mark Tasks complete 
def mark_task():
	comp_task = int(input("Enter Task no. that is completed : "))
	if comp_task>len(tasks) or comp_task<=0:
		print("Invalid Task Number")
	else:
		tasks[(comp_task)-1]["status"] = "Completed"
		print("Task Updated successfully✅")

#Delete Tasks
def del_task():
	deltask = int(input("Enter Task Number to Delete: "))
	if deltask > len(tasks) or deltask<=0:
		print("Invalid Task Number")
	else:
		del tasks[(deltask)-1]
		print("Task Deleted Successfully✅")
	
#Search Tasks
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
			print("Priority:", i["priority"])
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
			
#Edit Tasks
def edit_task():
	if len(tasks) == 0:
		print("No tasks available")
		return
	view_task()
	try:
		edit = int(input("Enter task number to edit"))
	except:
		print("Please Enter a valid number")
		return
	if edit<=0 or edit > len(tasks):
		print("Invalid Task number")
		return
	print("Selected Task:\n\n\n")
	print("Tasks:",tasks[edit - 1]["task"])
	print("Status:",tasks[edit-1]["status"])
	print("Priority:",tasks[edit-1]["priority"])
	if tasks[edit - 1]["deadline"] == "":
		print("Deadline:","Not set")
	else:
		print("Deadline:",tasks[edit-1]["deadline"])
	print("\n\nWhat do you want to edit ?\n")
	print("1. Task Name")
	print("2. Deadline")
	print("3. Priority")
	print("4. Cancel")
	try:
		Edit_num = int(input())
	except:
		print("Enter Valid Number(1-4)")
		return
	
	if Edit_num == 1:
		new_task = input("Set new task name: ")
		if new_task == "":
			print("Task cannot be empty!")
			return
		tasks[edit-1]["task"] = new_task
		print("Task changed successfully✅")
	elif Edit_num == 2:
		while True:
			edit_deadline = input("Set new deadline\n(Press Enter to remove deadline)")
			if edit_deadline == "":
				break
			else:
				try:
					datetime.strptime(edit_deadline, "%d-%m-%Y")
					break
				except:
					print("Invalid date format! Please use DD-MM-YYYY or press Enter to skip.")
			
		tasks[edit-1]["deadline"] = edit_deadline
		print("Deadline Changed successfully✅")
	elif Edit_num == 3:
	       edit_priority = input("Select Priority or press Enter to skip.\n1) High\n2) Medium\n3) Low\nYour Response(1-3): ")
	       if edit_priority == "1":
	           tasks[edit - 1]["priority"] = "High"
	       elif edit_priority == "2":
	           tasks[edit - 1]["priority"]= "Medium"
	       elif edit_priority == "3":
	           tasks[edit - 1]["priority"] = "Low"
	       else:
	           tasks[edit - 1]["priority"]= "Not set"
	       print("Priority changed successfully✅")
	elif Edit_num == 4:
	    return
	else:
		print("Enter Valid Number (1-3)")
		
#Statistics
def statistics():
	if len(tasks)==0:
		print("No tasks available")
		return
	total_tasks = len(tasks)
	completed = 0
	pending = 0
	overdue = 0
	print("=" * 50)
	print("STATISTICS".center(50))
	print("=" * 50)
	print("\n\n\n")
	for i in tasks:
		if i["status"] == "Completed":
			completed += 1
		elif i["status"] == "Pending":
			pending += 1
		if i["deadline"] != "":
			if i["status"] == "Pending":
				deadline = datetime.strptime(i["deadline"],"%d-%m-%Y").date()
				days_left = (deadline - today).days
				if days_left < 0:
					overdue += 1
	Completion_rate = (completed/(total_tasks)) * 100
	print("Total Tasks:\t",len(tasks))
	print("Completed Tasks:\t",completed)
	print("Pending Tasks:\t",pending)
	print("Overdue Tasks:\t",overdue)
	print(f"Completion Rate:\t {Completion_rate:.1f}%")
			

'''
====================
File Handling Functions 
====================
'''	
	
#Save tasks 
def save_task():
	my_file = open("tasks.txt","w")
	for i in tasks:
		task_text= i["task"] + "|" + i["status"] + "|" + i["deadline"] + "|" + i["priority"]
		my_file.write(task_text + "\n")
	my_file.close()

#Load Task
def load_task():
	loadtask = open("tasks.txt","r")
	for line in loadtask:
		x = line.strip()
		parts = x.split("|")
		task_dict2 = {"task":parts[0],"status":parts[1],"deadline":parts[2], "priority" : parts[3]}
		tasks.append(task_dict2)
	loadtask.close()
	
	
'''
================
|| MAIN PROGRAM  ||
================
'''
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
	print("5. Search Tasks")
	print("6. Edit Task")
	print("7. Statistics")
	print("8. Exit")
	try:
		choice = int(input("Enter choice (1-8) : "))
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

#Edit Task	
	elif choice == 6:
		edit_task()

#Statistics 								
	elif choice == 7:
	    statistics()
#Exit programme			
	elif choice == 8:
		save_task()
		print("\n" * 30)
		break		
		
#Wrong choice 
	else :
		print("Wrong choice, Only type valid number")