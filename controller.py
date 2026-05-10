from model import TaskManager
from view import View


class MenuController:
    def __init__(self):
        self.model = TaskManager()
        self.view = View()
        self.filename = "tasks.json"

    def run(self):
        self.model.load_from_file(self.filename)
        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            if choice == 0:
                self.model.save_to_file(self.filename)
                self.view.show_message("До свидания!")
                break
            elif choice == 1:
                self.view.show_tasks(self.model.tasks)
            elif choice == 2:
                data = self.view.input_task_data()
                if data:
                    title, description, priority = data
                    task = self.model.add_task(title, description, priority)
                    self.view.show_message(f"Задача добавлена. ID: {task.id}")
            elif choice == 3:
                task_id = self.view.get_task_id()
                if task_id is None:
                    self.view.show_message("Некорректный ID.")
                    continue
                task = self.model.get_task_by_id(task_id)
                if not task:
                    self.view.show_message("Задача не найдена.")
                    continue
                self.view.show_message(f"Редактируем: {task}")
                edit_data = self.view.input_edit_data()
                self.model.edit_task(
                    task_id,
                    title=edit_data["title"],
                    description=edit_data["description"],
                    priority=edit_data["priority"],
                    status=edit_data["status"]
                )
                self.view.show_message("Задача обновлена.")
            elif choice == 4:
                task_id = self.view.get_task_id()
                if task_id is None:
                    self.view.show_message("Некорректный ID.")
                    continue
                if self.model.delete_task(task_id):
                    self.view.show_message("Задача удалена.")
                else:
                    self.view.show_message("Задача не найдена.")
            elif choice == 5:
                if self.model.undo():
                    self.view.show_message("Последнее действие отменено.")
                else:
                    self.view.show_message("Нечего отменять.")
            elif choice == 6:
                status = self.view.choose_filter_status()
                if status:
                    tasks = self.model.filter_by_status(status)
                    self.view.show_tasks(tasks)
                else:
                    self.view.show_message("Некорректный выбор.")
            elif choice == 7:
                priority = self.view.choose_filter_priority()
                if priority:
                    tasks = self.model.filter_by_priority(priority)
                    self.view.show_tasks(tasks)
                else:
                    self.view.show_message("Некорректный выбор.")
            elif choice == 8:
                self.view.show_tasks(self.model.get_priority_queue())
            elif choice == 9:
                self.model.save_to_file(self.filename)
                self.view.show_message(f"Сохранено в {self.filename}")
            elif choice == 10:
                if self.model.load_from_file(self.filename):
                    self.view.show_message(f"Загружено из {self.filename}")
                else:
                    self.view.show_message("Ошибка загрузки.")
            else:
                self.view.show_message("Неверный выбор. Попробуйте снова.")
