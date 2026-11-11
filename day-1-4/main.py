
from client_tracker import add_lead, view_leads, show_menu


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            lead_id = int(input("Enter lead ID: "))
            name = input("Enter customer name: ")
            score = int(input("Enter lead score: "))

            add_lead(lead_id, name, score)
            print("Lead added successfully")

        elif choice == "2":
            view_leads()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
  
