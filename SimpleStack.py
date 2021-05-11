class SimpleStack:
    counter = 0
    def __init__(self, init = []):
        print("stack object created")
        Stack.counter += 1
        self.__stack = init
    
    def push(self, val):
        self.__stack.append(val)
    
    def push_e(self, val):
        self.__stack.extend(val)
        
    def pop(self):
        return self.__stack.pop()
    
    def getsize(self):
        return len(self.__stack)
    
    def __str__(self):
        return str(self.__stack)

if __name__ == "__main__":
    stackObject = Stack()

    for i in range(100):
        stackObject.push(i)
    print(stackObject)
    
    for i in range(100):
        print(stackObject.pop())
    print(stackObject)

    print(stackObject.__dict__)