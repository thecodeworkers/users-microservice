from mongoengine import Document, StringField, ListField, ObjectIdField

class Profiles(Document):
    user = ObjectIdField(required=True, unique=True)
    name = StringField(max_length=255)
    lastname = StringField(max_length=255)
