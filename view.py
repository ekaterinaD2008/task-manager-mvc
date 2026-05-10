from task import Priority, Status


class View:
    @staticmethod
    def show_menu():
        print("\n=== TASK MANAGER ===")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("5. Отменить последнее действие (Undo)")
        print("6. Фильтр по статусу")
        print("7. Фильтр по приоритету")
        print("8. Показать очередь по приоритету")
        print("9. Сохранить в файл")
        print("10. Загрузить из файла")
        print("0. Выход")
        print("=====================")

    @staticmethod
    def get_user_choice():
        try:
            return int(input("Выберите действие: "))
        except ValueError:
            return -1

    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("Задач нет.")
            return
        print("\n--- Список задач ---")
        for task in tasks:
            print(f"ID: {task.id}")
            print(f"  Название: {task.title}")
            print(f"  Описание: {task.description}")
            print(f"  Приоритет: {task.priority.value}")
            print(f"  Статус: {task.status.value}")
            print("  ---")

    @staticmethod
    def input_task_data():
        title = input("Название задачи: ").strip()
        if not title:
            print("Ошибка: название не может быть пустым.")
            return None

        description = input("Описание (можно пропустить): ").strip()

        print("Приоритет: 1 - Low, 2 - Medium, 3 - High")
        priority_choice = input("Выберите приоритет (по умолчанию Medium): ").strip()
        priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH}
        priority = priority_map.get(priority_choice, Priority.MEDIUM)

        return title, description, priority

    @staticmethod
    def get_task_id():
        try:
            return int(input("Введите ID задачи: "))
        except ValueError:
            return None

    @staticmethod
    def input_edit_data():
        print("Оставьте поле пустым, чтобы не менять его.")
        title = input("Новое название: ").strip()
        description = input("Новое описание: ").strip()

        print("Приоритет: 1 - Low, 2 - Medium, 3 - High (Enter - не менять)")
        priority_choice = input("Выберите приоритет: ").strip()
        priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH}
        priority = priority_map.get(priority_choice, None)

        print("Статус: 1 - To Do, 2 - In Progress, 3 - Done (Enter - не менять)")
        status_choice = input("Выберите статус: ").strip()
        status_map = {"1": Status.TODO, "2": Status.IN_PROGRESS, "3": Status.DONE}
        status = status_map.get(status_choice, None)

        return {
            "title": title if title else None,
            "description": description if description else None,
            "priority": priority,
            "status": status
        }

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def choose_filter_status():
        print("1 - To Do")
        print("2 - In Progress")
        print("3 - Done")
        choice = input("Выберите статус: ").strip()
        status_map = {"1": Status.TODO, "2": Status.IN_PROGRESS, "3": Status.DONE}
        return status_map.get(choice, None)

    @staticmethod
    def choose_filter_priority():
        print("1 - Low")
        print("2 - Medium")
        print("3 - High")
        choice = input("Выберите приоритет: ").strip()
        priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH}
        return priority_map.get(choice, None)
