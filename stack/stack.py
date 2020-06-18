"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             # .pop in Python, accepts an index as a parameter,
#             # if no param is given, it defauls to -1 (the last index)
#             return self.storage.pop()

#         else:
#             return None

class Node: 
    def __init__(self, value = None, next_node = None ):
        self.value = value
        self.next_node = next_node 

class Stack:
    def __init__(self):
        self.size = 0
        self.first_node = None

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        new_node = Node(value)

        if self.first_node == None:
            self.first_node = new_node
            return self.first_node

        current_node = self.first_node

        while current_node.next_node != None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def pop(self):
        if self.size == 0:
            return None

        current_node = self.first_node

        if self.first_node.next_node == None:
            self.size = 0
            self.first_node = None
            return current_node.value

        prior_node = self.first_node
        current_node = self.first_node.next_node

        while current_node.next_node != None:
            new_prior_node = current_node
            current_node = current_node.next_node
            prior_node = new_prior_node

        prior_node.next_node = None
        self.size -= 1

        return current_node.value