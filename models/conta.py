from time import sleep

from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:
    cod: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.cod
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 150
        self.__saldo_total: float = self._calcula_saldo_total
        self.__extrato = []
        Conta.cod += 1

    def __str__(self: object) -> str:
        return f"---------------------------------------------------\n" \
               f"- Número da Conta : {self.numero} \n- Cliente : {self.cliente.nome} " \
               f"\n- Saldo em conta : {formata_float_str_moeda(self.saldo)}\n- Limite disponível: {formata_float_str_moeda(self.saldo_total)}\n" \
               f"- Saldo Total Disponível : {self._calcula_saldo_total}" \
               f"\n---------------------------------------------------"

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, vlr: float) -> None:
        self.__limite = self.limite - vlr  # no setter não usa retorno

    @property
    def saldo_total(self: object):
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def extrato(self: object):
        return self.__extrato

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.limite + self.saldo

    def depositar(self: object, valor: float) -> None:
        if self.limite < 150:
            self.limite += valor
            if self.limite > 150:
                rest = self.limite - 150
                self.saldo += rest
                print(f'O Valor R$ {valor} foi Depositado com Sucesso !!!')
        elif valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print(f'O Valor R$ {valor} foi Depositado com Sucesso !!!')

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:

            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                print(f'O valor de R$ {valor} foi sacado com sucesso!!')
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                print(f'Saque de R$ {valor} Realizado com Sucesso !!')

        else:
            print('Saque não realizado!!!')
            sleep(1)
            print('Saldo Insulficiente!!!')

    def trasferir(self: object, destino: object, valor: float) -> None:

        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = destino._calcula_saldo_total
                print('Tranferência realizada com sucesso!')
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
                print('Transferência Realizada com Sucesso !!')
        else:
            print('Tranferência não realizada, Tente novamente!!')
