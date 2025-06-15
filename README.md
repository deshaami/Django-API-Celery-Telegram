# 🚀 Django REST API with Celery and Telegram Bot Integration

## 🔖 Project Summary

This Django-based project demonstrates core backend development skills including API development using **Django REST Framework**, user **authentication**, **Celery with Redis** for asynchronous tasks, and **Telegram Bot** integration.

Built as part of an internship assignment, the application provides public and protected APIs, handles user registration and login, triggers asynchronous email sending upon registration, and interacts with users through a Telegram bot.

---

## 🧠 Features Implemented

### 1. **API Endpoints (using Django REST Framework)**

- **Public Endpoint**: Returns a public message accessible to all users.
- **Protected Endpoint**: Requires token-based authentication.
- **User Registration**: Registers a new user and sends a welcome email asynchronously using Celery.
- **User Login**: Returns an authentication token on successful login.

### 2. **Celery Integration**

- Integrated Celery with **Redis** as the message broker.
- Sends a **welcome email** to the user in the background after successful registration.

### 3. **Telegram Bot Integration**

- Telegram bot is set up using **Telegram Bot API**.
- On receiving a `/start` command, the bot saves the user’s Telegram username and chat ID into the Django database.

### 4. **Security and Configuration**

- `DEBUG=False` set in production settings.
- Sensitive values (Secret Key, DB credentials, API keys) stored using `.env` file.

---

## 📊 Folder Structure
<pre><code>📁 django_assignment/ ├── 📂 api/ │ ├── views.py │ ├── urls.py │ ├── tasks.py │ └── models.py │ └── ... # other modules/files ├── 📂 myproject/ │ ├── settings.py │ ├── urls.py │ └── celery.py → Celery app setup ├── 📄 .env → Environment variables ├── 📄 requirements.txt → Project dependencies ├── 📄 README.md → Project documentation └── 📄 manage.py </code></pre>

### 📁 Environment Variables (`.env`)

Create a `.env` file in the project root and include:

- DEBUG=False
- SECRET_KEY=django-insecure-123your-secret-key-here
- EMAIL_HOST_USER=your_email@gmail.com # your email
- EMAIL_HOST_PASSWORD=your_app_password # app password (not your actual email password)
- TELEGRAM_TOKEN=your_telegram_bot_token # from BotFather

  ## 🚀 Running the Project Locally

Once your environment is configured, follow the steps below to run the project locally:

---

### 1️⃣ Apply Migrations

This sets up your database schema.

```bash
python manage.py makemigrations
python manage.py migrate

2️⃣ Start Celery Worker
Open a new terminal window or tab, then run the following command to start the Celery worker:

bash
Copy
Edit
celery -A myproject worker --loglevel=info
