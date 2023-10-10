##pylint: disable=eval-used

from src.models.lista import Lista


class Sorter:
    def __init__(self) -> None:
        pass
    
    def sort_list(self, lista: Lista, context: str):
        p = lista.head

        while p:
            min_node = p
            next_node = eval(f'p.{context}_next')

            while next_node:
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = eval(f'next_node.{context}_next')
            
            p.value, min_node.value = min_node.value, p.value
            p = eval(f'p.{context}_next')

        return lista
