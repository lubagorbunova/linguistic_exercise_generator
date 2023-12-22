import unittest
from src.exercise import SentProcessor, Exercise
import numpy
from pymorphy2.tagset import OpencorporaTag
from src.files import NothingToWriteError

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

    def test_syn_exercise(self):
        sents = []
        sent = SentProcessor('Крепко спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents, number_of_sent_in_each_ex=1)
        ex.syn_ant_exercise('synonym')
        value = False
        if ex.first_ex and ex.first_answers:
            value = True
        self.assertTrue(value, 'Упражнение не создано.')

    def test_run_exercises_correct_ex_exist(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents, number_of_sent_in_each_ex=1)
        ex.run_exercises([3, 6])
        value = False
        if (len(ex.third_ex) != 0) and \
            (len(ex.third_answers) != 0) and \
            (len(ex.sixth_ex) != 0) and \
            (len(ex.sixth_answers) != 0):
            value = True
        self.assertTrue(value, msg='Упражнения не сформированы')

    def test_run_exercises_wrong_ex_run(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents, number_of_sent_in_each_ex=1)
        ex.run_exercises([3, 6, 4, 5])
        value = False
        if (len(ex.first_ex) == 0) and \
                (len(ex.first_answers) == 0) and \
                (len(ex.second_ex) == 0) and \
                (len(ex.second_answers) == 0):
            value = True
        self.assertTrue(value, msg='Лишние упражнения сформированы')

    def test_form_exercises(self):
        sents = []
        sent = SentProcessor('Кошка.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents, number_of_sent_in_each_ex=1)
        ex.run_exercises([3])
        exercises, answers = ex.form_exercises()
        self.assertEqual(exercises, '\nЗадание №3. Составьте предложение из слов '
                                    'и поставьте их в правильную форму:\n[кошка]\n')
        self.assertEqual(answers, '\nОтветы на задание №3:\nКошка.\n')

    def test_form_exercises_before_form(self):
        sents = []
        sent = SentProcessor('Кошка спит.')
        sent.process_text()
        sents.append(sent)
        ex = Exercise(sents, number_of_sent_in_each_ex=1)
        with self.assertRaises(NothingToWriteError):
            ex.form_exercises()
