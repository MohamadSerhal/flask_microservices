import connexion
import six

from openapi_server.models.borrow_book import BorrowBook  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def borrow_book(borrow_book):  # noqa: E501
    """borrow_book

    Borrow a book from the library # noqa: E501

    :param borrow_book: 
    :type borrow_book: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        borrow_book = BorrowBook.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_borrowed_book(book_name):  # noqa: E501
    """get_borrowed_book

    Returns info on the borrowing of the book (if borrowed) # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: List[BorrowBook]
    """
    return 'do some magic!'


def get_borrowed_list():  # noqa: E501
    """get_borrowed_list

    get the books that have been borrowed with pagination. # noqa: E501


    :rtype: List[BorrowBook]
    """
    return 'do some magic!'


def remove_borrowed_book(book_name):  # noqa: E501
    """remove_borrowed_book

    Deletes the borrowed book entry. # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
