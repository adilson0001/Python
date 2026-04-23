def contar_caminhos(n, m):
    if n == 1 or m == 1:
        return 1
    return contar_caminhos(n - 1, m) + contar_caminhos(n, m - 1)