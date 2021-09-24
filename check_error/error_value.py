import pandas as pd


class ErrorValue:
    _total_authors = 0
    __error_list = []

    def __init__(self, path_to_table: str, path_to_dictionary: str):
        self.table_df = pd.read_excel(path_to_table)
        self.dictionary_names = pd.read_excel(path_to_dictionary)["names"].to_list()

    def get_authors(self) -> list:
        pass

    def get_error_list(self) -> list:
        self.__error_list = []
        authors_list = self.get_authors()
        dictionary_string = "".join(self.dictionary_names)
        for author in authors_list:
            if dictionary_string.find(author) == -1:
                self.__error_list.append(author)
        print(self.__error_list)
        return self.__error_list

    def get_error_value(self) -> float:
        return len(self.__error_list) / self._total_authors * 100
