from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from bson import ObjectId
from ...models import BankAccounts
from ...utils.validate_session import is_auth
from ...protos import *
from ...utils import *
from ..bootstrap import grpc_server

class BankAccountService(BankAccountServicer):
    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '05_bank_account_get_all')

        bank_accounts = parser_all_object(BankAccounts.objects.all())
        for bank_account in bank_accounts: del bank_account['user']

        response = BankAccountMultipleResponse(bankAccount=bank_accounts)

        return response

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '05_bank_account_save')

            bank_account_object = MessageToDict(request)
            bank_account_object['user'] = user

            bank_account = BankAccounts(**bank_account_object).save()
            bank_account = parser_one_object(bank_account)
            del bank_account['user']

            response = BankAccountResponse(bankAccount=bank_account)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '05_bank_account_update')

            bank_account_object = MessageToDict(request)
            bank_account_object['user'] = user

            bank_account = BankAccounts.objects(id=bank_account_object['id'])
            if not bank_account: del bank_account_object['id']

            bank_account = BankAccounts(**bank_account_object).save()
            bank_account = parser_one_object(bank_account)
            del bank_account['user']

            response = BankAccountResponse(bankAccount=bank_account)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_bank_account_delete')

            bank_account = BankAccounts.objects.get(id=request.id)
            bank_account = bank_account.delete()
            response = BankAccountEmpty()

            return response

        except BankAccounts.DoesNotExist as e:
            not_exist_code(context, e)

def start_bank_account_service():
    add_BankAccountServicer_to_server(BankAccountService(), grpc_server)
