a=str(input('Digite algo:'))

print(a, ' é do tipo: ', type(a))
print('é númerico? {}'.format(a.isnumeric()))
print('é alfabético? {}'.format(a.isalpha()))
print('é decimal? {}'.format(a.isdecimal()))
print('é alfanumérico? {}'.format(a.isalnum()))
print('é digit? {}'.format(a.isdigit()))