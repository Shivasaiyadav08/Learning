
leads = []


def validate_lead(lead_id, name, score):
    if type(lead_id) is not int or lead_id <= 0:
        raise ValueError("Invalid lead ID")

    if type(name) is not str:
        raise ValueError("Name must be a string")

    name = name.strip()

    if not name:
        raise ValueError("Name is required")

    if type(score) is not int or not 0 <= score <= 100:
        raise ValueError("Invalid score")

    return {
        "id": lead_id,
        "name": name,
        "score": score
    }


def add_lead(lead_id, name, score):
    lead = validate_lead(lead_id, name, score)

    if any(item["id"] == lead_id for item in leads):
        raise ValueError("Lead ID already exists")

    leads.append(lead)
    return lead


def view_leads():
    if not leads:
        print("No leads found")
        return

    for lead in leads:
        print(lead)


def build_lead_index(items):
    index = {}

    for lead in items:
        index[lead["id"]] = lead

    return index


def qualified_names(items, minimum=70):
    return [
        lead["name"]
        for lead in items
        if lead["score"] >= minimum
    ]
  
