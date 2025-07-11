class TaskManager:
    def __init__(self):
        self.tasks = []

    # Метод для добавления новой задачи
    def add_task(self, description, due_date=None):
        task = {
            'description': description,
            'due_date': due_date,
            'is_completed': False
        }
        self.tasks.append(task)

    # Метод для отметки задачи как выполненной
    def mark_as_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['is_completed'] = True
        else:
            print("Неверный индекс задачи.")

    # Метод для отображения всех невыполненных задач
    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task['is_completed']]
        return incomplete_tasks


# Пример использования менеджера задач
if __name__ == "__main__":
    manager = TaskManager()

    # Добавляем две задачи
    manager.add_task('Написать отчет', '2025-10-30')
    manager.add_task('Подготовить презентацию', '2025-11-05')

    # Список активных задач
    print("Список текущих задач:")
    for i, task in enumerate(manager.list_incomplete_tasks()):
        print(f"{i + 1}. {task['description']} ({task['due_date']})")

    # Выполняем первую задачу
    manager.mark_as_complete(0)

    # Повторяем вывод оставшихся задач
    print("\nОстаточные задачи после завершения первой:")
    for i, task in enumerate(manager.list_incomplete_tasks()):
        print(f"{i + 1}. {task['description']} ({task['due_date']})")