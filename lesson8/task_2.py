# Задание-2
# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from collections import deque


class MyTree:
    def __init__(self, node, left, right, code, is_root):
        self.node = node
        self.left = left
        self.right = right
        self.code = code
        self.is_root = is_root

    def __repr__(self):
        return f'{self.node}'

    def check_node(self, value):
        if self.left == value:
            return '0'
        if self.right == value:
            return '1'
        return None

    def add_code(self, value):  # здесь будем добавлять '0' или '1', чтобы использовать при формированиикода символа
        self.code = value


def build_tree(d):                                  # строим дерево
    new_tree = MyTree(None, None, None, None, None)
    for i in range(len(d)-1):
        d = deque(sorted(d, key=lambda x: x[1]))   # сортируем новые узлы по возрастанию частоты
        left_val = d[0][0]                         # формирование нового узла
        right_val = d[1][0]
        node_val = d[0][1] + d[1][1]
        new_tree = MyTree(node_val, left_val, right_val, None, None)
        d.popleft()                                # извлекаем старые  узлы
        d.popleft()
        d.appendleft([new_tree, new_tree.node])    # добавляем новый узел дерева и его новый 'вес'
    new_tree.is_root = True  # корень дерева
    return new_tree


def show_tree(tree):
    if hasattr(tree, 'node'):
        print(f"tree.node = {tree.node}")
        print(f"tree.left = {tree.left}")
        print(f"tree.right = {tree.right}")
        if hasattr(tree.left, 'node'):
            print("left:")
            show_tree(tree.left)
        if hasattr(tree.right, 'node'):
            print("right:")
            show_tree(tree.right)


def build_way(tree):                             # строим все пути из '0' и '1'
    if hasattr(tree.left, 'node'):
        if tree.is_root:                          # от самой вершины идем влево
            tree.add_code('0')
        tree.add_code('0')                       # добавляем коды '0' и '1' в дерево
        build_way(tree.left)
    if hasattr(tree.right, 'node'):
        if tree.is_root:                          # от самой вершины идем вправо
            tree.add_code('1')
        tree.add_code('1')                        # добавляем коды '0' и '1' в дерево
        build_way(tree.right)


def build_code(tree, b):                        # генерируем код символа и записываем его в словарь
    global code_values                          # таблица кодов

    if tree.check_node(b) is not None:          # нашли искомый символ в дереве
        code_values[b] += tree.check_node(b)    # записываем в какой ветке(0/1)
        return
    elif tree.code is not None:                # еще не нашли символ, но есть код пути в дереве, по которому идем (0/1)
        code_values[b] += tree.code
    if hasattr(tree.left, 'node'):
        build_code(tree.left, b)
    if hasattr(tree.right, 'node'):
        build_code(tree.right, b)


def check_way(tree):                          # смотрим какие символы в левом/правом поддереве (от корня)
    global symbols_side
    if isinstance(tree.right, str):
        symbols_side.append(tree.right)
    if isinstance(tree.left, str):
        symbols_side.append(tree.left)
    if hasattr(tree.left, 'node'):
        check_way(tree.left)
    if hasattr(tree.right, 'node'):
        check_way(tree.right)


s = input("Введите строку: ")
symbols = Counter()
d = deque()                             # очередь из списков для хранения частоты символов
for each in s:                          # и 'веса' новых узлов дерева
    symbols[each] += 1
for each in symbols:
    d.append([each, symbols[each]])
res_tree = build_tree(d)                # строим дерево
code_values = {key: '' for key in s}    # таблица кодов Хаффмана
build_way(res_tree)                     # строим все пути из '0' и '1'
symbols_side = []
check_way(res_tree.left)               # записываем символы из левого поддерева
for each in symbols_side:              # строим коды для символов из левого поддерева
    code_values[each] = '0'            # первый ход в левое поддерево
    build_code(res_tree.left, each)
symbols_side.clear()
check_way(res_tree.right)              # записываем символы из правого поддерева
for each in symbols_side:              # строим коды для символов из правого поддерева
    code_values[each] = '1'            # первый ход в правое поддерево
    build_code(res_tree.right, each)
print(f"code_values = {code_values}")
print("Закодированная строка:")
for each in s:                         # выводим результат кодировки
    print(f"{code_values[each]}", end=' ')
