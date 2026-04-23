def explorar_salas(sala, mapa, visitadas=None):
    if visitadas is None:
        visitadas = set()
    if sala not in visitadas:
        print(sala)
        visitadas.add(sala)
        for conexao in mapa.get(sala, []):
            explorar_salas(conexao, mapa, visitadas)