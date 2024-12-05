from dataclasses import dataclass

from projeto.funcionario import Funciomario


@dataclass
class Medico(Funciomario):
    crm: str
    def mostrar_dados_funcionario(self):
        return "mostrando os dados do medico"