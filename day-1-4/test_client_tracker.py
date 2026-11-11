
import pytest
from client_tracker import add_lead, view_leads, leads


@pytest.fixture(autouse=True)
def clear_leads():
    leads.clear()
    yield
    leads.clear()


def test_add_lead():
    lead = add_lead(101, "Rahul", 80)

    assert lead["id"] == 101
    assert lead["name"] == "Rahul"
    assert lead["score"] == 80
    assert len(leads) == 1


def test_view_leads(capsys):
    add_lead(102, "Ravi", 70)

    view_leads()

    captured = capsys.readouterr()

    assert "Ravi" in captured.out


def test_empty_leads(capsys):
    view_leads()

    captured = capsys.readouterr()

    assert "No leads found" in captured.out
  
