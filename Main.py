

from TicketSystem import *


RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BGYELLOW = "\033[43m"
LIGHTYELLOW = "\033[93m"
LIGHTCYAN = "\033[96m"
LIGHTRED = "\033[91m"
RESET = "\033[0m"

if __name__ == "__main__":

    ts = TicketSystem()
    #ts.display_all_tickets()

    while True:
        print(f"\n=========={LIGHTYELLOW} Kia Ora! Welcome to the Ticketing System! {RESET}==========\n")
        print("_______________________________________________________________\n")
        print(f"1. To {LIGHTCYAN}display statistics{RESET}, press {BLUE}'1'{RESET}")
        print(f"2. To {LIGHTCYAN}print submitted tickets{RESET}, press {BLUE}'2'{RESET}")
        print(f"3. To {LIGHTCYAN}submit{RESET} a new ticket, press{BLUE}'3' {RESET}")
        print(f"4. To {LIGHTCYAN}respond{RESET} to a ticket, press {BLUE}'4'{RESET}")
        print(f"5. To {LIGHTCYAN}reopen{RESET} a ticket, press {BLUE}'5'{RESET}")
        print(f"6. To {RED}exit{RESET} the main menu, press {BLUE}'0'{RESET}")

        user_choice = input("\nEnter your choice: ")

        if user_choice == "1":
            ts.display_stats()
        elif user_choice == "2":
            ts.display_all_tickets()
        elif user_choice == "3":
            ts.add_new_ticket()
        elif user_choice == "4":
            ts.respondTicket()
        elif user_choice == "5":
            ts.reopenTicket()
        elif user_choice == "0":
            exit()
            
            