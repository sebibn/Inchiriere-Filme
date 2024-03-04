from repository.clientFileRepository import ClientFileRepository
from repository.clientFilmFileRepository import ClientFilmFileRepository
from repository.filmFileRepository import FilmFileRepository
from service.clientService import ClientService
from service.clientFilmService import ClientFilmService
from service.filmService import FilmService
from ui.consola import Consola


def main():
    clientFileRepository = ClientFileRepository("clienti.txt")
    filmFileRepository = FilmFileRepository("filme.txt")
    clientFilmRepository = ClientFilmFileRepository("inchirieri.txt")

    clientService = ClientService(clientFileRepository, clientFilmRepository)
    filmService = FilmService(filmFileRepository, clientFileRepository, clientFilmRepository)
    clientFilmService = ClientFilmService(clientFilmRepository, clientFileRepository, filmFileRepository)

    consola = Consola(filmService, clientService, clientFilmService)

    consola.meniu()

main()