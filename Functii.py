# 1.Funcție care să calculeze și să returneze suma a două numere
def suma(a, b):
    suma = a+b
    print(f'Suma celor doua numere este {suma}')
    return suma

print(suma(2, 6))
print(suma(4, 6))
print(suma(5,8))

# 1.1 Funcție care să calculeze și să returneze suma a trei numere
def suma_2(a, b, c):
    suma_2 = a+b+c
    print(f'suma celor trei numere este {suma_2}')
    return suma_2

print(suma_2(1,1,1))
print(suma_2(2,4,6))

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(par_impar(3))
print(par_impar(8))

'''3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''

def nr_caractere(nume):
    counter = 0
    for i in nume:
        counter = counter + 1
    return counter

nume = 'Popa Carmen Elena'
print(nr_caractere(nume))

# 4. Funcție care returnează aria dreptunghiului
def arie_dreptunghi(lungime, latime):
    arie_dreptunghi = lungime * latime
    print(f' Aria dreptunghiului este {arie_dreptunghi}')
    return arie_dreptunghi
print(arie_dreptunghi(6, 9))
print(arie_dreptunghi(5, 9))


# 5. Funcție care returnează aria cercului

from math import pi

def arie_cerc(pi, r):
    arie_cerc = (pi * r**2)
    print(f'Aria cercului este {arie_cerc}')
    return arie_cerc
print(arie_cerc(pi, 2))
print(arie_cerc(pi, 4))
print(arie_cerc(pi, 3))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

def string(text):
    text = 'Este prea devreme si vreau sa dorm'
    x = 'q'
    if x in text:
        return True
    else:
        return False
print(string('text'))

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
def numere_pozitive(lista):
    pozitive = []
    for numar in lista:
        if numar > 0:
             pozitive.append(numar)
    return pozitive

lista = [1, 6, -8, 5, 9, -1, 4]
print(numere_pozitive(lista))

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''
def functie(a, b):
    if a > b:
        print(f'Primul numar {a} este mai mare decat al doilea {b}')
    if b > a:
        print(f'Al doilea numar {b} este mai mare decat primul {a}')
    if a == b:
        print(f' Numerele sunt egale')
print(functie(2, 3))

'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''

lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
def dictionar(lista):
    dict = {}
    for i in lista:
        dict[i] = lista.count(i)
    return dict
print(dictionar(lista))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def nr_max(a, b, c):
    numar_max = max(a, b, c)
    return numar_max
print(nr_max(2, 5, 7))
print(nr_max(-2, 8, -32))


'''1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}'''

def numere_comune(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    if (list1_set & list2_set):
        print(list1_set & list2_set)

list1 = [8, 1, 5, 3, 7, 6, 2, 1]
list2 = [2, 8, 1, 3, 7, 4, 8, 10, 23, 14]
print(numere_comune(list1, list2))


# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
# importam modulul datetime => modul pentru a citi data curenta

from datetime import date
# citim data de azi
print(date.today())
print(f'Astazi este: {date.today()}')

# citim data de azi
# Funcția now() este o altă funcție utilă pentru modulul datetime => se citesc data și ora curente

from datetime import datetime
data_ora = datetime.now()
print(f'Data si ora curente sunt: {data_ora}')

