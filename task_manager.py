import os

# file to store tasks
FILE_Name = "tasks.txt"

# Load tasks from file
def load_tasks():
    task = {}
    if os.path.exists(FILE_Name):
        with open(FILE_Name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:  # skip empty lines
                    continue
                parts = line.split("|")
                if len(parts) != 3:  # skip malformed lines
                    continue
                task_id, title, status = parts
                task[int(task_id)] = {"title": title, "status": "complete" if status == "1" else "incomplete"}
    return task

                      
# Save tasks to file
def save_tasks(tasks):
    with open(FILE_Name, "w") as file:
        for task_id, task in tasks.items():
            status_val = "1" if task['status'] == "complete" else "0"
            file.write(f"{task_id}|{task['title']}|{status_val}\n")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

# Mark task completion status
def mark_task_competed(tasks):
    task_id = int(input("Enter task ID to mark completion: ")) 
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: ")) 
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Invalid task number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_competed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
