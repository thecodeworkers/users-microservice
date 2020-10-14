from mongoengine import Document, StringField, ListField, ObjectIdField

class Favorites(Document):
    user = ObjectIdField(required=True)
    names = StringField(max_length=255, required=True)
    username = StringField(max_length=255, required=True)
