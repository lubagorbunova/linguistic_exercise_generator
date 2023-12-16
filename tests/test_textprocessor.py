import unittest
from src.exercise import SentProcessor


class SentProcessorBaseTests(unittest.TestCase):

    def test_sentprocessor_getrawtext(self):
        instance = SentProcessor('Кошка спит на диване!')
        self.assertEqual(instance.get_raw_text(), 'Кошка спит на диване!')

    def test_tokenise(self):
        instance = SentProcessor('Кошка спит на диване!')
        instance.process_text()
        self.assertEqual(instance.get_tokens(), ('кошка', 'спит', 'на', 'диване'))
