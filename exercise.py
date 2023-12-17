import random

from navec import Navec
from nltk.tokenize import sent_tokenize
import nltk.text
from pathlib import Path
from pymorphy2 import MorphAnalyzer
import os.path
from typing import List


from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
ASSETS_PATH = PROJECT_ROOT / 'tmp' / 'articles'
punctuation = r'''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~«»—'''

class SentProcessor:
    """
    Предобрабатывает исходный текст:
    разбивает на токены, находит начальные формы, морфологические признаки и векторы.
    """
    def __init__(self, text: str):
        self._raw_text = text
        self._lemma_text = None
        self._tokens = []
        self._morph_analyzer = MorphAnalyzer()
        self._morph = None
        self._vector = {}

    def _tokenise_text(self, text: str) -> None:
        """
        Очищает текст от знаков препинания, приводит к нижнему регистру, разбивает на токены
        return: None
        """
        for el in punctuation:
            text = text.replace(el, ' ')
        self._tokens = tuple(text.lower().split())

    def _lemmatise_text(self):
        """
        Полина
        посмотреть прошлогоднюю лабу
        :return:
        """
        self._lemma_text = [self._morph_analyzer.parse(token)[0].normal_form for token in self._tokens]

    def _morph_text(self):
        """
        Полина
        выделить морфологические признаки слов
        :return:
        """
        self._morph = [self._morph_analyzer.parse(token)[0].tag for token in self._tokens]

    def _vectorize_text(self):
        """
        предобученная на основе корпуса художественных текстов на русском языке модель
        находит векторы для каждого токена. Пары токен-вектор хранятся в словаре
        :return: None
        """
        path = os.path.dirname(__file__) + '/../navec_hudlit_v1_12B_500K_300d_100q.tar'
        navec = Navec.load(path)
        for token in self._tokens:
            if token in navec.vocab:
                self._vector[token] = navec[token]
            else:
                self._vector[token] = None

    def process_text(self):
        """
        Выполняет предобработку текста.
        :return: None
        """
        self._tokenise_text(self.get_raw_text())
        self._lemmatise_text()
        self._morph_text()
        self._vectorize_text()

    def get_raw_text(self):
        """
        возвращает исходный текст
        :return:
        """
        return self._raw_text

    def get_lemmas(self):
        """
        возвращает словарные формы слов
        :return:
        """
        return self._lemma_text

    def get_morph(self):
        """
        возвращает морфологические признаки слов
        :return:
        """
        return self._morph

    def get_tokens(self):
        """
        возвращает токены
        :return:
        """
        return self._tokens

    def get_vectors(self):
        """
        возвращает словарь, ключи в котором - токены, а значения - векторы.
        :return: dict
        """
        return self._vector


