from aed_ds.lists.singly_linked_list import *

class Familia:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.id = identificador

class Serie:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.id = identificador

class Temporada:
    def __init__(self):
        pass

class Episodio:
    def __init__(self):
        pass

class Cliente:
    def __init__(self, nome, plano, identificador):
        self.nome = nome
        self.plano = plano
        self.id = identificador
        self.familia = None

    def trocar_plano(self, plano):
        self.plano = plano

    def __str__(self):
        return f"{self.plano} {self.nome}"

class Loja:
    def __init__(self):
        self.clientes = SinglyLinkedList()
        self.familias = SinglyLinkedList()
        self.series = SinglyLinkedList()
        self.standard = Plano("STANDARD", 4)
        self.premium = Plano("PREMIUM", 7)
        self.pack = Plano("PACK", 4)
        self.cancelado = Plano("CANCELADO", 0)

    def registar_cliente(self, cliente):
        self.clientes.insert_last(cliente)

    def registar_familia(self, familia):
        self.familias.insert_last(familia)

    def registar_serie(self, nome, identificador):
        self.nome = nome
        self.id = identificador

    def mostrar_familias(self):
        return self.familias

    def mostrar_clientes(self):
        return self.clientes

class Plano:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo

    def __repr__(self):
        return self.nome