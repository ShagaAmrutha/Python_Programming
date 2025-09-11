class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(f"Name: {self.name},sal: {self.sal}")
class manager(employee):
    def __init__(self,name,sal,dept):
        super().__init__(name,sal)
        self.dept=dept
    def display(self):
        print(f"Name: {self.name},sal: {self.sal},dept:{self.dept}")
emp = employee("Alice",23995)
man = manager("bob",45788,"testing")
emp.display()
man.display()