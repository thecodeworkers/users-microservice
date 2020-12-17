from mongoengine import Document, StringField, ListField, ObjectIdField

class Whitelists(Document):
    user = ObjectIdField(required=True)
    address = StringField(min_length=2, max_length=255, required=True)
    currency = StringField(min_length=2, max_length=10, required=True)

    meta = {
        'indexes': [
            {
                'fields': ['+user', '+address'],
                'unique': True
            }
        ]
    }
