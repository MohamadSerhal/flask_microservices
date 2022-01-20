import connexion
import six

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.user_login_body import UserLoginBody  # noqa: E501
from openapi_server.models.user_register_body import UserRegisterBody  # noqa: E501
from openapi_server import util

import pymongo
from passlib.hash import sha256_crypt
from flask import make_response, jsonify
import json
from bson import json_util
from .auth_module import authentication_module


# connect to cluster on cloud
client = pymongo.MongoClient("mongodb+srv://user1:user1password@libraryapp.bssao.mongodb.net"
                                "/myFirstDatabase?retryWrites=true&w=majority")
# connect to database on cluster
db = client.Authentication
users_collection = db.users


def login_user():  # noqa: E501
    """login_user

    login user and returns a json web token # noqa: E501

    :param user_login_body: 
    :type user_login_body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        user_login_body = UserLoginBody.from_dict(connexion.request.get_json())  # noqa: E501
        if " " in user_login_body._username or " " in user_login_body._password:
            return make_response("Cannot have white space in username or password", 400)
        if user_login_body._username == "" or user_login_body._password == "" :
            return make_response("Username and password cannot be empty", 400)
        user_found = users_collection.find_one({"username": user_login_body._username})
        if user_found is None:
            return make_response("User with this username does not exist!", 403)
        authenticated = sha256_crypt.verify(user_login_body._password, user_found["hashed_pass"])
        if authenticated == False:
            return make_response("Invalid username or password!", 403)
        u = json.loads(json_util.dumps(user_found))
        token = authentication_module.create_token(u['_id']['$oid'])
        return make_response({"token" : token}, 200)
    return make_response("ERROR: Request body should be JSON", 400)


def register_user():  # noqa: E501
    """register_user

    register user to the app # noqa: E501

    :param user_register_body: 
    :type user_register_body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        connexionJson = connexion.request.get_json()
        for key in connexionJson:
            if connexionJson[key] == "":
                return make_response(str(key) + " cant be empty string", 400)
            if key != "full_name":
                if " " in connexionJson[key]:
                    return make_response(str(key) + " cannot contain whitespace", 400)
        user_register_body = UserRegisterBody.from_dict(connexionJson)  # noqa: E501
        hashed = sha256_crypt.encrypt(user_register_body._password)
        if user_register_body._type != "NORMAL" and user_register_body._type != "LIBRARIAN":
            return make_response("Type has to be 'NORMAL' or 'LIBRARIAN'.", 400)
        json_user = {"username":user_register_body._username,
                        "full_name": user_register_body._full_name,
                        "hashed_pass": hashed, 
                        "type": user_register_body._type}
        users_collection.create_index([ ("username", pymongo.ASCENDING) ] , unique= True)
        u_json = json.dumps(json_user)
        data = json.loads(u_json)
        try: 
            users_collection.insert_one(data)
            return make_response("Created user successfully", 201)
        except:
            return make_response("ERROR: Cant add user, username must be unique!", 400)
    return make_response("ERROR: Request body should be JSON", 400)
