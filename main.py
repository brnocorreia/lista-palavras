#pylint: disable=wildcard-import, undefined-variable
from src import *

def main():
    regulator = Regulator()
    while True:
        command = input()
        match command:
            case 'e':
                break
            
            case 'i':
                word = input().strip()
                regulator.insert_regulator(word)

            case 'l':
                lista = int(input())
                regulator.lister_general_regulator(lista)

            case 'x':
                number = int(input())
                regulator.lister_by_number_regulator(number)

            case 'o':
                init = input().strip()
                end = input().strip()
                regulator.lister_by_alphabetic_regulator(init, end)

            case 'r':
                pass

            case _:
                pass


if __name__ == "__main__":
    main()
