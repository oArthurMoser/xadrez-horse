# Passeio do Cavalo - Usando Regra de Warnsdorff
# Link: https://www.quora.com/How-does-the-Warnsdorffs-algorithm-work

N = 8  # tamanho do tabuleiro (8x8)

# movimentos possíveis do cavalo
moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
moves_y = [1, 2, 2, 1, -1, -2, -2, -1]


def dentro_do_tabuleiro(x, y):
    return 0 <= x < N and 0 <= y < N


def contar_movimentos(x, y, tabuleiro):
    """Conta quantos movimentos válidos existem a partir de (x,y)."""
    count = 0
    for i in range(8):
        nx, ny = x + moves_x[i], y + moves_y[i]
        if dentro_do_tabuleiro(nx, ny) and tabuleiro[nx][ny] == -1:
            count += 1
    return count


def proximo_movimento(x, y, tabuleiro):
    """Escolhe o próximo movimento usando a heurística de Warnsdorff."""
    min_grau = 9
    next_x, next_y = -1, -1
    for i in range(8):
        nx, ny = x + moves_x[i], y + moves_y[i]
        if dentro_do_tabuleiro(nx, ny) and tabuleiro[nx][ny] == -1:
            grau = contar_movimentos(nx, ny, tabuleiro)
            if grau < min_grau:
                min_grau = grau
                next_x, next_y = nx, ny
    return next_x, next_y


def passeio_do_cavalo(x_inicial=0, y_inicial=0):
    # inicializa tabuleiro
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]

    # posição inicial
    x, y = x_inicial, y_inicial
    tabuleiro[x][y] = 1  # primeira posição é passo 1

    for passo in range(2, N * N + 1):
        x, y = proximo_movimento(x, y, tabuleiro)
        if x == -1 and y == -1:
            print("Não foi possível completar o passeio.")
            return None
        tabuleiro[x][y] = passo

    return tabuleiro


def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{cel:2}" for cel in linha))


if __name__ == "__main__":
    try:
        x = int(input("Digite a coordenada X inicial (1 a 8): ")) - 1
        y = int(input("Digite a coordenada Y inicial (1 a 8): ")) - 1

        if not (0 <= x < N and 0 <= y < N):
            print("Coordenadas inválidas! Digite valores entre 1 e 8.")
        else:
            tabuleiro = passeio_do_cavalo(x, y)
            if tabuleiro:
                imprimir_tabuleiro(tabuleiro)
    except ValueError:
        print("Entrada inválida! Digite números inteiros.")
