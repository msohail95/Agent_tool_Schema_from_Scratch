week5_travel_agent/

│
├── main.py
├── agent.py
├── planner.py
├── executor.py
├── evaluator.py
├── replanner.py
├── validator.py
├── approval.py
├── config.py
│
├── tools/
│   ├── __init__.py
│   ├── weather_tool.py
│   ├── hotel_tool.py
│   ├── distance_tool.py
│   └── email_tool.py
│
├── database/
│   ├── travel.db
│   └── create_db.py
│
└── schemas/
    └── tool_schema.py


python -m venv .venv
.venv\Scripts\activate

pip install groq requests python-dotenv

pip install ddgs

pip install secure-smtplib


