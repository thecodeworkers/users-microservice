# from app.protos import auth_pb2, auth_pb2_grpc, role_pb2, role_pb2_grpc
# from app.protos import send_money_pb2, send_money_pb2_grpc, exchange_pb2_grpc, exchange_pb2
from app.protos import bank_account_pb2, bank_account_pb2_grpc
from app.constants import HOST
import grpc

try:
    channel = grpc.insecure_channel(HOST)

    # stub = role_pb2_grpc.RoleStub(channel)

    # request = role_pb2.RoleEmpty()
    # metadata = [('auth_token', 'Bd2j7vjLKwwsUAEixffh69oqVeCYSP')]

    # response = stub.get_all(request=request, metadata=metadata)

    # request = role_pb2.RoleNotIdRequest(
    #     name="basic user",
    #     code="001",
    #     scopes=['']
    # )

    # response = stub.save(request)

    # stub = auth_pb2_grpc.AuthStub(channel)

    # request = auth_pb2.SignupRequest(
    #     email="caceres.vc95@gmail.com",
    #     password="12345678",
    #     role="001"
    # )

    # response = stub.signup(request)

    # request = auth_pb2.SigninRequest(
    #     username="caceres.vc95@gmail.com",
    #     password="12345678"
    # )

    # response = stub.signin(request)

    # channel = grpc.insecure_channel(HOST)

    # stub = send_money_pb2_grpc.SendMoneyStub(channel)

    # request = send_money_pb2.SendMoneyRequest(account='sjhsdjdshdjshshjhdh', amount=0.001, currency='BTC')
    # metadata = [('provider', 'binance')]

    # response = stub.withdraw(request=request, metadata=metadata)

    # print(response)

    # stub = send_money_pb2_grpc.SendMoneyStub(channel)

    # request = send_money_pb2.SendMoneyRequest(account='sjhsdjdshdjshshjhdh', amount=0.001, currency='BTC')
    # # metadata = [('provider', 'binance')]

    # response = stub.sent(request=request)

    # print(response)

    # stub = exchange_pb2_grpc.ExchangeStub(channel)
    # request = exchange_pb2.ExchangeRequest(out_currency='BTC', in_currency='ETH', out_amount=0.001)
    # metadata = [('provider', 'binance')]

    # response = stub.simple_exchange(request=request)

    stub = bank_account_pb2_grpc.BankAccountStub(channel)

    # request = bank_account_pb2.BankAccountNotIdRequest(
    #     chase = 'hjhhjjjhjhj',
    #     branchAddress = 'fhfhfhhhfhgggh',
    #     checkingAccount = 'hjjhggfgfgfgg',
    #     routingNumber = 'hgfgrrtfffh',
    #     bank = '5f45aa109a53614d98fb4c4b'
    # )

    # metadata = [('auth_token', 'Bd2j7vjLKwwsUAEixffh69oqVeCYSP')]

    # response = stub.save(request=request, metadata=metadata)

    # request = bank_account_pb2.BankAccountRequest(
    #     id = '5f87a756a451d6e2c957c819',
    #     chase = 'hjhhjjjhjhj',
    #     branchAddress = 'fhfhfhhhfhgggh',
    #     checkingAccount = 'hjjhggfgfgfgg',
    #     routingNumber = 'Nuevo routing',
    #     bank = '5f45aa109a53614d98fb4c4b'
    # )

    # metadata = [('auth_token', 'Bd2j7vjLKwwsUAEixffh69oqVeCYSP')]

    # response = stub.update(request=request, metadata=metadata)


    # request = bank_account_pb2.BankAccountIdRequest(
    #     id='5f87a7ba4c00ba7cad031b1b'
    # )

    # metadata = [('auth_token', 'Bd2j7vjLKwwsUAEixffh69oqVeCYSP')]

    # response = stub.delete(request=request, metadata=metadata)


    request = bank_account_pb2.BankAccountEmpty()

    metadata = [('auth_token', 'Bd2j7vjLKwwsUAEixffh69oqVeCYSP')]

    response = stub.get_all(request=request, metadata=metadata)

    print(response)

except grpc.RpcError as e:
    print(e)
