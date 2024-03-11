import json
from datetime import datetime

# Function to load tasks from a file
def load_tasks(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

# Function to add a new task
def add_task(tasks, task_name, priority, due_date=None):
    task = {'name': task_name, 'priority': priority, 'completed': False, 'due_date': due_date}
    tasks.append(task)

# Function to remove a task
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    else:
        print("Invalid task index")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            due_date = task['due_date'] if task['due_date'] else "No due date"
            print(f"{i + 1}. {task['name']} - Priority: {task['priority']} - Status: {status} - Due Date: {due_date}")

# Main function
def main():
    tasks = load_tasks('tasks.json')
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Complete Task\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task_name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
            if due_date:
                due_date = datetime.strptime(due_date, '%Y-%m-%d')
            add_task(tasks, task_name, priority, due_date)
        elif choice == '2':
            task_index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks, 'tasks.json')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()