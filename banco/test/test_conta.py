import pytest

from banco.models.conta import Conta


@pytest.fixture 
def conta_valida():
    return Conta (123,556)
    
def test_verificando_atributo_numero_da_conta(conta_valida):
    assert conta_valida.conta == 123

def test_verificando_atributo_agencia_da_conta(conta_valida):
    assert conta_valida.agencia == 556

def test_verificando_atributo_saldo(conta_valida):
    assert conta_valida._saldo == 0 

def test_verificando_deposito_da_conta(conta_valida):
    conta_valida.depositar(100)
    assert conta_valida._saldo == 100

def test_verificando_sacar_valor_possitivo(conta_valida):
    conta_valida.depositar(100)
    conta_valida.sacar(100)
    assert conta_valida._saldo == 0
    
