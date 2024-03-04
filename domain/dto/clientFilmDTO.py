from dataclasses import dataclass

@dataclass()
class ClientSortareDTO:
    nume : str
    nrFilme : int

@dataclass()
class FilmSortareDTO:
    titlu : str
    nrInchirieri : int

class ClientSortareDTOAssembler:
    @staticmethod
    def create_client_dto(client, filme_inchiriate):

        nume = client.getNume()
        n = len(filme_inchiriate)

        return ClientSortareDTO(nume, n)

class FilmSortareDTOAssembler:
    @staticmethod
    def create_film_dto(film, inchirieri):

        titlu = film.getTitlu()
        n = len(inchirieri)

        return FilmSortareDTO(titlu, n)