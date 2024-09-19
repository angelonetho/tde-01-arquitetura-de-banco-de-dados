import uuid

from db.connection import Base
from sqlalchemy import Column, String, Date, TIMESTAMP, func
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String(45), unique=True)
    password = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())

    tickets = relationship('Ticket', back_populates='customer')

    def __repr__(self):
        return "<Customer(id='%s', name='%s', cpf='%s', email='%s', phone_number='%s')>" % (
            self.id,
            self.name,
            self.cpf,
            self.email,
            self.phone_number,
        )