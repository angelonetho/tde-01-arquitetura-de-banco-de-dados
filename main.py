import uuid
from datetime import date
from datetime import datetime

from db.models.customers import Customer
from db.models.employees import Employee
from db.models.events import Event
from db.models.ticket_types import TicketType
from db.models.tickets import Ticket
from db.connection import get_session, create_tables

create_tables()

session = get_session()


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

def get_all_employees():
    return session.query(Employee).all()

def get_employee_by_id(employee_id):
    return session.query(Employee).where(Employee.id == employee_id).first()

def get_all_customers():
    return session.query(Customer).all()

def get_customer_by_id(customer_id):
    return session.query(Customer).where(Customer.id == customer_id).first()

def get_all_events():
    return session.query(Event).all()

def get_event_by_id(event_id):
    return session.query(Event).where(Event.id == event_id).first()

def get_all_ticket_types():
    return session.query(TicketType).all()

def get_ticket_type_by_id(ticket_type_id):
    return session.query(TicketType).where(TicketType.id == ticket_type_id).first()

def get_all_tickets():
    return session.query(Ticket).all()

def get_ticket_by_id(ticket_id):
    return session.query(Ticket).where(Ticket.id == ticket_id).first()

create_employee("Angelo", "09944779962")

create_customer("Maria Clara", "03344669972", "maria.clara@example.com", "password", date(1994, 1, 18))

create_event("Ready To Be", "Twice Concert", "Allianz Parque", datetime.now())

event = session.query(Event).first()

create_ticket_type("PISTA", "Setor da PISTA", "450", event.id)

ticket_type = session.query(TicketType).first()

customer = session.query(Customer).first()

create_ticket(ticket_type.id, customer.id)

print(get_all_customers())
print(get_all_employees())
print(get_all_events())
print(get_all_ticket_types())
print(get_all_tickets())

session.close()