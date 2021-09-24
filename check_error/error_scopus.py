from check_error.error_value import ErrorValue


class ErrorScopus(ErrorValue):
    def get_authors(self) -> list:
        self._total_authors = 0
        result_list = []
        authors_list = self.table_df["Authors with affiliations"].to_list()
        for authors in authors_list:
            for author in authors.split("; "):
                if author.find("Omsk State Technical University") != -1:
                    self._total_authors += 1
                    item_split = author.split(", ")
                    need_author = item_split[0] + " " + item_split[1] + ";"
                    result_list.append(need_author.lower())
        return list(set(result_list))
