from src.views.people_register_view import PeopleRegisterView
from src.controller.people_register_controller import PeopleRegisterController


def people_register_constructor() -> bool:
    people_register_view = PeopleRegisterView()
    people_register_controller = PeopleRegisterController()

    new_person_information = people_register_view.registry_person_view()
    response = people_register_controller.register(new_person_information)

    if (response["sucess"]):
        people_register_view.register_person_sucess(response["message"])   
    else: 
        people_register_view.register_person_fail(response["error"])
        
    register_or_not = people_register_view.register_or_menu()
    return register_or_not
