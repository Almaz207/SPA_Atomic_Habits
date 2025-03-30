from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="email пользователя",
        help_text="укажите email пользователя",
    )
    telegram_id = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Telegram_id",
        help_text="укажите ваш телеграм-id",
    )
    phone_number = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name="номер телефона",
        help_text="укажите ваш номер телефона",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
