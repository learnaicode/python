class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_number):
        if task_number <= len(self.tasks) and task_number > 0:
            self.tasks[task_number-1]["completed"] = True
        else:
            print("Invalid task number.")
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = 'Done' if task['completed'] else 'Pending'
            print(f'{index}. {task["task"]} - {status}')

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task completed")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
            print(f"'{task}' added to the list.")
        elif choice == '2':
            to_do_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            to_do_list.mark_completed(task_number)
            print(f"Task {task_number} marked as completed.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()