from mongoengine import Document, StringField, ListField, ObjectIdField

class Whitelists(Document):
    user = ObjectIdField(required=True)
    address = StringField(max_length=255, required=True)
    currency = StringField(max_length=10, required=True)
