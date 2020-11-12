from mongoengine import Document, StringField, ListField, ObjectIdField, QuerySet
from bson import json_util

class CustomQuerySet(QuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))

class BankAccounts(Document):
    user = ObjectIdField(required=True)
    chase = StringField(min_length=2, max_length=255, required=True)
    branchAddress = StringField(min_length=2, max_length=255, required=True)
    checkingAccount = StringField(min_length=2, max_length=255, required=True)
    routingNumber = StringField(min_length=2, max_length=255, required=True)
    bank = ObjectIdField(required=True)

    meta = {'queryset_class': CustomQuerySet}

    def to_json(self):
        data = self.to_mongo()
        data['bank'] = str(self.bank)

        return json_util.dumps(data)
