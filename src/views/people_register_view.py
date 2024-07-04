from typing import Dict
import os


class PeopleRegisterView:
    def registry_person_view(self) ->Dict:
        os.system('cls||clear')
        print('Cadastrar Nova Pessoa \n\n')
        name = input('Determine o nome da pessoa: ')
        age = input('Determine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')
        new_person_information = {
            "name": name, "age" : age, "height": height
        }
        return new_person_information
    
    def register_person_sucess(self,message:Dict) ->None:
        os.system('cls||clear')
        success_message = f"""
    Usuário cadastrado com sucesso! 

        Tipo: { message["type"] }
        Registros: { message["count"] }
        Infos: 
            Nome: {message["attributes"]["name"]}
        """
        print(success_message)

    def register_or_menu(self) -> bool:
        answer = input('Deseja cadastrar mais um usuário ou retornar ao menu\n(1-> Sim | 2-> Não): ')
        answer = answer.lower()
        choice = {
            '1': True,'2':False
        }
        
        print(choice[answer],type(choice[answer]))
        return choice[answer]
    
    def register_person_fail(self,error:str) ->None:
        os.system('cls||clear')
        fail_message = f"""
                Falha ao cadastrar o usuário! 

                Error: { error }
                
        """
        print(fail_message)
