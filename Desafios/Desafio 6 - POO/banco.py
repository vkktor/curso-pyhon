
class Banco:
    def __init__(self):
        self._agencias = [1111, 2222, 3333]
        self._clientes = []
        self._contas = []

    @property
    def agencias(self):
        return self._agencias

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
