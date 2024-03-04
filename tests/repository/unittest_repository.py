from unittest import TestCase

from domain.entitate import Entitate
from repository.repository import Repository
from domain.exceptii.duplicateError import DuplicateError

class TestDuplicateError(TestCase):
    def testStr(self):
        duplicateError = DuplicateError("mesaj")
        self.assertTrue(duplicateError.__str__() == 'DuplicateError: mesaj')

class TestRepository(TestCase):
    def setUp(self):
        self.repository = Repository()

    def testAdauga(self):
        entitate = Entitate(1)
        self.repository.adauga(entitate)
        self.assertTrue(len(self.repository.getAll()) == 1)
        with self.assertRaises(DuplicateError):
            self.repository.adauga(entitate)

    def testModifica(self):
        entitate = Entitate(1)
        entitateNoua = Entitate(1)
        self.repository.adauga(entitate)
        self.repository.modifica(entitateNoua)
        self.assertTrue(len(self.repository.getAll()) == 1)

        with self.assertRaises(KeyError):
            self.repository.modifica(Entitate(2))

    def testSterge(self):
        entitate = Entitate(1)
        self.repository.adauga(entitate)
        self.assertTrue(len(self.repository.getAll()) == 1)
        self.repository.sterge(entitate.getIdEntitate())
        self.assertTrue(len(self.repository.getAll()) == 0)

        with self.assertRaises(KeyError):
            self.repository.sterge(2)

    def tearDown(self) -> None:
        pass