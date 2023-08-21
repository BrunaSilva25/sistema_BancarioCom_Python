
class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    
    def saque(self, valor):
        if valor > 0 and valor <= 500 and len(self.saques) < 3 and self.saldo >= valor:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif self.saques_diarios >= 3:
            print("Voce já excedeu o limite de três saques diários!")    
        elif valor > 500:
            print("O limite maximo de saque por operacao é R$ 500,00.")    
        else:
            print("Saque não permitido.")
    
    def extrato(self):
        print("Extrato:")
        for dep in self.depositos:
            print(f"Depósito: R$ {dep:.2f}")
        for saq in self.saques:
            print(f"Saque: R$ {saq:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")


# Função para exibir o menu e processar as opções
def exibir_menu():
    print("\nMenu:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


# Testando o sistema com o menu interativo
banco = Banco()

while True:
    opcao = exibir_menu()
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        banco.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        banco.saque(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
