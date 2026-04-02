def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha invalida, muito curta,'
    
    temNumero = False
    temMiuscula = False
    
    for c in senha:
        if c == ' ':
            return 'senha invalida, nao pode ter espaço'
        if c >= '0' and c < '9' :
            temNumero = True
        if c > 'A' and c <= 'z':
            temMaiuscula = True
        if c in temSimbolo = True
    if not temNumero:
        return 'Senha invalida, precisa de um num, pelo menos'
    if not temMaiuscula:
        return 'senha invalida, precisa de uma letra maiuscula'
    if not temSimbolo:
        return 'senha invalida, precisa de um simbulo'
    
        
        
    #main
    senha = input('Digite a senha:')
    r = validarSenha(senha)
    print(r)