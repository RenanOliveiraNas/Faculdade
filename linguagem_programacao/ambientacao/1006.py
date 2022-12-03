valor = float(input('Valor do item: '))
quantidade = int(input('Quantidade: '))
total = quantidade * valor

desconto = total * 0.10
vlr_final = total - desconto
print(f'Total com desconto: R$ {vlr_final:.2f}')
