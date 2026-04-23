def decodificar_mensagem(s):
    print(s)
    if len(s) > 1:
        decodificar_mensagem(s[1:])