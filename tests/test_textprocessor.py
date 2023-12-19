from src.exercise import SentProcessor, Exercise
from src.word import Word
import unittest


class SentProcessorBaseTests(unittest.TestCase):

    def test_sentprocessor_getrawtext(self):
        instance = SentProcessor('Кошка спит на диване!')
        self.assertEqual(instance.get_raw_text(), 'Кошка спит на диване!')

    def test_tokenise(self):
        instance = SentProcessor('Кошка спит на диване!')
        instance.process_text()
        self.assertEqual(instance.get_tokens(), ['кошка', 'спит', 'на', 'диване'])

    def test_antonyms(self):
        word = Word('холодный', 0)
        word. extract_synonyms_antonyms('холодный')
        correct = {'нехолодный', 'теплый по цвету', 'теплый'}
        if all(correct) in word.get_antonyms:
            test_value = True
        msg = 'Something is wrong'
        self.assertTrue(test_value, msg)

    def test_synonyms(self):
        word = Word('холодный', 0)
        word.extract_synonyms_antonyms('холодный')
        correct = {'ледяной', 'студёный', 'холодный'}
        if all(correct) in word.get_synonyms:
            test_value = True
        msg = 'Something is wrong'
        self.assertTrue(test_value, msg)