"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __str__(self):
#         return f"Your queue is good!"
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self) == 0:
#             return None
#         else:
#             dequeued_item = self.storage[0]
#             self.storage.pop(0)
#             return dequeued_item

class Node: 
    def __init__(self, value = None, next_node = None ):
        self.value = value
        self.next_node = next_node 

class Queue:
    def __init__(self):
        self.size = 0
        self.first_node = None

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        my_node = Node(value)

        if self.first_node == None:
            self.first_node = my_node
            return 

        current_node = self.first_node

        while current_node.next_node != None:
            current_node = current_node.next_node

        current_node.next_node = my_node

    def dequeue(self):
        if self.size == 0:
            return None

        value = self.first_node.value

        self.first_node = self.first_node.next_node
        self.size -= 1

        return value