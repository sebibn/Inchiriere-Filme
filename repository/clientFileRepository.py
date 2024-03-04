from domain.client import Client
from repository.repository import Repository


class ClientFileRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, client):
        super().adauga(client)
        self.__writeFile()

    def modifica(self, client):
        super().modifica(client)
        self.__writeFile()

    def sterge(self, idClient):
        super().sterge(idClient)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClient = line.split()[0]
                nume = line.split()[1]
                CNP = line.split()[2]
                client = Client(idClient, nume, CNP)
                self._entitati[idClient] = client

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for client in self.getAll():
                f.write(f'{client.getIdEntitate()} {client.getNume()} {client.getCNP()}\n')