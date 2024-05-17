import os


def count_files_folders(directory: str = "", recursive: bool = False) -> dict:
    """Функция"""
    directory = directory or os.path.abspath(__file__)
    if not os.path.isdir(directory):
        return {"error": "Указанный путь не является директорией"}

    files_count, folders_count = 0, 0
    for root, dirs, files in (
        os.walk(directory) if recursive else [("", [], [entry.name for entry in os.scandir(directory)])]
    ):
        files_count += len(files)
        folders_count += len(dirs)

    return {"files": files_count, "folders": folders_count}


# запрос пути у пользователя: например "src или tests"
user_directory = input("Введите путь к директории: ")

# использование функции с пользовательским вводом
result = count_files_folders(user_directory, recursive=True)
print(result)
