
def introductuin_page() ->str:
    "Exibe a escolha "
    intro_message:str = """
Sistema Cadastral 

    * Cadastrar Pessoa - 1
    * Buscar Pessoa Por Nome - 2
    * Sair - 5
        """
    print(intro_message)
    command = input('Comando: ')
    return command
