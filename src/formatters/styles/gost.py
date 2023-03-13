"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    JournalArticleModel,
    NewsPaperModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class GOSTBook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title. – $edition$city: $publishing_house, $year. – $pages с."
        )

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class GOSTInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article // $website URL: $link (дата обращения: $access_date)."
        )

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class GOSTCollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $collection_title. – $city: $publishing_house, $year. – С. $pages."
        )

    def substitute(self) -> str:
        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTJournal(BaseCitationStyle):
    """
    Форматирование для статьи из журнала.
    """

    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article // $journal. $publishing_year. №$journal_id. С. $pages"
        )

    def substitute(self) -> str:
        logger.info('Форматирование статьи из журнала "%s" ...', self.data.article)

        return self.template.substitute(
            authors=self.data.authors,
            article=self.data.article,
            journal=self.data.journal,
            journal_id=self.data.journal_id,
            publishing_year=self.data.publishing_year,
            pages=self.data.pages,
        )


class GOSTNewsPaper(BaseCitationStyle):
    """
    Форматирование для статьи из газеты.
    """

    data: NewsPaperModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article // $news. $publishing_year. $publishing_date. Ст. $news_number."
        )

    def substitute(self) -> str:
        logger.info('Форматирование статьи из газеты "%s" ...', self.data.article)

        return self.template.substitute(
            authors=self.data.authors,
            article=self.data.article,
            news=self.data.news,
            publishing_year=self.data.publishing_year,
            publishing_date=self.data.publishing_date,
            news_number=self.data.news_number,
        )


class GOSTCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        JournalArticleModel.__name__: GOSTJournal,
        NewsPaperModel.__name__: GOSTNewsPaper,
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
