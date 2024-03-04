from unittest import TestCase

class TestFilm(TestCase):
    def setUp(self):
        from domain.film import Film
        self.film = Film(1, "film 1", "desc 1", "gen 1")

    def testId(self):
        self.assertTrue(self.film.getIdEntitate() == 1)
        self.film.setIdEntitate(2)
        self.assertTrue(self.film.getIdEntitate() == 2)

    def testTitlu(self):
        self.assertTrue(self.film.getTitlu() == "film 1")
        self.film.setTitlu("film 2")
        self.assertTrue(self.film.getTitlu() == "film 2")

    def testDescriere(self):
        self.assertTrue(self.film.getDescriere() == "desc 1")
        self.film.setDescriere("desc 2")
        self.assertTrue(self.film.getDescriere() == "desc 2")

    def testGen(self):
        self.assertTrue(self.film.getGen() == "gen 1")
        self.film.setGen("gen 2")
        self.assertTrue(self.film.getGen() == "gen 2")

    def testStr(self):
        self.assertTrue(self.film.__str__() == f"id: {self.film.getIdEntitate()}, titlu: {self.film.getTitlu()}, descriere: {self.film.getDescriere()}, gen: {self.film.getGen()}")

    def tearDown(self) -> None:
        pass