
from My_classes.class_Stack import Stack
if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('first')
    my_stack.push('second')
    my_stack.push('third')
    my_stack.push('last')

    print(f"{my_stack.stack}, {my_stack.isEmpty()}\n{my_stack.peek()}\n{my_stack.size()}")
    print()

    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()

    print(f"{my_stack.stack}, {my_stack.isEmpty()}\n{my_stack.peek()}\n{my_stack.size()}")


