from domain.film import Film
from repository.repository import Repository


class FilmFileRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, film):
        super().adauga(film)
        self.__writeFile()

    def modifica(self, film):
        super().modifica(film)
        self.__writeFile()

    def sterge(self, idFilm):
        super().sterge(idFilm)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idFilm = line.split(',')[0]
                titlu = line.split(',')[1]
                descriere = line.split(',')[2]
                gen = line.split(',')[3]
                film = Film(idFilm, titlu, descriere, gen)
                self._entitati[idFilm] = film

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for film in self.getAll():
                f.write(f'{film.getIdEntitate()},{film.getTitlu()},{film.getDescriere()},{film.getGen()},\n')