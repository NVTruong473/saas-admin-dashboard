# Project 6 - Admin SaaS Dashboard

A full-stack web application built with FastAPI, SQLite, JWT Authentication, and Streamlit.

## Live Features

- User Register
- User Login
- JWT Authentication
- Protected Routes
- Role System (Admin / User)
- Admin Dashboard
- User Management
- Delete Users
- Export Users CSV
- Analytics Charts
- Premium UI Dashboard

## Tech Stack

### Backend

- FastAPI
- SQLite
- SQLAlchemy
- JWT
- Passlib
- Uvicorn

### Frontend

- Streamlit
- Pandas
- Requests

### Tools

- Google Colab
- ngrok
- GitHub

## Project Structure

    project6/
    ├── main.py
    ├── frontend.py
    ├── requirements.txt
    ├── README.md
    ├── screenshots/
    └── app/
        ├── database.py
        ├── models.py
        ├── schemas.py
        └── routes/
            └── users.py

## Installation

    pip install -r requirements.txt

## Run Backend (Local)

    uvicorn main:app --reload

## Run Frontend (Local)

    streamlit run frontend.py

## Run on Google Colab

### Start Backend

    !pkill -f uvicorn
    !nohup uvicorn main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

### Start Frontend

    !pkill -f streamlit
    !nohup streamlit run frontend.py --server.port 8501 > front.log 2>&1 &

## Google Colab Public URL (Optional)

Use ngrok to create a public URL for Streamlit app.

    from pyngrok import ngrok
    from google.colab import userdata

    authtoken = userdata.get("NGROK_TOKEN")
    ngrok.set_auth_token(authtoken)

    public_url = ngrok.connect(8501)
    print(public_url)

Note:
- Save your ngrok token in Colab Secrets as NGROK_TOKEN
- Port 8501 is used for Streamlit frontend
- Re-run ngrok after restarting Colab runtime

## Default Roles

- Username admin => Admin role
- Other usernames => User role

## API Endpoints

- POST /register
- POST /login
- GET /me
- GET /users
- DELETE /users/{user_id}

## Demo Screenshots

Save UI images inside:

    screenshots/

Suggested files:

- login-page.png
- admin-dashboard.png
- analytics-chart.png
- users-table.png

## Notes / Limitations

- SQLite is used for demo purposes
- Admin role is assigned when username = admin
- JWT secret key should be moved to environment variables in production
- Use PostgreSQL/MySQL for real production systems
- Deploy backend and frontend separately for best results

## Future Improvements

- Edit User Feature
- Change Password
- Audit Logs
- Search Filters
- Role Permissions Expansion
- Cloud Database
- Docker Deployment

## Author

Nguyen Van Truong

GitHub:
https://github.com/NVTruong473
