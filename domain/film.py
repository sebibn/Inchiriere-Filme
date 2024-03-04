from domain.entitate import Entitate

class Film(Entitate):
    def __init__(self, idFilm, titlu, descriere, gen):
        super().__init__(idFilm)
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def getTitlu(self):
        return self.__titlu

    def getDescriere(self):
        return self.__descriere

    def getGen(self):
        return self.__gen

    def setTitlu(self, titlu):
        self.__titlu = titlu

    def setDescriere(self, descriere):
        self.__descriere = descriere

    def setGen(self, gen):
        self.__gen = gen

    def __str__(self):
        return f"id: {self.getIdEntitate()}, titlu: {self.__titlu}, descriere: {self.__descriere}, gen: {self.__gen}"