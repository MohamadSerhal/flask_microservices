import connexion
import six

from openapi_server.models.borrow_book import BorrowBook  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util

from flask import make_response , jsonify
import json
from bson import json_util
from bson.objectid import ObjectId
from .mongo.mongo_connection import client

db = client.Library
borrow_collection = db.borrowings
books_collection = db.books

db_users = client.Authentication
users_collection = db_users.users

def valid_dates(borrow_date, return_date):
    borrow_year = borrow_date[0:4]
    return_year = return_date[0:4]
    if int(return_year) < int(borrow_year):
        return False
    elif int(return_year) > int(borrow_year):
        return True
    
    borrow_month = borrow_date[5:7]
    return_month = return_date[5:7]
    if int(return_month) < int(borrow_month):
        return False
    elif int(return_month) > int(borrow_month):
        return True
    
    borrow_day = borrow_date[8:]
    return_day = return_date[8:]
    if int(return_day) < int(borrow_day):
        return False
    return True

def borrow_book(user):  # noqa: E501
    """borrow_book

    Borrow a book from the library # noqa: E501

    :param borrow_book: 
    :type borrow_book: dict | bytes

    :rtype: InlineResponse200
    """
    username = users_collection.find_one({"_id": ObjectId(user)})
    if username is None:
        return make_response({"Error message":"User does not exist"}, 403)
    if connexion.request.is_json:
        borrow_book = connexion.request.get_json()  # noqa: E501
        if valid_dates(borrow_book["borrowed_date"], borrow_book["return_date"]) == False:
            return make_response("Borrow date have to be earlier or equal to return date.", 400)
        book_count = books_collection.find_one({"name": borrow_book["book"]})  
        if book_count is None:
            return make_response({"Error message": "This book does not exist in the library."}, 400)
        borrow_book["borrower"] = username["username"]
        borrow_collection.create_index([("book", 1)], unique=True)
        try:
            borrow_collection.insert_one(borrow_book)
            return make_response({"message": borrow_book["book"] + " is now borrowed."}, 201)
        except:
            return make_response({"Error message": borrow_book["book"] + " is already borrowed."}, 400)
    return


def get_borrowed_book(book_name):  # noqa: E501
    """get_borrowed_book

    Returns info on the borrowing of the book (if borrowed) # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: List[BorrowBook]
    """
    borrowed = borrow_collection.find_one({"book": book_name}, {"_id": 0})
    if borrowed is None:
        return make_response({"Error message": book_name + " is not currently borrowed by anyone."}, 400)
    return make_response(json.loads(json_util.dumps(borrowed)), 200)


def get_borrowed_list():  # noqa: E501
    """get_borrowed_list

    get the books that have been borrowed with pagination. # noqa: E501


    :rtype: List[BorrowBook]
    """
    borrowed_books = borrow_collection.find({}, {"_id": 0})
    return make_response(jsonify( json.loads(json_util.dumps(borrowed_books)) ), 200)


def remove_borrowed_book(book_name, user):  # noqa: E501
    """remove_borrowed_book

    Deletes the borrowed book entry. # noqa: E501

    :param book_name: 
    :type book_name: str

    :rtype: InlineResponse200
    """
    user_type = users_collection.find_one({"_id": ObjectId(user)}, {"type": 1})
    if user_type is None:
        return make_response({"Error message":"User does not exist"}, 403)
    if user_type["type"] != "LIBRARIAN":
        return make_response({"Error message": "Only librarians can report a borrowed book as returned."}, 403)
    borrow_collection.delete_one({"book": book_name})
    return make_response({"message": book_name + " returned to library successfully."}, 200)
