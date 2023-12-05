from nltk.tokenize import sent_tokenize

class Exercise:
    def __init__(self, text: str):
        self.raw_text = text
        self.lemma_text = None
        self.tokens = None
        self.morph = None
        self.vector = None
        self.sentences = None  # массив

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

    def split_to_sentences(self):
        """
        люба
        разбить на предложения, сложить в массив
        :return:
        """
        self.sentences = sent_tokenize(self.raw_text)

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

"""
идеи для упражнений:
1. синонимы - Соня
2. антонимы - Соня
3. поменять структуру предложений (вопрос из утверждения и тд) - Полина
4. выбрать нужный падеж - Полина
5. выбрать правильную форму слова - Люба
6. выбрать из списка слов те, которые сочетаются с предложенным словом (найти колокации?) - Люба
"""