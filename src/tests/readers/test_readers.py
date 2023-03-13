"""
Тестирование функций чтения данных из источника.
"""
from typing import Any

import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    JournalArticleModel,
    NewsPaperModel,
)
from readers.reader import (
    BookReader,
    SourcesReader,
    InternetResourceReader,
    ArticlesCollectionReader,
    JournalArticleReader,
    NewsPaperReader,
)
from settings import TEMPLATE_FILE_PATH


class TestReaders:
    """
    Тестирование функций чтения данных из источника.
    """

    @pytest.fixture
    def workbook(self) -> Any:
        """
         Получение объекта тестовой рабочей книги.
        :return:
        """

        return SourcesReader(TEMPLATE_FILE_PATH).workbook

    def test_book(self, workbook: Any) -> None:
        """
        Тестирование чтения книги.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = BookReader(workbook).read()

        assert len(models) == 4
        model = models[0]

        model_type = BookModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.title == "Наука как искусство"
        assert model.edition == "3-е"
        assert model.city == "СПб."
        assert model.publishing_house == "Просвещение"
        assert model.year == 2020
        assert model.pages == 999

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 7

    def test_internet_resource(self, workbook: Any) -> None:
        """
        Тестирование чтения интернет-ресурса.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = InternetResourceReader(workbook).read()

        assert len(models) == 3
        model = models[0]

        model_type = InternetResourceModel

        assert isinstance(model, model_type)
        assert model.article == "Наука как искусство"
        assert model.website == "Ведомости"
        assert model.link == "https://www.vedomosti.ru"
        assert model.access_date == "01.01.2021"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 4

    def test_articles_collection(self, workbook: Any) -> None:
        """
        Тестирование чтения сборника статей.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = ArticlesCollectionReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = ArticlesCollectionModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.article_title == "Наука как искусство"
        assert model.collection_title == "Сборник научных трудов"
        assert model.city == "СПб."
        assert model.publishing_house == "АСТ"
        assert model.year == 2020
        assert model.pages == "25-30"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 7

    def test_journal(self, workbook: Any) -> None:
        """
        Тестирование чтения статьи из журнала.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = JournalArticleReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = JournalArticleModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.article == "Наука как искусство"
        assert model.journal == "Образование и наука"
        assert model.journal_id == "10"
        assert model.publishing_year == 2020
        assert model.pages == "25-30"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 6

    def test_newspaper(self, workbook: Any) -> None:
        """
        Тестирование чтения статьи из газеты.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = NewsPaperReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = NewsPaperModel

        assert isinstance(model, model_type)
        assert model.article == "Наука как искусство"
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.news == "Южный Урал"
        assert model.publishing_year == 1980
        assert model.publishing_date == "01.10"
        assert model.news_number == 5

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 6

    def test_sources_reader(self) -> None:
        """
        Тестирование функции чтения всех моделей из источника.
        """

        models = SourcesReader(TEMPLATE_FILE_PATH).read()
        # проверка общего считанного количества моделей
        assert len(models) == 10

        # проверка наличия всех ожидаемых типов моделей среди типов считанных моделей
        model_types = {model.__class__.__name__ for model in models}
        assert model_types == {
            BookModel.__name__,
            InternetResourceModel.__name__,
            ArticlesCollectionModel.__name__,
            JournalArticleModel.__name__,
            NewsPaperModel.__name__,
        }
