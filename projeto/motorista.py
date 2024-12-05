from dataclasses import dataclass
from projeto.funcionario import Funcionario


@dataclass
class Motorista(Funcionario):
    cnh: str

    def  mostrar_dados_funcionario(self):
        pass