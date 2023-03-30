''' 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
 a) Afiseaz-o '''
note_muzicale=['do','re','mi','fa', 'sol','la', 'si' ,'do']
print(note_muzicale)
''' b) Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata) '''
note_muzicale=note_muzicale[::-1]
print(note_muzicale)

'''c)Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială '''
note_muzicale.reverse()
print(note_muzicale)

# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
print(note_muzicale.count('do'))

# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
list1=[3, 1, 0, 2]
list2=[6, 5, 4]
list3=list1+list2
print(list3)
list1.extend(list2)
print(list1)

''' 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
folosind o functie si apoi afiseaza din nou lista '''
list1.sort()
list1.remove(0)
print(list1)

''' 5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)'''
if len(list3)==0:
    print('Lista e goala')
else:
    print('Lista nu e goala')

# 6. Foloseste o functie care sa goleasca lista de la exercitiul 3
list3.clear()
print(list3)

''' 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
afiseze ca lista e goala'''
if len(list3)==0:
    print('Lista e goala')
else:
    print('Lista nu e goala')

''' 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
afisezi Elevii (cheile)'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

''' 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie'''
x=int(dict1.get('Ana'))
print(f'Ana a luat nota {x}')
y=int(dict1.get('Gigel'))
print(f'Gigel a luat nota {y}')
z=int(dict1.get('Dorel'))
print(f'Dorel a luat nota {z}')

''' 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
- Modifica nota lui Dorel in 6
- Printeaza nota lui dupa modificare'''
dict1['Dorel']=6
print(dict1)
print(dict1.get('Dorel'))

''' 11. Imagineaza-ti ca Gigel se transfera din clasa.
- Cauta o functie care sa il stearga
Vine un coleg nou.
- Adaugati-l in lista pe Ionica, cu nota 9
- Printati dictionarul cu noii elevi'''
dict1.pop('Gigel')
dict1['Ionica']=9
print(dict1)

''' 12. Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.'''

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt) #Nu apre duplicat ziua de luni

'''13. Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean'''

if weekend.issubset(zile_sapt):
    print(True)
else:
    print(False)

''' 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
sunt in weekend si invers)'''

print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

''' 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
ambele seturi). Hint: Va puteti folosi de o functie'''

print(zile_sapt.intersection(weekend))


''' Optionale
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python”'''

SCHIMBARI_MAXIME = 3
lista_jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
lista_jucatori_rezerva = ['j6','j7','j8','j9','j10']
lista_jucatori_scosi = []
# calculam si initializam schimbari ramase
schimbari_ramase = SCHIMBARI_MAXIME - len(lista_jucatori_scosi)
jucator_in = 'j6'
jucator_out = 'j1'

# daca jucatorul e in teren SI daca mai am schimbari
if jucator_out in lista_jucatori_teren and schimbari_ramase > 0:
    if jucator_in in lista_jucatori_rezerva and jucator_in not in lista_jucatori_teren: # eliminam cazul cand jucatorul este deja in teren
        lista_jucatori_teren.remove(jucator_out)  # scoatem jucatorul
        lista_jucatori_scosi.append(jucator_out)
        lista_jucatori_teren.append(jucator_in)  # adaugam jucatorul nou
        lista_jucatori_rezerva.remove(jucator_in)
        schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
        print(f'Schimbare efectuata cu succes!')
        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai ai schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {lista_jucatori_teren}')
print(f"Jucatorii care au fost scosi sunt: {lista_jucatori_scosi}")