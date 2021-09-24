from check_error.error_value import ErrorValue


class ErrorWos(ErrorValue):
    def get_authors(self) -> list:
        self._total_authors = 0
        result_list = []
        authors_list = self.table_df["Authors"].to_list()
        authors_with_affiliation = self.table_df["Addresses"].to_list()
        for i in range(len(authors_with_affiliation)):
            authors_list_split = authors_list[i].split("; ")
            authors_with_affiliation_split = authors_with_affiliation[i].split("; [")
            for j in authors_with_affiliation_split:
                if j.find("Omsk State Tech Univ") != -1:
                    authors_omstu = j.split("]")[0]
                    authors_omstu_split = authors_omstu.split("; ")
                    for elem in range(len(authors_omstu_split)):
                        self._total_authors += 1
                        result_list.append(authors_list_split[elem].lower()+";")
        return list(set(result_list))
