from TicketSystem import *

class TicketStatistics():

    def displayAllTickets(self):
        return len(TicketSystem.ticket_list)
        
    def openTickets(self):
        openTicketsCount = 0
        for ticket_item in TicketSystem.ticket_list:
            if ticket_item.status == "SUBMITTED" or ticket_item.status == "REOPENED":
                openTicketsCount = openTicketsCount + 1
        return int(openTicketsCount)
    
    def closedTickets(self):
        closedTicketsCount = 0
        for ticket_item in TicketSystem.ticket_list:
            if ticket_item.status == "CLOSED":
                closedTicketsCount = closedTicketsCount + 1
        return int(closedTicketsCount)
    
    def reopenTicket(self, ticket_id):
        for ticket in self.ticket_list:
            if ticket.ticketID == ticket_id:
                if ticket.status == "CLOSED":
                    input("Enter Ticket Number: ")
                    ticket.status = "REOPENED"
                    print(f"Ticket {ticket_id} has been reopened.")
                    
                    openTicketsCount = openTicketsCount + 1
                    closedTicketsCount = closedTicketsCount - 1
                else:
                    print(f"Ticket {ticket_id} is already open.")
                return
        
        print(f"Ticket {ticket_id} not found.") 
        
    def displayStatistics(self):
        print(f"\n█▓▒▒░░░{BLUE} TICKET STATISTICS {RESET}░░░▒▒▓█\n")
        print("Submitted Tickets:", self.displayAllTickets())
        print("Open Tickets:", self.openTickets())
        print("Closed Tickets:", self.closedTickets())


stats = TicketStatistics()
stats.displayStatistics()