from models.models import *

def DD():
    pass

def RC(nome, plano):
    if cliente_existe(nome):
        raise Exception("Cliente existente.")
    if plano not in ("STANDARD", "PREMIUM", "PACK", "CANCELADO"):
        raise Exception("Plano inexistente.")
    iden = sum([ord(c) for c in nome])
    loja.registar_cliente(Cliente(nome, getattr(loja, plano.lower()), iden))
    print(f"Cliente registado com identificador {iden}.")

def RP(nome):
    if familia_existe(nome):
        raise Exception("Família existente.")
    iden = sum([ord(c) for c in nome])
    loja.registar_familia(Familia(nome, iden))

def RS(nome):
    if serie_existe(nome):
        raise Exception("Série existente.")
    iden = sum([ord(c) for c in nome])
    loja.registar_serie(Serie(nome, iden))
    print(f"Série registada com o identificador {iden}.")

def RE():
    pass

def AP():
    pass

def CP():
    pass

def AF():
    pass

def DF():
    pass

def ES():
    pass

def EC():
    pass

def LP():
    for c in loja.clientes:
        print(c)

def LF():
    pass

def LS():
    pass

def LSA():
    pass

def LSAF():
    pass

def AS():
    pass

def CA():
    pass

def cliente_existe(nome):
    if not loja.clientes.is_empty():
        for c in loja.clientes:
            if c.nome == nome:
                return True
    return False

def familia_existe(nome):
    if not loja.familias.is_empty():
        for c in loja.familias:
            if c.nome == nome:
                return True
    return False

def serie_existe(nome):
    if not loja.series.is_empty():
        for c in loja.series:
            if c.nome == nome:
                return True
    return False

loja = Loja()