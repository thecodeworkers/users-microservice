from mongoengine import Document, StringField, ListField, ObjectIdField

class Favorites(Document):
    user = ObjectIdField(required=True)
    names = StringField(min_length=2,max_length=255, required=True)
    username = StringField(min_length=2,max_length=255, required=True)
