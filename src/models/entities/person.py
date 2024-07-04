from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    height: int

    def __repr__(self) -> str:
        return f"Nome: {self.name} |Idade: {self.age} anos| Altura: {self.height} cm."
    








class TestPersonClass:
    def __init__(self,person1:Person,person2:Person = None,person3:Person = None) ->None:
        self.person1 = person1
        self.person2 = person2
        self.person3 = person3


    def print_person(self) ->str:
        if self.person2 is None: 
            print(self.person1)
        elif self.person3 is None: 
            print(f'pessoa 1: {self.person1}\npessoa 2: {self.person2}')

p1 = Person("Amós",25,170)
p2 = Person("Victor",30,178)

teste = TestPersonClass(p1,p2)
teste.print_person()
