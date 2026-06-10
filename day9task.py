class TaskNotFoundError(Exception):
    pass

class InvalidTaskDataError(Exception):
    pass

tasks: dict[int, dict] = {}
next_id = 1


def get_all_tasks():
    return list(tasks.values())


def get_task(task_id: int):
    if task_id not in tasks:
        raise TaskNotFoundError(f"Task {task_id} not found")
    return tasks[task_id]


def create_task(data: dict):
    global next_id

    if not isinstance(data, dict):
        raise InvalidTaskDataError("Data must be dict")

    if "title" not in data or not data["title"].strip():
        raise InvalidTaskDataError("Title required")

    task = {
        "id": next_id,
        "title": data["title"],
        "completed": data.get("completed", False)
    }

    tasks[next_id] = task
    next_id += 1
    return task


def update_task(task_id: int, data: dict):
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")

    tasks[task_id].update(data)
    return tasks[task_id]


def delete_task(task_id: int):
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")

    del tasks[task_id]
    return True


def menu():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Create task")
        print("2. View all tasks")
        print("3. Get task by id")
        print("4. Update task")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Enter title: ")
                print(create_task({"title": title}))

            elif choice == "2":
                print(get_all_tasks())

            elif choice == "3":
                task_id = int(input("Enter id: "))
                print(get_task(task_id))

            elif choice == "4":
                task_id = int(input("Enter id: "))
                title = input("New title: ")
                completed = input("Completed (yes/no): ").lower() == "yes"
                print(update_task(task_id, {"title": title, "completed": completed}))

            elif choice == "5":
                task_id = int(input("Enter id: "))
                delete_task(task_id)
                print("Deleted successfully")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except (TaskNotFoundError, InvalidTaskDataError, ValueError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()

