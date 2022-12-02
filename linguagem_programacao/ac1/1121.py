preco = float(input())
quantidade = int(input())

total = preco * quantidade
desconto = total * (10 + quantidade)/100
vlr_final = total - desconto

print(f'{total:.2f}')
print(f'{vlr_final:.2f}')
