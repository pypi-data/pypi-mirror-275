import re
from typing import Optional

from bs4 import BeautifulSoup, ResultSet, Tag

from turandot.model import OptionalConverter, ConversionJob


class ListOfFiguresCollector(OptionalConverter):

    ENABLED_CONFIG_KEY = ['opt_processors', 'list_of_figures_collector', 'enable']
    TOKEN_CONFIG_KEY = ['opt_processors', 'list_of_figures_collector', 'token']
    TAG_ID_PREFIX = "list_of_figure_reference_"
    CONTAINER_CLASS_NAME = "list_of_figures"
    PAGE_NO_CONTAINER_CLASS = "listoffigures_pageno"

    def __int__(self):
        super().__init__()
        self.result_set: Optional[ResultSet] = None

    def check_config(self, config: dict) -> bool:
        status = bool(
            self.conversion_job.config.get_key(self.ENABLED_CONFIG_KEY, False)
        )
        return status

    @staticmethod
    def _get_result_set(soup: BeautifulSoup) -> ResultSet:
        return soup.find_all("figcaption")

    def process_step(self) -> ConversionJob:
        soup = BeautifulSoup(self.conversion_job.current_step.content, features="html5lib")
        result_set = self._get_result_set(soup)
        list_container = soup.new_tag("ul")
        list_container["class"] = self.CONTAINER_CLASS_NAME
        for n, i in enumerate(result_set):
            link_id = f"{self.TAG_ID_PREFIX}{str(n)}"
            link_target = f"#{link_id}"
            i["id"] = link_id
            item = soup.new_tag("li")
            link = soup.new_tag("a")
            link["href"] = link_target
            link.string = i.text
            item.append(link)
            pageno = soup.new_tag("a")
            pageno["class"] = self.PAGE_NO_CONTAINER_CLASS
            pageno["href"] = link_target
            item.append(pageno)
            list_container.append(item)
        self.conversion_job.current_step.content = soup.prettify()
        self.conversion_job.current_step.content = self.conversion_job.current_step.content.replace(
            self.conversion_job.config.get_key(self.TOKEN_CONFIG_KEY),
            list_container.prettify()
        )
        return self.conversion_job
