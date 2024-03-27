from collections import deque

def height(root):
    # Пустое дерево # имеет высоту 0
    if root is None:
        return 0

    # создает пустую queue и ставит в queue корневой узел
    queue = deque()
    queue.append(root)

    height = 0

    # Цикл # до тех пор, пока queue не станет пустой
    while queue:

        # вычисляет общее количество узлов на текущем уровне
        size = len(queue)

        # обрабатывает каждый узел текущего уровня и ставит их в queue.
        # непустые левый и правый потомки
        while size > 0:
            front = queue.popleft()

            if front.left:
                queue.append(front.left)

            if front.right:
                queue.append(front.right)

            size = size - 1

        # увеличивает высоту на 1 для каждого уровня
        height = height + 1

    return height
