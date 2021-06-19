from controllers.controllers import *

def main():
    while True:
        command = str(input("\nDefinir data atual - [DD]\n"
                        "Registar cliente - [RC]\n"
                        "Registar família - [RP]\n"
                        "Registar série - [RS]\n"
                        "Registar episódio - [RE]\n"
                        "Alterar plano - [AP]\n"
                        "Cancelar plano - [CP]\n"
                        "Associar cliente a família - [AF]\n"
                        "Desassociar cliente de família - [DF]\n"
                        "Eliminar série, temporada, ou episódio - [ES]\n"
                        "Eliminar cliente - [EC]\n"
                        "Listar clientes - [LP]\n"
                        "Listar famílias - [LF]\n"
                        "Listar séries - [LS]\n"
                        "Listar séries alugadas [LSA]\n"
                        "Listar séries alugadas por família - [LSAF]\n"
                        "Alugar série - [AS]\n"
                        "Cancelar aluguer - [CA]\n"
                        ">>> ")).upper().strip()
        if command.startswith("DD"):
            DD()
        elif command.startswith("RC"):
            command = command.split(" ")
            RC(command[1], command[2])
        elif command.startswith("RP"):
            command = command.split(" ")
            RP(command[1])
        elif command.startswith("RS"):
            command = command.split(" ", 1)
            RS(command[1])
        elif command.startswith("RE"):
            RE()
        elif command.startswith("AP"):
            AP()
        elif command.startswith("CP"):
            CP()
        elif command.startswith("AF"):
            AF()
        elif command.startswith("DF"):
            DF()
        elif command.startswith("ES"):
            ES()
        elif command.startswith("EC"):
            EC()
        elif command.startswith("LP"):
            LP()
        elif command.startswith("LF"):
            LF()
        elif command.startswith("LS"):
            LS()
        elif command.startswith("LSA"):
            LSA()
        elif command.startswith("LSAF"):
            LSAF()
        elif command.startswith("AS"):
            AS()
        elif command.startswith("CA"):
            CA()
        else:
            raise Exception("Instrução inválida.")
