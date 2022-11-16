# numero =  int(input('\nbase de conversão:\n 1-binario\n 2-octal \n 3-hexadecimal \nQual será a conversão Digite:'))
'''
- 1 para binário;
- 2 para octal;
- 3 para hexadecimal.
'''

#  CORREÇÃO DO GUANABARA 
num = int(input('Digete um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:                                                          # V isso é o fatiamento, ele vai começar a mostrar apartir da 3 terceira posicao 
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
   print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[:2])) 
else:
    print('Escolha INVALIDA! ')