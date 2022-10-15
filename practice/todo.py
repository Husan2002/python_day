from decorators import check_pincode

pincodes = ['12345', 'artur', 'python', 'itacademy', 'pincode']

class Todo:
    def __init__(self, pincode, name, rules=[]):
        self.tasks = []
        self.rules = rules
        self.name = name
        self.pincode = pincode
        self.authenticated = False
        if pincode in pincodes:
            self.authenticated = True


    @check_pincode
    def add_task(self, task):
        if self.authenticated:
            self.tasks.append(task)
            return self.tasks


    @check_pincode
    def get_tasks(self):
        if self.authenticated:
            return self.tasks
    

    @check_pincode
    def remove_task_by_index(self, index: int):
        if self.authenticated:
            return self.taks.pop(index)


    @check_pincode
    def change_name(self, new_name: str):
        if self.authenticated:
            self.name = new_name
            return self.name


    @check_pincode
    def get_name(self):
        if self.authenticated:
            return self.name


todo = Todo(rules=['some rules'], name="Artur", pincode='12345')
todo.add_task('add task')
todo.add_task('add task2')
todo.add_task('add task3')
print('===========')
todo.get_tasks()
# todo.change_name('Nuranov')

