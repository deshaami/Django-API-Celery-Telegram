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

Set up your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 2️⃣ Start Redis Server

Make sure Redis is installed and running:

```bash
redis-server.exe
```

> ✅ If you're on Windows, make sure Redis is running via WSL or Docker.

---

### 3️⃣ Start Celery Worker

Open a **new terminal window/tab** and run the Celery worker:

```bash
celery -A myproject worker --loglevel=info
```

---

### 4️⃣ Run Django Development Server

Finally, start the Django dev server:

```bash
python manage.py runserver
```

---

## ⚙️ Celery Tasks Working

After user registration, a **welcome email** is sent asynchronously using **Celery** and **Redis**.

1. Redis must be running in the background:
   ```bash
   redis-server
   ```

2. Celery worker listens for tasks from Django:
   ```bash
   celery -A myproject worker --loglevel=info
   ```

3. On successful registration:
   - The user data is saved to the database.
   - A welcome email is automatically queued and sent using the `send_welcome_email` task.

---

## 🤖 Telegram Bot Integration

1. Start your Django server:

   ```bash
   python manage.py runserver
   ```

2. Expose your local server using [ngrok](https://ngrok.com/):

   ```bash
   ngrok http 8000
   ```

3. Set up the Telegram webhook using your bot token and ngrok public URL:

   ```bash
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://<your-ngrok-subdomain>.ngrok.io/telegram/
   ```

4. Open Telegram, search for your bot, and send the `/start` command.

5. The bot will:
   - Save your Telegram **username** and **chat ID** to the Django database.
   - Optionally respond with a welcome message.

> 🧪 Test this by checking your Django admin or database — new Telegram user entries will appear after `/start`.




---

## 📄 License & Author

### 🔖 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute the code for personal and educational purposes with proper attribution.

---

### 👤 Author

Developed with ❤️ by **Aleena Roy**

- 🎓 M.Tech in Robotics and Artificial Intelligence, RIT Pampady, Kerala  
- 💻 Passionate about AI, Robotics, Machine Learning, and Research  
- 📫 Contact: aleenapallippadavil@gmail.com
Feel free to connect with me for research, collaboration, or opportunities related to AI and Robotics.

---

### 📢 Acknowledgements

- Special thanks to the Django, DRF, Celery, and Telegram Bot API communities for their excellent documentation and tools.


