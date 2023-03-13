"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    JournalArticleModel,
    NewsPaperModel,
)


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date="01.01.2021",
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )


@pytest.fixture
def journal_model_fixture() -> JournalArticleModel:
    """
    Фикстура модели статьи из журнала.

    :return: RegulationModel
    """

    return JournalArticleModel(
        authors="Иванов И.М., Петров С.Н.",
        article="Наука как искусство",
        journal="Образование и Наука",
        journal_id="10",
        publishing_year="2020",
        pages="25-30",
    )


@pytest.fixture
def newspaper_model_fixture() -> NewsPaperModel:
    """
    Фикстура модели статьи из газеты.

    :return: NewsPaperModel
    """

    return NewsPaperModel(
        article="Наука как искусство",
        authors="Иванов И.М., Петров С.Н.",
        news="Южный Урал",
        publishing_year="1980",
        publishing_date="01.10",
        news_number="5",
    )
