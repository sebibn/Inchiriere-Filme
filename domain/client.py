from domain.entitate import Entitate

class Client(Entitate):
    def __init__(self, idClient, nume, CNP):
        super().__init__(idClient)
        self.__nume = nume
        self.__CNP = CNP

    def getNume(self):
        return self.__nume

    def getCNP(self):
        return self.__CNP

    def setNume(self, nume):
        self.__nume = nume

    def setCNP(self, CNP):
        self.__CNP = CNP

    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}, CNP: {self.__CNP}"