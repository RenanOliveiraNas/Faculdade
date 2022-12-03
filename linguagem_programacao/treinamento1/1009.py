nome = input()
salario = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
vlr_total = salario + comissao
print(f'TOTAL = R$ {vlr_total:.2f}')
