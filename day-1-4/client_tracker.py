
leads = []


def add_lead(lead_id, name, score):
    lead = {
        "id": lead_id,
        "name": name,
        "score": score
    }
    leads.append(lead)
    return lead


def view_leads():
    if not leads:
        print("No leads found")
        return

    for lead in leads:
        print(lead)


def show_menu():
    print("\n--- Client Tracker ---")
    print("1. Add Lead")
    print("2. View Leads")
    print("3. Exit")
  
