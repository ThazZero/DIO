menu = '''
===================================
Banco Python

1 - Depositar
2 - Sacar
3 - Saldo
4 - Extrato
5 - Trocar de conta
6 - Cadastrar conta
7 - Sair
===================================
'''

class Conta:
    def __init__(self, numero: int, titular: str):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
        self.__extrato = []
        self.__saques_realizados = 0

    def depositar(self, valor: float):
        self.__saldo += valor
        self.__extrato.append(f'Depósito: R${valor:.2f}')
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')

    def sacar(self, valor: float, maximo_valor_saque: float, maximo_quantidade_saques: int):
        if self.__saldo < valor:
            print('Saldo insuficiente!')
            return
        
        if valor > maximo_valor_saque:
            print(f'Valor máximo para saque: R${maximo_valor_saque:.2f}')
            return
        
        if self.__saques_realizados >= maximo_quantidade_saques:
            print(f'Quantidade máxima de saques diários atingida: {maximo_quantidade_saques}')
            return
    
        self.__saldo -= valor
        self.__extrato.append(f'Saque: R${valor:.2f}')
        self.__saques_realizados += 1

        print(f'Saque de R${valor:.2f} realizado com sucesso!')


    def saldo(self):
        print(f'Saldo: R${self.__saldo:.2f}')

    def extrato(self):
        print('Extrato:')
        for item in self.__extrato:
            print(item)

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

class Banco:
    def __init__(self):
        self.__maximo_valor_saque = 500
        self.__maximo_quantidade_saques = 3

        self.__contas = []

    def __buscar_conta(self, numero: int):
        for conta in self.__contas:
            if conta.numero == numero:
                return conta

        return None
    
    def cadastrar_conta(self):
        titular = input('Digite o nome do titular: ')
        n = len(banco._Banco__contas) + 1
        conta = Conta(n, titular)
        banco._Banco__contas.append(conta)
        print(f'Conta criada com sucesso! Número: {n}')

    def depositar(self, valor: float, numero: int):
        conta = self.__buscar_conta(numero)
        if conta is None:
            print('Conta não encontrada!')
            return

        conta.depositar(valor)
    
    def sacar(self, valor: float, numero: int):
        conta = self.__buscar_conta(numero)
        if conta is None:
            print('Conta não encontrada!')
            return

        conta.sacar(valor, self.__maximo_valor_saque, self.__maximo_quantidade_saques)

    def saldo(self, numero: int):
        conta = self.__buscar_conta(numero)
        if conta is None:
            print('Conta não encontrada!')
            return

        conta.saldo()

    def extrato(self, numero: int):
        conta = self.__buscar_conta(numero)
        if conta is None:
            print('Conta não encontrada!')
            return

        conta.extrato()

banco = Banco()
numero = None

while True:
    if numero is None:
        if len(banco._Banco__contas) == 0:
            print('Nenhuma conta cadastrada!')
            print('Cadastre uma conta para continuar...')
            banco.cadastrar_conta()

        print('Contas disponíveis:')
        for conta in banco._Banco__contas:
            print(f'Número: {conta._Conta__numero} | Titular: {conta._Conta__titular}')
        
        n = int(input('Digite o número da conta: '))
        conta = banco._Banco__buscar_conta(n)
        if conta is None:
            print('Conta não encontrada!')
            continue
        
        numero = n
        print(f'Bem vindo(a), {conta._Conta__titular}!')

    print(menu)
    
    opcao = input('Digite uma opção: ')

    if opcao == '1':
        valor = float(input('Digite o valor a ser depositado: '))
        banco.depositar(valor, numero)
    elif opcao == '2':
        valor = float(input('Digite o valor a ser sacado: '))
        banco.sacar(valor, numero)
    elif opcao == '3':
        banco.saldo(numero)
    elif opcao == '4':
        banco.extrato(numero)
    elif opcao == '5':
        print('Trocando de conta...')
        numero = None

    elif opcao == '6':
        banco.cadastrar_conta()
        numero = None

    elif opcao == '7':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
