import connexion
import six

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util

from .mongo.mongo_connection import client
from flask import make_response , jsonify
import json
from bson import json_util
from bson.objectid import ObjectId

db = client.Library
books_collection = db.books

db_users = client.Authentication
users_collection = db_users.users

def add_book(user):  # noqa: E501
    """add_book

    Add a book to the library # noqa: E501

    :param book: 
    :type book: dict | bytes

    :rtype: None
    """
    # check if user is librarian
    # only librarians can add books to the DB
    user_type = users_collection.find_one({"_id": ObjectId(user)}, {"type": 1})
    if user_type is None:
        return make_response({"Error message":"User does not exist"}, 403)
    if user_type["type"] != "LIBRARIAN":
        return make_response({"Error message": "Only librarians can add a book to DB"}, 403)
    if connexion.request.is_json:
        book = connexion.request.get_json()  # noqa: E501
        if len(book["name"])==0 or len(book["authors"])==0:
            return make_response("Neither length of name or authors can be 0", 400)
        books_collection.create_index([ ("name", 1) ], unique = True)
        try:
            books_collection.insert_one(book)
            return make_response({"message": "Book created successfully"}, 201)
        except:
            return make_response({"Error message": "Book with this name already exists"}, 400)

    return make_response({"Error message": "Body must be json"}, 400)


def delete_book(book_name, user):  # noqa: E501
    """delete_book

    Delete book from the library database # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: InlineResponse200
    """
    # check if user is librarian
    # only librarians can add books to the DB
    user_type = users_collection.find_one({"_id": ObjectId(user)}, {"type": 1})
    if user_type is None:
        return make_response({"Error message":"User does not exist"}, 403)
    if user_type["type"] != "LIBRARIAN":
        return make_response({"Error message": "Only librarians can add a book to DB"}, 403)
    books_collection.delete_one({"name": book_name})
    return make_response("Book deleted successfully", 200)


def get_book(book_name):  # noqa: E501
    """get_book

    get a book from the library database # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: InlineResponse200
    """
    book = books_collection.find_one({"name": book_name}, {"_id": 0})
    if book is None:
        return make_response("Book not found", 404)
    return make_response(json.loads(json_util.dumps(book)), 200)


def get_books_list(limit=0, offset=0):  # noqa: E501
    """get_books_list

    Gets a list of books in alphabetical order # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the items to be displayed
    :type offset: int

    :rtype: List[Book]
    """
    if limit < 0 or offset < 0:
        return make_response({"Error message": "Both limit and offset need to be non negative."}, 400)
    books = books_collection.find({}, {"_id": 0}).sort("name", 1).skip(limit*offset).limit(limit)
    return make_response(jsonify( json.loads(json_util.dumps(books)) ) , 200)
