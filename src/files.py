import shutil

from pathlib import Path
from src.constants import ASSETS_PATH
from typing import Union


def prepare_environment(base_path: Union[Path, str]) -> None:
    """
    Creates ASSETS_PATH folder if no created and removes existing folder
    """
    if base_path.exists():
        shutil.rmtree(base_path)
    base_path.mkdir(parents=True)


class EmptyFileError(BaseException):
    """
    Файл пустой.
    """


class NoFileError(BaseException):
    """
    Файл не указан.
    """


class NothingToWriteError(BaseException):
    """
    В файл ничего не записывается.
    """


class Files:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.text_path = ASSETS_PATH.parent / file_name

    def read_file(self) -> str:
        with open(self.text_path, encoding='utf-8') as file:
            text = file.read()
        if len(text)==0:
            raise EmptyFileError
        return text

    def get_exercises_path(self) -> Path:
        """
        Returns path for requested exercise
        """
        if self.file_name == '':
            raise NoFileError
        exercise_name = f"{self.file_name[:self.file_name.index('.')]}_exercises.txt"
        return ASSETS_PATH / exercise_name

    def get_answers_path(self) -> Path:
        """
        Returns path for requested exercise
        """
        if self.file_name == '':
            raise NoFileError
        answer_name = f"{self.file_name[:self.file_name.index('.')]}_answers.txt"
        return ASSETS_PATH / answer_name

    def write_to_file(self, ex_text: str, answer_text: str) -> None:
        """
        записывает упражнения и ответы в файлы, которые передаются пользователю
        :return:
        """
        if (len(ex_text) == 0) or (len(answer_text) == 0):
            raise NothingToWriteError
        with open(self.get_exercises_path(), 'w', encoding='utf-8') as file_1:
            file_1.write(ex_text)
        with open(self.get_answers_path(), 'w', encoding='utf-8') as file_2:
            file_2.write(answer_text)
