from typing import Dict
import os

class PeopleFinderView:
    def find_person_view(self) ->Dict:
        os.system('cls||clear')
        print('Buscar Pessoa \n\n')
        name = input('Determine o nome da pessoa pra busca: ')
        person_finder_informations = {
            "name": name
        }
        return person_finder_informations
    
    def find_person_sucess(self,message:Dict) ->None:
        sucess_messsage = f"""
            Usuário encontrado com sucesso! 

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                Nome: {message["infos"]["name"]}
                Idade: {message["infos"]["age"]} anos
                Altura: {message["infos"]["height"]} cm
        """
        print(sucess_messsage)
    
    def find_person_fail(self,error:str) ->None:
        fail_message = f"""
            Falha ao encontrar usuário! 

            Error: {error}
        """
        print(fail_message)