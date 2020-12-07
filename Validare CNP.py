from datetime import datetime
import locale

# valid = 'CNP este valid'
# gresit = 'CNP este invalid'
# cod_validare = [279146358279]
# if len(CNP) != 13:
#     print('Lungimea CNP este gresită')
# else:
#     print(valid)
#
# cnp = (1, 7, 7, 0, 8, 2, 6, 0, 4, 3, 5, 4)
# cod_validare = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
# print(sum(x * y for x, y in zip(cnp, cod_validare)) % 11)
#
# import datetime


# print(datetime.datetime.now())


cnp = str(input('Introduceti un CNP: '))

an = cnp[1:3]
luna = cnp[3:5]
zi = cnp[5:7]
judet = cnp[7:9]
numar_ordine = cnp[9:12]
cod_verificare = cnp[12]

print(an, luna, zi, judet, numar_ordine, cod_verificare)

# data_string = str('19' + an + '-' + luna + '-' + zi)
# data_object = datetime.strptime(data_string, '%Y-%m-%d').date()
# print(data_object)
#
# formatare_RO = ['ro_RO.utf-8']
# for loc in formatare_RO:
#     locale.setlocale(locale.LC_ALL, loc)
#     print(data_object.strftime('%d %B %Y').title()) # printat in format RO
