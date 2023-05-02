"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass
 #-----------------------------------------------------
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass
 #-----------------------------------------------------
class Animal:
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass

# Nova versão: ---------------------------------------------------

class AnimalDB:

    def save(self, animal: Animal):
        #Salva animal no DB
        return

class Animal:
    def __init__(self, name: str):
        self.__name = name
        self.__banco_de_dados = AnimalDB()
    
    def get_name(self) -> str:
        return self.__name

    def save(self):
        self.__banco_de_dados.save(animal = self)
        return