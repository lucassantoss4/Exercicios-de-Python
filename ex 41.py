idade = int(input('Ano de nascimento: '))

categoria = 2022 - idade

if categoria < 9:
    print("MIRIM")
elif categoria >9 and categoria <= 14:
    print('INFANTIL')
elif categoria > 14 and categoria <=19:
    print('Junior')
elif categoria ==20:
    print('SENIOR')
else:
    print('MASTER')