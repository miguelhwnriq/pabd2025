class Conta:
    def __init__(self, cliente, agencia, numero, pix, saldo): 
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self.pix = pix
        self.saldo = saldo
        
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(self.saldo < valor):
            print('deu bom')
            return False
        else:
            print('deu ruim')
            self.saldo -= valor
            return True
        self.saldo -= valor

    def extrato(self):
        print(f'Nome: {self.cliente.nome}\ncpf: {self.cliente.cpf} \nagencia: {self.agencia}\nnumero: {self.numero}\npix: {self.pix}\nsaldo: {self.saldo:.2f}')

    def transfere(self, destino, valor):
        if(self.saca(valor)):
            destino.deposita(valor)
            return True
        else:
            print('sem saldo')
            return False   
        