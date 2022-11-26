'''1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

from math import pi

class Cerc:
    # doua atribute
    # constructor pentru ambele atribute
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # metode
    def descrie_cerc(self):
        print(self.culoare, self.raza)
    def aria(self):
        aria = pi * (self.raza**2)
        return aria
    def diametru(self):
        diametru = self.raza *2
        return diametru
    def circumferinta(self):
        circumferinta = 2*pi*self.raza
        return circumferinta

# # instantiem un obiect al clasei Cerc (cerc1)
cerc1 = Cerc(3, 'roz')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

# instantiem un al doilea obiect al clasei Cerc (cerc2)
cerc2 = Cerc(5, 'galben')
cerc2.descrie_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())


'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''

class Dreptunghi:
    # lungime, latime, culoare = atribute
    # constructor pentru toate atributele
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    # metode
    def descriere(self):
        print(f'Am un dreptunghi de culoare {self.culoare}, cu lungime {self.lungime} si cu latime {self.latime}')
    def aria(self):
        aria = self.latime * self.lungime
        return aria
    def perimetrul(self):
        perimetrul = 2*self.lungime + 2*self.latime
        return perimetrul
    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


# instantiem un obiect al clasei Dreptunghi (dreptunghi1)
dreptunghi1 = Dreptunghi(10, 5, 'roz')
dreptunghi1.descriere()
print(dreptunghi1.aria())
print(dreptunghi1.perimetrul())

# Verific schimbarea culorii prin apelarea metodei descrie()
dreptunghi1.schimba_culoarea('rosu de nervi')
dreptunghi1.descriere()


# instantiem un obiect al clasei Dreptunghi (dreptunghi2)
dreptunghi2 = Dreptunghi(20, 10, 'alb')
dreptunghi2.descriere()
print(dreptunghi2.aria())
print(dreptunghi2.perimetrul())

# Verific schimbarea culorii prin apelarea metodei descrie()
dreptunghi2.schimba_culoarea('negru')
dreptunghi2.descriere()

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

class Angajat:
    # nume, prenume, salariu = atribute
    # constructor pentru toate atributele
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    # metode
    def descrie(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume} si are un salariu de {self.salariu}')
    def nume_complet(self):
        nume_complet = self.nume +self.prenume
        return nume_complet
    def salariu_lunar(self):
        salariu_lunar = self.salariu
        return salariu_lunar
    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return salariu_anual
    def marire_salariu(self, procent):
        marire_salariu = self.salariu * procent/100
        return marire_salariu


# instantiem un obiect al clasei Angajat (angajat1)
angajat1 = Angajat('Popa', 'Carmen', 5000)
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu(10))

# instantiem un obiect al clasei Angajat (angajat2)
angajat2 = Angajat('Popescu', 'Gabriel', 6000)
angajat2.descrie()
print(angajat2.nume_complet())
print(angajat2.salariu_lunar())
print(angajat2.salariu_anual())
print(angajat2.marire_salariu(15))

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''

class Cont:
    # iban, titular_cont, sold = atribute
    # constructor pentru toate atributele
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    # metode
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self, suma):
        if suma <= self.sold:
            self.sold = self.sold - suma
            return self.sold
        else: print(f'Nu aveti fonduri suficiente')
    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        return self.sold

# instantiem un obiect al clasei Cont (client1)
client1 = Cont('RO42RZBR','Popa Carmen', 100)
client1.afisare_sold()
print(client1.debitare_cont(50))
print(client1.creditare_cont(200))

# instantiem un obiect al clasei Cont (client2)
# debitam contul cu o suma mai mica decat soldul disponibil
client2 = Cont('RO10INGB', 'Popescu Mircea', 200)
client2.afisare_sold()
print(client2.debitare_cont(50))
print(client2.creditare_cont(100))


# instantiem un obiect al clasei Cont (client2)
# debitam contul cu o suma mai mare decat soldul disponibil
client2 = Cont('RO10INGB', 'Popescu Mircea', 200)
client2.afisare_sold()
print(client2.debitare_cont(300))
print(client2.creditare_cont(100))

'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''

class Masina:
    # atributele clasei marca, model, viteza maxima, viteza_actuala, culoare,culori_disponibile (set), inmatriculata (bool)
    # constructor:model si viteza maxima
    marca = 'BMW'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'rosu', 'negru', 'alb', 'bej', 'argintiu'}
    inmatriculata = False
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    # metode
    def descrie(self):
        print(f'Marca masinii este {self.marca}')
        print(f'Modelul masinii este {self.model}')
        print(f'Culoarea masinii este {self.culoare}')
        print(f'Masina este inmatriculata {self.inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata
    def vopseste_culoare(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            culoare_noua == self.culoare
            return culoare_noua
        else:
            print(f'Culoarea aleasa nu este disponibila! Culoarea masinii va ramane {self.culoare}!')
    # accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e negativă-eroare,
    # daca viteza e mai mare decat viteza_max - masina va accelera până la viteza maximă

    def accelereaza(self,viteza_intermediara):
        if viteza_intermediara < 0:
            print(f'Viteza invalida! Eroare!')
        elif viteza_intermediara == self.viteza_maxima:
            print(f'Masina ruleaza si a atins viteza de {self.viteza_maxima}!')
        elif viteza_intermediara > self.viteza_maxima:
            self.viteza_actuala == self.viteza_maxima
            print(f'Masina ruleaza cu viteza maxima de {self.viteza_maxima} si nu poate depasi aceasta viteza!')
        else:
            viteza_intermediara < self.viteza_maxima
            return viteza_intermediara
    def franeaza(self):
        # franeaza() - mașina se va opri și va avea viteza 0
        if self.viteza_actuala == 0:
            print(f'Masina s-a oprit! Viteza actuala este {self.viteza_actuala}!')


# instantiem primul obiect in clasa Masina
masina1 = Masina('520D', 180)
masina1.descrie()
print(masina1.inmatriculare())
print(masina1.vopseste_culoare('Portocaliu'))
print(masina1.accelereaza(80))
print(masina1.franeaza())

# instantiem al doilea obiect in clasa Masina
masina2 = Masina('320D', 160)
masina2.descrie()
print(masina2.inmatriculare())
print(masina2.vopseste_culoare('negru'))
print(masina2.accelereaza(160))
print(masina2.franeaza())
