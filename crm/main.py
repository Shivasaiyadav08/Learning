
from pathlib import Path

from crm.client_tracker import (
    leads,
    add_lead,
    view_leads
)
from crm.storage import save_leads, load_leads


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "leads.json"
)


def show_menu():
    print("\n--- CRM Lead Tracker ---")
    print("1. Add Lead")
    print("2. View Leads")
    print("3. Exit")


def main():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    leads.clear()
    leads.extend(load_leads(DATA_FILE))

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                lead_id = int(input("Enter lead ID: "))
                name = input("Enter customer name: ")
                score = int(input("Enter lead score: "))

                lead = add_lead(lead_id, name, score)

                try:
                    save_leads(DATA_FILE, leads)
                except OSError:
                    leads.remove(lead)
                    raise

                print("Lead added successfully")

            except ValueError as error:
                print("Invalid input:", error)

            except OSError as error:
                print("File error:", error)

        elif choice == "2":
            view_leads()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
  
