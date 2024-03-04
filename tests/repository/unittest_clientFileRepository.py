from unittest import TestCase

from domain.client import Client
from repository.clientFileRepository import ClientFileRepository


class TestClientFileRepository(TestCase):
    def setUp(self):
        f = open("testClienti.txt", "w")
        self.repository = ClientFileRepository("testClienti.txt")
        f.close()

    def testAdaugaClient(self):
        client = Client(1, "Andrei", "593185391")
        self.repository.adauga(client)
        with open("testClienti.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClient = line.split()[0]
                nume = line.split()[1]
                CNP = line.split()[2]
                clientNou = Client(idClient, nume, CNP)

        self.assertTrue(clientNou.getNume() == "Andrei")
        self.assertTrue(clientNou.getCNP() == "593185391")

    def testModificaClient(self):
        client = Client(1, "Andrei", "593185391")
        self.repository.adauga(client)
        client = Client(1, "Maria", "51953195")
        self.repository.modifica(client)

        with open("testClienti.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClient = line.split()[0]
                nume = line.split()[1]
                CNP = line.split()[2]
                clientNou = Client(idClient, nume, CNP)

        self.assertTrue(clientNou.getNume() == "Maria")
        self.assertTrue(clientNou.getCNP() == "51953195")

    def testStergeClient(self):
        client = Client(1, "Andrei", "593185391")
        self.repository.adauga(client)

        lista = []
        with open("testClienti.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClient = line.split()[0]
                nume = line.split()[1]
                CNP = line.split()[2]
                clientNou = Client(idClient, nume, CNP)
                lista.append(clientNou)

        self.assertTrue(len(lista) == 1)
        self.repository.sterge(1)

        with open("testClienti.txt", 'r') as f:
            lines = f.readlines()

        self.assertTrue(lines == [])

    def testReadFile(self):
        entitati = {}
        client = Client(1, "Andrei", "593185391")
        self.repository.adauga(client)

        with open("testClienti.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClient = line.split()[0]
                nume = line.split()[1]
                CNP = line.split()[2]
                clientNou = Client(idClient, nume, CNP)
                entitati[idClient] = clientNou

        self.assertTrue(str(client) == str(clientNou))
        self.assertTrue(idClient == "1")
        self.assertTrue(nume == "Andrei")
        self.assertTrue(CNP == "593185391")
        self.assertTrue(str(entitati["1"]) == "id: 1, nume: Andrei, CNP: 593185391")