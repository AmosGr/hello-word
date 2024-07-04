from src.main.constructor.introtuction_process import introduction_process
from src.main.constructor.people_finder_constructor import people_finder_constructor
from src.main.constructor.people_register_constructor import people_register_constructor

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': 
            register_or_not = True
            while register_or_not:
                if register_or_not:
                    register_or_not = people_register_constructor()
                    
        elif command == '2': people_finder_constructor()
        elif command == '5': exit()
        else: print('\nComando não encontrado! \n\n')
