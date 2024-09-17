import uuid
from datetime import date
from datetime import datetime

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import func, create_engine, Column, String, Date, TIMESTAMP, DECIMAL, ForeignKey

Base = declarative_base()

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

class Employee(Base):
    __tablename__ = "employees"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)

    tickets = relationship('Ticket', back_populates='employee')

class Event(Base):
    __tablename__ = "events"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    avenue = Column(String, nullable=False)
    event_time = Column(TIMESTAMP, nullable=False)

    ticket_types = relationship('TicketType', back_populates='event')

class TicketType(Base):
    __tablename__ = "ticket_types"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)

    event_id = Column(String(36), ForeignKey('events.id'), nullable=False)

    event = relationship('Event', back_populates='ticket_types')
    tickets = relationship('Ticket', back_populates='ticket_type')

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
    
engine = create_engine("sqlite:///harutickets.db")

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def create_employee(name, cpf):
    new_employee = Employee(name=name, cpf=cpf)
    session.add(new_employee)
    session.commit()

def create_customer(name, cpf, email, password, birth_date):
    new_customer = Customer(name=name, cpf=cpf, email=email, password=password, birth_date=birth_date)
    session.add(new_customer)
    session.commit()

def create_event(name, description, avenue, event_time):
    new_event = Event(name=name, description=description, avenue=avenue, event_time=event_time)
    session.add(new_event)
    session.commit()

def create_ticket_type(name, description, price, event_id):
    new_ticket_type = TicketType(name=name, description=description, price=price, event_id=event_id)
    session.add(new_ticket_type)
    session.commit()

def create_ticket(ticket_type_id, customer_id):
    new_ticket = Ticket(ticket_type_id=ticket_type_id, customer_id=customer_id)
    session.add(new_ticket)
    session.commit()

create_employee("Angelo", "09944779962")

create_customer("Maria Clara", "03344669972", "maria.clara@example.com", "password", date(1994, 1, 18))

create_event("Ready To Be", "Twice Concert", "Allianz Parque", datetime.now())

event = session.query(Event).first()

create_ticket_type("PISTA", "Setor da PISTA", "450", event.id)

ticket_type = session.query(TicketType).first()

customer = session.query(Customer).first()

create_ticket(ticket_type.id, customer)

session.close()