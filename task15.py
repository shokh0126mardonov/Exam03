class TodoList:
    def __init__(self):
        self.__tasks = []
        
    def add_task(self,task):
        self.__tasks.append(task)
        
    def show_tasks(self):
        for index,tasks in enumerate(self.__tasks,start=1):
            print(f"{index}. {tasks}")
            

todo = TodoList()
todo.add_task("Do homework")
todo.add_task("Clean room")
todo.show_tasks()