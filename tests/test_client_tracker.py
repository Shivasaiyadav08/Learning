
import pytest

from crm.client_tracker import (
    leads,
    add_lead,
    validate_lead,
    qualified_names,
    build_lead_index
)
from crm.storage import save_leads, load_leads


@pytest.fixture(autouse=True)
def clear_leads():
    leads.clear()
    yield
    leads.clear()


def test_add_lead():
    lead = add_lead(101, "Rahul", 85)

    assert lead["id"] == 101
    assert lead["name"] == "Rahul"
    assert lead["score"] == 85


def test_invalid_score():
    with pytest.raises(ValueError):
        add_lead(102, "Ravi", 150)


def test_clean_name():
    lead = validate_lead(103, "  Shiva  ", 90)
    assert lead["name"] == "Shiva"


def test_duplicate_id():
    add_lead(101, "Rahul", 85)

    with pytest.raises(ValueError):
        add_lead(101, "Ravi", 70)


def test_qualified_names():
    items = [
        {"id": 1, "name": "Rahul", "score": 85},
        {"id": 2, "name": "Ravi", "score": 60}
    ]

    assert qualified_names(items) == ["Rahul"]


def test_build_index():
    items = [
        {"id": 101, "name": "Rahul", "score": 85}
    ]

    index = build_lead_index(items)
    assert index[101]["name"] == "Rahul"


def test_json_persistence(tmp_path):
    path = tmp_path / "leads.json"
    items = [{"id": 101, "name": "Rahul", "score": 85}]

    save_leads(path, items)

    assert load_leads(path) == items


def test_missing_json(tmp_path):
    path = tmp_path / "missing.json"

    assert load_leads(path) == []
  
