'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while. '''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for x in mașini:
    print(f'Mașina mea preferată este {x}')
print('Al 2 lea exemplu de for')
for i in range (0, len(mașini)):
    print(f'Mașina mea preferată este {mașini[i]}')
print('---------------While-----------')
i=0
while i <len(mașini):
        print(f'Mașina mea preferată este,{mașini[i]}')
        i += 1
'''
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.'''
print('---------------2----------------')
for i, masina in enumerate(mașini):
    if i==0 or i==len(mașini)-1 :
        continue
    mașini[i]=masina.upper()
    print(f' Mașina mea preferată este {mașini[i]}')
else:
    print(mașini)

'''3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘'''
print('---------3------------')
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for x in mașini:
    if x == 'Mercedes':
        print('am găsit mașina dorită de dvs')
        break
    else:
        print(f' Am gasit masina {x}, Mai cautam')

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.'''
print('-----------------4-----------------')
for masina in mașini:
    if masina=='Trabant' or masina=='Lăstun':
        continue
    else:
        print(f'S-ar putea să vă placă mașina {masina}')

'''5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.'''
print('------------5----------')
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi= []
for i in range (0, len(mașini)):
    if mașini[i]=='Lăstun' or mașini[i]=='Trabant':
        masini_vechi.append(mașini[i])
        mașini[i]='Tesla'
print(f'Masini noi : {mașini}')
print(f'Masini vechi : {masini_vechi}')


'''6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
print('----------------6--------------')
pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
buget=15000
for masina,pret in pret_masini.items():
    if pret<=buget:
        print(f'Pentru un buget sub {buget} euro, puteti alege masina: {masina}')
for masina in pret_masini:
    if pret_masini[masina] <= buget:
        print(masina)

'''7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

print('----------------7--------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s=0
for numar in numere:
    if numar==3:
        s+=1
print(f'Numarul 3 apare de {s} ori')

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''
print('----------------8--------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s=0
for numar in numere:
    s=s+numar
print(f'Suma numerelor din lista este: {s} ')

'''9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
print('----------------9--------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim=numere[numar]
for numar in numere:
    if numar > maxim:
        maxim=numar
print(f'Numarul cel mai mare din lista este: {maxim}')

'''10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă. '''

print('----------------10--------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
list1=[]
for numar in numere:
    if numar>0:
        list1.append(-numar)
    else:
        list1.append(numar)
print(list1)

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
Google.
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
print('----------optional 1--------')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar %2== 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar>0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'lista nr pare: {numere_pare}')
print(f'lista nr impare: {numere_impare}')
print(f'lista nr paozitive: {numere_pozitive}')
print(f'lista nr negative: {numere_negative}')

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4'''
print('----------optional 2--------')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
list2=[]
for numar in range(len(alte_numere)):
    mic=alte_numere[0]
    for numar in alte_numere:
        if numar<mic:
            mic=numar
    list2.append(mic)
    alte_numere.remove(mic)
print (f'Lista ordonata este: {list2}')

#sau alt mod
print('--------------------Alt mod optional 2--------------------------------')
print('\nE12 - Ordonati crescator lista de la E11 fara functia "sort"')
numere2 = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
aux = 0
for i in range(len(numere2)):
    for j in range(i + 1, len(numere2)):
        if numere2[i] > numere2[j]:
            aux = numere2[i]
            numere2[i] = numere2[j]
            numere2[j] = aux
print(f'\n{numere2}')

'''3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!'''

print('------------------------Optional 3--------------------------')
print('\nE13 - Ghicitoare de numar: genereaza un numar de la 1 la 30 si ghiceste-l cu un while.')
import random
numar_random = random.randint(1, 30)
print("numarul de ghicit e ", numar_random)
numar_ghicit=''
while numar_random != numar_ghicit:
    numar_ghicit = int(input('\nGhiceste numarul: '))
    if not numar_ghicit in range(1,31):
        print('Numarul trebuie sa fie intre 1 si 30!')
    elif numar_ghicit < numar_random:
        print('Nr secret e mai mare!')
    elif numar_ghicit > numar_random:
        print('Nr secret e mai mic!')
    else:
        print('Felicitari! Ai ghicit!')
'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333'''
print('---------Optional 4--------')
numar=int(input('Introduceti un nr: '))
for i in range(0,numar+1):
    print(str(i)*i)

''''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)'''

print('----------------------Optional 5----------------------------------')
print('\nE5 optional - tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]];'
      '\nCu un "nested for" printati: "Cifra curenta este x"')

tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta e {tastatura_telefon[i][j]}')
