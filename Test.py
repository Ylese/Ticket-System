# class HelpDesk:
#     def __init__(self):
#         self.tickets = []
#         self.next_ticket_number = 1
#         self.submitted_ticket_count = 0

#     def submit_password_change_ticket(self, username):
#         ticket = {
#             'ticket_number': self.next_ticket_number,
#             'username': username,
#             'status': 'Open'
#         }
#         self.tickets.append(ticket)
#         self.next_ticket_number += 1
#         self.submitted_ticket_count += 1
#         return ticket['ticket_number']

#     def get_ticket_counts(self):
#         open_count = sum(1 for ticket in self.tickets if ticket['status'] == 'Open')
#         closed_count = sum(1 for ticket in self.tickets if ticket['status'] == 'Closed')
#         return self.submitted_ticket_count, open_count, closed_count

# # Create an instance of the HelpDesk class
# help_desk = HelpDesk()

# def main():
#     print("Welcome to the Help Desk Portal")
#     username = input("Enter your username: ")
    
#     ticket_number = help_desk.submit_password_change_ticket(username)
#     print(f"Password change ticket submitted successfully. Ticket Number: {ticket_number}")

#     submitted_count, open_count, closed_count = help_desk.get_ticket_counts()
#     print(f"Total submitted tickets: {submitted_count}")
#     print(f"Total open tickets: {open_count}")
#     print(f"Total closed tickets: {closed_count}")

# if __name__ == "__main__":
#     main()

# def generate_password(username, name):
#     # Take the first three characters of the username
#     username_part = username[:3]
    
#     # Take the first two characters of the name
#     name_part = name[:2]
    
#     # Combine the two parts
#     password = username_part + name_part
    
#     return password

# # Example usage
# username = "my9username"
# name = "JohnDoe"
# password = generate_password(username, name)
# print("Generated Password:", password)
