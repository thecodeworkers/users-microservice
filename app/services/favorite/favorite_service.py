from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from bson import ObjectId
from ...models import Favorites
from ...utils.validate_session import is_auth
from ...protos import *
from ...utils import *
from ..bootstrap import grpc_server

class FavoriteService(FavoriteServicer):
    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '05_favorite_get_all')

        favorites = parser_all_object(Favorites.objects.all())
        for favorite in favorites: del favorite['user']

        response = FavoriteMultipleResponse(favorite=favorites)

        return response

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '05_favorite_save')

            favorite_object = MessageToDict(request)
            favorite_object['user'] = user

            favorite = Favorites(**favorite_object).save()
            favorite = parser_one_object(favorite)
            del favorite['user']

            response = FavoriteResponse(favorite=favorite)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '05_favorite_update')

            favorite_object = MessageToDict(request)
            favorite_object['user'] = user

            favorite = Favorites.objects(id=favorite_object['id'])
            if not favorite: del favorite_object['id']

            favorite = Favorites(**favorite_object).save()
            favorite = parser_one_object(favorite)
            del favorite['user']

            response = FavoriteResponse(favorite=favorite)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_favorite_delete')

            favorite = Favorites.objects.get(id=request.id)
            favorite = favorite.delete()
            response = FavoriteEmpty()

            return response

        except Favorites.DoesNotExist as e:
            not_exist_code(context, e)

def start_favorite_service():
    add_FavoriteServicer_to_server(FavoriteService(), grpc_server)
