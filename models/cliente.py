from datetime import date
from utils.helper import date_para_str, str_para_date


class Cliente:
    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, dt_nasc: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__dt_nasc: date = str_para_date(dt_nasc)
        self.__dt_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def dt_nasc(self: object) -> str:
        return date_para_str(self.__dt_nasc)

    @property
    def dt_cadastro(self: object) -> str:
        return date_para_str(self.__dt_cadastro)

    def __str__(self:object):
        return f"Código:  {self.codigo} \nNome: {self.nome} \nEmail: {self.email} " \
               f"\nData Nascimento : {self.dt_nasc} \nData de Cadastro: {self.dt_cadastro}"
