# instanciar objetos
from projeto.medico import Medico


medico = Medico()
medico.nome = input("digite seu nome: ")
medico.idade = input("digite sua idade: ")
medico.crm = input("digite seu crm: ")
medico.endereco,numero = input("digite o numero da residencia: ")

medico.mostrar_dados_funcionario()