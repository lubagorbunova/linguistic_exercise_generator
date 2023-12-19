import unittest
from src.exercise import SentProcessor, Exercise
import numpy
from pymorphy2.tagset import OpencorporaTag
from src.word import Word


class SentProcessorBaseTests(unittest.TestCase):

    def test_sentprocessor_getrawtext(self):
        instance = SentProcessor('Кошка спит на диване!')
        self.assertEqual(instance.get_raw_text(), 'Кошка спит на диване!')

    def test_tokenise(self):
        instance = SentProcessor('Кошка спит на диване!')
        instance.process_text()
        self.assertEqual(instance._tokens, ['кошка', 'спит', 'на', 'диване'])

    def test_vectorise(self):
        sentences = ['Кошка', 'stjrdvrdjfvkjy']
        for sent in sentences:
            instance = SentProcessor(sent)
            instance.process_text()
            self.assertEqual(type(instance._vector[sent.lower()]), numpy.ndarray)

        instance = SentProcessor('')
        instance.process_text()
        self.assertEqual(instance._vector, {})

    def test_get_vectors(self):
        instance = SentProcessor('кошка')
        instance._vector = 0
        self.assertEqual(instance.get_vectors(), 0)


    def test_process_text(self):
        instance = SentProcessor('Кошка спит на диване 0!')
        instance.process_text()
        self.assertEqual(instance.get_tokens(), ['кошка', 'спит', 'на', 'диване', '0'])
        self.assertEqual(instance.get_lemmas(), ['кошка', 'спать', 'на', 'диван', '0'])
        self.assertEqual(instance.get_morph(), [OpencorporaTag('NOUN,anim,femn sing,nomn'), OpencorporaTag('VERB,impf,intr sing,3per,pres,indc'),
         OpencorporaTag('PREP'), OpencorporaTag('NOUN,inan,masc sing,loct'), OpencorporaTag('NUMB,intg')])
        for vector in instance.get_vectors().values():
            self.assertEqual(type(vector), numpy.ndarray)


class ExerciseBaseTests(unittest.TestCase):

    def test_select_grammatical_form(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.select_grammatical_form(1)
        self.assertEqual(ex.fifth_ex , '_____ [кошка] _____ [спать].\n')
        self.assertEqual(ex.fifth_answers, 'Кошка спит.\n')

    def test_find_collocations(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.find_collocations(1)
        self.assertEqual(ex.sixth_ex, '_____[девочка, животное, кошка, птица, рыба, собака] спит.\n')
        self.assertEqual(ex.sixth_answers, '\nКошка спит.')

    def test_antonyms(self):
        word = Word('холодный', 0)
        word.extract_synonyms_antonyms('холодный')
        test_value = False
        correct = {'нехолодный', 'теплый по цвету', 'теплый'}
        if all(correct) in word.get_antonyms():
            test_value = True
        msg = 'Something is wrong'
        self.assertTrue(test_value, msg)

    def test_synonyms(self):
        word = Word('холодный', 0)
        word.extract_synonyms_antonyms('холодный')
        correct = {'ледяной', 'студёный', 'холодный'}
        test_value = False
        if all(correct) in word.get_synonyms():
            test_value = True
        msg = 'Something is wrong'
        self.assertTrue(test_value, msg)
