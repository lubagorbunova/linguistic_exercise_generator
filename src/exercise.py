import random
import re
from src.constants import punctuation, ASSETS_PATH, most_frequent_nouns
from navec import Navec
from pathlib import Path
from pymorphy2 import MorphAnalyzer
from typing import List
from numpy import dot
from src.word import Word
from numpy.linalg import norm
import heapq

import os.path
import random


path = os.path.dirname(__file__) + '/../navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)

class SentProcessor:
    """
    Предобрабатывает исходный текст:
    разбивает на токены, находит начальные формы, морфологические признаки и векторы.
    """
    def __init__(self, text: str):
        self._raw_text = text
        self._lemma_text = None
        self._tokens = None
        self._morph_analyzer = MorphAnalyzer()
        self._morph = None
        self._vector = {}

    def _tokenise_text(self) -> None:
        """
        Очищает текст от знаков препинания, приводит к нижнему регистру, разбивает на токены
        return: None
        """
        for el in punctuation:
            self._raw_text = self._raw_text.replace(el, ' ')
        self._tokens = self._raw_text.lower().split()

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
        for lemma in self._lemma_text:
            if lemma in navec.vocab:
                self._vector[lemma] = navec[lemma]
            else:
                self._vector[lemma] = navec['<pad>']

    def process_text(self):
        """
        Выполняет предобработку текста.
        :return: None
        """
        self._tokenise_text()
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
        self.processed_text = processed_text
        # функции упражнений записывают строки в атрибуты
        self.first_ex = ''
        self.first_answers = ''
        self.second_ex = ''
        self.second_answers = ''
        self.third_ex = ''
        self.fourth_ex = ''
        self.fifth_ex = ''
        self.fifth_answers = ''
        self.sixth_ex = ''
        self.sixth_answers = ''

    def form_exercises(self):
        '''
        объединяет все упражнения в один файл
        :return:
        '''

        self.syn_ant_exercise('synonym')
        self.syn_ant_exercise('antonym')

    def syn_ant_exercise(self, task_type: str):
        sentence = random.choice(self.processed_text)
        lemmas = sentence.get_lemmas()
        synonyms = {}
        antonyms = {}
        for i, lemma in enumerate(lemmas):
            word = Word(lemma, i)
            word.fill_sets()
            if len(word.get_synonyms()) >= 1:
                synonyms[i] = word.get_synonyms()
            if len(word.get_antonyms()) >= 1:
                antonyms[i] = word.get_antonyms()
        new_sentence = sentence.get_tokens()

        if task_type == 'synonym':
            if len(synonyms) == 0:
                self.first_ex = 'NO TASK WITH SYNONYMS'
            target_word, correct, synonym_task, = self._get_options(synonyms, lemmas)
            new_sentence[target_word] = new_sentence[target_word].upper()
            self.first_ex = f"""Выберите синоним к выделенному слову: \n
    {' '.join(new_sentence)} \n
    {synonym_task}"""

        if task_type == 'antonym':
            if len(antonyms) == 0:
                self.second_ex = 'NO TASK WITH ANTONYMS'
            target_word, correct, antonym_task = self._get_options(antonyms, lemmas)
            new_sentence[target_word] = new_sentence[target_word].upper()
            self.second_ex = f"""Выберите антоним к выделенному слову: \n
    {' '.join(new_sentence)} \n
    {antonym_task}"""
            self.second_answers = correct

    def _get_options(self, thesaurus: dict, lemmas: list[str]):
        answer = ''
        word_id = 0
        num_words = 0
        while num_words <= 1:
            word_id = random.choice(list(thesaurus.keys()))
            limit = random.randint(0, len(thesaurus[word_id]) - 1)
            answer = random.sample(list(thesaurus[word_id]), 1)[random.randint(0, limit)]
            if answer == lemmas[word_id]:
                num_words = 0
            else:
                num_words = len(thesaurus[word_id])
        options = []
        for i in list(thesaurus.values()):
            options.extend(i)
        task_choices = set(random.sample(options, 3))
        if answer not in task_choices:
            task_choices.add(answer)
        elif lemmas[word_id] in task_choices:
            task_choices.discard(lemmas[word_id])
        else:
            while len(task_choices) != 4:
                task_choices.add(random.choice(options))
        final_choices = list(task_choices)
        correct = final_choices.index(answer) + 1
        task = f"""Варианты:\n 
            1 - {final_choices[0].upper()} \n 
            2 - {final_choices[1].upper()} \n 
            3 - {final_choices[2].upper()} \n 
            4 - {final_choices[3].upper()}"""
        return word_id, correct, task

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
            full_text += sent_text + '\n'
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
                pattern = re.compile(old, re.IGNORECASE)
                sent_text = pattern.sub(new, sent_text)

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
            full_text += '\n' + sent_text
            vectors = sent.get_vectors()
            tokens = sent.get_tokens()
            lemmas = sent.get_lemmas()
            morphs = sent.get_morph()
            possible_change = {}

            for i in range(len(tokens)):
                if 'NOUN' in str(morphs[i]):
                    possible_change[tokens[i]] = lemmas[i]

            change_token = random.sample(possible_change.keys(), 1)[0]
            change_lemma = possible_change[change_token]
            change_vector = vectors[change_lemma]

            other_nouns = {}

            for noun in most_frequent_nouns:
                other_vector = navec[noun]
                cosine = dot(change_vector, other_vector)
                other_nouns[cosine]=noun
            other_keys = heapq.nlargest(5, other_nouns.keys())

            new = []
            for key in other_keys:
                most_similar_noun = other_nouns[key]
                new.append(most_similar_noun)
            if change_lemma not in new:
                new.append(change_lemma)
            random.shuffle(new)
            answers = ', '.join(new)

            pattern = re.compile(change_token, re.IGNORECASE)
            sent_text = pattern.sub(f'_____[{answers}]', sent_text)
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
