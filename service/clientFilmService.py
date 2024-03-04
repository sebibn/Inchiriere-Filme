from domain.dto.clientFilmDTO import FilmSortareDTOAssembler
from domain.clientFilm import ClientFilm
from domain.exceptii.duplicateError import DuplicateError
from repository.repository import Repository


class ClientFilmService:
    def __init__(self, clientFilmRepository: Repository,
                 clientRepository: Repository,
                 filmRepository: Repository):
        self.__clientFilmRepository = clientFilmRepository
        self.__clientRepository = clientRepository
        self.__filmRepository = filmRepository

    def adaugaInchiriere(self, idClientFilm, idClient, idFilm):
        if self.__clientRepository.getById(idClient) is None:
            raise KeyError("Nu exista un client cu id-ul dat")
        if self.__filmRepository.getById(idFilm) is None:
            raise KeyError("Nu exista un film cu id-ul dat")

        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient and inchiriere.getIdFilm() == idFilm:
                raise DuplicateError("Clientul a inchiriat deja filmul dat")

        inchiriere = ClientFilm(idClientFilm, idClient, idFilm)
        self.__clientFilmRepository.adauga(inchiriere)

    def getAllInchirieri(self):
        return self.__clientFilmRepository.getAll()

    def stergeInchiriere(self, idClient, idFilm):
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient and inchiriere.getIdFilm() == idFilm:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

    def celeMaiInchiriateFilme(self):
        film_dtos = self.__createFilmDTOs()
        film_dtos = sorted(film_dtos, key=lambda x:(x.titlu, x.nrInchirieri), reverse=False)
        for i in film_dtos:
            print(f"titlu: {i.titlu}, nr inchirieri: {i.nrInchirieri}")

    def __createFilmDTOs(self):
        film_dtos = []
        for film in self.__filmRepository.getAll():
            nr_inchirieri = self.__getInchirieri(film)
            dto = FilmSortareDTOAssembler.create_film_dto(film, nr_inchirieri)
            film_dtos.append(dto)
        return film_dtos

    def __getInchirieri(self, film):
        inchirieri = self.__clientFilmRepository.getAll()
        return list(filter(lambda f: f.getIdFilm() == film.getIdEntitate(), inchirieri))