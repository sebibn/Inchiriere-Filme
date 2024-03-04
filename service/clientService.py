import operator
from domain.client import Client
from repository.repository import Repository


class ClientService:
    def __init__(self, clientRepository: Repository, clientFilmRepository: Repository):
        self.__clientRepository = clientRepository
        self.__clientFilmRepository = clientFilmRepository

    def getAllClienti(self):
        '''
        returneaza lista de clienti
        :return: o lista de obiecte de tipul Client
        '''
        return self.__clientRepository.getAll()

    def adaugaClient(self, idClient, nume, CNP):
        '''
        adauga un client
        :param idClient: string
        :param nume: string
        :param CNP: string
        :return:
        '''
        client = Client(idClient, nume, CNP)
        self.__clientRepository.adauga(client)

    def modificaClient(self, idClient, numeNou, CNPNou):
        '''
        modifica un client dupa id
        :param idClient: string
        :param numeNou: string
        :param CNPNou: string
        :return:
        '''
        clientNou = Client(idClient, numeNou, CNPNou)
        self.__clientRepository.modifica(clientNou)

    def stergeClient(self, idClient):
        '''
        sterge un client dupa id
        :param idClient: string
        :return:
        '''
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())
        self.__clientRepository.sterge(idClient)

    def cautareClienti(self, nume):
        '''
        cauta clientii cu numele dat
        :param nume: string
        :return: clientii cautati
        '''
        clienti = self.__clientRepository.getAll()
        for client in clienti:
            if client.getNume() == nume:
                print(client)

    def primii30Clienti(self):
        '''
        returneaza primii 30% clienti cu cele mai multe filme
        :return: primii 30% clienti cu cele mai multe filme
        '''
        clienti = self.__clientRepository.getAll()
        inchirieri = self.__clientFilmRepository.getAll()
        rez = []
        for client in clienti:
            rez.append([client.getIdEntitate(), 0])
        for inchiriere in inchirieri:
            if inchiriere.getIdEntitate() != "":
                rez[int(inchiriere.getIdEntitate())-1][1] += 1
        rez.sort(key=operator.itemgetter(1), reverse=True)
        for i in range(0,(int(len(rez)*0.3))):
            print("idClient: " + str(rez[i][0]) + ", nr filme inchiriate: " + str(rez[i][1]))