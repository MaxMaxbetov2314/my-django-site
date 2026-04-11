import os
import django

# Указываем Django, где лежат настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# --- НАСТРОЙКИ (ЗАМЕНИТЕ НА СВОИ!) ---
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@example.com'
ADMIN_PASSWORD = 'exRctvYB'  # <--- СМЕНИТЕ ЭТОТ ПАРОЛЬ!
# --------------------------------------

user, created = User.objects.get_or_create(
    username=ADMIN_USERNAME,
    defaults={'email': ADMIN_EMAIL}
)

if created:
    user.set_password(ADMIN_PASSWORD)
    user.save()
    print(f"✅ Суперпользователь '{ADMIN_USERNAME}' успешно создан!")
else:
    # Если пользователь уже существует, обновляем пароль на всякий случай
    user.set_password(ADMIN_PASSWORD)
    user.save()
    print(f"ℹ️ Пользователь '{ADMIN_USERNAME}' существовал. Пароль обновлен.")