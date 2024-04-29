from Animal import *

class Usuario:
    def __init__(self, user_id):
        self.id = user_id
        self.animal_estimacao = None
        self.alimento_enviado = False
        self.objetivos = []
        self.objetivos_completos = []

    def chooseAnimalEstimacao(self, animal):
        self.animal_estimacao = animal
        print(f"Animal de estimação escolhido: {animal.getNome()}")


    #criar def para fazer o envio de alimentos e seus valores de status

    
    def getObjetivos(self):
        return self.objetivos


    #criar def de objetivos completos


# Exemplo de uso:
status_do_animal = Status(10, 50, 80, 70, 60)
animal1 = Animal(1, "Rex", status_do_animal)

usuario1 = Usuario(1)
usuario1.chooseAnimalEstimacao(animal1)
usuario1.sendAlimento()