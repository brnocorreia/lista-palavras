from src.models.lista import Lista
from src.utils.sorter import Sorter


class Regulator:
    def __init__(self) -> None:
        self.lista_1 = Lista()
        self.lista_2 = Lista()
        self.lista_3 = Lista()
        self.lista_4 = Lista()
        self.sort = Sorter()

    def insert_controller(self, word: str):
        length = len(word)
        if length <= 5:
            self.insert(word, self.lista_1)

        elif 5 < length <= 10:
            self.insert(word, self.lista_2)
        
        else:
            self.insert(word, self.lista_3)
        
    def insert(self, word: str, lista: Lista):
        res, node = lista.basic_insert(word)
        if res == False:
            return print(f'palavra ja existente: {word}')
        
        res, _ = self.lista_4.general_insert(node)
        return print(f'palavra inserida: {word}')
    
    def lister_general_controller(self, lista: int):
        match lista:
            case 1:
                self.sort.sort_list(self.lista_1, 'basic')
                self.lista_1.display()
            
            case 2:
                self.sort.sort_list(self.lista_2, 'basic')
                self.lista_2.display()
            
            case 3:
                self.sort.sort_list(self.lista_3, 'basic')
                self.lista_1.display()
            
            case 4:
                self.sort.sort_list(self.lista_4, 'general')
                self.lista_1.display_all()
    
    def lister_by_number_controller(self, number: int):
        self.sort.sort_list(self.lista_4, 'general')
        self.lista_4.display_by_number(number)

    def lister_by_alphabetic_controller(self, init: str, end: str):
        self.sort.sort_list(self.lista_4, 'general')
        self.lista_4.display_by_alphabetic(init, end)

    def remove_controller(self, word: str):
        length = len(word)
        if length <= 5:
            self.remove(word, self.lista_1)
        elif 5 < length < 10:
            self.remove(word, self.lista_2)
        else:
            self.remove(word, self.lista_3)
    
    def remove(self, word: str, lista: Lista):
        res = lista.basic_remove(word)
        if not res:
            return print(f'palavra inexistente: {word}')

        res = self.lista_4.general_remove(word)
        return print(f'palavra removida: {word}')