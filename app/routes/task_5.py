from fastapi import APIRouter, UploadFile
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
from fastapi.responses import FileResponse

router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""
@router.post("/upload_file", description="Задание_5. API для хранения файлов")
async def upload_file(file: UploadFile) -> int:
    """Описание."""

    folder = Path('app/files/')
    file_id = len(list(folder.iterdir())) + 1

    try:
        with ZipFile(f"{folder}/{file_id}.zip", "w", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
            myzip.writestr(file.filename, file.file.read())
            return file_id
    except Exception as e:
        raise e


@router.get("/download_file/{file_id}", description="Задание_5. API для хранения файлов")
async def download_file(file_id: int):
    """Описание."""

    try:
        folder = Path('app/files/')
        file = FileResponse(path=f"{folder}/{file_id}.zip", filename=f"{file_id}.zip")
        return file
    except Exception as e:
        raise e

