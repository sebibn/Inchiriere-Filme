from unittest import TestCase

class TestEntitate(TestCase):
    def setUp(self):
        from domain.entitate import Entitate
        self.entitate = Entitate(1)

    def testId(self):
        self.assertTrue(self.entitate.getIdEntitate() == 1)
        self.entitate.setIdEntitate(2)
        self.assertTrue(self.entitate.getIdEntitate() == 2)

class TestClient(TestCase):
    def setUp(self):
        from domain.client import Client
        self.client = Client(1, "Maria", "123456789")

    def testId(self):
        self.assertTrue(self.client.getIdEntitate() == 1)
        self.client.setIdEntitate(2)
        self.assertTrue(self.client.getIdEntitate() == 2)

    def testNume(self):
        self.assertTrue(self.client.getNume() == "Maria")
        self.client.setNume("Andreea")
        self.assertTrue(self.client.getNume() == "Andreea")

    def testCNP(self):
        self.assertTrue(self.client.getCNP() == "123456789")
        self.client.setCNP("987654321")
        self.assertTrue(self.client.getCNP() == "987654321")

    def testStr(self):
        self.assertTrue(self.client.__str__() == f"id: {self.client.getIdEntitate()}, nume: {self.client.getNume()}, CNP: {self.client.getCNP()}")

    def tearDown(self) -> None:
        pass