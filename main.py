from datetime import date
from datetime import datetime

from db.models.customers import Customer
from db.models.employees import Employee
from db.models.events import Event
from db.models.ticket_types import TicketType
from db.models.tickets import Ticket
from db.connection import get_session, create_tables

from use_cases import register_customer, register_employee, register_event, register_ticket, register_ticket_type

create_tables()

session = get_session()

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

register_employee.execute("Angelo", "09944779962")

register_customer.execute("Maria Clara", "03344669972", "maria.clara@example.com", "password", date(1994, 1, 18))

register_event.execute("Ready To Be", "Twice Concert", "Allianz Parque", datetime.now())

event = session.query(Event).first()

register_ticket_type.execute("PISTA", "Setor da PISTA", "450", event.id)

ticket_type = session.query(TicketType).first()

customer = session.query(Customer).first()

register_ticket.execute(ticket_type.id, customer.id)

print(get_all_customers())
print(get_all_employees())
print(get_all_events())
print(get_all_ticket_types())
print(get_all_tickets())

session.close()