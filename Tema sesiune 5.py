# 1. Functie care sa calculeze si sa returneze suma a 2 numere

def suma_nr(a,b):
    suma=a+b
    return suma
print(suma_nr(2,6)),

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
print('------------EX2------------')
def par_impar(x):
    if x%2==0:
        print('nr este par')
    else:
        print('Nr este impar')
par_impar(4)
par_impar(5)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
print('------------EX3------------')
def carcactere_nume_complet(nume,prenume,nume_mijlociu):
    nr_caractere=len(nume)+len(prenume)+len(nume_mijlociu)
    return nr_caractere
print(carcactere_nume_complet('Ilies','Alexandru','Adrian'))

# 4. Functie care returneaza aria dreptunghiului
print('------------EX4------------')
def aria_dreptunghi(lungime,latime):
    aria=lungime*latime
    return aria
print(f'Aria dreptunghiului este: {aria_dreptunghi(2,5)}')

# 5. Functie care returneaza aria cercului
print('------------EX5------------')
def aria_cerc(raza):
    aria=3.141592653589793*raza*raza
    return aria
print(f'Aria cercului este: {aria_cerc(3.14)}')

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
print('------------EX6------------')
def gaseste_carcater(text):
    carcacter=text.count('x')
    if carcacter !=0:
        return True
    else:
        return False
print(gaseste_carcater('Am castigat de 3x fata de cat am cheltuit'))

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case exte y
print('------------EX7------------')
def lower_upper(text):
    lower=0
    upper=0
    for litera in text:
        if litera.islower():
            lower+=1
        else:
            upper+=1
    print(f'Nr de caractere lower case este {lower}')
    print(f'Nr de caractere upper case este {upper}')
print(lower_upper('Trei iezi CUcuIEti'))

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
print('------------EX8------------')
def lista_nr(list):
    lista_nr_poz=[]
    for i in list:
        if i >0:
            lista_nr_poz.append(i)
    return lista_nr_poz
print(lista_nr([-10,5,-5,1,2,3]))

# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# -	Numerele sunt egale.
print('------------EX9------------')
def no_return(x,y):
    if x>y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif y>x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print(f'Numerele sunt egale')
print(no_return(3,5))
print(no_return(3,3))
print(no_return(13,5))

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
print('------------EX10-----------')
def numar_set(numar,set):
    if numar not in set:
        set.add(numar)
        print(f'Am adaugat numarul nou in set {set}')
        return True
    else:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
print(numar_set(1,{1,2,3}))
print(numar_set(13,{1,2,3}))


# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
print('------ex11------------')
from calendar import monthrange
def number_of_days_in_month(year, month):
    return monthrange(year, month)[1]
print(number_of_days_in_month(2023, 3))

#  12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
print('---------------Ex 12----------------')
def calculator(x,y):
    suma=x+y
    diferenta=x-y
    inmultirea=x*y
    impartirea=(x/y)
    return suma,diferenta,inmultirea,impartirea

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

'''
13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare litera
'''
lista1 = [1, 1, 2, 7, 7, 7]

def count(lista):
    cnt = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in cnt.keys():
        for j in lista:
            if i == j:
                cnt[i] = cnt[i] + 1
    return cnt

print(count(lista1))

# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
print('------------EX14-----------')
def val_max(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
print(val_max(3,2,1))
print(val_max(11,12,13))
print(val_max(10,30,20))

#15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
#Ex: daca dam nr 3
#Suma va fi 6 (0+1+2+3)
print('------------EX15-----------')
def suma_nr(x):
    suma=0
    for i in range(0,x+1):
        suma+=i
    return suma
print(suma_nr(2))
print(suma_nr(3))

#16. Funcție care primește 2 liste de numere (numerele pot fi dublate).Returnati numerele comune
print('------------EX16-----------')
def nr_comune(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3
print(nr_comune([1,1,2,3],[2,2,3,4]))

#17. Functie care sa aplice o reducere de pret
'''Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalid'''
print('---------Ex17----------')
def reducere_pret(val_produs,reducere):

    if val_produs>0 and reducere<100:
        pret_final=val_produs-(reducere/100*val_produs)
        return pret_final
    else:
        return ('Reducere invalida')
print(reducere_pret(100,10))
print(reducere_pret(100,120))

#18. Functie care sa afiseze data si ora curenta din ro.(bonus: afisati si data si ora curenta din China)
print('------------Ex 18-----------')
from datetime import datetime, timedelta, timezone
def data_ora_curenta():
    now = datetime.now()
    print(f"Data si ora curenta in Romania: {now}")
    print(f"Data si ora curenta in China: {now + timedelta(hours=5)}")
data_ora_curenta()

# 19. Functie care sa afiseze cate zile mai sunt pana la ziua ta /
# sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
print('---------Ex19-------')
import datetime
def ziua_mea_de_nastere(year,month, day):
    my_birthday=datetime.date(year,month,day) -datetime.date.today()
    return my_birthday.days
print(ziua_mea_de_nastere(2023,3,13))