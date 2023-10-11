import copy

from src.models.lista import Lista
from src.utils.sorter import Sorter


class Regulator:
    def __init__(self) -> None:
        self.lista_1 = Lista()
        self.lista_2 = Lista()
        self.lista_3 = Lista()
        self.lista_4 = Lista()
        self.sort = Sorter()

    def insert_regulator(self, word: str):
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
    
    def lister_general_regulator(self, lista: int):
        match lista:
            case 1:
                copy_list = copy.deepcopy(self.lista_1)
                self.sort.sort_list(copy_list, 'basic')
                copy_list.display()
            
            case 2:
                copy_list = copy.deepcopy(self.lista_2)
                self.sort.sort_list(copy_list, 'basic')
                copy_list.display()
            
            case 3:
                copy_list = copy.deepcopy(self.lista_3)
                self.sort.sort_list(copy_list, 'basic')
                copy_list.display()
            
            case 4:
                copy_list = copy.deepcopy(self.lista_4)
                self.sort.sort_list(copy_list, 'general')
                copy_list.display_all()
    
    def lister_by_number_regulator(self, number: int):
        copy_list = copy.deepcopy(self.lista_4)
        self.sort.sort_list(copy_list, 'general')
        copy_list.display_by_number(number)

    def lister_by_alphabetic_regulator(self, init: str, end: str):
        copy_list = copy.deepcopy(self.lista_4)
        self.sort.sort_list(copy_list, 'general')
        copy_list.display_by_alphabetic(init, end)

    def remove_regulator(self, word: str):
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