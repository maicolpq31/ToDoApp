class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool =  False
        self.tags: list[str] = []


    def mark_completed(self) -> bool:
        self.completed = True


    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


    def __str__(self):
        return f"code_ide {self.code_id}, title {self.title}"


class TodoBook:
    def __init__(self):
        self.todos: dict[int,Todo] = {}


    def add_todo(self,title: str, description: str) -> int:
        generar_id = len(self.todos) + 1
        objeto = Todo("107416", "renabado", description)
        self.todos[generar_id] = objeto
        return generar_id


    def pending_todos(self):
        return [todos for todo in self.todos.values() if not todo.completed]



