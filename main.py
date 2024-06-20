class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []

# Добавление новой задачи
    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print(f"Задача '{description}' добавлена со сроком выполнения {deadline}.")

# Выполнение задчи
    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Задача '{self.tasks[task_index].description}' выполнена.")
        else:
            print("Ошибка индекса задачи.")

    def display_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for index, task in enumerate(current_tasks, start=1):
                print(f"{index}. {task.description} (Срок: {task.deadline})")
        else:
            print("Нет текущих задач.")


task_manager = TaskManager()
task_manager.add_task("Погулять с собакой", "2024-06-20")
task_manager.add_task("Поменять солому у хомяков", "2024-06-22")
task_manager.display_current_tasks()
task_manager.mark_task_as_completed(0)
task_manager.display_current_tasks()
task_manager.mark_task_as_completed(1)
task_manager.display_current_tasks()
