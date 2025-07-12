# 📅 MINI-PROJECT 2: SIMPLE DAILY PLANNER

def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # No file yet, start with empty list
        pass
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("🗒️ Your task list is empty.")
    else:
        print("🗒️ Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter the task you want to add: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task added: {task}")
    else:
        print("⚠️ Empty task not added.")

def main():
    print("📅 Welcome to your Simple Daily Planner!\n")
    tasks = load_tasks()

    while True:
        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Save and exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()