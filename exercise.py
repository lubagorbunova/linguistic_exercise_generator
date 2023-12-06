from nltk.tokenize import sent_tokenize
import string
from gensim.models.phrases import Phrases, Phraser
import multiprocessing
from gensim.models import Word2Vec
from navec import Navec


class TextProcessor:
    def __init__(self, text: str):
        self._raw_text = text
        self._lemma_text = None
        self._tokens = []
        self._morph = None
        self._vector = []
        self._sentences = None  # массив

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
        Люба
        найти векторы слов для упражнений на семантику
        :return:
        """
        path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
        navec = Navec.load(path)
        for token in self._tokens:
            self._vector.append(navec[token])


    def split_to_sentences(self):
        """
        люба
        разбить на предложения, сложить в массив
        :return:
        """
        self._sentences = sent_tokenize(self._raw_text)

    def process_text(self):
        """
        заполняет все атрибуты класса? делает всю обработку текста?
        :return:
        """
        self.tokenise_text()
        self.lemmatise_text()
        self.morph_text()
        self.vectorize_text()
        self.split_to_sentences()
        self.vectorize_text()

    def get_raw_text(self):
        return self._raw_text

    def get_lemmas(self):
        return self._lemma_text

    def get_morph(self):
        return self._morph

    def get_sentences(self):
        return self._sentences

    def get_tokens(self):
        return self._tokens

    def get_vectors(self):
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