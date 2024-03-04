from unittest import TestCase

from domain.clientFilm import ClientFilm
from domain.exceptii.duplicateError import DuplicateError
from repository.repository import Repository
from service.clientFilmService import ClientFilmService
from service.clientService import ClientService
from service.filmService import FilmService


class TestService(TestCase):
    def setUp(self):
        clientFilmRepository = Repository()
        clientRepository = Repository()
        filmRepository = Repository()
        self.repository = Repository()
        self.clientFilmRepository = Repository()
        self.clientRepository = Repository()
        self.filmRepository = Repository()
        self.clientService = ClientService(clientRepository, clientFilmRepository)
        self.clientFilmService = ClientFilmService(clientFilmRepository, clientRepository, filmRepository)
        self.filmService = FilmService(filmRepository, clientFilmRepository)

# ----------------------------------------------------- CLIENT SERVICE -------------------------------------------------

    def testAdaugaClient(self):
        self.clientService.adaugaClient(1, "Andrei", "49185395819")
        self.assertTrue(len(self.clientService.getAllClienti()) == 1)

    def testModificaClient(self):
        self.clientService.adaugaClient(1, "Andrei", "49185395819")
        self.clientService.modificaClient(1, "Maria", "4192814298")
        clienti = self.clientService.getAllClienti()
        for client in clienti:
            if client.getIdEntitate() == 1:
                self.assertTrue(client.getNume() == "Maria")
                self.assertTrue(client.getCNP() == "4192814298")

    def testStergeClient(self):
        self.clientService.adaugaClient(1, "Andrei", "49185395819")
        self.filmService.adaugaFilm(1, "titlu", "desc", "gen")
        self.assertTrue(len(self.clientService.getAllClienti()) == 1)

        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 1)

        self.clientService.stergeClient(1)
        self.assertTrue(len(self.clientService.getAllClienti()) == 0)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 0)


    def testCautareClienti(self):
        self.clientService.adaugaClient(1, "Andrei", "412094201")
        self.assertTrue(self.clientService.cautareClienti("Andrei") == print("id: 1, nume: Andrei, CNP: 412094201"))

    def testPrimii30Clienti(self):
        self.clientService.adaugaClient(1, "Andrei", "319319819")
        self.clientService.adaugaClient(2, "Ion", "931859138593")
        self.clientService.adaugaClient(3, "Maria", "4918591359")
        self.clientService.adaugaClient(4, "vasile", "531875831")
        self.assertTrue(len(self.clientService.getAllClienti()) == 4)

        self.filmService.adaugaFilm(1, "titlu 1", "desc 1", "gen 1")
        self.filmService.adaugaFilm(2, "titlu 2", "desc 2", "gen 2")
        self.filmService.adaugaFilm(3, "titlu 3", "desc 3", "gen 3")
        self.assertTrue(len(self.filmService.getAllFilme()) == 3)

        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.clientFilmService.adaugaInchiriere(2, 1, 2)
        self.clientFilmService.adaugaInchiriere(3, 1, 3)

        self.assertTrue(self.clientService.primii30Clienti() == print("idClient: 1, nr filme inchiriate: 3"))

