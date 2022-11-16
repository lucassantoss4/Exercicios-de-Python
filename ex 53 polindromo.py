frase = str(input("Digite uma frase: ")).strip().upper() # strip: tira os espaços e upper: deixa a letra grande 
dicio_frase = frase.split()
junto = ''.join(dicio_frase)
inverso = ''
for frase in range (len(junto)-1,-1,-1):
    inverso += junto[frase]
    print(junto,inverso, end ='')
    