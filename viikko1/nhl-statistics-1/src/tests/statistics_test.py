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