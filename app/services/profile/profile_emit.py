from ..channel import service_bus_connection
from ...models import Profiles
from ...utils import parser_one_object

class ProfileEmitter():
    def __init__(self):
        self.__start_emitters()

    def emit_create_profile(self):
        service_bus_connection.add_queue('create_profile', self.__create_profile)

    def emit_get_profile(self):
        service_bus_connection.add_queue('get_profile', self.__get_profile)

    def __create_profile(self, data):
        try:
            profile = Profiles(**data).save()
            return self.__profile_instance(profile)

        except Exception as error:
            return str(error)

    def __get_profile(self, data):
        try:
            profile = Profiles.objects(user=data['id']).first()
            if not profile: return {}

            return self.__profile_instance(profile)

        except Exception as error:
            return str(error)

    def __start_emitters(self):
        self.emit_create_profile()
        self.emit_get_profile()

    def __profile_instance(self, profile):
        profile = parser_one_object(profile)
        del profile['user']
        del profile['id']

        return profile

def start_profile_emit():
    ProfileEmitter()
    service_bus_connection.send()
