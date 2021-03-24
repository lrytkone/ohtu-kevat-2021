import unittest
from ..statistics import Statistics
from ..player_reader_stub import PlayerReaderStub


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_oikean_joukkueen_pelaajat(self):
        edm = self.statistics.team("EDM")
        players = len(edm)
        self.assertEqual(players, 3)

    def test_haku(self):
        self.assertEqual(self.statistics.search("Yze").name, "Yzerman")

    def test_top_scorers(self):
        top = self.statistics.top_scorers(3)
        self.assertEqual(top[0].name,"Gretzky")

    def test_tyhjahaku(self):
        player = self.statistics.search("Hansen")
        self.assertEqual(player, None)