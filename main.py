from check_error.error_scopus import ErrorScopus
from check_error.error_wos import ErrorWos
from update_dictionary.ud import UpdateDictionary
import pandas as pd


def main():
    dictionary_update = UpdateDictionary("data/dictionary.xlsx")
    dictionary_df = dictionary_update.add_translit_names()
    dictionary_df.to_excel("dictionary.xlsx", index=False)
    error_scopus = ErrorScopus("./data/scopus_2020_2021.xlsx", "./dictionary.xlsx")
    error_wos = ErrorWos("./data/wos_2020_2021.xls", "./dictionary.xlsx")
    error_scopus_list = error_scopus.get_error_list()
    error_wos_list = error_wos.get_error_list()
    error_wos_value = error_wos.get_error_value()
    error_scopus_value = error_scopus.get_error_value()
    error_wos_df = pd.DataFrame({"wos": error_wos_list})
    error_scopus_df = pd.DataFrame({"scopus": error_scopus_list})
    print(f"Wos Error: {error_wos_value}%")
    print(f"Scopus Error: {error_scopus_value}%")
    error_wos_df.to_excel("ErrorWos.xlsx")
    error_scopus_df.to_excel("ErrorScopus.xlsx")
