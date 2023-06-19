menu = '''
===================================
Banco Python

1 - Depositar
2 - Sacar
3 - Saldo
4 - Extrato
5 - Sair
===================================
'''

class Banco:
    def __init__(self):
        self.__maximo_valor_saque = 500
        self.__maximo_quantidade_saques = 3
        self.__saques_realizados = 0

        self.__saldo = 0
        self.__extrato = []

    def depositar(self, valor: float):
        self.__saldo += valor
        self.__extrato.append(f'Depósito: R${valor:.2f}')
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
    
    def sacar(self, valor: float):
        if self.__saldo < valor:
            print('Saldo insuficiente!')
            return
        
        if valor > self.__maximo_valor_saque:
            print(f'Valor máximo para saque: R${self.__maximo_valor_saque:.2f}')
            return
        
        if self.__saques_realizados >= self.__maximo_quantidade_saques:
            print(f'Quantidade máxima de saques diários atingida: {self.__maximo_quantidade_saques}')
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


banco = Banco()

while True:
    print(menu)
    opcao = input('Digite uma opção: ')

    if opcao == '1':
        valor = float(input('Digite o valor a ser depositado: '))
        banco.depositar(valor)
    elif opcao == '2':
        valor = float(input('Digite o valor a ser sacado: '))
        banco.sacar(valor)
    elif opcao == '3':
        banco.saldo()
    elif opcao == '4':
        banco.extrato()
    elif opcao == '5':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
