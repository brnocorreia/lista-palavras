#pylint: disable=wildcard-import, undefined-variable
from src import *

def main():
    regulator = Regulator()
    command = 'a'
    while command != 'e':
        command = input()
        match command:
            case 'e':
                break
            
            case 'i':
                word = input().strip()
                regulator.insert_controller(word)

            case 'l':
                lista = int(input())
                regulator.lister_general_controller(lista)

            case 'x':
                number = int(input())
                regulator.lister_by_number_controller(number)

            case 'o':
                init = input().strip()
                end = input().strip()
                regulator.lister_by_alphabetic_controller(init, end)

            case 'r':
                word = input().strip()
                regulator.remove_controller(word)

            case _:
                pass


if __name__ == "__main__":
    main()
