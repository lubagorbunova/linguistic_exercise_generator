from constants import punctuation, ASSETS_PATH
from navec import Navec
from nltk.tokenize import sent_tokenize
from pathlib import Path
from pymorphy2 import MorphAnalyzer


class TextProcessor:
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
        self._sentences = []

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
        path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
        navec = Navec.load(path)
        for token in self._tokens:
            self._vector[token] = navec[token]

    def _split_to_sentences(self):
        """
        Разбивает исходный текст на предложения, сохраняя исходное форматирование
        :return: None
        """
        self._sentences = sent_tokenize(self._raw_text)

    def process_text(self):
        """
        Выполняет предобработку текста.
        :return: None
        """
        self._tokenise_text(self.get_raw_text())
        self._lemmatise_text()
        self._morph_text()
        self._vectorize_text()
        self._split_to_sentences()

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

    def get_sentences(self):
        """
        возвращает список предложений с исходным форматирвоанием
        :return: list
        """
        return self._sentences

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
    def __init__(self, processed_text: TextProcessor):
        """
        идеи для упражнений:
        1. синонимы - Соня
        2. антонимы - Соня
        3. поменять структуру предложений (вопрос из утверждения и тд) - Полина
        4. выбрать нужный падеж - Полина
        5. выбрать правильную форму слова - Люба
        6. выбрать из списка слов те, которые сочетаются с предложенным словом (найти колокации?) - Люба
        """
        self.processed_text = processed_text
        self.first_ex = '' #функции упражнений записывают строки в атрибуты
        self.second_ex = ''
        self.third_ex = ''
        self.fourth_ex = ''
        self.fifth_ex = ''
        self.sixth_ex = ''

    def form_exercises(self):
        '''
        объединяет все упражнения в один файл
        :return:
        '''


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
