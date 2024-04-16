from abc import ABC, abstractmethod
from io import StringIO
import pandas as pd
import numpy as np
from fastapi import UploadFile, HTTPException

ar_dict = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
           (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def convert_arabic_to_roman(number: int) -> str:
    result = ""
    while number > 0:
        for a, r in ar_dict:
            while number >= a:
                result += r
                number -= a
    return result


def convert_roman_to_arabic(number: str) -> int:
    result = 0
    for a, r in ar_dict:
        while number.startswith(r):
            result += a
            number = number[len(r):]
    return result


def average_age_by_position(file: UploadFile):
    e = HTTPException(status_code=400, detail='Невалидный файл')
    try:
        file.filename.endswith('.csv')
        df = pd.read_csv(file.file)
        if list(df.columns) == ['Имя', 'Возраст', 'Должность']:
            df = df.replace({np.nan: None})
            avg_age = df.groupby(['Должность'])['Возраст'].mean().replace({np.nan: None})
            return {str(key): (None if value is None else float(value)) for key, value in avg_age.items()}
        else:
            raise e
    except Exception:
        raise e


"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""


class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""

    pass


class CSVWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    pass


class YAMLWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""

    pass


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""

        self.data = data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""

        pass
