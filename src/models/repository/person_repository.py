from src.models.entities.person import Person

class PersonRepository:
    def __init__(self) -> None:
        self.__people:list[Person] = []
    
    def registry_person(self,person:Person) ->None:
        self.__people.append(person)
    
    def find_person_by_name(self,name:str) ->Person:
        for person in self.__people:
            if person.name == name:
                return person
        return None
    
person_repository = PersonRepository()