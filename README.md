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

### Frontend

- Streamlit
- Pandas
- Requests

## Project Structure

    project6/
    ├── main.py
    ├── frontend.py
    ├── requirements.txt
    ├── README.md
    └── app/
        ├── database.py
        ├── models.py
        ├── schemas.py
        └── routes/
            └── users.py

## Installation

    pip install -r requirements.txt

## Run Backend

    uvicorn main:app --reload

## Run Frontend

    streamlit run frontend.py

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

## Default Roles

- Username admin => Admin role
- Other usernames => User role

## Demo Screens

- Login Page
- Admin Dashboard
- Charts Analytics
- CSV Export
- User Management

## Author

Nguyen Van Truong

GitHub:
https://github.com/NVTruong473
