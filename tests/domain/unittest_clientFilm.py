from unittest import TestCase

class TestClientFilm(TestCase):
    def setUp(self):
        from domain.clientFilm import ClientFilm
        self.clientFilm = ClientFilm(1, 1, 1)

    def testId(self):
        self.assertTrue(self.clientFilm.getIdEntitate() == 1)
        self.clientFilm.setIdEntitate(2)
        self.assertTrue(self.clientFilm.getIdEntitate() == 2)

    def testIdClient(self):
        self.assertTrue(self.clientFilm.getIdClient() == 1)
        self.clientFilm.setIdClient(2)
        self.assertTrue(self.clientFilm.getIdClient() == 2)

    def testIdFilm(self):
        self.assertTrue(self.clientFilm.getIdFilm() == 1)
        self.clientFilm.setIdFilm(2)
        self.assertTrue(self.clientFilm.getIdFilm() == 2)

    def testStr(self):
        self.assertTrue(self.clientFilm.__str__() == f'id: {self.clientFilm.getIdEntitate()}, id client: {self.clientFilm.getIdClient()}, id film: {self.clientFilm.getIdFilm()}')

    def tearDown(self) -> None:
        pass