from datetime import date
from datetime import datetime

from db.models.customers import Customer
from db.models.employees import Employee
from db.models.events import Event
from db.models.ticket_types import TicketType
from db.models.tickets import Ticket
from db.connection import get_session, create_tables

from use_cases import delete_customer, delete_employee, delete_event, delete_ticket, delete_ticket_type, edit_customer, fetch_customers, fetch_employees, fetch_events, fetch_ticket_types_by_event_id, fetch_tickets_by_customer_id, fetch_tickets_by_ticket_type_id, register_customer, register_employee, register_event, register_ticket, register_ticket_type, validate_ticket

create_tables()

session = get_session()

register_employee.execute("Angelo", "09944779962")

print(register_customer.execute("Maria Clara", "03344669972", "maria.clara@example.com", "password", date(1994, 1, 18)))

register_event.execute("Ready To Be", "Twice Concert", "Allianz Parque", datetime.now())

event = session.query(Event).first()

register_ticket_type.execute("PISTA", "Setor da PISTA", "450", event.id)

ticket_type = session.query(TicketType).first()

customer = session.query(Customer).first()
employee = session.query(Employee).first()

register_ticket.execute(ticket_type.id, customer.id)
ticket = session.query(Ticket).first()

print(fetch_customers.execute())
print(fetch_employees.execute())
print(fetch_events.execute())

print(fetch_tickets_by_customer_id.execute(customer_id=customer.id))

print(edit_customer.execute(customer_id=customer.id, name="Maria Clara H"))
#delete_customer.execute(customer_id=customer.id)
#delete_employee.execute(employee_id=employee.id)
#delete_ticket.execute(ticket_id=ticket.id)
#delete_ticket_type.execute(ticket_type_id=ticket_type.id)
#delete_event.execute(event_id=event.id)

validate_ticket.execute(employee_id=employee.id, ticket_id=ticket.id)

session.close()