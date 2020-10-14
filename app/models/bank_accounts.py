from mongoengine import Document, StringField, ListField, ObjectIdField

class BankAccounts(Document):
    user = ObjectIdField(required=True)
    chase = StringField(max_length=255, required=True)
    branch_address = StringField(max_length=255, required=True)
    checking_account = StringField(max_length=255, required=True)
    routing_number = StringField(max_length=255, required=True)
    bank = ObjectIdField(required=True)
