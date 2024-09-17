class Conta:
    def __init__ (self,conta:int,agencia:int) ->None:
        self.conta = conta 
        self.agencia = agencia 
        self._saldo = 0 

    def depositar(self,valor):
        self._saldo += valor 

    def sacar (self,valor):
        self._saldo -= valor