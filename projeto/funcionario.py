from abc import ABC, abstractmethod
from dataclasses import dataclass

from projeto.endereco import Endereco

@dataclass
class Funciomario(ABC):
    nome: str
    idade: int
    endereco: Endereco

    @abstractmethod
    def mostrar_dados_funcionario(self):
        pass