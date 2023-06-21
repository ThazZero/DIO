from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


engine = create_engine('sqlite:///banco.db')

Session = sessionmaker()
session = Session(bind=engine)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9), unique=True)
    endereco = Column(String(9))

    def __repr__(self):
        return f'Cliente: {self.nome}'


class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    saldo = Column(Integer)
    cliente = relationship('Cliente', backref='contas')

    def __repr__(self):
        return f'Conta: {self.id}'
    


Base.metadata.create_all(engine)

# Inserindo dados
cliente1 = Cliente(nome='João', cpf='123456789', endereco='Rua A')
cliente2 = Cliente(nome='Maria', cpf='987654321', endereco='Rua B')

session.add(cliente1)
session.add(cliente2)

conta1 = Conta(tipo='Conta Corrente', agencia='0001', num=123456, id_cliente=1, saldo=1000)
conta2 = Conta(tipo='Conta Poupança', agencia='0001', num=654321, id_cliente=2, saldo=500)

session.add(conta1)
session.add(conta2)
session.commit()


# Consultando dados
clientes = session.query(Cliente).all()
print(clientes)
print('====================')
contas = session.query(Conta).all()
print(contas)
print('====================')
conta1 = session.query(Conta).filter_by(id=1).first()
print(f'Conta: {conta1} pertence ao cliente: {conta1.cliente.nome}')

