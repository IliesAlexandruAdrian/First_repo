# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
print('-------------Ex 1 Clasa Cerc------------')
class Cerc:
    raza= '4'
    culoare='alb'

    def __init__(self, raza, culoare):
        self.raza=raza
        self.culoare=culoare

    def descrie_cerc(self):
        print(f'Raza este: {self.raza}')
        print(f'Culoarea este: {self.culoare}')

    def aria(self,raza,pi):
        pi=3.14
        self.aria=raza*raza*pi
        print(f'Aria cercului este: {self.aria}')

    def diametru(self,raza):
        self.diametru=raza*2
        print(f'Diametrul cercului este: {self.diametru}')

    def circumferinta(self,raza):
        self.circumferinta=2*raza*3.14
        print(f'Circumferinta cercului este: {self.circumferinta}')
cerc1=Cerc(66,'red')
cerc2=Cerc(100, 'yellow')
cerc1.descrie_cerc()
cerc2.descrie_cerc()
cerc1.aria(4,3.14)
cerc2.diametru(3)
cerc1.circumferinta(2)

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().
print('-------------Ex 2 Clasa Dreptunghi------------')
class Dreptunghi:
    def __init__(self, latime, lungime, culoare):
        self.latime= latime
        self.lungime = lungime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea: {self.lungime}  si latimea {self.latime} , de culoare {self.culoare}')

    def aria(self, lungime, latime):
        self.aria=lungime*latime
        print(f'Aria dreptunghiului este: {self.aria}')

    def perimetru(self,lungime,latime):
        self.perimetru=2*lungime +2*latime
        print(f'Perimetrul dreptunghiului este: {self.perimetru}')

    def change_culoare(self,noua_culoare):
        self.culoare=noua_culoare

dreptunghi1=Dreptunghi(2,3,'red')
dreptunghi2=Dreptunghi(4,5,'pink')
dreptunghi1.aria(2,6)
dreptunghi1.perimetru(5,3)
dreptunghi1.descrie()
print('------------------')
dreptunghi2.descrie()
dreptunghi2.change_culoare('black')
dreptunghi2.descrie()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
print('-------------Ex 3 Clasa Angajat------------')
class Angajat:
    def __init__(self,nume,prenume,salariu):
        self.nume=nume
        self.prenume=prenume
        self.salariu=salariu

    def descrie(self):
        print(f'Numele angajatului este:: {self.nume}  si prenumele: {self.prenume} , cu salariul de: {self.salariu} Euro')

    def nume_complet(self):
        print(f'Numele complet este: {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este: {self.salariu} Euro')

    def salariu_anual(self):
        print(f'Salariul anual este: {12*self.salariu}')

    def marire_salariu(self, marire):
        self.salariu*=1+marire/100
        print(f'Salut {self.nume} {self.prenume}! aveti o marire de salariu de {marire} % , aveti acum un salariu lunar de {self.salariu} Euro')
angajat1=Angajat('Hagi', 'Gica',100000)
angajat1.nume_complet()
angajat1.descrie()
angajat1.salariu_lunar()
angajat1.marire_salariu(20)
angajat1.salariu_anual()
angajat1.descrie()

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
print('-------------Ex 4 Clasa Cont------------')
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold

    def afisare_sold(self):
        print (f'Titularul {self.titular_cont} are in contul {self.iban}, {self.sold} Ron')

    def debitare_cont(self,suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'Buna {self.titular_cont}, ati retras suma de {suma} Ron, din contul {self.iban}, mai aveti {self.sold} Ron')
        else:
            print('Fonduri insuficiente')

    def creditare_cont(self, suma):
        self.sold+=suma
        print(f'Buna {self.titular_cont}, ati depus suma de {suma} Ron, din contul {self.iban}, aveti {self.sold} Ron')

cont1=Cont('Ro001', 'Ion', 10000)
cont2=Cont('Ro002', 'Vasile', 20000)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.afisare_sold()
cont2.debitare_cont(1000)
cont1.creditare_cont(550)

#Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
'''1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/'''
print('----------------Ex 5 --------------')
from datetime import date
today = date.today()
print("Today date is: ", today)
from datetime import datetime
now = datetime.now()
print("now = ", now)
