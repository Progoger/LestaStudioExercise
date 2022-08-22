class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link


class Queue:
    def __init__(self):
        self._head = Node()

    def __str__(self):
        tmp = self._head
        if not tmp.value:
            return '[]'
        res = ']'
        while tmp:
            res = ', ' + str(tmp.value) + res
            tmp = tmp.link
        res = '[' + res[2:]
        return res

    def add(self, value):
        if not self._head.value:
            self._head.value = value
        else:
            tmp = self._head
            self._head = Node(value, tmp)

    def pop(self):
        tmp = self._head
        while tmp.link.link:
            tmp = tmp.link
        res = tmp.link
        tmp.link = None
        return res


class Node2:
    def __init__(self, value=None, prev=None, follow=None):
        self.prev = prev
        self.value = value
        self.follow = follow


class Queue2:
    def __init__(self):
        self._head = Node2()
        self._tail = Node2()

    def __str__(self):
        tmp1 = self._head
        tmp2 = self._tail
        if not tmp1.value:
            return '[]'
        elif tmp1 == tmp2:
            return '[' + str(tmp1.value) + ']'
        else:
            res1 = ''
            res2 = ''
            while tmp1 != tmp2 and (tmp1.prev is None or tmp1.prev != tmp2):
                res1 = ', ' + str(tmp1.value) + res1
                res2 = res2 + str(tmp2.value) + ', '
                tmp2 = tmp2.prev
                tmp1 = tmp1.follow

            if tmp1 == tmp2:
                res1 = str(tmp1.value) + res1
            elif tmp1.prev == tmp2:
                res1 = res1[2:]
            return '[' + res2 + res1 + ']'

    def add(self, value):
        if not self._head.value:
            self._head.value = value
            self._tail = self._head
        elif self._head == self._tail:
            self._head = Node2(value, follow=self._tail)
            self._tail.prev = self._head
        else:
            tmp = self._head
            self._head = Node2(value, follow=tmp)
            tmp.prev = self._head

    def pop(self):
        res = self._tail
        if self._tail == self._head:
            self._tail = Node2()
            self._head = Node2()
        else:
            self._tail = self._tail.prev
            self._tail.follow = None
        return res


"""
Первая реализация хороша, во-первых своей простотой, во-вторых, довольно малым объёмом памяти, по сравнению со второй. 
По сути это односвязный список выполненный в виде очереди.
Вторая реализация быстрее первой, но имеет минус в плане обёма занимаемой памяти по сравнению с первым способом.
По сути это двусвязный список выполненный в виде очереди
"""
