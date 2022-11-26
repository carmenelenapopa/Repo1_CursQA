'''
Q: 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

# suprascriem si printam ordinea inversa a elementelor
note_invers = note_muzicale[::-1]
print(note_invers)

# o alta metoda care inverseaza ordinea elementelor - reverse()
# obtinem 'none' - ceva nu fac bine !!!!!
note_invers.reverse()
print(note_invers)

# Q: 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

'''
Q: 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''

# prima varianta este extend ()
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1.extend(lista2)
print(lista1)

# a doua varianta - concatenare de liste
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista3 = lista1 + lista2
print(lista3)


'''
Q: 4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
# sortam lista in ordine descrescatoare
lista3.sort(reverse=True)
print(lista3)

# ● Sortează și afișază lista generată la exercițiul anterior.
lista3.sort()
print(lista3)

# ● Sortează numărul 0 folosind o funcție
# ● Afișaza iar lista.
lista3.remove(0)
print(lista3)
'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
'''

# Varianta 1: Verificam lungimea listei. Lista goala trebuie sa aiba valoare 0
if(len(lista3) == 0):
    print("Lista este goala")
else:
    print('Lista nu este goala')

# Variante 2: utilizam bool()
# Listele goale sunt considerate FALSE

if(bool(lista3) == True):
    print('Lista nu este goala')
else:
    print('Lista este goala')


# 6. Folosește o funcție care să șteargă lista de la exercițiul 3

# functia clear() a sters elementele din lista3
lista3.clear()
print(lista3)

# del sterge complet lista si in acest caz rezultatul asteptat este o eroare
# del lista3
# print(lista3)


''' Q: 7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.'''

if(len(lista3) == 0):
    print("Lista este goala")
else:
    print('Lista nu este goala')

''' Q: 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

''' Q: 9. Printează cei 3 elevi și notele lor
Ex: Doar nota o vei lua folosindu-te de cheie
'''
# am printat valorile din dictionar
print(dict1.values())

# functia items()
for key, value in dict1.items():
    print(key, 'a luat nota', value)

'''
Q: 10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
# am actualizat nota lui Dorel dupa contestatie
# am printat nota dupa actualizare
# am printat dict1 actualizat

dict1['Dorel'] = 6
print(dict1.get('Dorel'))
print(dict1)

'''
Q: 11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''

# metoda pop
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)


'''
Q: 12. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt  '''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# adaugam un element care deja exista in lista => rezultatul asteptat: elementul nu va fi adaugat
zile_sapt.add('luni')
print(zile_sapt)

''' Q: 13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.'''

# issubset ()
print(weekend.issubset(zile_sapt))

zile = weekend.issubset(zile_sapt)
if(zile == True):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

# Q: 14. Afișează diferențele dintre aceste 2 seturi.
# difference()

zile = zile_sapt.difference(weekend)
print(zile)

# Q: 15. Afișază intersecția elementelor din aceste 2 seturi.
# intersection()
zile = zile_sapt.intersection(weekend)
print(zile)

'''
Q 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
Google search hint
“how to check if item îs în list python”
'''


# 3 schimbari disponibile
# Prima schimbare: a iesit Ronaldo si intra Hagi
# schimbari efectuate = 1
# jucator intrat = Hagi
# jucator iesit = Ronaldo

echipa = ['Ronaldo', 'Mbappe', 'Neymar', 'Ibrahimovic', 'Messi']
schimbari_max = 3
schimbari_efectuate = 0

jucator_intrat = 'Hagi'
jucator_iesit = 'Ronaldo'

if schimbari_efectuate < 3:
    if jucator_iesit in echipa:
        schimbari_efectuate = schimbari_efectuate + 1
        echipa.remove(jucator_iesit)
        echipa.append(jucator_intrat)
        print((f'A intrat {jucator_intrat} si a ieșit {jucator_iesit}'))
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren')
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('Ai epuizat toate schimbarile')

print(echipa)

# A doua schimbare: il scot pe Maradona si intra in locul lui Pele
# jucator iesit = Maradona
# jucator intrat = Pele

jucator_intrat = 'Pele'
jucator_iesit = 'Maradona'

if schimbari_efectuate < 3:
    if jucator_iesit in echipa:
        schimbari_efectuate = schimbari_efectuate + 1
        echipa.remove(jucator_iesit)
        echipa.append(jucator_intrat)
        print((f'A intrat {jucator_intrat} si a ieșit {jucator_iesit}'))
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren')
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('Ai epuizat toate schimbarile')
print(echipa)

# A doua schimbare: il scot pe Ibrahimovic si intra in locul lui Pele
jucator_iesit = 'Ibrahimovic'
jucator_intrat = 'Pele'

if schimbari_efectuate < 3:
    if jucator_iesit in echipa:
        schimbari_efectuate = schimbari_efectuate + 1
        echipa.remove(jucator_iesit)
        echipa.append(jucator_intrat)
        print((f'A intrat {jucator_intrat} si a ieșit {jucator_iesit}'))
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren')
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('Ai epuizat toate schimbarile')
print(echipa)

# ultima schimbare
jucator_iesit = 'Neymar'
jucator_intrat = 'Ronaldo'

if schimbari_efectuate < 3:
    if jucator_iesit in echipa:
        schimbari_efectuate = schimbari_efectuate + 1
        echipa.remove(jucator_iesit)
        echipa.append(jucator_intrat)
        print((f'A intrat {jucator_intrat} si a ieșit {jucator_iesit}'))
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren')
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('Ai epuizat toate schimbarile')
print(echipa)

# desi am epuizat toate schimbarile, incerc sa fac inca o schimbare
jucator_iesit = 'Ronaldo'
jucator_intrat = 'Neymar'

if schimbari_efectuate < 3:
    if jucator_iesit in echipa:
        schimbari_efectuate = schimbari_efectuate + 1
        echipa.remove(jucator_iesit)
        echipa.append(jucator_intrat)
        print((f'A intrat {jucator_intrat} si a ieșit {jucator_iesit}'))
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren')
        print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('Ai epuizat toate schimbarile')
print(echipa)

