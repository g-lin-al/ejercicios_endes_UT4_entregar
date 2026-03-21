import random

DEPURAR: bool = True
MINA: str = "M"
FALLO: str = "X"
VACIO: str = "-"
ACIERTO_TAB: str = "O"
TAMANIO_MAX: int = 10
TAMANIO_DEF: int = 5


def establecer_minas(tab):
    contador: int = 0
    num_minas: int = 0
    longitud_tab: int = 0
    longitud_tab = len(tab[0])
    print(longitud_tab) if DEPURAR else None
    num_minas = round(longitud_tab * longitud_tab * 0.1)
    print(num_minas) if DEPURAR else None
    while contador < num_minas:
        x = random.randrange(longitud_tab)
        y = random.randrange(longitud_tab)
        if tab[x][y] == VACIO:
            tab[x][y] = MINA
            contador += 1

    return num_minas


def jugar(tab, num_minas):
    fin_juego: bool = False
    num_minas_total = num_minas * 2
    while num_minas_total > 0 and not fin_juego:
        long = len(tab[0])
        print("  ", " ".join([str(x) for x in range(long)]))
        for x in range(long):
            print(x, " ", end='')
            for y in range(long):
                if tab[x][y] != MINA:
                    print(tab[x][y], "", end="")
                else:
                    print(VACIO, "", end="")
            print("")

        posicion_x = int(input("Posición x?"))
        posicion_y = int(input("Posición y?"))
        acierto = None
        if tab[posicion_x][posicion_y] == MINA:
            tab[posicion_x][posicion_y] = ACIERTO_TAB
            acierto = True
        else:
            tab[posicion_x][posicion_y] = FALLO
            acierto = False
        if not acierto:
            num_minas_total -= 1
            print(num_minas_total) if DEPURAR else None
        else:
            fin_juego = True if MINA not in [i for item in tab for i in item] else False
    if fin_juego:
        print("Has ganado")
    else:
        print("Has perdido")


def mostrar_tablero(tab):
    longitud_linea: int = len(tab[0])
    print("  ", " ".join([str(x) for x in range(longitud_linea)]))
    for x in range(longitud_linea):
        print(x, " ", end='')
        for y in range(longitud_linea):
            print(tab[x][y], "", end="")
        print("")


tablero: list[list[str]] = []
tamanio = int(input("Establecer número de celdas (máx 10): "))
tamanio = tamanio if tamanio <= TAMANIO_MAX else TAMANIO_DEF
tablero = [[VACIO for _ in range(tamanio)] for _ in range(tamanio)]
numero_minas = establecer_minas(tablero)
mostrar_tablero(tablero) if DEPURAR else None
print(tablero) if DEPURAR else None
jugar(tablero, numero_minas)
