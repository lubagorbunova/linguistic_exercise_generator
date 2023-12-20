import unittest
from src.exercise import SentProcessor, Exercise
import numpy
from pymorphy2.tagset import OpencorporaTag
from src.word import Word


class SentProcessorBaseTests(unittest.TestCase):

    def test_getrawtext(self):
        sentences = ['Кошка спит на диване', 'Кошка спит', 'кошка,,,,, спит.....']
        for sent in sentences:
            instance = SentProcessor(sent)
            self.assertEqual(instance.get_raw_text(), sent)

    def test_getrawtext_corrupted(self):
        instance = SentProcessor(None)
        self.assertEqual(instance.get_raw_text(), None)

    def test_getrawinput_incorrect_input(self):
        sentences = [123, ('Кошка спит', ), [None]]
        for sent in sentences:
            instance = SentProcessor(sent)
            self.assertEqual(instance.get_raw_text(), None)

    def test_tokenise(self):
        instance = SentProcessor('Кошка спит на диване!')
        instance.process_text()
        self.assertEqual(instance._tokens, ['кошка', 'спит', 'на', 'диване'])

    def test_lemmas(self):
        text = 'Кошка спит на диване!'
        instance = SentProcessor(text)
        instance.process_text()
        expected_lemmas = ['кошка', 'спать', 'на', 'диван']
        self.assertEqual(instance._lemma_text, expected_lemmas)

    def test_lemma_text_empty_after_processing_empty_text(self):
        empty_text = ''
        instance = SentProcessor(empty_text)
        instance.process_text()
        expected_lemmas = []
        self.assertEqual(instance._lemma_text, expected_lemmas)

    def test_get_lemmas_unusual_characters(self):
        text = 'Кошка спит....zzZZzz'
        instance = SentProcessor(text)
        instance.process_text()
        lemmas = instance.get_lemmas()
        expected_lemmas = ['кошка', 'спать', 'zzzzzz']
        self.assertEqual(lemmas, expected_lemmas)

    def test_get_lemmas_no_words(self):
        text = '!@#$%^&*()'
        instance = SentProcessor(text)
        instance.process_text()
        lemmas = instance.get_lemmas()
        expected_lemmas = []
        self.assertEqual(lemmas, expected_lemmas)

    def test_vectorise(self):
        sentences = ['Кошка', 'stjrdvrdjfvkjy']
        for sent in sentences:
            instance = SentProcessor(sent)
            instance.process_text()
            self.assertEqual(type(instance._vector[sent.lower()]), numpy.ndarray)

    def test_vectorise_corrupted_input(self):
        instance = SentProcessor('')
        instance.process_text()
        self.assertEqual(instance._vector, {})

    def test_get_vectors_access_check(self):
        instance = SentProcessor('кошка')
        instance._vector = 0
        self.assertEqual(instance.get_vectors(), 0)

    def test_get_vectors_type_check(self):
        instance = SentProcessor('кошка')
        instance.process_text()
        self.assertEqual(type(instance.get_vectors()['кошка']), numpy.ndarray)
        self.assertEqual(type(instance.get_vectors()), dict)

    def test_process_text_values(self):
        instance = SentProcessor('Кошка спит на диване 0!')
        instance.process_text()
        self.assertEqual(instance._tokens, ['кошка', 'спит', 'на', 'диване', '0'])
        self.assertEqual(instance._lemma_text, ['кошка', 'спать', 'на', 'диван', '0'])
        self.assertEqual(instance._morph, [OpencorporaTag('NOUN,anim,femn sing,nomn'),
                                                OpencorporaTag('VERB,impf,intr sing,3per,pres,indc'),
                                                OpencorporaTag('PREP'),
                                                OpencorporaTag('NOUN,inan,masc sing,loct'),
                                                OpencorporaTag('NUMB,intg')])
        for vector in instance._vector.values():
            self.assertEqual(type(vector), numpy.ndarray)

    def test_process_text_types(self):
        instance = SentProcessor('Кошка спит на диване 0!')
        instance.process_text()
        self.assertEqual(type(instance.get_tokens()[0]), str)
        self.assertEqual(type(instance.get_lemmas()[0]), str)
        self.assertEqual(type(instance.get_morph()[0]), OpencorporaTag)
        self.assertEqual(type(instance.get_vectors()['кошка']), numpy.ndarray)

        self.assertEqual(type(instance.get_tokens()), list)
        self.assertEqual(type(instance.get_lemmas()), list)
        self.assertEqual(type(instance.get_morph()), list)
        self.assertEqual(type(instance.get_vectors()), dict)


