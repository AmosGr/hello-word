from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PeopleRegisterController:
    def register(self,new_person_information:Dict) ->Dict:
        try:
            self.__validate_fields(new_person_information)
            self.__save_person(new_person_information)
            response = self.__format_response(new_person_information)
            return {"sucess": True, "message": response}
        except Exception as exception: 
            return {"sucess": False, "error": str(exception)}

    def __validate_fields(self,new_person_information:Dict) -> None:
        if not isinstance(new_person_information['name'],str):
            raise Exception('Campo Nome Incorreto ')
        try:int(new_person_information['age'])
        except: raise Exception('Campo Idade Incorreto')
        try:int(new_person_information['height'])
        except: raise Exception('Campo Altura Incorreto')

    def __save_person(self,new_person_information:Dict):
        name = new_person_information["name"]
        age = new_person_information["age"]
        height = new_person_information["height"]

        new_person = Person(name,age,height)
        person_repository.registry_person(new_person)

    def __format_response(self,new_person_information:Dict) ->None:
        return {
            "count":1,
            "type": "Person",
            "attributes":new_person_information
        }