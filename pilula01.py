def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha inválida: muito curta'

    temNumero = False
    temMaiuscula = False
    temSimbolo = False

    for c in senha:
        if c == ' ':
            return 'Senha inválida: não pode conter espaço'

        if c >= '0' and c <= '9':
            temNumero = True

        if c >= 'A' and c <= 'Z':
            temMaiuscula = True

        if not c.isalnum():  # símbolo (não é letra nem número)
            temSimbolo = True

    if not temNumero:
        return 'Senha inválida: precisa de pelo menos um número'

    if not temMaiuscula:
        return 'Senha inválida: precisa de pelo menos uma letra maiúscula'

    if not temSimbolo:
        return 'Senha inválida: precisa de pelo menos um símbolo'

    return 'Senha válida ✅'


# main
senha = input('Digite a senha: ')
resultado = validarSenha(senha)
print(resultado)
