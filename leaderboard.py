class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    '''Fairly standard Linked List where insert is the 
    only function required'''
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
    def __init__(self, file, name, display_limit = 10):
        '''Main function of init is taking leaderboard file
        and inserting into data structure where score is key
        and username is value, average takes username as key
        and list of scores as value'''
        self.file = file
        self.name = name
        self.data = {}
        self.average = {}
        self.display_limit = display_limit
        for line in self.file:
            name, score = line.strip().split(';')
            self._insert(name, int(score))

    def _insert(self, name, score):
        '''Inserts into appropriate data structures'''
        if name not in self.average:
            self.average[name] = []
        if score not in self.data:
            self.data[score] = LinkedList()
        self.data[score].insert(name)
        self.average[name].append(score)

    def __str__(self):
        '''Returns string in correct format, displays selected
        number of top scores and average scores for the user'''
        self.count = 0
        ret_str = 'Leaderboard:\n'
        for key, value in reversed(sorted(self.data.items())):
            temp = value.head
            while temp != None:
                self.count += 1
                ret_str += f'\t{temp.data}: {key}\n'
                temp = temp.next
                if self.count == self.display_limit: break
            if self.count == self.display_limit: break
        if self.name in self.average:
            ret_str += f'{self.name}, your average score is {int(sum(self.average[self.name]) / len(self.average[self.name]))}'
        else:
            ret_str += f'{self.name}, you have no saved scores'
        return ret_str

    # for key, value in sorted(node.data.items()):
    #     print(f'{key}, {value}')
