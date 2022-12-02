'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’'''

from abc import abstractmethod, ABC
class FormaGeormetrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError #pass

    def descrie(self):
        print('Cel mai probabil am colturi')

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''

class Patrat(FormaGeormetrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print (f'Latura mea este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura1):
        self.__latura = latura1
        return self.__latura
        print(f'Valoarea laturei noi este {self.__latura}')

    @latura.deleter
    def latura(self):
        self.__latura = None
        print(f'Am sters latura')
        return self.__latura

    def aria(self):
        # self.__aria = self.__latura**2
        # return self.__aria
        print(f'Aria patratului este {self.__latura**2}')

'''
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
'''

class Cerc(FormaGeormetrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza mea este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza1):
        self.__raza = raza1
        return self.__raza
        print(f'Noua valoare a razei este {self.__raza}')

    @raza.deleter
    def raza(self):
        self.__raza = None
        print('Am sters raza')

    def aria(self):
        # self.__aria = self.PI * self.__raza**2
        # return self.__aria
        print(f'Raza cercului este {self.PI * self.__raza**2}')

    def descrie(self):
        print('Eu nu am colturi')

'''
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
'''

print('***************Creează un obiect de tip Patrat și joacă-te cu metodele lui')

p1 = Patrat(5)
p1.descrie()
p1.aria()
p1.latura
p1.latura = 6
p1.latura
del p1.latura

print('***************Creează un obiect de tip Cerc și joacă-te cu metodele lui')
c1 = Cerc(4)
c1.descrie()
c1.aria()
c1.raza
c1.raza = 5
c1.raza
del c1.raza