from datetime import datetime

from db.connection import get_session
from db.models.employees import Employee
from db.models.tickets import Ticket
from db.models.ticket_types import TicketType

session = get_session()

def execute(ticket_id, employee_id):
    try:
        employee = session.query(Employee).where(Employee.id == employee_id).first()

        if not employee:
            return 'Employee not found.'
        
        ticket = session.query(Ticket).where(Ticket.id == ticket_id).first()

        if not ticket:
            return 'Ticket not found.'
        
        ticket.employee_id = employee_id
        ticket.validated_at = datetime.now()

        session.commit()
        
        return ticket
    finally:
        session.close()
    