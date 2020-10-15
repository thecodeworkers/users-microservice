from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from bson import ObjectId
from ...models import Whitelists
from ...utils.validate_session import is_auth
from ...protos import *
from ...utils import *
from ..bootstrap import grpc_server

class WhitelistService(WhitelistServicer):
    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '05_whitelist_get_all')

        whitelists = parser_all_object(Whitelists.objects.all())
        for whitelist in whitelists: del whitelist['user']

        response = WhitelistMultipleResponse(whitelist=whitelists)

        return response

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '05_whitelist_save')

            whitelist_object = MessageToDict(request)
            whitelist_object['user'] = user

            whitelist = Whitelists(**whitelist_object).save()
            whitelist = parser_one_object(whitelist)
            del whitelist['user']

            response = WhitelistResponse(whitelist=whitelist)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '05_whitelist_update')

            whitelist_object = MessageToDict(request)
            whitelist_object['user'] = user

            whitelist = Whitelists.objects(id=whitelist_object['id'])
            if not whitelist: del whitelist_object['id']

            whitelist = Whitelists(**whitelist_object).save()
            whitelist = parser_one_object(whitelist)
            del whitelist['user']

            response = WhitelistResponse(whitelist=whitelist)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_whitelist_delete')

            whitelist = Whitelists.objects.get(id=request.id)
            whitelist = whitelist.delete()
            response = WhitelistEmpty()

            return response

        except Whitelists.DoesNotExist as e:
            not_exist_code(context, e)

def start_whitelist_service():
    add_WhitelistServicer_to_server(WhitelistService(), grpc_server)
