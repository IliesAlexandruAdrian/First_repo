
''' 1. if else  functioneaza in felul urmator:
Daca se indeplineste conditia dupa if se trece mai departe si se executa codul altfel (else) se executa cealalta varianta
'''

print(random.randint(0,9))

# 2. Nr natural

x=int(input('Introdu nr x:'))
if x >=0 :
    print('nr natural')
else:
    print('nr nu e natural')

#3. Nr pozitiv negativ sau neutru
if x==0:
    print('nr neutru')
elif x<0:
    print('nr negativ')
else:
    print('nr pozitiv')

# 4. interval [-2 13]
if x>=-2 and x<=13 :
    print('nr este in interval')

#5. abs
y=int(input('Y = '))
if abs(x - y) < 5:
    print('The difference between x and y is less than 5')
else:
    print('The difference between x and y is greater than 5')

#6. verifica daca x nu este intre 5 si 27
if not x>=5 and x<=27 :
    print('nr nu este in interval')
else:
    print('nr este in interval')

#7. x egal cu y , daca da afiseaza acst lucru daca nu afiseaza care este mai mare
y=int(input('Y = '))
if x==y:
    print('x egal cu y')
elif x>y:
    print(f'nr mai mare este, {x}')
else:
    print(f'nr mai mare este: {y}')

#8. verifica daca triunghiul este isoscel, echilateral sau oarecare
z=int(input('Introdu nr z: '))
if x==y and z==y and x>0 and y>0 and z>0 :
    print('Triunghi echilateral')
elif x==y or x==z or y==z and x>0 and y>0 and z>0:
    print('Triunghi isoscel')
elif x!=y and x!=z and z!=y and x>0 and y>0 and z>0 :
    print('Triunghi oarecare')
else:
    print('triunghi invalid')

#9.vocale upper si lower
litera = input('Introduceti o litera: ')
if litera in['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print("Litera este o vocala")
else:
        print("Litera este o consoana")

#10. conversie note in format american
a=int(input('Introdu nota: '))
if a>9:
    print(f'Ai luat nota: A')
elif a>8 and a<=9:
    print(f'Ai luat nota: B')
elif a>7 and a<=8:
    print(f' Ai luat nota: C')
elif a>6 and a<=7:
    print(f'Ai luat nota: D')
elif a>4 and a<=6:
    print(f'Ai luat nota: E')
else:
    print(f'Ai luat nota:F')

#Optionale
#1.Verifica daca x are 4 cifre
x=input('x= ')
if len(x)>=4 :
    print(f'Numarul are: {len(x)} cifre')
else:
    print('Numarul are mai putin de 4 cifre')

#2. verifica daca are exact 4 cifre
x=input('x= ')
if len(x)==4:
    print(f'Numarul are: {len(x)} cifre')
else:
    print('Numarul nu are 4 cifre')

#3 Numar par sau impar
x=int(input('x= '))
if x%2==0:
    print('Numarul este par')
else:
    print('Numarul este impar')

#4. Care variabila este mai mare
x=int(input('x= '))
y=int(input('y= '))
z=int(input('z= '))
if x>y and x>z :
    print(f'Numarul cel mai mare este {x}')
elif y>x and y>z :
    print(f'Numarul cel mai mare este {y}')
else:
    print(f'Numarul cel mai mare este {z}')

#5. Optionale Dif intre x si y
y = int(input('introduceti y= '))
z = int(input('introduceti z= '))
if x+y+z==180 or (x+y>z and x+z>y and y+z>x):
    print('Triunghi valid')
else:
    print('Triunghi invalid')


#BONUS 1.
varsta=int(input('Introduceti varsta: '))
pasaport=True
Insotit_de_mama=True
Insotit_de_tata=False
Act_permisiune_mama=False
Act_permisiune_tata=True
if varsta>=18 and pasaport or (varsta <18 and pasaport and Insotit_de_mama and Insotit_de_tata)or ((varsta <18 and pasaport and(Insotit_de_mama or Insotit_de_tata)and(Act_permisiune_mama or Act_permisiune_tata))):
    print('Esti gata de imbarcare')

else:
    print('Nu ai acces la imbarcare')

