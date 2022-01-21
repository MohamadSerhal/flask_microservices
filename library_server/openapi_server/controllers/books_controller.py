import connexion
import six

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def add_book(book):  # noqa: E501
    """add_book

    Add a book to the library # noqa: E501

    :param book: 
    :type book: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        book = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book(book_name):  # noqa: E501
    """delete_book

    Delete book from the library database # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_book(book_name):  # noqa: E501
    """get_book

    get a book from the library database # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_books_list(limit=None, offset=None):  # noqa: E501
    """get_books_list

    Gets a list of books in alphabetical order # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the items to be displayed
    :type offset: int

    :rtype: List[Book]
    """
    return 'do some magic!'
