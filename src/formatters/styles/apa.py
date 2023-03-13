"""
Стиль цитирования по American Psychological Association
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, NewsPaperModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class APABook(BaseCitationStyle):
    """
    Форматирование для книги.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $title. $publishing_house.")

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
        )


class APANewsPaperResource(BaseCitationStyle):
    """
    Форматирование для статьи из газеты.
    """

    data: NewsPaperModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($publishing_year, $publishing_date). $article. $news."
        )

    def substitute(self) -> str:
        logger.info('Форматирование газеты "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            authors=self.data.authors,
            news=self.data.news,
            publishing_year=self.data.publishing_year,
            publishing_date=self.data.publishing_date,
        )


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        NewsPaperModel.__name__: APANewsPaperResource,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.
        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            if type(model).__name__ in self.formatters_map.keys():
                if formatter := self.formatters_map.get(type(model).__name__):
                    formatted_items.append(formatter(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.
        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
