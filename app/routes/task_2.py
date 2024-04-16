from typing import Annotated

from fastapi import APIRouter, Body

from app.core import convert_arabic_to_roman, convert_roman_to_arabic
from app.models import ConverterResponse

router = APIRouter(tags=["Стажировка"])

"""
Задание_2. Конвертер
    1. Реализовать функции convert_arabic_to_roman() и convert_roman_to_arabic() из пакета app.core
    2. Написать логику и проверки для вводимых данных. Учитывать, что если арабское число выходит за пределы 
    от 1 до 3999, то возвращать "не поддерживается"
    3. Запустить приложение и проверить результат через swagger
"""


@router.post("/converter", description="Задание_2. Конвертер")
async def convert_number(number: Annotated[int | str, Body()]) -> ConverterResponse:
    """
    Принимает арабское или римское число.
    Конвертирует его в римское или арабское соответственно.
    Возвращает первоначальное и полученное числа в виде json:
    {
        "arabic": 10,
        "roman": "X"
    }
    """

    # Попытка преобразования входной строки в число
    try:
        int(number)
    # Если ошибка - значит введено римское число
    except ValueError:
        arabic = convert_roman_to_arabic(number)
        roman = number
    # Если нет ошибки - значит введено арабское
    else:
        arabic = number
        if 0 < number < 4000:
            roman = convert_arabic_to_roman(number)
        else:
            roman = "Не поддерживается"
    # Создание экземпляра модели
    converter_response = ConverterResponse(
        roman=roman,
        arabic=arabic
    )
    return converter_response
