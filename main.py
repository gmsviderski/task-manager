from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Некорректный индекс задачи")

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        return current_tasks

    def show_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if not current_tasks:
            print("Все задачи выполнены!")
        else:
            for idx, task in enumerate(current_tasks):
                print(f"{idx}. {task}")

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавляем задачи
    manager.add_task("Сделать домашнее задание", "2023-10-15")
    manager.add_task("Купить продукты", "2023-10-10")
    manager.add_task("Забрать посылку", "2023-10-12")
