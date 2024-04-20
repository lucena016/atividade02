class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser maior que zero.')

    def mostrar_saldo(self):
        print(f'Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}')


conta = ContaBancaria(numero_conta='123456', titular='João da Silva', saldo=1000)
conta.mostrar_saldo()

conta.depositar(500) 
conta.mostrar_saldo()  

conta.sacar(200) 
conta.mostrar_saldo()  

conta.sacar(1500)  

