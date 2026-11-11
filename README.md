
# Python CRM — Learning Project

A Python-based Customer Relationship Management (CRM) application developed as part of my **60-Day AI-Native Engineering Journey**.

## Features

- Add and view customer leads
- Validate lead IDs, names, and scores
- Prevent duplicate lead IDs
- Filter qualified leads
- Search leads using dictionary indexing
- Save and load customer data using JSON
- Automated unit testing with pytest

## Tech Stack

- Python
- JSON
- pytest

## Project Structure

```text
Learning/
├── crm/
│   ├── __init__.py
│   ├── main.py
│   ├── client_tracker.py
│   └── storage.py
├── tests/
│   ├── __init__.py
│   └── test_client_tracker.py
├── data/
│   └── .gitkeep
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Shivasaiyadav08/Learning.git
cd Learning
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

From the repository root, run:

```bash
python -m crm.main
```

## Run Tests

Run all automated tests using pytest:

```bash
python -m pytest -q
```

## Roadmap

- [x] Python fundamentals
- [x] Functions and dictionaries
- [x] Exception handling and validation
- [x] JSON file persistence
- [x] Basic unit testing
- [ ] Object-oriented programming (OOP)
- [ ] Complete CRUD operations
- [ ] FastAPI backend
- [ ] PostgreSQL database
- [ ] Authentication and authorization
- [ ] AI-powered lead qualification
- [ ] Voice and chat agents
- [ ] WhatsApp integration
- [ ] Agentic AI workflows
- [ ] Evaluation and monitoring
- [ ] Production deployment

## Project Goal

Build a scalable, AI-powered CRM system while progressively learning:

**Python → Backend Development → Databases → GenAI → Agentic AI → AI Evaluation → Deployment**

The long-term goal is to develop a CRM capable of integrating AI-powered voice agents, chat agents, and WhatsApp automation for business lead management.

## Author

**Shiva Sai**

- GitHub: [Shivasaiyadav08](https://github.com/Shivasaiyadav08)
- Portfolio: [shivasai.is-a.dev](https://shivasai.is-a.dev)

---

*Built and improved throughout my 60-day AI-native engineering learning journey.*
