from unittest import TestCase

from domain.clientFilm import ClientFilm
from repository.clientFilmFileRepository import ClientFilmFileRepository
from domain.client import Client
from repository.clientFileRepository import ClientFileRepository
from domain.film import Film
from repository.filmFileRepository import FilmFileRepository


class TestClientFilmFileRepository(TestCase):
    def setUp(self):
        f = open("testInchirieri.txt", "w")
        self.clientFilmFileRepository = ClientFilmFileRepository("testInchirieri.txt")
        self.clientRepository = ClientFileRepository("testClienti.txt")
        self.filmRepository = FilmFileRepository("testFilme.txt")
        f.close()

    def testAdaugaClient(self):
        client = Client(1, "Andrei", "12345")
        self.clientRepository.adauga(client)
        film = Film(1, "Titlu", "Desc", "Gen")
        self.filmRepository.adauga(film)
        inchiriere = ClientFilm(1, 1, 1)
        self.clientFilmFileRepository.adauga(inchiriere)
        self.clientFilmFileRepository._readFile()
        with open("testInchirieri.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClientFilm = line.split()[0]
                idClient = line.split()[1]
                idFilm = line.split()[2]
                clientFilmNou = ClientFilm(idClientFilm, idClient, idFilm)

        self.assertTrue(clientFilmNou.getIdClient() == "1")
        self.assertTrue(clientFilmNou.getIdFilm() == "1")

    def testModificaClient(self):
        client = Client(1, "Andrei", "12345")
        self.clientRepository.adauga(client)
        film1 = Film(1, "Titlu", "Desc", "Gen")
        self.filmRepository.adauga(film1)
        film2 = Film(2, "Titlu 2", "Desc 2", "Gen 2")
        self.filmRepository.adauga(film2)
        inchiriere = ClientFilm(1, 1, 1)
        self.clientFilmFileRepository.adauga(inchiriere)
        inchiriere = ClientFilm(1, 1, 2)
        self.clientFilmFileRepository.modifica(inchiriere)

        with open("testInchirieri.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClientFilm = line.split()[0]
                idClient = line.split()[1]
                idFilm = line.split()[2]
                clientFilmNou = ClientFilm(idClientFilm, idClient, idFilm)

        self.assertTrue(clientFilmNou.getIdClient() == "1")
        self.assertTrue(clientFilmNou.getIdFilm() == "2")

    def testStergeClient(self):
        client = Client(1, "Andrei", "12345")
        self.clientRepository.adauga(client)
        film = Film(1, "Titlu", "Desc", "Gen")
        self.filmRepository.adauga(film)
        inchiriere = ClientFilm(1, 1, 1)
        self.clientFilmFileRepository.adauga(inchiriere)

        lista = []
        with open("testInchirieri.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClientFilm = line.split()[0]
                idClient = line.split()[1]
                idFilm = line.split()[2]
                clientFilmNou = ClientFilm(idClientFilm, idClient, idFilm)
                lista.append(clientFilmNou)

        self.assertTrue(len(lista) == 1)
        self.clientFilmFileRepository.sterge(1)

        with open("testInchirieri.txt", 'r') as f:
            lines = f.readlines()

        self.assertTrue(lines == [])

    def testReadFile(self):
        entitati = {}
        client = Client(1, "Andrei", "12345")
        self.clientRepository.adauga(client)
        film = Film(1, "Titlu", "Desc", "Gen")
        self.filmRepository.adauga(film)
        inchiriere = ClientFilm(1, 1, 1)
        self.clientFilmFileRepository.adauga(inchiriere)

        with open("testInchirieri.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClientFilm = line.split()[0]
                idClient = line.split()[1]
                idFilm = line.split()[2]
                clientFilmNou = ClientFilm(idClientFilm, idClient, idFilm)
                entitati[idClient] = clientFilmNou

        self.assertTrue(str(inchiriere) == str(clientFilmNou))
        self.assertTrue(idClientFilm == "1")
        self.assertTrue(idClient == "1")
        self.assertTrue(idFilm == "1")
        self.assertTrue(str(entitati["1"]) == "id: 1, id client: 1, id film: 1")