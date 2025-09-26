# Alerting & Notification Platform

## Description
This is the **MVP backend for an Alerting & Notification System**.  
It allows admins to create, update, and archive alerts, and users to fetch alerts, snooze them, and mark read/unread.  
The system also includes **reminder logic** (recurring every 2 hours) and an **analytics dashboard** to track alert activity.

---

## Features

### Admin
- Create unlimited alerts (Title, Message, Severity, Delivery Type, Start/Expiry Time, Visibility)
- Update existing alerts
- Archive alerts
- List all alerts with filtering options (Severity, Status, Audience)

### User
- Fetch alerts based on visibility (Org/Team/User)
- Snooze alerts for the current day
- Mark alerts as read/unread
- Track snoozed alerts history

### System
- Reminder logic (alerts repeat every 2 hours until snoozed or expired)
- Analytics endpoint with total alerts, delivered, read, snoozed counts, and severity breakdown

---

## Technologies
- Python 3.11
- FastAPI (Backend API)
- SQLAlchemy (ORM)
- MySQL (Database)
- APScheduler (Reminder Scheduler)
- Uvicorn (ASGI server)

---

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/alerting-system.git
cd alerting-system
````

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

* Windows: `venv\Scripts\activate`
* Mac/Linux: `source venv/bin/activate`

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Database

* Create a MySQL database named `alerts_db`
* Update `app/database.py` with your database credentials

### 6. Seed sample data (Optional, for testing)

```sql
-- Users
INSERT INTO users (id, name, team, email) VALUES 
(1, 'Alice', 'Engineering', 'alice@example.com'),
(2, 'Bob', 'Marketing', 'bob@example.com'),
(3, 'Charlie', 'Engineering', 'charlie@example.com');

-- Teams
INSERT INTO teams (id, name) VALUES
(1, 'Engineering'),
(2, 'Marketing');

-- Sample Alert
INSERT INTO alerts (title, message, severity, delivery_type, start_time, expiry_time, reminder_frequency, reminders_enabled, visibility_type, target_ids, archived)
VALUES
('Server Maintenance', 'Server down from 2 PM to 4 PM', 'Info', 'IN_APP', NOW(), DATE_ADD(NOW(), INTERVAL 1 DAY), 120, 1, 'ORG', JSON_ARRAY(1,2,3), 0);
```

---

### 7. Run the server

```bash
uvicorn app.main:app --reload
```

### 8. Access Swagger API documentation

Open browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
You can test all Admin, User, and Analytics APIs interactively.

---

## API Endpoints

### Admin

* `POST /admin/alerts` → Create alert
* `GET /admin/alerts` → List alerts
* `PUT /admin/alerts/{alert_id}` → Update alert
* `PUT /admin/alerts/{alert_id}/archive` → Archive alert

### User

* `GET /user/alerts?user_id=<id>` → Fetch alerts
* `POST /user/alerts/{alert_id}/snooze?user_id=<id>` → Snooze alert
* `POST /user/alerts/{alert_id}/read?user_id=<id>` → Mark read
* `POST /user/alerts/{alert_id}/unread?user_id=<id>` → Mark unread

### Analytics

* `GET /analytics/` → Show alert statistics

---

## Requirements

Copy-paste into `requirements.txt`:

```
fastapi==0.111.1
uvicorn==0.26.1
sqlalchemy==2.0.22
pydantic==2.5.2
mysql-connector-python==8.1.0
apscheduler==3.12.0
python-dotenv==1.0.0
```

Install via:

```bash
pip install -r requirements.txt
```

---

## Notes

* Reminder frequency is **2 hours** by default for MVP
* Snoozed alerts will not trigger reminders for the same day
* Future improvements can include email/SMS delivery, scheduled alerts, and role-based access

---

