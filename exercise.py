from nltk.tokenize import sent_tokenize
from navec import Navec


class TextProcessor:
    """
    Предобрабатывает исходный текст:
    разбивает на токены, находит начальные формы, морфологические признаки и векторы.
    """
    def __init__(self, text: str):
        self._raw_text = text
        self._lemma_text = None
        self._tokens = []
        self._morph = None
        self._vector = {}
        self._sentences = []

    def tokenise_text(self):
        """
        Соня
        посмотреть прошлогоднюю лабу
        :return:
        """

    def lemmatise_text(self):
        """
        Полина
        посмотреть прошлогоднюю лабу
        :return:
        """

    def write_to_file(self):
        """
        Соня
        файл с упражнениями, который передается пользователю
        :return:
        """

    def morph_text(self):
        """
        Полина
        выделить морфологические признаки слов
        :return:
        """

    def vectorize_text(self):
        """
        предобученная на основе корпуса художественных текстов на русском языке модель
        находит векторы для каждого токена. Пары токен-вектор хранятся в словаре
        :return: None
        """
        path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
        navec = Navec.load(path)
        for token in self._tokens:
            self._vector[token] = navec[token]

    def split_to_sentences(self):
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
        self.tokenise_text()
        self.lemmatise_text()
        self.morph_text()
        self.vectorize_text()
        self.split_to_sentences()
        self.vectorize_text()

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