import uuid

from db.connection import Base
from sqlalchemy import Column, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    validated_at = Column(TIMESTAMP)

    ticket_type_id = Column(String(36), ForeignKey('ticket_types.id'), nullable=False)
    customer_id = Column(String(36), ForeignKey('customers.id'), nullable=False)
    employee_id = Column(String(36), ForeignKey('employees.id'))

    ticket_type = relationship("TicketType", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")
    employee = relationship("Employee", back_populates="tickets")