#  ----------------------------------------------- FILM SERVICE --------------------------------------------------------

    def testModificaFilm(self):
        self.filmService.adaugaFilm(1, "titlu", "desc", "gen")
        self.filmService.modificaFilm(1, "titluNou", "descNou", "genNou")
        filme = self.filmService.getAllFilme()
        for film in filme:
            if film.getIdEntitate() == 1:
                self.assertTrue(film.getTitlu() == "titluNou")
                self.assertTrue(film.getDescriere() == "descNou")
                self.assertTrue(film.getGen() == "genNou")

    def testStergeFilm(self):
        self.filmService.adaugaFilm(1, "titlu", "desc", "gen")
        self.clientService.adaugaClient(1, "Andrei", "519358319")
        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 1)
        self.assertTrue(len(self.filmService.getAllFilme()) == 1)
        self.filmService.stergeFilm(1)
        self.assertTrue(len(self.filmService.getAllFilme()) == 0)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 0)

    def testCautareFilme(self):
        self.filmService.adaugaFilm(1, "titlu", "desc", "gen")
        self.assertTrue(self.filmService.cautareFilme("titlu") == print("id: 1, titlu: titlu, descriere: desc, gen: gen"))

    def testRapoarteNrFilme(self):
        self.clientService.adaugaClient(1, "Andrei", "319319819")
        self.clientService.adaugaClient(2, "Ion", "931859138593")
        self.clientService.adaugaClient(3, "Maria", "4918591359")
        self.clientService.adaugaClient(4, "vasile", "531875831")
        self.assertTrue(len(self.clientService.getAllClienti()) == 4)

        self.filmService.adaugaFilm(1, "titlu 1", "desc 1", "gen 1")
        self.filmService.adaugaFilm(2, "titlu 2", "desc 2", "gen 2")
        self.filmService.adaugaFilm(3, "titlu 3", "desc 3", "gen 3")
        self.assertTrue(len(self.filmService.getAllFilme()) == 3)

        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.clientFilmService.adaugaInchiriere(2, 1, 2)
        self.clientFilmService.adaugaInchiriere(3, 1, 3)

        self.assertTrue(self.filmService.rapoarteNrFilme() == print("id client: 1, nr filme inchiriate: 3"))

    def testCeleMaiInchiriateFilme(self):
        self.clientService.adaugaClient(1, "Andrei", "319319819")
        self.clientService.adaugaClient(2, "Ion", "931859138593")
        self.clientService.adaugaClient(3, "Maria", "4918591359")
        self.clientService.adaugaClient(4, "vasile", "531875831")
        self.assertTrue(len(self.clientService.getAllClienti()) == 4)

        self.filmService.adaugaFilm(1, "titlu 1", "desc 1", "gen 1")
        self.filmService.adaugaFilm(2, "titlu 2", "desc 2", "gen 2")
        self.filmService.adaugaFilm(3, "titlu 3", "desc 3", "gen 3")
        self.assertTrue(len(self.filmService.getAllFilme()) == 3)

        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.clientFilmService.adaugaInchiriere(2, 1, 2)
        self.clientFilmService.adaugaInchiriere(3, 1, 3)
        self.clientFilmService.adaugaInchiriere(4, 2, 1)
        self.clientFilmService.adaugaInchiriere(5, 3, 1)

        self.assertTrue(self.clientFilmService.celeMaiInchiriateFilme() == print("id film: 1, nr inchirieri.txt: 3\nid film: 2, nr inchirieri.txt: 1\nid film: 3, nr inchirieri.txt: 1"))

# ---------------------------------------------- CLIENT FILM SERVICE ---------------------------------------------------

    def testAdaugaInchiriere(self):
        self.clientService.adaugaClient(1, "Andrei", "319319819")
        self.filmService.adaugaFilm(1, "titlu 1", "desc 1", "gen 1")
        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 1)

        with self.assertRaises(KeyError):
            self.clientFilmService.adaugaInchiriere(2, 2, 2)

        with self.assertRaises(KeyError):
            self.clientFilmService.adaugaInchiriere(2, 1, 2)

        with self.assertRaises(DuplicateError):
            self.clientFilmService.adaugaInchiriere(2, 1, 1)

    def testStergeInchiriere(self):
        self.clientService.adaugaClient(1, "Andrei", "319319819")
        self.filmService.adaugaFilm(1, "titlu 1", "desc 1", "gen 1")
        self.clientFilmService.adaugaInchiriere(1, 1, 1)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 1)
        self.clientFilmService.stergeInchiriere(1, 1)
        self.assertTrue(len(self.clientFilmService.getAllInchirieri()) == 0)

    def tearDown(self) -> None:
        pass