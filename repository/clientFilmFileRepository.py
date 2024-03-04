from domain.clientFilm import ClientFilm
from repository.repository import Repository


class ClientFilmFileRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self._readFile()

    def adauga(self, clientFilm):
        super().adauga(clientFilm)
        self.__writeFile()

    def modifica(self, clientFilm):
        super().modifica(clientFilm)
        self.__writeFile()

    def sterge(self, idClientFilm):
        super().sterge(idClientFilm)
        self.__writeFile()

    def _readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idClientFilm = line.split()[0]
                idClient = line.split()[1]
                idFilm = line.split()[2]
                clientFilm = ClientFilm(idClientFilm, idClient, idFilm)
                self._entitati[idClientFilm] = clientFilm

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for clientFilm in self.getAll():
                f.write(f'{clientFilm.getIdEntitate()} {clientFilm.getIdClient()} {clientFilm.getIdFilm()}\n')