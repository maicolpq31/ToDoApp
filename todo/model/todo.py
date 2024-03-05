class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []


    def mark_completed(self):
        self.completed = True


    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


    def __str__(self):
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self, todos: dict[int, Todo] = {}):
        self.todos: dict[int, Todo] = {}


    def add_todo(self, title: str, description: str) -> int:
        G_id = len(self.todos.values()) + 1         #?
        objeto = Todo(G_id,title,description)
        self.todos[G_id] = objeto  #tod["key"] = se le asigna a un objeto
        return G_id

   #7
    def pending_todos(self):
        #      output       collection                  condition
        return[todos for todo in self.todos.values() if todo.completed == False]
        #return [todos for x in self.todos.values() if x.completed == False]  la variable iteradora es x

    def completed_todos(self):
        return[todos for todo in self.todos.values() if todo.completed == True]


    def tags_todo_count(self):
        tags = []
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag not in tags:
                    tags.append(tag)

todo_book = TodoBook()
todo_book.add_todo("hola", "description")
todo_book.add_todo("oe", "description")
print(todo_book.todos[2])

tarea = todo_book.todos[2]
tarea.add_tag("matematicas")
print(todo_book.todos[2].tags)









