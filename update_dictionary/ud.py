import pandas as pd
from pandas import DataFrame
from transliterate.decorators import transliterate_function


class UpdateDictionary:
    def __init__(self, dictionary: str):
        self.__dictionary = pd.read_excel(dictionary)

    @staticmethod
    def __spelling_options(fio: str) -> str:
        dictionary_letter = {
            "ja": "ya", "ya": "ja", "w": "v", "v": "w", "ts": "tz", "tz": "ts",
        }
        dictionary_symbol = {
            " ": ", ", ".": "., "
        }
        return_string = ""
        for key, item in dictionary_letter.items():
            get_fio_list = fio.split()
            if get_fio_list[0].find(key) != -1:
                return_string += f"{get_fio_list[0].replace(key, item)} {get_fio_list[1]}"
        for key, item in dictionary_symbol.items():
            if fio.find(key) != -1:
                return_string += f"{fio.replace(key, item, 1)}"
        return fio + return_string

    @staticmethod
    @transliterate_function(language_code='ru', reversed=True)
    def __translit_scopus(text):
        surname, name, *patronymic = text.split()
        try:
            patronymic = f"{patronymic[0][0]}."
        except IndexError:
            patronymic = ""
        return f"{surname} {name[0]}.{patronymic};".lower()

    @staticmethod
    @transliterate_function(language_code='ru', reversed=True)
    def __translit_wos(text):
        surname, name, *patronymic = text.split()
        try:
            patronymic = patronymic[0][0]
        except IndexError:
            patronymic = ""
        return f"{surname}, {name[0]}{patronymic};".lower()

    def add_translit_names(self) -> DataFrame:
        names_list = self.__dictionary["Сотрудник"].to_list()
        keys_list = self.__dictionary["names"].to_list()
        for i in range(len(names_list)):
            translit_name_scopus = self.__translit_scopus(names_list[i])
            translit_name_wos = self.__translit_wos(names_list[i])
            if isinstance(keys_list[i], float):
                keys_list[i] = self.__spelling_options(translit_name_scopus) + self.__spelling_options(
                    translit_name_wos)
                continue
            if keys_list[i].find(translit_name_scopus) == -1:
                keys_list[i] += self.__spelling_options(translit_name_scopus)
            if keys_list[i].find(translit_name_wos) == -1:
                keys_list[i] += self.__spelling_options(translit_name_wos)
        self.__dictionary["names"] = keys_list
        return self.__dictionary

    def to_excel(self, path: str):
        self.__dictionary.to_excel(path, index=False)
