from domain.exceptii.duplicateError import DuplicateError
from service.clientService import ClientService
from service.filmService import FilmService
from service.clientFilmService import ClientFilmService


class Consola:
    def __init__(self, filmService: FilmService, clientService: ClientService, clientFilmService: ClientFilmService):
        self.__filmService = filmService
        self.__clientService = clientService
        self.__clientFilmService = clientFilmService

    def adaugaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            descriere = input("Dati descrierea filmului: ")
            gen = input("Dati genul filmului: ")
            self.__filmService.adaugaFilm(idFilm, titlu, descriere, gen)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de modificat: ")
            titluNou = input("Dati titlul nou al filmului: ")
            descriereNou = input("Dati descrierea noua a filmului: ")
            genNou = input("Dati genul nou al filmului: ")
            self.__filmService.modificaFilm(idFilm, titluNou, descriereNou, genNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def stergeFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de sters: ")
            self.__filmService.stergeFilm(idFilm)
        except KeyError as e:
            print(e)

    def cautareFilme(self):
        try:
            titlu = input("Dati titlul filmului cautat: ")
            self.__filmService.cautareFilme(titlu)
        except KeyError as e:
            print(e)

    def adaugaClient(self):
        try:
            idClient = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            self.__clientService.adaugaClient(idClient, nume, CNP)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except DuplicateError as e:
            print(e)

    def modificaClient(self):
        try:
            idClient = input("Dati id-ul clientului de modificat: ")
            numeNou = input("Dati numele nou al clientului: ")
            CNPNou = input("Dati CNP-ul nou al clientului: ")
            self.__clientService.modificaClient(idClient, numeNou, CNPNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def stergeClient(self):
        try:
            idClient = input("Dati id-ul clientului de sters: ")
            self.__clientService.stergeClient(idClient)
        except KeyError as e:
            print(e)

    def cautareClienti(self):
        try:
            nume = input("Dati numele clientului cautat: ")
            self.__clientService.cautareClienti(nume)
        except KeyError as e:
            print(e)

    def primii30Clienti(self):
        try:
            self.__clientService.primii30Clienti()
        except KeyError as e:
            print(e)

    def inchiriereFilm(self):
        try:
            idClientFilm = input("Dati id-ul inchirierii: ")
            idClient = input("Dati id-ul clientului: ")
            idFilm = input("Dati id-ul filmului: ")
            self.__clientFilmService.adaugaInchiriere(idClientFilm, idClient, idFilm)
        except DuplicateError as e:
            print(e)
        except KeyError as e:
            print(e)

    def returnareFilm(self):
        idClient = input("Dati id-ul clientului: ")
        idFilm = input("Dati id-ul filmului: ")
        self.__clientFilmService.stergeInchiriere(idClient, idFilm)

    def rapoarteNrFilme(self):
        self.__filmService.rapoarteNrFilme()

    def celeMaiInchiriateFilme(self):
        self.__clientFilmService.celeMaiInchiriateFilme()

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("-----------------------------------------------------------------------------------------------------")
        print("a.1: Adauga client")
        print("a.2: Modifica client")
        print("a.3: Sterge client")
        print("a.4: Cautare client dupa nume")
        print("a.5: Primii 30% clienti cu cele mai multe filme")
        print("b.1: Adauga film")
        print("b.2: Modifica film")
        print("b.3: Sterge film")
        print("b.4: Cautare film dupa titlu")
        print("b.5: Afisare clienti cu filme inchiriate ordonati dupa nume si nr de filme inchiriate")
        print("b.6: Afisare cele mai inchiriate filme")
        print("a.c: Afiseaza toti clientii")
        print("a.f: Afiseaza toate filmele")
        print("a.i: Afiseaza toate inchirierile")
        print("i: Inchiriere film")
        print("r: Returnare film")
        print("x. Iesire")
        print("-----------------------------------------------------------------------------------------------------")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == "a.1":
                self.adaugaClient()
            elif optiune == "a.2":
                self.modificaClient()
            elif optiune == "a.3":
                self.stergeClient()
            elif optiune == "a.4":
                self.cautareClienti()
            elif optiune == "a.5":
                self.primii30Clienti()
            elif optiune == "b.1":
                self.adaugaFilm()
            elif optiune == "b.2":
                self.modificaFilm()
            elif optiune == "b.3":
                self.stergeFilm()
            elif optiune == "b.4":
                self.cautareFilme()
            elif optiune == "b.5":
                self.rapoarteNrFilme()
            elif optiune == "b.6":
                self.celeMaiInchiriateFilme()
            elif optiune == "a.c":
                self.afiseaza(self.__clientService.getAllClienti())
            elif optiune == "a.f":
                self.afiseaza(self.__filmService.getAllFilme())
            elif optiune == "a.i":
                self.afiseaza(self.__clientFilmService.getAllInchirieri())
            elif optiune == "i":
                self.inchiriereFilm()
            elif optiune == "r":
                self.returnareFilm()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")