# Setarea listei de cuvinte si selectia aleatorie a unui cuvant din lista
import random

listaCuvinte = ['PALARIE', 'DEGET', 'PICIOR', 'ABECEDAR', 'CER', 'VALIZA', 'PARALELOGRAM', 'COLUMBIA']
cuvant = list(str(random.choice(listaCuvinte)))
ascuns = []
for character in cuvant:
    ascuns.append('_')

incercari = 0
incercari_maxime = 7

# Bucla pana la castigare sau pierderea jocului
joculRuleaza = True
while joculRuleaza:

    # Afisare evolutie (omuletul, litere ghicite, incercari ramase)
    print('     -------')
    print('     |     |')
    print('     |    ' + (' O' if incercari > 0 else ''))
    print('     |    ' + ('/' if incercari == 2 else ('/|\\' if incercari > 2 else '')))
    print('     |    ' + (' |' if incercari > 3 else ''))
    print('     |    ' + ('/' if incercari == 5 else ('/ \\' if incercari > 5 else '')))
    print('     |  ' + ('Game Over' if incercari > 6 else ''))
    print('     |    ')
    print('-----------------')
    print(f'Mai ai {incercari_maxime - incercari} incercari ramase')  # Contorizare incercari ramase
    print('\n')
    print(f'Cuvantul este: {" ".join(ascuns)}')  # Afisarea cuvantului cu spatiere intre litere
    print('\n')

    # Solicitare introducere caracter
    ''''''
    literaIntrodusa = input('Te rog incearca o litera :').upper()
    print('\n')
    if literaIntrodusa in cuvant:
        print(f'Bravo! Litera  {literaIntrodusa}  există în cuvânt')
        for i in range(len(cuvant)):
            character = cuvant[i]
            if character == literaIntrodusa:
                ascuns[i] = cuvant[i]
                cuvant[i] = '_'
    else:
        print(f'Litera  {literaIntrodusa}  nu există în cuvânt')
        incercari += 1

    # Mesaj daca a castigat
    if all('_' == char for char in cuvant):
        print('Felicitari! Ai castigat.')
        joculRuleaza = False

    # Mesaj daca a pierdut
    if incercari >= incercari_maxime:
        print('Ai pierdut! Incearca din nou')
        joculRuleaza = False
