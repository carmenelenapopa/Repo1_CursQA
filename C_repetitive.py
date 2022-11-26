'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# for
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

# for each
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# while
print(len(masini))
i = 0
while i <= len(masini)-1:
    print(f' Masina mea preferata este {masini[i]}')
    i = i+1

'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range (len(masini)):
    masini[i] = masini[i].upper()
    if i == 0 or i == (len(masini)-1):
        masini[i] = masini[i].title()
else:
    print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

masina = 'Mercedes'
for masina in masini:
    print('Am gasit masina dorita de dvs')
    break
else:
    print("Am găsit mașina X. Mai căutam")


'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

''' 5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.'''

masini_vechi = []

i = 0
while i < len(masini):
    if masini[i] == 'Trabant' or masini[i] =='Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
    i= i+1

print(masini_vechi)
print(masini)


'''
6. Având dict:
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

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

for marca, pret in pret_masini.items():
    if pret_masini[marca] < 15000:
        print(f' Acesta masina se incadreaza in bugetul dvs: {marca}, {pret_masini[marca]}')


'''
7. Având lista: numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
frecventa3 = 0
for numar in numere:
    if numar == 3:
        frecventa3 +=1
print(f'Numarul 3 apare de {frecventa3}')

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
i = 0
for numar in numere:
    suma = suma + numere[i]
    i = i+1
print(f' Suma numerelor este {suma}')


'''9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

nr_max = numere[0]
for numar in numere:
    if numar > nr_max:
      nr_max = numar
print(f'Nr cel mai mare este {nr_max}')

