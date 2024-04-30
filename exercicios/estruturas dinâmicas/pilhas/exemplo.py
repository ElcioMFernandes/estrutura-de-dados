class Node: ## Claase 
    def __init__(self):
        self.__value = 0
        self.next = None

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class Stack:
    def __init__(self):
        self.__top = None        

    def push(self):
        temp_node = Node()
        if temp_node:
            temp_node.set_value(int(input("value: ")))
            temp_node.set_next(self.__top)
            self.__top = temp_node

    def pop(self):
        if self.__top:
            print("value to remove: ", self.__top.get_value())
            self.__top = self.__top.get_next()
        else:
            print("empty stack...")

    def get_all(self):
        if not self.__top:
            print("empty stack...")
            return
        
        temp_node = self.__top
        output = "stack:\n"
        while temp_node:
            output += f"{str(temp_node.get_value())}\n"
            temp_node = temp_node.get_next()
        print(output)


app = Stack()
while True:
    op = int(input("\n1. stack up\n2. unstack\n3. get stack\n4. quit\n\nentry: "))
    if op == 1:
        app.push()
    elif op == 2:
        app.pop()
    elif op == 3:
        app.get_all()
    else:
        break