import uuid

from db.connection import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = "employees"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)

    tickets = relationship('Ticket', back_populates='employee')

    def __repr__(self):
        return "<Employee(id='%s', name='%s', cpf='%s')>" % (
            self.id,
            self.name,
            self.cpf,
        )