class ExerciseBaseTests(unittest.TestCase):

    def test_generate_scrambled_sentence_none(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        instance = Exercise(sents)
        instance.generate_scrambled_sentence()
        self.assertIsNotNone(instance.third_ex)
        self.assertIsNotNone(instance.third_answers)

    def test_generate_scrambled_sentence(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.generate_scrambled_sentence()
        test_value = False
        if ex.third_ex == '\nЗадание №3. Составьте предложение из слов и поставьте их в правильную форму:\n[спать], [кошка]\n'\
                or ex.third_ex == '\nЗадание №3. Составьте предложение из слов и поставьте их в правильную форму:\n[кошка], [спать]\n':
            test_value = True
        self.assertTrue(test_value, 'WRONG OPTIONS')
        self.assertEqual(ex.third_answers, '\nОтветы на задание №3:\nКошка спит.\n')

    def test_generate_case_exercise(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.generate_case_exercise()

        self.assertEqual(ex.fourth_ex,
                         f"Задание №4: Выберите правильный падеж для слова 'КОШКА' в предложении 'Кошка спит':\n")

        self.assertEqual(ex.fourth_answers, f"Правильный ответ: Именительный")

    def test_generate_case_exercise(self):
        sent = SentProcessor('Кошка спит')
        sent.process_text()
        sents = []
        sents.append(sent)
        instance = Exercise(sents, number_of_sent_in_each_ex=1)
        instance.generate_case_exercise()
        self.assertIsNotNone(instance.fourth_ex)
        self.assertIsNotNone(instance.fourth_answers)

    def test_select_grammatical_form_correct_input(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.select_grammatical_form(1)
        self.assertEqual(ex.fifth_ex , '\nЗадание №5: Поставьте слово в скобках в правильную форму:\n_____ [кошка] _____ [спать].\n')
        self.assertEqual(ex.fifth_answers, '\nОтветы на задание №5: \nКошка спит.\n')

    def test_select_grammatical_form_empty_input(self):
        sents = []
        sent = SentProcessor('')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.select_grammatical_form(1)
        self.assertEqual(ex.fifth_ex , '\nЗадание №5: Поставьте слово в скобках в правильную форму:\n\n')
        self.assertEqual(ex.fifth_answers, '\nОтветы на задание №5: \n\n')

    def test_select_grammatical_form_no_nouns_or_verbs(self):
        sents = []
        sent = SentProcessor('И где опять?')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.select_grammatical_form(1)
        self.assertEqual(ex.fifth_ex , '\nЗадание №5: Поставьте слово в скобках в правильную форму:\nИ где опять?\n')
        self.assertEqual(ex.fifth_answers, '\nОтветы на задание №5: \nИ где опять?\n')

    def test_find_collocations(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.find_collocations(1)
        self.assertEqual(ex.sixth_ex, '\nЗадание №6: Выберите одно или несколько слов из списка, которые подходят в предложение по смыслу.\nПоставьте слово в правильную форму.\n_____[девочка, животное, кошка, птица, рыба, собака] спит.\n')
        self.assertEqual(ex.sixth_answers, '\nОтветы на задание №6:\nКошка спит.')

    def test_find_collocations_no_nouns(self):
        sents = []
        sent = SentProcessor('Крепко спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents)
        ex.find_collocations(1)
        self.assertEqual(ex.sixth_ex, '\nЗадание №6: Выберите одно или несколько слов из списка, которые подходят в предложение по смыслу.\nПоставьте слово в правильную форму.\nКрепко спит.\n')
        self.assertEqual(ex.sixth_answers, '\nОтветы на задание №6:\nКрепко спит.')

    def test_synonyms(self):
        word = Word('холодный', 0)
        word.extract_synonyms_antonyms('холодный')
        correct = {'ледяной', 'студёный', 'холодный'}
        res = word.get_synonyms()
        test_value = []
        if len(correct) == len(res):
            for el in correct:
                if el in res:
                    test_value.append(True)
        msg = 'Something is wrong'
        self.assertTrue(all(test_value), msg)

    def test_antonyms(self):
        word = Word('холодный', 0)
        word.extract_synonyms_antonyms('холодный')
        correct = {'нехолодный', 'теплый по цвету', 'теплый'}
        res = word.get_antonyms()
        test_value = []
        if len(correct) == len(res):
            for el in correct:
                if el in res:
                    test_value.append(True)
        msg = 'Something is wrong'
        self.assertTrue(all(test_value), msg)

    def test_run_exercises(self):
        pass

    def test_run_exercises_incorrect_input(self):
        pass

    def form_exercises(self):
        pass

    def form_exercises_before_form(self):
        pass