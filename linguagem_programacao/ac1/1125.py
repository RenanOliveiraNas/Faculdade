trabalhos = float(input())
prova = float(input())

media = (trabalhos + prova) / 2
if media >= 6:
    print('Aprovado')
else:
    media = (trabalhos + 10) / 2
    if media >= 6.0:
        print('talvez com a sub')
    else:
        print('reprovado')
    
