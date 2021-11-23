from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from utils.helper import formata_float_str_moeda

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=================================')
    print('========== Bank of Python =======')
    print('=================================')
    print()
    print('--------- Menu de Opções ---------')
    print('[1] - Criar Conta')
    print('[2] - Efetuar Saque')
    print('[3] - Efetuar Depósito')
    print('[4] - Efetuar Tranferência ')
    print('[5] - Listar Contas')
    print('[6] - Sair do Sistema')
    print('----------------------------------')
    print()
    opc = int(input('Digite a opção desejada : '))

    if opc == 1:
        criar_conta()
    elif opc == 2:
        efetuar_saque()
    elif opc == 3:
        efetuar_deposito()
    elif opc == 4:
        efetuar_tranferencia()
    elif opc == 5:
        listar_contas()
    elif opc == 6:
        sleep(1)
        print('-----------------------')
        sleep(1)
        print(' -- - - - - Obrigado por Utilizar o Bank of Python - - - - -- - --')
        sleep(1)
        print('Bye Bye')
        sleep(1)
        exit(1)
    else:
        print(' - - - - Opção Inválida - - - - - ')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('========== Bank of Python =======')
    sleep(1.5)
    print(' - - - - Criação de Conta - - - - - ')
    sleep(1)
    nome: str = input('- Informe o nome completo do titular da Contas : >')
    email: str = input('- Informe o e-mail do titular da conta : >')
    cpf: str = input('- Informe o CPF do titular da conta : >')
    dt_nasc: str = input('- Informe a data de nascimento do titular da conta (ex 01/01/2021 : >')
    cliente: Cliente = Cliente(nome, email, cpf, dt_nasc)
    conta: Conta = Conta(cliente)
    contas.append(conta)
    sleep(2)
    print(f' - - - - Cadastro realizado em {cliente.dt_cadastro} com SUCESSO!!!')
    sleep(0.5)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        sleep(1)
        print('------- Saque da Conta -------')
        sleep(1)
        numero: int = int(input('- Informe o número da Conta : > '))
        conta: Conta = procura_conta(numero)
        if conta:
            valor: float = float(input('Informe o valor que deseja sacar : R$ '))
            conta.sacar(valor)
            menu()
        else:
            print(f' - - Desculpe, não encontramos a conta nº {numero}')
            listar_contas()
    else:
        print('Ainda não existem contas cadastradas!!')
        sleep(1.5)
        criar_conta()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta para o depósito : > '))
        conta: Conta = procura_conta(numero)
        if conta:
            vlr: float = float(input(f'Informe o valor que deseja depositar na conta nº{numero} : > '))
            conta.depositar(vlr)
            menu()
        else:
            print(f' - - Desculpe, não encontramos a conta nº {numero}')
            listar_contas()
    else:
        print('Não existem contas cadastradas em nosso banco de dados!!!')
        criar_conta()


def efetuar_tranferencia() -> None:
    if len(contas) > 0:
        num_o= int(input('Informe o número da conta sua conta : > '))
        conta_o: Conta = procura_conta(num_o)
        num_d = int(input('Informe o número da conta de destino: > '))
        conta_d: Conta = procura_conta(num_d)
        if conta_d:
            valor = float(input('Digite o valor que deseja tranferir : R$ '))
            opc = int(input(f'Deseja realmente transferir {formata_float_str_moeda(valor)} para a conta nº {num_d}\n'
                            f'em nome de {conta_d.cliente.nome} :? \n'
                            f'[1] - sim \n[2] - Não\n >>>'))
            if opc == 1:
                conta_o.trasferir(conta_d, valor)
                sleep(2)
                print('Tranferência realizada com sucesso !!')
                sleep(1)
                menu()

            elif opc == 2:
                print(' - - Efetuando o cancelamento da transferência ....')
                sleep(1)
                menu()

            else:
                print('Opção inválida !!!')

        else:
            print(f' - - Desculpe, não encontramos a conta nº {num}')
            listar_contas()

    else:
        print('Não existem contas cadastradas em nosso banco de dados!!!')
        criar_conta()


def listar_contas() -> None:
    if len(contas) > 0:
        for conta in contas:
            print('----------------------')
            print(f'Número da Conta : {conta.numero}')
            print(f'Nome : {conta.cliente.nome}')
            print(f'Saldo : R$ {conta.saldo}')
            print(f'Limite : R$ {conta.limite}')
            print(f'Saldo Total : R$ {conta.saldo_total}')
            print(f'---------------------------')
            sleep(1)
    else:
        sleep(1)
        print('Não há nenhuma conta em nosso banco de dados ainda !!!')
        sleep(1)
    menu()


def procura_conta(num: int) -> Conta:
    cont: Conta = None

    if len(contas) > 0:
        print(' - - - - - Checando os dados no Registro ... - - - - ')
        sleep(2.5)
        for conta in contas:
            if conta.numero == num:
                cont = conta
        print(f'Busca realizada com sucesso !! \n {cont}\n'
              f'---------------------------------')
        sleep(1)

        return cont
    else:
        print("Ainda não há nenhhum registro em nosso banco de dados")
        menu()


if __name__ == '__main__':
    main()
