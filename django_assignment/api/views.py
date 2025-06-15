from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.models import User  # Django's built-in user model
from .tasks import send_welcome_email
from .models import TelegramUser
import requests
import json
import logging

logger = logging.getLogger(__name__)

# -----------------------------
# ✅ Celery Email + Registration API
# -----------------------------
@csrf_exempt
def private_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.debug(f"Received private_api POST data: {data}")

            email = data.get('email')
            username = data.get('username', email.split('@')[0] if email else None)
            password = data.get('password', 'defaultpassword123')

            if not email:
                logger.warning("Email not provided in private_api request")
                return JsonResponse({'error': 'Email not provided.'}, status=400)

            # Optional: register the user if not already
            user, created = User.objects.get_or_create(email=email, defaults={'username': username})
            if created:
                user.set_password(password)
                user.save()
                logger.info(f"Created new user: {email}")

            # Trigger the Celery task
            task = send_welcome_email.delay(email)
            logger.info(f"Sent welcome email task for: {email}, task id: {task.id}")

            return JsonResponse({
                'message': 'User registered and welcome email task submitted.',
                'task_id': task.id,
                'user_created': created
            })
        except json.JSONDecodeError:
            logger.error("Invalid JSON received in private_api")
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            logger.error(f"Error in private_api: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST allowed.'}, status=405)


# -----------------------------
# ✅ Telegram Webhook Endpoint
# -----------------------------
@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print("Received data:", data)  # <--- Add this to check data received
            message = data.get('message', {})
            chat = message.get('chat', {})
            text = message.get('text')
            
            telegram_id = chat.get('id')
            username = chat.get('username')
            first_name = chat.get('first_name')

            print(f"Chat ID: {telegram_id}, Text: {text}")  # <--- Check message text and chat ID

            if text == '/start' and telegram_id:
                TelegramUser.objects.get_or_create(
                    telegram_id=telegram_id,
                    defaults={'username': username, 'first_name': first_name}
                )
                send_message(telegram_id, f"Hi {first_name or username}, you're now registered!")
                print("Sent welcome message.")  # <--- Confirm message sending triggered

            return JsonResponse({"status": "ok"})
        except Exception as e:
            print("Error in webhook:", e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST allowed.'}, status=405)


# -----------------------------
# ✅ Helper to Send Telegram Message
# -----------------------------
def send_message(chat_id, text):
    token = settings.TELEGRAM_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
    }
    try:
        resp = requests.post(url, json=payload)
        if not resp.ok:
            logger.error(f"Failed to send Telegram message: {resp.status_code} {resp.text}")
        else:
            logger.debug(f"Telegram message sent successfully: {resp.text}")
    except requests.RequestException as e:
        logger.error(f"Exception while sending Telegram message: {e}")
