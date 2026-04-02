def calcularNota():
    n1 = float(input('N1:'))
    n2 = float(input('N2:'))
    n3 = float(input('N3:'))
    media = (n1+n2+n3) / 3
    if media < 6:
        rec = float(input('Nota da rec:' ))
        media = (media + rec)/2
        return media
#main
m = calcularNota
if m >- 6:
    print('aprovado')
else:
    print('Reprovado')
