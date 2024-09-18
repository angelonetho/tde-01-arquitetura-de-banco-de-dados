import uuid

from db.connection import Base
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = "events"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    avenue = Column(String, nullable=False)
    event_time = Column(TIMESTAMP, nullable=False)

    ticket_types = relationship('TicketType', back_populates='event')
