from My_classes.class_Stack import Stack
from Module_task_2.Fun_balanced import balanced_parenthesis

my_string = '[{{{}}}]()(())'

if __name__ == '__main__':
    balans_stack = Stack()
    print(balanced_parenthesis(my_string, balans_stack))





