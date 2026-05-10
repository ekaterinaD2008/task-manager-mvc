from enum import Enum


class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Status(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


class Task:
    def __init__(self, title="", description="", priority=Priority.MEDIUM, status=Status.TODO):
        self._title = title
        self._description = description
        self._priority = priority
        self._status = status
        self._id = id(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not value.strip():
            raise ValueError("Название не может быть пустым")
        self._title = value.strip()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value.strip() if value else ""

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if isinstance(value, Priority):
            self._priority = value
        elif isinstance(value, str):
            try:
                self._priority = Priority(value)
            except ValueError:
                raise ValueError("Приоритет должен быть Low, Medium или High")
        else:
            raise ValueError("Некорректный приоритет")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, Status):
            self._status = value
        elif isinstance(value, str):
            try:
                self._status = Status(value)
            except ValueError:
                raise ValueError("Статус должен быть To Do, In Progress или Done")
        else:
            raise ValueError("Некорректный статус")

    @property
    def id(self):
        return self._id

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "priority": self._priority.value,
            "status": self._status.value
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data["title"],
            description=data["description"],
            priority=Priority(data["priority"]),
            status=Status(data["status"])
        )
        task._id = data["id"]
        return task

    def __str__(self):
        return f"[{self._status.value}] {self._title} (Приоритет: {self._priority.value})"
