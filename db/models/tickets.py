import uuid

from db.connection import Base
from sqlalchemy import Column, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    validated_at = Column(TIMESTAMP)

    ticket_type_id = Column(String(36), ForeignKey('ticket_types.id', ondelete='CASCADE'), nullable=False)
    customer_id = Column(String(36), ForeignKey('customers.id', ondelete='SET NULL'))
    employee_id = Column(String(36), ForeignKey('employees.id', ondelete='SET NULL'))

    ticket_type = relationship("TicketType", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")
    employee = relationship("Employee", back_populates="tickets")

    def __repr__(self):
        return "<Ticket(id='%s', created_at='%s', validated_at='%s', ticket_type_id='%s', customer_id='%s', employee_id='%s')>" % (
            self.id,
            self.created_at,
            self.validated_at,
            self.ticket_type_id,
            self.customer_id,
            self.employee_id,
        )
