from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy import create_engine, inspect

Base = declarative_base()

class User(Base):
    __tablename__ = 'users_account'  # corrigido para __tablename__
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    
class Address(Base):
    __tablename__ = 'address'  # corrigido para __tablename__
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('users_account.id'), nullable=False)  # corrigido para ForeignKey
    
    user = relationship("User", back_populates="address")
    
    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"

print(User.__tablename__)
print(Address.__tablename__)

#conexão com o banco de dados
engine = create_engine("sqlite://")

#cria as class como tabelas no banco de dados
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("users_account"))

print(inspetor_engine.get_table_names())

with Session(engine) as session:
    juliana = User(
        name="Juliana",
        fullname="Juliana Oliveira",
        address=[Address(email_address='julianaO@gmail.com')]
    )

    sandy = User(
        name="Sandy",
        fullname="Sandy Oliveira",
        address=[Address(email_address='sandy0@gmail.com'),
                 Address(email_address='sandy@email.com')]
    )
    
    patrick = User(
        name="Patrick",
        fullname="Patrick Oliveira")
    
    #enviando para o BD(persitencia de dados)
    session.add_all([juliana, sandy, patrick])
    
    session.commit()
    
stmt = select(User).where(User.name.in_(["Juliana"]))
print(stmt)
