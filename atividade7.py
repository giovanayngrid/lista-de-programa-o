#atividade7
print('Bem-vindo ao Hipermercado Tabajara!')
print('Lembre-se:')
print('Promoção válida para apenas 1 tipo de carne por cliente')
print('Cartão tabajara garante 5% de desconto')
print('Boas Compras!')

carne=input('qual carne você quer comprar? ')
kgscarne=float(input('Quantos kgs de carne você comprou? '))
pagamento=input('qual será a forma de pagamento? ')

if carne =='file duplo':
    if kgscarne <= 5:
       valor=45.00 * kgscarne
    else:
       valor=58.00 *kgscarne

if carne=='alcatra':
    if kgscarne <= 5:
       valor=kgscarne * 59.00
    else:
       valor=kgscarne * 68.00
 
if carne=='picanha':
    if kgscarne<=5:
     valor=kgscarne * 69.00
    else:
     valor=kgscarne * 78.00

if pagamento=='cartão tabajara':
   total=valor-(5/100)
elif pagamento=='dineheiro'or'cartão de credito'or'cartão de debito'or'pix':
   total=valor

print('Cupom fiscal:')
print('Tipo de carne escolhida:', carne)
print('Quantidade de kgs:', kgscarne,'Kg')
print('Valor:R$', valor)
print('forma de pagamento:', pagamento)
print('Valor total com desconto:R$', total)
