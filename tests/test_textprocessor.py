import unittest
from src.exercise import SentProcessor


class SentProcessorBaseTests(unittest.TestCase):

    def test_sentprocessor_getrawtext(self):
        instance = SentProcessor('кошка спит на диване!')
        self.assertEqual(instance.get_raw_text(), 'кошка спит на диване!')
