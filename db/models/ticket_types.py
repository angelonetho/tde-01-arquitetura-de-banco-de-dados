import uuid

from db.connection import Base
from sqlalchemy import Column, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

class TicketType(Base):
    __tablename__ = "ticket_types"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)

    event_id = Column(String(36), ForeignKey('events.id', ondelete='CASCADE'), nullable=False)

    event = relationship('Event', back_populates='ticket_types')
    tickets = relationship('Ticket', back_populates='ticket_type', cascade='all, delete')