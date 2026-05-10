import json
from collections import deque
from task import Task, Priority, Status


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._undo_stack = []
        self._priority_queue = deque()

    @property
    def tasks(self):
        return self._tasks

    def add_task(self, title, description, priority):
        task = Task(title=title, description=description, priority=priority)
        self._tasks.append(task)
        self._update_priority_queue()
        self._undo_stack.append(("add", task))
        return task

    def delete_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                self._update_priority_queue()
                self._undo_stack.append(("delete", task))
                return True
        return False

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        for task in self._tasks:
            if task.id == task_id:
                old_state = {
                    "title": task.title,
                    "description": task.description,
                    "priority": task.priority,
                    "status": task.status
                }
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if priority is not None:
                    task.priority = priority
                if status is not None:
                    task.status = status
                self._update_priority_queue()
                self._undo_stack.append(("edit", task, old_state))
                return True
        return False

    def undo(self):
        if not self._undo_stack:
            return False
        action = self._undo_stack.pop()
        if action[0] == "add":
            task = action[1]
            self._tasks = [t for t in self._tasks if t.id != task.id]
        elif action[0] == "delete":
            self._tasks.append(action[1])
        elif action[0] == "edit":
            task = action[1]
            old_state = action[2]
            task.title = old_state["title"]
            task.description = old_state["description"]
            task.priority = old_state["priority"]
            task.status = old_state["status"]
        self._update_priority_queue()
        return True

    def filter_by_status(self, status):
        if isinstance(status, str):
            status = Status(status)
        return [task for task in self._tasks if task.status == status]

    def filter_by_priority(self, priority):
        if isinstance(priority, str):
            priority = Priority(priority)
        return [task for task in self._tasks if task.priority == priority]

    def get_priority_queue(self):
        return list(self._priority_queue)

    def _update_priority_queue(self):
        priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}
        self._priority_queue = deque(
            sorted(self._tasks, key=lambda t: priority_order[t.priority])
        )

    def save_to_file(self, filename):
        data = [task.to_dict() for task in self._tasks]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._tasks = [Task.from_dict(item) for item in data]
            self._update_priority_queue()
            self._undo_stack.clear()
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def get_task_by_id(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
