from unittest import TestCase

from domain.film import Film
from repository.filmFileRepository import FilmFileRepository


class TestFilmFileRepository(TestCase):
    def setUp(self):
        f = open("testFilme.txt", "w")
        self.repository = FilmFileRepository("testFilme.txt")
        f.close()

    def testAdaugaFilm(self):
        film = Film(1, "Titlu", "Desc", "Gen")
        self.repository.adauga(film)

        with open("testFilme.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idFilm = line.split(',')[0]
                titlu = line.split(',')[1]
                descriere = line.split(',')[2]
                gen = line.split(',')[3]
                filmNou = Film(idFilm, titlu, descriere, gen)

        self.assertTrue(filmNou.getTitlu() == "Titlu")
        self.assertTrue(filmNou.getDescriere() == "Desc")
        self.assertTrue(filmNou.getGen() == "Gen")

    def testModificaFilm(self):
        film = Film(1, "Titlu", "Desc", "Gen")
        self.repository.adauga(film)
        film = Film(1, "Titlu 2", "Desc 2", "Gen 2")
        self.repository.modifica(film)

        with open("testFilme.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idFilm = line.split(',')[0]
                titlu = line.split(',')[1]
                descriere = line.split(',')[2]
                gen = line.split(',')[3]
                filmNou = Film(idFilm, titlu, descriere, gen)

        self.assertTrue(filmNou.getTitlu() == "Titlu 2")
        self.assertTrue(filmNou.getDescriere() == "Desc 2")
        self.assertTrue(filmNou.getGen() == "Gen 2")

    def testStergeFilm(self):
        film = Film(1, "Titlu", "Desc", "Gen")
        self.repository.adauga(film)

        lista = []
        with open("testFilme.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idFilm = line.split(',')[0]
                titlu = line.split(',')[1]
                descriere = line.split(',')[2]
                gen = line.split(',')[3]
                filmNou = Film(idFilm, titlu, descriere, gen)
                lista.append(filmNou)

        self.assertTrue(len(lista) == 1)
        self.repository.sterge(1)

        with open("testFilme.txt", 'r') as f:
            lines = f.readlines()

        self.assertTrue(lines == [])

    def testReadFile(self):
        entitati = {}
        film = Film(1, "Titlu", "Desc", "Gen")
        self.repository.adauga(film)

        with open("testFilme.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idFilm = line.split(',')[0]
                titlu = line.split(',')[1]
                descriere = line.split(',')[2]
                gen = line.split(',')[3]
                filmNou = Film(idFilm, titlu, descriere, gen)
                entitati[idFilm] = filmNou

        lines2 = []
        lines2.append(f'{idFilm},{titlu},{descriere},{gen},\n')
        self.assertTrue(str(lines) == str(lines2))
        self.assertTrue(str(film) == str(filmNou))
        self.assertTrue(filmNou.getTitlu() == "Titlu")
        self.assertTrue(filmNou.getDescriere() == "Desc")
        self.assertTrue(filmNou.getGen() == "Gen")
        self.assertTrue(str(entitati["1"]) == "id: 1, titlu: Titlu, descriere: Desc, gen: Gen")