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
        if self.tag not in self.tags:
            self.tags.append[tag]


    def __str__(self) -> str:
        return f"code_ide {self.code_id}, title {self.title}"




class TodoBook:
    def __init__(self, todos: = dict[]):
        self.todos = dict[int]


    def add_todo(self, title: str):


