def rede_conexoes(usuario, rede, visitados=None):
    if visitados is None:
        visitados = set()
    if usuario not in visitados:
        print(usuario)
        visitados.add(usuario)
        for colega in rede.get(usuario, []):
            rede_conexoes(colega, rede, visitados)