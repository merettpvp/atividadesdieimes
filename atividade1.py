class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def ver_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')


# Exemplo de uso da classe ContaBancaria
conta_exemplo = ContaBancaria(titular='João')

conta_exemplo.depositar(1000)
conta_exemplo.sacar(500)
conta_exemplo.ver_saldo()

conta_exemplo.sacar(700)  # Tentativa de saque com saldo insuficiente
conta_exemplo.ver_saldo()
