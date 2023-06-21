import pymongo


cluster = pymongo.MongoClient("mongodb://localhost:27017/")
db = cluster["DIO"]

collection_clientes = db["clientes"]
collection_contas = db["contas"]

# Inserindo dados

cliente1 = {"_id": 1, "nome": "João", "cpf": "123456789", "endereco": "Rua A"}
cliente2 = {"_id": 2, "nome": "Maria", "cpf": "987654321", "endereco": "Rua B"}

collection_clientes.insert_one(cliente1)
collection_clientes.insert_one(cliente2)

conta1 = {"_id": 1, "tipo": "Conta Corrente", "agencia": "0001", "num": 123456, "id_cliente": 1, "saldo": 1000}
conta2 = {"_id": 2, "tipo": "Conta Poupança", "agencia": "0001", "num": 654321, "id_cliente": 2, "saldo": 500}

collection_contas.insert_one(conta1)
collection_contas.insert_one(conta2)


# Consultando dados
clientes = collection_clientes.find()
for cliente in clientes:
    print(cliente)
print('====================')
contas = collection_contas.find()
for conta in contas:
    print(conta)
print('====================')


