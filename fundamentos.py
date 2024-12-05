# herança
# polimorfismo

# objetivo:
# reaproveitamento de codigo

#exemplo
from abc import ABC

# serve como modelo para outras classes
class pessoa(ABC): 
    # atributo é uma variavel dentro de uma classe
    nome: str # atributo nome
    idade: int  # atributo idade

    # POLIMORFISMO
    #função é igual a methodo
    @abstractmethod
    def deveres(self):
        pass

# HERANÇA
class Aluno(pessoa):
    ra: str
    #POLIMOFISMO
    def deveres(self):
        return "estudar"
# HERANÇA
class Professor(pessoa):
    matricula: str

    # POLIMORFISMO
    def deveres(self):
        return "ensinar"
# instanciano objetos
aluno = Aluno()
aluno.nome = input("digite seu nome: ")
aluno.ra = input("digite seu R.A: ")

professor = Professor()
professor.nome = input("digite se nome: ")