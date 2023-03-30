# b.1. O variabila este o zona din memorie care tine date, valori

# b.2. Declarare si initializare variabile string,integer, float si boolean
mancare = 'ciorba'
feluri_mancare = 3
pret = 30.99
multumire = True

# b.3. Functia type
print(type(mancare))
print(type(feluri_mancare))
print(type(pret))
print(type(multumire))

# b.4. Rotunjire float si supra scriere
pret=round(pret)
print(pret)
print(type(pret))

# b.5. Print 4 propozitii cu variabile
print(f'Azi am mancat {mancare}')
print(f'Am avut {feluri_mancare} feluri')
print(f'Am platit {pret} lei')
print(f'Am fost {multumire} multumit')

# b.6. citire de la tastatura si nr caractere
nume =input('introdu Numele: ')
prenume = input('introdu Prenumele: ')
print('Numele complet are:' ,len(nume + prenume) , 'caractere')

# b.7. citire tastatura si afisare arie
lungime =int(input('Introdu lungimea: '))
latime =int(input('Introdu latimea: '))
print('Aria dreptunghiului este : ' , lungime*latime)

# b.8. Count
citat = 'Coral is either the stupidest animal or the smartest rock'
print(citat.count('the'))

# b.9. upper the
print(citat.replace('the', 'THE'))

# b.10. Assert
assert not citat.isdigit() is True

