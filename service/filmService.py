from domain.dto.clientFilmDTO import ClientSortareDTOAssembler
from domain.film import Film
from repository.repository import Repository


class FilmService:
    def __init__(self, filmRepository: Repository, clientRepository: Repository, clientFilmRepository: Repository):
        self.__filmRepository = filmRepository
        self.__clientRepository = clientRepository
        self.__clientFilmRepository = clientFilmRepository

    def getAllFilme(self):
        '''
        returneaza lista de filme
        :return: o lista de obiecte de tipul Film
        '''
        return self.__filmRepository.getAll()

    def adaugaFilm(self, idFilm, titlu, descriere, gen):
        '''
        adauga un film
        :param idFilm: string
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return:
        '''
        film = Film(idFilm, titlu, descriere, gen)
        self.__filmRepository.adauga(film)

    def modificaFilm(self, idFilm, titluNou, descriereNoua, genNou):
        '''
        modifica un film dupa id
        :param idFilm: string
        :param titluNou: string
        :param descriereNoua: string
        :param genNou: string
        :return:
        '''
        filmNou = Film(idFilm, titluNou, descriereNoua, genNou)
        self.__filmRepository.modifica(filmNou)

    def stergeFilm(self, idFilm):
        '''
        sterge un film dupa id
        :param idFilm: string
        :return:
        '''
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm() == idFilm:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())
        self.__filmRepository.sterge(idFilm)

    def cautareFilme(self, titlu):
        '''
        cauta un film dupa titlu
        :param titlu: string
        :return: filmele cautate
        '''
        filme = self.__filmRepository.getAll()
        for film in filme:
            if film.getTitlu() == titlu:
                print(film)

    def rapoarteNrFilme(self):
        client_dtos = self.__createClientDTOs()
        client_dtos = sorted(client_dtos, key=lambda x:(x.nume, x.nrFilme), reverse=True)
        for i in client_dtos:
            print(f"nume: {i.nume}, nr filme: {i.nrFilme}")

    def __createClientDTOs(self):
        client_dtos = []
        for client in self.__clientRepository.getAll():
            filme_inchiriate = self.__getFilmeClient(client)
            dto = ClientSortareDTOAssembler.create_client_dto(client, filme_inchiriate)
            client_dtos.append(dto)
        return client_dtos

    def __getFilmeClient(self, client):
        inchirieri = self.__clientFilmRepository.getAll()
        return list(filter(lambda c: c.getIdClient() == client.getIdEntitate(), inchirieri))