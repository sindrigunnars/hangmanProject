class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        ret_str = ''
        temp = self.head
        while temp != None:
            ret_str += str(temp.data)
            temp = temp.next
        return ret_str

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.size += 1

class Leaderboard:
    def __init__(self, file):
        self.file = file
        self.data = {}
        for line in self.file:
            name, score = line.strip().split(';')
            self._insert(name, score)

    def _insert(self, name, score):
        if score not in self.data:
            self.data[score] = LinkedList()
        self.data[score].insert(name)

    def __str__(self):
        count = 0
        ret_str = ''
        for key, value in reversed(sorted(self.data.items())):
            temp = value.head
            while temp != None:
                count += 1
                ret_str += f'{temp.data}: {key}\n'
                temp = temp.next
                if count == 10: break
            if count == 10: break
        return ret_str.strip()

with open('leaderboard.csv') as ldr:
    node = Leaderboard(ldr)
    print(node)
    # for key, value in sorted(node.data.items()):
    #     print(f'{key}, {value}')
