"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    NewsPaperModel,
)
from formatters.styles.apa import APABook, APANewsPaperResource


class TestAPA:
    """
    Тестирование оформления списка источников согласно APA
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. Просвещение."
        )

    def test_news_paper(self, newspaper_model_fixture: NewsPaperModel) -> None:
        """
        Тестирование форматирования статьи из газеты.

        :param ArticlesCollectionModel newspaper_model_fixture: Фикстура модели статьи из газеты
        :return:
        """

        model = APANewsPaperResource(newspaper_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (1980, 01.10). Наука как искусство. Южный Урал."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        newspaper_model_fixture: NewsPaperModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param ArticlesCollectionModel newspaper_model_fixture: Фикстура модели статьи из газеты
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APANewsPaperResource(newspaper_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[0]
