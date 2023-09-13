from Ticket import *
import time

RED = "\033[31m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
LIGHTMAGENTA = "\033[95m"
RESET = "\033[0m"

class TicketSystem():
    ticket_list = []
    ticketID = 2000

    num_open = 0
    num_closed = 0

    #displaying example tickets
    def __init__(self):

        new_ticket = Ticket(2001, "Raven Henry", "KNZRAY", "rav.henry@kanoraunz.co.nz", "Printer is broken.")
        self.ticket_list.append(new_ticket)

        new_ticket = Ticket(2002, "Anica Botha", "KNZANICA", "anica.botha@kanoraunz.co.nz", "PC 5 is not working.")
        self.ticket_list.append(new_ticket)

        self.num_open = 2

        self.next_id = 2003

    #displaying all tickets (submitted, open, closed, reopened)
    def display_all_tickets(self):
        print(f"\n\n\n█▓▒▒░░░{BLUE} SUBMITTED TICKETS {RESET}░░░▒▒▓█\n")

        if len(self.ticket_list) == 0:
            print("No submitted tickets to show")

        for t in self.ticket_list:
            t.display()
            

    #function for submitting new tickets
    def add_new_ticket(self):
        print(f"\n {CYAN}SUBMIT NEW TICKET{RESET} \n")

        #input creator name
        creator_name = input("Enter Ticket Creator:")
        #input staff id
        staffID = input("Enter Staff ID:")
        #input email
        email = input("Enter email address:")
        #input description
        description = input("Description of the issue: ")
        
        
        # if "password" in description:
        # if description.find("password"):
        #     password = staffID[:3] + creator_name[:2]
        #     self.response = "This is your new password:" + password
        #     self.status = "CLOSED"
        #     self.num_closed +=1
        #     self.num_open -=1
            # return
    
        new_ticket = Ticket(self.next_id, creator_name, staffID, email, description)
        self.ticket_list.append(new_ticket)
        self.next_id += 1
        if new_ticket.status == "CLOSED":
            self.num_closed +=1
        else:
            self.num_open +=1

    #password generator
    # def changePassword(self):
        # if "password" in self.description:
        #     password = self.staffID[:3] + self.creator_name[:2]
        #     self.response = password
        #     # print("This is your new password:", password)
        # return

        
    
    #function for reopening ticket
    def reopenTicket(self):
        print(f"\n{LIGHTMAGENTA}To reopen a ticket... {RESET}")
        ticket_id = int(input("     Enter Ticket Number: "))

        for ticket in self.ticket_list:
            if ticket.ticketID == ticket_id:
                if ticket.status == "CLOSED":
                    ticket.status = "REOPENED"
                    self.num_open += 1
                    self.num_closed -=1
                    print(f"\n\n{GREEN}Ticket {ticket_id} has been reopened.{RESET}")
                else:
                    print(f"\n\nTicket {ticket_id} is already {GREEN}open.{RESET}")
                return
        
        print(f"\n\n{RED}Ticket {ticket_id} not found.{RESET}") 


    #function for responding to a ticket
    def respondTicket(self):
        print(f"\n{LIGHTMAGENTA}To respond to a ticket... {RESET}")
        ticket_id = int(input("     Enter Ticket Number: "))
        
        time.sleep(1)
        print("Finding ticket, please wait...")
        time.sleep(2)
        for ticket in self.ticket_list:
            if ticket.ticketID == ticket_id:
                response = (input("\nEnter your response:"))
                if ticket.response != "":
                    ticket.status = "\033[31m" "CLOSED" "\033[0m"
                    ticket.response = response
                    self.num_closed +=1
                    self.num_open -=1
                    return

               
    #function for displaying overall statistics           
    def display_stats(self):
        print(f"\n█▓▒▒░░░{BLUE} TICKET STATISTICS {RESET}░░░▒▒▓█\n")
        print("Submitted Tickets:", len(self.ticket_list))
        print("Open Tickets:", self.num_open)
        print("Closed Tickets:", self.num_closed)


# ticketsystem = TicketSystem()
# ticketsystem.display_all_tickets()
# ticketsystem.add_new_ticket()