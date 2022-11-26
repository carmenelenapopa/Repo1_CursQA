# Q: 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
'''A: Structura alternativa If executa un bloc de cod cand o anumita conditie este indeplinita. Daca conditia este indeplinita,
trece la urmatoarea linie si ruleaza codul.
'''

# Q: 2. Verifică și afișează dacă x este număr natural sau nu.
# A: Numere naturale = numere pozitive si intregi - folosesc metodele isnumeric() si isdigit()

# variabila X a fost initializata direct in cod si am folosit metoda isnumeric()
# am atribuit valoarea 25 => X este un numar natural
# am atribuit valoarea -25 => X NU este un numar natural

variabila_x = '-25'
if variabila_x.isnumeric():
    print('X este un numar natural')
else:
    print('X NU este un numar natural')

# variabila X este citita de la tastatura si am folosit metoda isdigit()
# am introdus valoarea 123 => si am obtinut 'Variabila X este numar natural'
# am introdus valoarea -123 => si am obtinut 'Variabila X NU este numar natural'
variabila_x = input('Introdu valoarea')
if variabila_x.isdigit():
    print('Variabila X este numar natural')
else:
    print('Variabila X NU este numar natural')


# Q: 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# A: numerele pozitive >0; numerele ngative <0; 0 == numar neutru

numar = int(input('Introdu numarul'))
if numar > 0:
    print('Numarul este pozitiv')
elif numar < 0:
    print('Numarul este negativ')
elif numar == 0:
    print('Numarul este neutru')
# Q: 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

variabila_x = 10
variabila_y = 5

if(variabila_x - variabila_y<5):
    print('Diferența dintre x și y este mai mică de 5')
elif(variabila_x-variabila_y>=5):
    print('Diferența dintre x și y NU este mai mică de 5')

# Q: 4. Verifică și afișează dacă x este între -2 și 13.
# A: Ma folosesc de operatorii logici

variabila_z = -1
if(variabila_z>-2 and variabila_z<13):
    print('Numarul se afla in interval')
elif(variabila_z<-2 and variabila_z>13):
    print('Numarul NU se afla in interval')
elif(variabila_z == -2 or variabila_z == 13):
    print('Limitele intervalului')

# Q: 7. x și y (int) Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# A: In cazul de mai jos x si y nu sunt egale si va afisa max dintre x si Y => -8
x = -8
y = -9

if(x == y):
     print('X si Y sunt egale')
else:
    print(max(x, y))

''' Q: 8. x, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
# triunghi isoscel atunci x = y, x!=z, y!=z
# triunghi echilateral x=y=z
# triunghi oarecare x!=y!=z
# x<y+z, y<x+z, z<x+y

x = 7
y = 10
z = 10

if((x < y + z) and (y < x + z) and (z < x + y)):
    if((x == y and x != z and y != z) or (x == z and x != y and z != y) or (y == z and x != y and x != z)):
        print('Triunghi isoscel')
    elif(x == y == z):
        print('Triunghi echilateral')
    elif(x != y != z):
        print('Triunghi oarecare')
else:
    print('Invalid data')



# Q: 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
# A: vocale a, e, i, o, u, A, E, I, O, U

vocale = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
litera = input('Introduceti litera')

if(litera in vocale):
   print('Litera este o vocala')
else:
    print('Litera este o consoana')

'''Q: 10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''

nota = int(input('Nota obtinuta este:'))
if(nota <=10 and nota>=9):
    print('A')
elif(nota >= 8 and nota < 9):
    print('B')
elif(nota >=7 and nota < 8 ):
    print('C')
elif(nota >= 6 and nota < 7):
    print('D')
elif(nota > 4 and nota < 6):
    print('E')
elif(nota <= 4 and nota >= 0):
    print('F')
else:
    print('Punctaj invalid')


'''
Q: 1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

y = '2202'
if(len(y) > 4):
    print(f'{y} are mai mult de 4 cifre')
elif(len(y) == 4):
    print(f'{y} are 4 cifre')
else:
    print(f'{y} are mai putin de 4 cifre')


# Q: 2.Verifică dacă x are exact 6 cifre.

x = '7777777'
if(len(x) == 6):
    print('Are 6 cifre')
else:
    print('Nu are 6 cifre')

# Q: 3.Verifică dacă x este număr par sau impar (x e int).
# numerele pare se divid cu 2 => restul 0
# folosesc functia % (modulo) => restul impartirii numerelor sa fie 0

number = int(input('Numarul:'))
if(number % 2) == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')


# Q: 4.  x, y, z (int). Afișează care este cel mai mare dintre ele
x = 60
y = 30
z = 40

print(max(x, y, z))

''' Q: 5. X, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.'''
# suma unghiurilor unui triunghi este intotdeauna 180 grade
# dam valori celor 3 unghiuri; daca suma este egala cu 180 atunci triunghiul este valid

unghiul_x = 40
unghiul_y = 60
unghiul_z = 58

if(unghiul_x + unghiul_y + unghiul_z == 180):
    print('Triunghiul este valid!')
else:
    print('Triunghiul este invalid!')

# Q: 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
#  Afișează stringul fără ultimele x caractere
#Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

string = 'Coral is either the stupidest animal or the smartest rock'

# afisez stringul complet
print(string[0:len(string)])
print(string[:])

x = int(input('Alege nr.'))

# afisez stringul fara ultimele X caractere
print(string[0:len(string) - x])


# 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5

string = 'Coral is either the stupidest animal or the smartest rock'

# declar si afisez un string nou care să fie format din primele 5 caractere + ultimele 5
string_nou = string[0:5] + string[len(string) - 5: len(string)]
print(string_nou)

# declar si afisez un string nou care să fie format din primele 5 caractere + ultimele 5
string_nou = string[0:5] + string[-5:]
print(string_nou)

''' Q: 8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest
'''

string = 'Coral is either the stupidest animal or the smartest rock'
# lungimea totala a stringului este 57
print(len(string))
# indexul de start al cuvântului rock - am folosint find ()
index_rock = string.find("rock")
print(index_rock)

# afișează tot stringul până la acest cuvant 'Coral is either the stupidest animal or the smartest'
print(string[0:53])

# Q: 10. Avand stringul '0123456789'
# Afișați doar numerele pare
# Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)

# slice(start, end, step)
# vor fi afisate numerele pare 
string = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
numere_pare = slice(0, 10, 2)
print(string[numere_pare])

# vor fi afisate numerele impare
numere_impare = slice(1, 10, 2)
print(string[numere_impare])


'''Exerciții Bonus (may need google) .
Q 11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y

'''

import random
valori_zar = [1, 2, 3, 4, 5, 6]

# aruncam zarul
dice_roll = random.choice(valori_zar)
print(dice_roll)

# declaram nr. ales de utilizat
nr_ales = int(input('Numar ales utilizator'))

'''Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''

if(nr_ales < dice_roll):
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales', nr_ales,'dar a fost', dice_roll)
elif(nr_ales > dice_roll):
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales', nr_ales,'dar a fost', dice_roll)
else:
    print(f'Ai ghicit. Felicitari! Ai ales', {nr_ales},'si zarul a fost', dice_roll)

