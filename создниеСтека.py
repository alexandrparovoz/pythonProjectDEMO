# Реализация стека в python

# Создаем стек
def create_stack():
    stack = []
    return stack

# Создаем пустой стек
def check_empty(stack):
    return len(stack) == 0

# Добавляем элементы в стек
def push(stack, item):
    stack.append(item)
    print("Добавлен элемент: " + item)

# Удаляем элементы из стека
def pop(stack):
    if check_empty(stack):
        return "Стек пуст"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(22))

print("Удаленный элемент: " + pop(stack))
print("Стек после добавления элемента: " + str(stack))