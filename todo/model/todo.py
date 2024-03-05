class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []


    def mark_completed(self):
        self.completed = True    #preguntar pistas de tipos


    def add_tag(self, tag: str):
        if tag not in self.tags:  #porque al tag no se le pone self?
            self.tags.append(tag)


    def __str__(self):
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self, todos: dict[int, Todo] = {}):
        self.todos: dict[int, Todo] = {}


    def add_todo(self, title: str, description: str) -> int:
        G_id = len(self.todos.values()) + 1         #?
        objeto = Todo(123,"title","description")
        self.todos[G_id] = objeto
        return G_id

   #7
    def pending_todos(self):
        retorn[todos for todo in todos.values()]


    def completed_todos(self):
        pass


    def tags_todo_count(self):
        self.









