import connexion
import six

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.late_borrowers import LateBorrowers  # noqa: E501
from openapi_server import util

import pymongo
from flask import make_response, jsonify
import json
from bson import json_util
import requests
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://user1:user1password@libraryapp.bssao.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Late_books
late_collection = db.late_books


def get_late(limit=0, offset=0):  # noqa: E501
    """get_late

    Get the usernames and books of people that are late + pagination. # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the items to be displayed
    :type offset: int

    :rtype: List[LateBorrowers]
    """
    if limit<0 or offset<0:
        return make_response( {"Error message": "Limit and offset have to be non negative."}, 400)
    borrowed_books = late_collection.find({}, {"_id": 0}).skip(limit * offset).limit(limit)
    return make_response(jsonify( json.loads(json_util.dumps(borrowed_books)) ), 200)


def update_db():  # noqa: E501
    """update_db

    updates the DB and fills it with the usernames of poeple who are late in returning their books # noqa: E501


    :rtype: InlineResponse200
    """
    late_list = []
    names_dict = {}
    today = datetime.today().strftime('%Y-%m-%d')
    response = requests.get("http://library-container:2001/borrow").json()
    # response = requests.get("http://172.17.0.2:2001/borrow").json()
    # response = requests.get("http://localhost:2001/borrow").json()
    for json_object in response:
        return_date = json_object["return_date"]
        # check if return date is earlier than today
        # this if statement gives true if the return date has passed
        if valid_dates(return_date, today):
            return_json = {"book": json_object["book"], 
                            "return_date": return_date
                            }
            if json_object["borrower"] in names_dict:
                names_dict[ json_object["borrower"] ].append(return_json)
            else:
                names_dict[ json_object["borrower"] ] = [return_json]
    for key in names_dict:
        final_json = { "borrower": key, "late_list" : names_dict[key]}
        late_list.append(final_json)
    try:
        late_collection.delete_many({})
        late_collection.insert_many(late_list)
        return make_response({"message" : "Updated late books successfully."}, 200)
    except:
        return make_response({"message": "Error occured while updating the DB, run the update again."}, 400)
    return 




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
