from bs4 import BeautifulSoup, ResultSet

from turandot.model.converter.optional import ListOfFiguresCollector


class ListOfTablesCollector(ListOfFiguresCollector):

    ENABLED_CONFIG_KEY = ['opt_processors', 'list_of_tables_collector', 'enable']
    TOKEN_CONFIG_KEY = ['opt_processors', 'list_of_tables_collector', 'token']
    TAG_ID_PREFIX = "list_of_table_reference_"
    CONTAINER_CLASS_NAME = "list_of_tables"
    PAGE_NO_CONTAINER_CLASS = "listoftables_pageno"

    @staticmethod
    def _get_result_set(soup: BeautifulSoup) -> ResultSet:
        return soup.find_all(class_="tablecaption")
