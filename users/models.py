from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    admin = 'admin'
    manager = 'manager'

    POSITION = (
        (admin, 'Администратор'),
        (manager, 'Менеджер')
    )

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта', unique=True)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    position = models.CharField(max_length=100, choices=POSITION, verbose_name='Должность')
    is_active = models.BooleanField(default=True, verbose_name='Работает')
    photo = models.ImageField(verbose_name='Фото', upload_to='users/', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'position']

    def __str__(self):
        status = 'работает' if self.is_active else 'не работает'
        return f"{self.first_name} {self.last_name} статус: {status}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
