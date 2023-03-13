"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):
    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class JournalArticleModel(BaseModel):
    """
    Модель статьи из журнала:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article="Наука как искусство",
            journal="Образование и Наука",
            journal_id="10",
            publishing_year="2020",
            pages="35-30"
        )
    """

    authors: str
    article: str
    journal: str
    journal_id: str
    publishing_year: int = Field(..., gt=0)
    pages: str


class NewsPaperModel(BaseModel):
    """
    Модель статьи из газеты:

    .. code-block::

        NewsPaperModel(
            article="Наука как искусство",
            authors="Иванов И.М., Петров С.Н.",
            news="Южный Урал",
            publishing_year="1980",
            publishing_date="01.10",
            news_number="5"
        )
    """

    article: str
    authors: str
    news: str
    publishing_year: int = Field(..., gt=0)
    publishing_date: str
    news_number: int = Field(..., gt=0)
