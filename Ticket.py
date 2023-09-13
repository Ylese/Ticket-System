import time


RED = "\033[31m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"

class Ticket():
    #counter = 0
    # ticketID: None
    # creator_name: None
    # staffID: None
    # email: None
    # description: None
    # #reopen: None
    # response: None
    # status: None

    def __init__(self, ticketID, creator_name, staffID, email, description, reopen = False):
        self.ticketID = ticketID
        self.creator_name = creator_name
        self.staffID = staffID
        self.email = email
        self.description = description
        self.reopen = reopen
        self.response = "Sorry, Not yet provided."
        self.status = "\033[32m" "OPEN" "\033[0m"

        if "password" in self.description:
            password = staffID[:3] + creator_name[:2]
            self.response = "\033[0m" "This is your new password => ""\033[36m" + password
            self.status = "\033[31m" "CLOSED" "\033[0m"
            # self.num_closed +=1
            # self.num_open -=1
        
    def display(self):
        print("\n____________________\n=======TICKET=======\n____________________\n")
        print("Ticket Number:","\033[36m", self.ticketID, "\033[0m")
        print("Ticket Creator:", "\033[36m", self.creator_name, "\033[0m")
        print("Staff ID:", "\033[36m", self.staffID, "\033[0m")
        print("Email Address:", "\033[36m", self.email, "\033[0m")
        print("Description of the issue:", "\033[36m", self.description, "\033[0m")
        print("Response:", "\033[31m", self.response, "\033[0m")
        print("Ticket Status:", self.status)