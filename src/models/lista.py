from .node import Node

class Lista:
    def __init__(self) -> None:
        self.head = None

    def __consult__(self, word: str):
        p = self.head
        while p is not None:
            if p.value == word:
                return True
            p = p.basic_next
        return False

    def basic_insert(self, word: str):
        res = self.__consult__(word)
        if res:
            return False, word
        
        p = Node(word)
        p.basic_next = self.head
        self.head = p

        return True, p

    def general_insert(self, p: Node):
        p.general_next = self.head
        self.head = p
        return True, p.value
    
    def display(self):
        if not self.head:
            return print('lista vazia')
        p = self.head
        while p:
            print(p.value)
            p = p.basic_next

    def display_all(self):
        if not self.head:
            return print('lista vazia')
        p = self.head
        while p:
            print(p.value)
            p = p.general_next
    
    def display_by_number(self, number: int):
        hasMatch = False
        p = self.head
        while p:
            if len(p.value) == number:
                hasMatch = True
                print(p.value)
            p = p.general_next
        if not hasMatch:
            print('lista vazia')
        
    def display_by_alphabetic(self, init: str, end: str):
        hasMatch = False
        p = self.head
        while p:
            if init <= p.value[0] and p.value[0] <= end:
                hasMatch = True
                print(p.value)
            p = p.general_next
        if not hasMatch:
            print('lista vazia')
