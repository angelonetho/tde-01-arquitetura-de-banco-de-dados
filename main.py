from datetime import date
from datetime import datetime

from db.models.customers import Customer
from db.models.employees import Employee
from db.models.events import Event
from db.models.ticket_types import TicketType
from db.models.tickets import Ticket
from db.connection import get_session, create_tables

from use_cases import edit_customer, fetch_customers, fetch_employees, fetch_events, register_customer, register_employee, register_event, register_ticket, register_ticket_type

create_tables()

session = get_session()

register_employee.execute("Angelo", "09944779962")

register_customer.execute("Maria Clara", "03344669972", "maria.clara@example.com", "password", date(1994, 1, 18))

register_event.execute("Ready To Be", "Twice Concert", "Allianz Parque", datetime.now())

event = session.query(Event).first()

register_ticket_type.execute("PISTA", "Setor da PISTA", "450", event.id)

ticket_type = session.query(TicketType).first()

customer = session.query(Customer).first()

register_ticket.execute(ticket_type.id, customer.id)

print(fetch_customers.execute())
print(fetch_employees.execute())
print(fetch_events.execute())

print(edit_customer.execute(customer_id=customer.id, name="Maria Clara H"))

session.close()