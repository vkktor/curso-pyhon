from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca
from banco import Banco

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Victor', 21)
cliente3 = Cliente('Marcela', 26)
cliente4 = Cliente('Laura', 40)

conta1 = ContaPoupanca(1111, 254681, 0)
conta2 = ContaCorrente(2222, 254682, 0)
conta3 = ContaPoupanca(4444, 254683, 0)
conta4 = ContaCorrente(5555, 254684, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)
cliente4.inserir_conta(conta4)

banco.inserir_cliente(cliente1)
banco.inserir_cliente(cliente2)
banco.inserir_cliente(cliente3)
banco.inserir_cliente(cliente4)

banco.inserir_conta(conta1)
banco.inserir_conta(conta2)
banco.inserir_conta(conta3)
banco.inserir_conta(conta4)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(10)
    cliente1.conta.sacar(10)
else:
    print('Cliente não autenticado.')

print('######################################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(10)
else:
    print('Cliente não autenticado.')

print('######################################')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(10)
    cliente3.conta.sacar(10)
else:
    print('Cliente não autenticado.')

print('######################################')

if banco.autenticar(cliente4):
    cliente4.conta.depositar(10)
    cliente4.conta.sacar(10)
else:
    print('Cliente não autenticado.')
