# Refactorizar

import random

DEPURAR = False
MINA = "M"
FALLO = "X"
VACIO = "-"
ACIERTO = "O"


def minas(t):
    cm = nm = l = 0
    l = len(t[0])
    print(l) if DEPURAR else None
    nm = round(l * l * 0.1)
    print(nm) if DEPURAR else None
    while cm < nm:
        x = random.randrange(l)
        y = random.randrange(l)
        if t[x][y] == VACIO:
            t[x][y] = MINA
            cm += 1

    return nm


def juego(t, nm):
    f = False
    nm_t = nm * 2
    while nm_t > 0 and not f:
        long = len(t[0])
        print("  ", " ".join([str(x) for x in range(long)]))
        for x in range(long):
            print(x, " ", end='')
            for y in range(long):
                if t[x][y] != MINA:
                    print(t[x][y], "", end="")
                else:
                    print(VACIO, "", end="")
            print("")

        posicion_x = int(input("Posición x?"))
        posicion_y = int(input("Posición y?"))
        acierto = None
        if t[posicion_x][posicion_y] == MINA:
            t[posicion_x][posicion_y] = ACIERTO
            acierto = True
        else:
            t[posicion_x][posicion_y] = FALLO
            acierto = False
        if not acierto:
            nm_t -= 1
            print(nm_t) if DEPURAR else None
        else:
            f = True if MINA not in [i for item in t for i in item] else False
    if f:
        print("Has ganado")
    else:
        print("Has perdido")


def MostrarTablero(t):
    ll = len(t[0])
    print("  ", " ".join([str(x) for x in range(ll)]))
    for x in range(ll):
        print(x, " ", end='')
        for y in range(ll):
            print(t[x][y], "", end="")
        print("")


tablero = []
tamanio = int(input("Número de celdas (máx 10?"))
tamanio = tamanio if tamanio <= 10 else 5
tablero = [[VACIO for _ in range(tamanio)] for _ in range(tamanio)]
numero_minas = minas(tablero)
MostrarTablero(tablero) if DEPURAR else None
print(tablero) if DEPURAR else None
juego(tablero, numero_minas)