class Exercise:
    def __init__(self, processed_text: List[SentProcessor]):
        """
        идеи для упражнений:
        1. синонимы - Соня
        2. антонимы - Соня
        3. поменять структуру предложений (вопрос из утверждения и тд) - Полина
        4. выбрать нужный падеж - Полина
        5. выбрать правильную форму слова - Люба
        6. выбрать из списка слов те, которые сочетаются с предложенным словом (найти колокации?) - Люба
        """
        self._morph_analyzer = MorphAnalyzer()
        self.processed_text = processed_text
        self.first_ex = '' #функции упражнений записывают строки в атрибуты
        self.second_ex = ''
        self.third_ex = ''
        self.third_answers = ''
        self.fourth_ex = ''
        self.fourth_answers = ''
        self.fifth_ex = ''
        self.fifth_answers = ''
        self.sixth_ex = ''
        self.sixth_answers = ''

    def form_exercises(self):
        '''
        объединяет все упражнения в один файл
        :return:
        '''

    def generate_scrambled_sentence(self):
        sentence = random.choice(self.processed_text)  # Выбираем случайное предложение из обработанного текста
        lemmas = sentence.get_lemmas()
        random.shuffle(lemmas)

        lemmatized_tokens = ', '.join(f'[{lemma}]' for lemma in lemmas)

        exercise_task = f"Составьте предложение из слов и поставьте их в правильную форму:\n{lemmatized_tokens}"

        full_text = sentence.get_raw_text()

        self.third_ex = exercise_task
        self.third_answers = full_text

    def generate_case_exercise(self):
        sentence = random.choice(self.processed_text)
        tokens = list(sentence.get_tokens())

        candidates = [word for word in tokens if 'NOUN' in self._morph_analyzer.parse(word)[0].tag]

        if not candidates:
            return "В данном предложении нет существительных."

        random.shuffle(tokens)

        word_to_change = random.choice(candidates)
        word_to_change1 = word_to_change.upper()

        raw_sentence = sentence.get_raw_text()

        # Словарь для соответствия аббревиатур падежей и их русских названий
        cases_dict = {
            'nomn': 'Именительный',
            'gent': 'Родительный',
            'datv': 'Дательный',
            'accs': 'Винительный',
            'ablt': 'Творительный',
            'loct': 'Предложный'
        }

        correct_case_abbr = self._morph_analyzer.parse(word_to_change)[0].tag.case
        correct_case = cases_dict.get(correct_case_abbr)

        exercise_task = f"Задание №4: Выберите правильный падеж для слова '{word_to_change1}' в предложении '{raw_sentence}':\n"

        exercise_task += f"1. {cases_dict['nomn']}\n"
        exercise_task += f"2. {cases_dict['gent']}\n"
        exercise_task += f"3. {cases_dict['datv']}\n"
        exercise_task += f"4. {cases_dict['accs']}\n"
        exercise_task += f"5. {cases_dict['ablt']}\n"
        exercise_task += f"6. {cases_dict['loct']}"

        full_text = f"Правильный ответ: {correct_case}"

        self.fourth_ex = exercise_task
        self.fourth_answers = full_text


    def select_grammatical_form(self):
        """
        выбрать правильную форму слова
        :return:
        """
        sentences = random.sample(self.processed_text, 5)
        full_text = ''
        text = ''

        for sent in sentences:
            sent_text = sent.get_raw_text()
            full_text += sent_text
            morphs = sent.get_morph()
            tokens = sent.get_tokens()
            lemmas = sent.get_lemmas()
            possible_change = []

            for i in range(len(tokens)):
                if ('NOUN' in str(morphs[i])) or ('VERB' in str(morphs[i])):
                    possible_change.append(i)

            to_change_index = random.sample(possible_change, 3)
            to_change = {}

            for ind in to_change_index:
                to_change[tokens[ind]] = f'_____ [{lemmas[ind]}]'

            for old, new in to_change.items():
                sent_text = sent_text.replace(old, new, 1)
            text += sent_text + '\n'

        self.fifth_ex = text
        self.fifth_answers = full_text

    def find_collocations(self):
        """
        выбрать из списка слов те, которые сочетаются с предложенным словом (найти колокации?)
        :return:
        """
        sentences = random.sample(self.processed_text, 5)
        full_text = ''
        text = ''

        for sent in sentences:
            sent_text = sent.get_raw_text()
            full_text += sent_text
            vectors = sent.get_vectors()
            tokens = sent.get_tokens()
            lemmas = sent.get_lemmas()
            morphs = sent.get_morph()
            possible_change = []

            for i in range(len(tokens)):
                if 'NOUN' in str(morphs[i]):
                    possible_change.append(i)

            to_change_index = random.sample(possible_change, 3)
            to_change = {}

            for ind in to_change_index:
                to_change[tokens[ind]] = f'_____ [{vectors[ind]}]'

            for old, new in to_change.items():
                sent_text = sent_text.replace(old, new, 1)
            text += sent_text + '\n'

        self.sixth_ex = text
        self.sixth_answers = full_text


class FinalFiles:
    def __init__(self):
        pass

    def get_exercises_path(self) -> Path:
        """
        Returns path for requested exercise
        """
        exercise_name = f"exercise_raw.txt"
        return ASSETS_PATH / exercise_name

    def write_to_file(self, ex_text: str) -> None:
        """
        Соня
        файл с упражнениями, который передается пользователю
        :return:
        """
        with open(self.get_exercises_path(), 'w', encoding='utf-8') as file:
            file.write(ex_text)
